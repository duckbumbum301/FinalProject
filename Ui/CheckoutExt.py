from PyQt6.QtWidgets import QMainWindow, QMessageBox, QPushButton, QHBoxLayout, QLabel, QLineEdit, QButtonGroup
from PyQt6 import QtCore
import os
import re

from Ui.Checkout import Ui_CheckoutWindow
from libs.DataConnector import DataConnector
from libs.OrderManager import OrderManager
from models.customer import Customer
from models.order import Order
from models.order_detail import OrderDetail


class CheckoutExt(QMainWindow, Ui_CheckoutWindow):
    def __init__(self, order_data, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.order_data = order_data
        self.data_connector = DataConnector()

        # Chuyển đổi bố cục từ dọc sang ngang
        self.setupCustomLayout()

        # Tạo QButtonGroup để nhóm các nút radio lại, đảm bảo chỉ chọn được một
        self.paymentButtonGroup = QButtonGroup(self)
        self.paymentButtonGroup.addButton(self.radioButton_cash)
        self.paymentButtonGroup.addButton(self.radioButtonOnlinePay)

        # Để theo dõi trạng thái hiện tại của quá trình nhập liệu
        self.current_input_step = 0
        self.input_fields = [
            {"label": self.label_2, "field": self.lineEditName},  # Customer Name
            {"label": self.label_3, "field": self.lineEditPhone},  # Customer Phone
            {"label": self.label_5, "field": self.lineEditEmail},  # Customer Email
            {"label": self.label_6, "field": self.lineEditAddress},  # Customer Address
        ]

        # Ẩn tất cả các mục nhập liệu ngang trừ mục đầu tiên
        self.hide_all_input_fields()
        self.show_current_input_field()

        # Set up the order summary
        self.display_order_summary()

        # Connect buttons
        self.pushButtonDone.clicked.connect(self.process_order)
        self.pushButton_Back.clicked.connect(self.go_back)
        self.pushButtonNext.clicked.connect(self.go_to_next_input)
        self.pushButtonPrevious.clicked.connect(self.go_to_previous_input)
        self.pushButtonPrevious.setVisible(False)  # Ẩn khi ở bước đầu tiên

        # Set default payment method
        self.radioButton_cash.setChecked(True)

        # Ẩn nút Done ban đầu, chỉ hiển thị khi đã nhập đủ thông tin
        self.pushButtonDone.setVisible(False)

    def setupCustomLayout(self):
        """Thiết lập bố cục tùy chỉnh sau khi setupUi đã chạy"""
        # Điều chỉnh kích thước cửa sổ thành nhỏ gọn hơn
        self.setMinimumSize(750, 650)
        self.resize(800, 700)

        # Điều chỉnh kích thước các vùng khác
        self.scrollArea.setGeometry(QtCore.QRect(40, 180, 720, 480))
        self.checkout_area.setGeometry(QtCore.QRect(240, 10, 340, 160))

        # Tạo nút Previous và Next trước
        self.buttonLayout = QHBoxLayout()

        self.pushButtonPrevious = QPushButton(parent=self.order_detail_area)
        self.pushButtonPrevious.setObjectName("pushButtonPrevious")
        self.pushButtonPrevious.setText("Back")
        self.pushButtonPrevious.setStyleSheet("\n"
                                              "QPushButton {\n"
                                              "            background-color:rgb(230, 215, 185);\n"
                                              "            color: rgb(91, 76, 43);\n"
                                              "            border-radius: 15px;\n"
                                              "            padding: 8px;\n"
                                              "            font-size: 14px;\n"
                                              "            min-width: 100px;\n"
                                              "        }\n"
                                              "        QPushButton:hover {\n"
                                              "            background-color: rgb(216, 203, 164);\n"
                                              "        }")
        self.buttonLayout.addWidget(self.pushButtonPrevious)

        self.pushButtonNext = QPushButton(parent=self.order_detail_area)
        self.pushButtonNext.setObjectName("pushButtonNext")
        self.pushButtonNext.setText("Next")
        self.pushButtonNext.setStyleSheet("\n"
                                          "QPushButton {\n"
                                          "            background-color:rgb(251, 236, 207);\n"
                                          "            color: rgb(91, 76, 43);\n"
                                          "            border-radius: 15px;\n"
                                          "            padding: 8px;\n"
                                          "            font-size: 14px;\n"
                                          "            min-width: 100px;\n"
                                          "        }\n"
                                          "        QPushButton:hover {\n"
                                          "            background-color: rgb(216, 203, 164);\n"
                                          "        }")
        self.buttonLayout.addWidget(self.pushButtonNext)

        # Tạo label và trường nhập liệu
        # Tạo các trường nhập liệu nếu chưa có
        if not hasattr(self, 'lineEditName'):
            self.lineEditName = QLineEdit(parent=self.order_detail_area)
            self.lineEditName.setObjectName("lineEditName")
            self.lineEditName.setStyleSheet(
                "background-color: #fdfae6; border: 1px solid #d8c49c; border-radius: 6px; padding: 4px; font-size: 12px; color: #5b4c2b;")
            self.lineEditName.setMaximumHeight(30)

        if not hasattr(self, 'lineEditPhone'):
            self.lineEditPhone = QLineEdit(parent=self.order_detail_area)
            self.lineEditPhone.setObjectName("lineEditPhone")
            self.lineEditPhone.setStyleSheet(
                "background-color: #fdfae6; border: 1px solid #d8c49c; border-radius: 6px; padding: 4px; font-size: 12px; color: #5b4c2b;")
            self.lineEditPhone.setMaximumHeight(30)

        if not hasattr(self, 'lineEditEmail'):
            self.lineEditEmail = QLineEdit(parent=self.order_detail_area)
            self.lineEditEmail.setObjectName("lineEditEmail")
            self.lineEditEmail.setStyleSheet(
                "background-color: #fdfae6; border: 1px solid #d8c49c; border-radius: 6px; padding: 4px; font-size: 12px; color: #5b4c2b;")
            self.lineEditEmail.setMaximumHeight(30)

        if not hasattr(self, 'lineEditAddress'):
            self.lineEditAddress = QLineEdit(parent=self.order_detail_area)
            self.lineEditAddress.setObjectName("lineEditAddress")
            self.lineEditAddress.setStyleSheet(
                "background-color: #fdfae6; border: 1px solid #d8c49c; border-radius: 6px; padding: 4px; font-size: 12px; color: #5b4c2b;")
            self.lineEditAddress.setMaximumHeight(30)

        # Xóa widgets đã có nếu có
        for i in reversed(range(self.orderDetailLayout.count())):
            item = self.orderDetailLayout.itemAt(i)
            if item.widget() in [self.label_2, self.label_3, self.label_5, self.label_6, self.lineEditTotal]:
                self.orderDetailLayout.removeItem(item)
                # Không xóa widget, chỉ xóa khỏi layout

        # Tạo layout ngang cho Customer Name
        self.nameLayout = QHBoxLayout()
        self.label_2.setMinimumWidth(200)
        self.nameLayout.addWidget(self.label_2)
        self.nameLayout.addWidget(self.lineEditName)

        # Tạo layout ngang cho Phone Number
        self.phoneLayout = QHBoxLayout()
        self.label_3.setMinimumWidth(200)
        self.phoneLayout.addWidget(self.label_3)
        self.phoneLayout.addWidget(self.lineEditPhone)

        # Tạo layout ngang cho Email
        self.emailLayout = QHBoxLayout()
        self.label_5.setMinimumWidth(200)
        self.emailLayout.addWidget(self.label_5)
        self.emailLayout.addWidget(self.lineEditEmail)

        # Tạo layout ngang cho Address
        self.addressLayout = QHBoxLayout()
        self.label_6.setMinimumWidth(200)
        self.addressLayout.addWidget(self.label_6)
        self.addressLayout.addWidget(self.lineEditAddress)

        # Xóa label_total khỏi bố cục
        self.label_total.setVisible(False)

        # Thêm layout ngang vào layout chính
        self.orderDetailLayout.addLayout(self.nameLayout)
        self.orderDetailLayout.addLayout(self.phoneLayout)
        self.orderDetailLayout.addLayout(self.emailLayout)
        self.orderDetailLayout.addLayout(self.addressLayout)
        self.orderDetailLayout.addLayout(self.buttonLayout)

        # Thêm một label mới cho tổng tiền
        self.label_totalAmount = QLabel(parent=self.order_detail_area)
        self.label_totalAmount.setObjectName("label_totalAmount")
        self.label_totalAmount.setText("Total:")
        self.label_totalAmount.setStyleSheet("font-size: 12px; font-weight: bold; color: #5b4c2b;")

        # Thêm lại total và nút Done
        self.orderDetailLayout.addWidget(self.label_totalAmount)
        self.orderDetailLayout.addWidget(self.lineEditTotal)
        self.orderDetailLayout.addWidget(self.pushButtonDone)

    def hide_all_input_fields(self):
        """Ẩn tất cả các trường nhập liệu và nhãn"""
        for item in self.input_fields:
            # Ẩn cả nhãn và trường nhập liệu
            if item["label"].parent() == self.order_detail_area:
                # Nếu là nhãn thuộc trực tiếp về order_detail_area
                item["label"].setVisible(False)
                item["field"].setVisible(False)
            elif hasattr(self, "nameLayout") and item["label"] == self.label_2:
                # Ẩn nameLayout
                self.nameLayout.itemAt(0).widget().setVisible(False)
                self.nameLayout.itemAt(1).widget().setVisible(False)
            elif hasattr(self, "phoneLayout") and item["label"] == self.label_3:
                # Ẩn phoneLayout
                self.phoneLayout.itemAt(0).widget().setVisible(False)
                self.phoneLayout.itemAt(1).widget().setVisible(False)
            elif hasattr(self, "emailLayout") and item["label"] == self.label_5:
                # Ẩn emailLayout
                self.emailLayout.itemAt(0).widget().setVisible(False)
                self.emailLayout.itemAt(1).widget().setVisible(False)
            elif hasattr(self, "addressLayout") and item["label"] == self.label_6:
                # Ẩn addressLayout
                self.addressLayout.itemAt(0).widget().setVisible(False)
                self.addressLayout.itemAt(1).widget().setVisible(False)

    def show_current_input_field(self):
        """Hiển thị trường nhập liệu hiện tại"""
        if 0 <= self.current_input_step < len(self.input_fields):
            current = self.input_fields[self.current_input_step]
            # Hiển thị cả nhãn và trường nhập liệu
            if current["label"].parent() == self.order_detail_area:
                # Nếu là nhãn thuộc trực tiếp về order_detail_area
                current["label"].setVisible(True)
                current["field"].setVisible(True)
            elif hasattr(self, "nameLayout") and current["label"] == self.label_2:
                # Hiển thị nameLayout
                self.nameLayout.itemAt(0).widget().setVisible(True)
                self.nameLayout.itemAt(1).widget().setVisible(True)
            elif hasattr(self, "phoneLayout") and current["label"] == self.label_3:
                # Hiển thị phoneLayout
                self.phoneLayout.itemAt(0).widget().setVisible(True)
                self.phoneLayout.itemAt(1).widget().setVisible(True)
            elif hasattr(self, "emailLayout") and current["label"] == self.label_5:
                # Hiển thị emailLayout
                self.emailLayout.itemAt(0).widget().setVisible(True)
                self.emailLayout.itemAt(1).widget().setVisible(True)
            elif hasattr(self, "addressLayout") and current["label"] == self.label_6:
                # Hiển thị addressLayout
                self.addressLayout.itemAt(0).widget().setVisible(True)
                self.addressLayout.itemAt(1).widget().setVisible(True)

            current["field"].setFocus()

            # Hiển thị hoặc ẩn nút Back dựa vào bước hiện tại
            self.pushButtonPrevious.setVisible(self.current_input_step > 0)

    def go_to_next_input(self):
        """Chuyển sang trường nhập liệu tiếp theo khi nhấn nút Next"""
        # Kiểm tra trường hiện tại
        current_field = self.input_fields[self.current_input_step]["field"]
        field_text = current_field.text().strip()

        # Kiểm tra trường bắt buộc (Tên)
        if self.current_input_step == 0 and not field_text:
            QMessageBox.warning(self, "Thông tin thiếu", "Vui lòng nhập họ tên!")
            return

        # Kiểm tra số điện thoại (phải có 10 chữ số)
        if self.current_input_step == 1:
            if not field_text:
                QMessageBox.warning(self, "Thông tin thiếu", "Vui lòng nhập số điện thoại!")
                return
            if not field_text.isdigit() or len(field_text) != 10:
                QMessageBox.warning(self, "Sai định dạng", "Số điện thoại phải có đúng 10 chữ số!")
                return

        # Kiểm tra định dạng email (phải có @.com)
        if self.current_input_step == 2 and field_text:
            email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.com$'
            if not re.match(email_pattern, field_text):
                QMessageBox.warning(self, "Sai định dạng", "Email phải đúng định dạng có '@.com'!")
                return

        # Ẩn trường hiện tại - sử dụng logic tương tự như trong hide_all_input_fields
        current = self.input_fields[self.current_input_step]
        if current["label"].parent() == self.order_detail_area:
            current["label"].setVisible(False)
            current["field"].setVisible(False)
        elif hasattr(self, "nameLayout") and current["label"] == self.label_2:
            self.nameLayout.itemAt(0).widget().setVisible(False)
            self.nameLayout.itemAt(1).widget().setVisible(False)
        elif hasattr(self, "phoneLayout") and current["label"] == self.label_3:
            self.phoneLayout.itemAt(0).widget().setVisible(False)
            self.phoneLayout.itemAt(1).widget().setVisible(False)
        elif hasattr(self, "emailLayout") and current["label"] == self.label_5:
            self.emailLayout.itemAt(0).widget().setVisible(False)
            self.emailLayout.itemAt(1).widget().setVisible(False)
        elif hasattr(self, "addressLayout") and current["label"] == self.label_6:
            self.addressLayout.itemAt(0).widget().setVisible(False)
            self.addressLayout.itemAt(1).widget().setVisible(False)

        # Tăng chỉ số bước và hiển thị trường tiếp theo
        self.current_input_step += 1

        # Nếu đã nhập đủ thông tin, hiển thị nút Done thay vì Next
        if self.current_input_step >= len(self.input_fields):
            self.pushButtonNext.setVisible(False)
            self.pushButtonPrevious.setVisible(True)
            self.pushButtonDone.setVisible(True)
            # Hiển thị tất cả các trường đã nhập để xem lại
            for item in self.input_fields:
                if item["label"].parent() == self.order_detail_area:
                    item["label"].setVisible(True)
                    item["field"].setVisible(True)
                elif hasattr(self, "nameLayout") and item["label"] == self.label_2:
                    self.nameLayout.itemAt(0).widget().setVisible(True)
                    self.nameLayout.itemAt(1).widget().setVisible(True)
                elif hasattr(self, "phoneLayout") and item["label"] == self.label_3:
                    self.phoneLayout.itemAt(0).widget().setVisible(True)
                    self.phoneLayout.itemAt(1).widget().setVisible(True)
                elif hasattr(self, "emailLayout") and item["label"] == self.label_5:
                    self.emailLayout.itemAt(0).widget().setVisible(True)
                    self.emailLayout.itemAt(1).widget().setVisible(True)
                elif hasattr(self, "addressLayout") and item["label"] == self.label_6:
                    self.addressLayout.itemAt(0).widget().setVisible(True)
                    self.addressLayout.itemAt(1).widget().setVisible(True)
        else:
            # Hiển thị trường tiếp theo
            self.show_current_input_field()

    def go_to_previous_input(self):
        """Quay lại trường nhập liệu trước đó"""
        # Nếu đang ở bước cuối cùng (hiển thị tất cả)
        if self.current_input_step >= len(self.input_fields):
            # Ẩn tất cả trường
            self.hide_all_input_fields()
            # Quay lại bước trước đó
            self.current_input_step = len(self.input_fields) - 1
            # Hiển thị lại Next và ẩn Done
            self.pushButtonNext.setVisible(True)
            self.pushButtonDone.setVisible(False)
        else:
            # Ẩn trường hiện tại
            current = self.input_fields[self.current_input_step]
            if current["label"].parent() == self.order_detail_area:
                current["label"].setVisible(False)
                current["field"].setVisible(False)
            elif hasattr(self, "nameLayout") and current["label"] == self.label_2:
                self.nameLayout.itemAt(0).widget().setVisible(False)
                self.nameLayout.itemAt(1).widget().setVisible(False)
            elif hasattr(self, "phoneLayout") and current["label"] == self.label_3:
                self.phoneLayout.itemAt(0).widget().setVisible(False)
                self.phoneLayout.itemAt(1).widget().setVisible(False)
            elif hasattr(self, "emailLayout") and current["label"] == self.label_5:
                self.emailLayout.itemAt(0).widget().setVisible(False)
                self.emailLayout.itemAt(1).widget().setVisible(False)
            elif hasattr(self, "addressLayout") and current["label"] == self.label_6:
                self.addressLayout.itemAt(0).widget().setVisible(False)
                self.addressLayout.itemAt(1).widget().setVisible(False)

        # Giảm chỉ số bước
        self.current_input_step -= 1

        # Đảm bảo không vượt quá giới hạn
        if self.current_input_step < 0:
            self.current_input_step = 0

        # Hiển thị trường mới
        self.show_current_input_field()

    def go_back(self):
        """Thoát khỏi cửa sổ Checkout khi nhấn nút Back góc trên bên trái"""
        self.close()

    def display_order_summary(self):
        """Display the order summary in the text edit"""
        summary = "=== ORDER SUMMARY ===\n\n"
        total = 0

        for item in self.order_data:
            product_id = item.product_id
            name = item.name
            price = item.price
            quantity = item.quantity
            subtotal = price * quantity
            total += subtotal

            summary += f"{product_id} - {name}\n"
            summary += f"Price: {price:,} VNĐ x {quantity} = {subtotal:,} VNĐ\n"
            if hasattr(item, 'notes') and item.notes:
                summary += f"Notes: {item.notes}\n"
            summary += "\n"

        summary += f"Total: {total:,} VNĐ"

        # Set the summary text and total
        self.order_summary_content.setText(summary)
        self.lineEditTotal.setText(f"{total:,} VNĐ")
        self.lineEditTotal.setReadOnly(True)

    def process_order(self):
        """Xử lý đơn hàng khi nhấn nút Done"""
        try:
            # Kiểm tra hình thức thanh toán
            if self.radioButton_cash.isChecked():
                payment_method = "cash"
            elif self.radioButtonOnlinePay.isChecked():
                payment_method = "online"
            else:
                QMessageBox.warning(self, "Thiếu thông tin", "Vui lòng chọn hình thức thanh toán!")
                return
                
            print(f"Payment method selected: {payment_method}")

            # Lấy thông tin khách hàng từ form
            name = self.lineEditName.text().strip()
            phone = self.lineEditPhone.text().strip()
            email = self.lineEditEmail.text().strip()
            address = self.lineEditAddress.text().strip()
            
            # Kiểm tra thông tin bắt buộc
            if not name or not phone:
                QMessageBox.warning(self, "Thiếu thông tin", "Vui lòng nhập đầy đủ họ tên và số điện thoại!")
                return
                
            print(f"Customer info - Name: {name}, Phone: {phone}, Email: {email}, Address: {address}")

            # Tìm kiếm khách hàng theo số điện thoại
            existing_customer = self.data_connector.find_customer_by_phone(phone)
            
            # Khởi tạo đối tượng khách hàng
            if existing_customer:
                # Cập nhật thông tin khách hàng nếu đã tồn tại
                customer = existing_customer
                customer.name = name
                customer.email = email
                customer.address = address
                print(f"Using existing customer: {customer.customer_id}")
            else:
                # Tạo khách hàng mới với ID trống để hàm save_customer tạo ID mới
                customer = Customer(
                    customer_id="",  # Để trống để tạo ID mới
                    name=name,
                    phone=phone,
                    email=email,
                    address=address
                )
                print(f"Created new customer object")
                
            # Lưu thông tin khách hàng - luôn cập nhật thông tin mới nhất
            saved_customer = self.data_connector.save_customer(customer)
            print(f"Customer saved with ID: {saved_customer.customer_id}")
            
            # DEBUG - Kiểm tra file customers.json
            customer_file = os.path.join(self.data_connector.base_path, "customers.json")
            print(f"Customers file path: {customer_file}")
            print(f"Customers file exists after save: {os.path.exists(customer_file)}")

            # Tính tổng tiền đơn hàng
            total_amount = 0
            for item in self.order_data:
                total_amount += item.price * item.quantity
            print(f"Total order amount: {total_amount}")

            # Tạo đơn hàng mới - LUÔN tạo mới, không bao giờ cập nhật đơn hàng cũ
            # OrderManager sẽ tạo ID mới dựa trên thời gian hiện tại
            order = Order(
                order_id="",  # Để trống để OrderManager tạo ID mới
                customer_id=saved_customer.customer_id,
                payment_method=payment_method,
                total_amount=total_amount,
                status="pending"
            )
            print(f"Created new order object for customer {saved_customer.customer_id}")
            
            # Tạo chi tiết đơn hàng
            order_details = []
            for item in self.order_data:
                # Lấy notes an toàn
                notes = item.notes if hasattr(item, 'notes') else None

                # Tạo chi tiết đơn hàng
                detail = OrderDetail(
                    order_id="",  # OrderManager sẽ cập nhật sau
                    product_id=item.product_id,
                    name=item.name,
                    price=item.price,
                    quantity=item.quantity,
                    notes=notes
                )
                order_details.append(detail)
            print(f"Added {len(order_details)} order details")

            # Lưu đơn hàng và chi tiết đơn hàng  
            print("Saving order using OrderManager...")
            
            # Tạo OrderManager và lưu đơn hàng
            order_manager = OrderManager(self.data_connector.base_path)
            saved_order = order_manager.save_order(order, order_details)
            print(f"Order saved with ID: {saved_order.order_id}")
            
            # Kiểm tra kết quả
            order_file = os.path.join(self.data_connector.base_path, "orders.json")
            print(f"Orders file exists after save: {os.path.exists(order_file)}")
            
            # Kiểm tra nội dung file orders.json
            if os.path.exists(order_file):
                try:
                    with open(order_file, 'r', encoding='utf-8') as f:
                        content = f.read()
                        print(f"Orders file content length: {len(content)}")
                        if len(content) < 100:  # Nếu nội dung ngắn, in ra để kiểm tra
                            print(f"Orders file content: {content}")
                except Exception as e:
                    print(f"Error reading orders.json: {str(e)}")

            QMessageBox.information(self, "Thành công", "Đơn hàng đã được xử lý thành công!")
            self.close()

        except Exception as e:
            QMessageBox.warning(self, "Lỗi", f"Không thể lưu đơn hàng: {str(e)}")
            print(f"Error saving order: {str(e)}")
            
            # Debug thêm chi tiết lỗi
            import traceback
            traceback.print_exc()