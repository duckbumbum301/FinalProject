from PyQt6.QtWidgets import QTableWidgetItem, QMessageBox
from PyQt6.QtCore import Qt
from Ui.WarehouseManagement import Ui_WarehouseManagementMainWindow
from libs.DataConnector import DataConnector
from Ui.invoice_report_dialog import InvoiceReportDialog
import json
import os

class WarehouseManagementExt(Ui_WarehouseManagementMainWindow):
    def __init__(self):
        super().__init__()
        self.data_connector = DataConnector()
        # Khởi tạo DataConnector sẽ tự động đọc dữ liệu khách hàng
        self.customers = self.data_connector.get_all_customers()
        # Đọc dữ liệu orders trực tiếp từ file JSON
        self.orders = self.read_orders_from_json()
        
    def read_orders_from_json(self):
        try:
            orders_file = os.path.join(self.data_connector.base_path, "orders.json")
            with open(orders_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error reading orders: {str(e)}")
            return []
        
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        
        # Thiết lập tiêu đề cửa sổ
        self.MainWindow.setWindowTitle("CADTY Order Management")
        
        # Thiết lập bảng sản phẩm
        self.setupTableHeaders()
        
        # Thiết lập sự kiện
        self.setupSignals()
        
        # Nạp dữ liệu khách hàng
        self.loadCustomers()

    def setupTableHeaders(self):
        # Thiết lập tiêu đề cho bảng sản phẩm
        headers = ["Product ID", "Product Name", "Price", "Quantity", "Subtotal"]
        self.tableWidgetProduct.setColumnCount(len(headers))
        self.tableWidgetProduct.setHorizontalHeaderLabels(headers)

    def setupSignals(self):
        # Kết nối sự kiện click vào khách hàng
        self.listWidgetWarehouse.itemClicked.connect(self.onCustomerSelected)
        
        # Kết nối các nút
        self.pushButtonRemoveCustomer.clicked.connect(self.removeCustomer)
        self.pushButtonClear.clicked.connect(self.clearCustomerDetails)
        self.pushButtonSaveUpdate.clicked.connect(self.updateCustomer)
        self.pushButtonDelete.clicked.connect(self.onDeleteButtonClicked)
        self.pushButtonInvoiceReporting.clicked.connect(self.generateInvoice)
        
        # Kết nối sự kiện thay đổi cell trong bảng
        self.tableWidgetProduct.cellChanged.connect(self.onCellChanged)

    def loadCustomers(self):
        # Xóa danh sách cũ
        self.listWidgetWarehouse.clear()
        
        # Sử dụng danh sách khách hàng đã được lấy trong __init__
        if self.customers:
            for customer in self.customers:
                self.listWidgetWarehouse.addItem(f"{customer.customer_id} - {customer.name}")

    def onCustomerSelected(self, item):
        # Lấy customer_id từ item được chọn
        customer_id = item.text().split(" - ")[0]
        
        # Lấy thông tin khách hàng
        customer = self.data_connector.find_customer_by_id(customer_id)
        if customer:
            # Hiển thị thông tin khách hàng
            self.displayCustomerDetails(customer)
            # Hiển thị đơn hàng của khách hàng
            self.displayCustomerOrders(customer_id)

    def displayCustomerDetails(self, customer):
        # Hiển thị thông tin khách hàng trong các lineEdit
        self.lineEditCustomerID.setText(customer.customer_id)
        self.lineEditCustomerName.setText(customer.name)
        self.lineEditPhone.setText(customer.phone)
        self.lineEditAddress.setText(customer.address)
        
        # Không cho phép chỉnh sửa Customer ID
        self.lineEditCustomerID.setReadOnly(True)
        # Không cho phép chỉnh sửa Order ID
        self.lineEditOrderID.setReadOnly(True)

    def displayCustomerOrders(self, customer_id):
        # Xóa dữ liệu cũ trong bảng
        self.tableWidgetProduct.setRowCount(0)
        
        # Lọc đơn hàng của khách hàng từ danh sách orders
        customer_orders = [order for order in self.orders if order['customer_id'] == customer_id]
        
        if not customer_orders:
            return
            
        # Lấy order đầu tiên để hiển thị
        order = customer_orders[0]  # Giả sử chỉ hiển thị đơn hàng đầu tiên
        self.lineEditOrderID.setText(order['order_id'])  # Hiển thị order ID
        
        # Ngắt kết nối tạm thời để tránh trigger sự kiện cellChanged
        self.tableWidgetProduct.cellChanged.disconnect()
        
        # Hiển thị chi tiết đơn hàng trong bảng
        if 'items' in order:
            total_value = 0
            for i, item in enumerate(order['items']):
                self.tableWidgetProduct.insertRow(i)
                
                # Lấy giá trị subtotal trực tiếp từ item
                subtotal = item.get('subtotal', 0)
                total_value += subtotal
                
                # Thêm thông tin vào bảng
                product_id_item = QTableWidgetItem(item.get('product_id', ''))
                product_id_item.setFlags(product_id_item.flags() & ~Qt.ItemFlag.ItemIsEditable)
                self.tableWidgetProduct.setItem(i, 0, product_id_item)
                
                product_name_item = QTableWidgetItem(item.get('name', ''))
                product_name_item.setFlags(product_name_item.flags() & ~Qt.ItemFlag.ItemIsEditable)
                self.tableWidgetProduct.setItem(i, 1, product_name_item)
                
                price_item = QTableWidgetItem(f"{item.get('price', 0):,}")
                price_item.setFlags(price_item.flags() | Qt.ItemFlag.ItemIsEditable)
                self.tableWidgetProduct.setItem(i, 2, price_item)
                
                quantity_item = QTableWidgetItem(str(item.get('quantity', 0)))
                quantity_item.setFlags(quantity_item.flags() | Qt.ItemFlag.ItemIsEditable)
                self.tableWidgetProduct.setItem(i, 3, quantity_item)
                
                subtotal_item = QTableWidgetItem(f"{subtotal:,}")
                subtotal_item.setFlags(subtotal_item.flags() & ~Qt.ItemFlag.ItemIsEditable)
                self.tableWidgetProduct.setItem(i, 4, subtotal_item)
            
            # Hiển thị tổng giá trị
            self.lineEditTotalValue.setText(f"{total_value:,} VND")
        
        # Kết nối lại sự kiện cellChanged
        self.tableWidgetProduct.cellChanged.connect(self.onCellChanged)

    def clearCustomerDetails(self):
        # Xóa thông tin khách hàng
        self.lineEditOrderID.setText("")  # Order ID
        self.lineEditCustomerID.setText("")  # Customer ID
        self.lineEditCustomerName.setText("")  # Customer Name
        self.lineEditPhone.setText("")  # Phone
        self.lineEditAddress.setText("")  # Address
        self.lineEditTotalValue.setText("0 VND")  # Total Value
        self.tableWidgetProduct.setRowCount(0)  # Xóa bảng sản phẩm

    def updateCustomer(self):
        # Lấy thông tin từ form
        customer_id = self.lineEditCustomerID.text()
        if not customer_id:
            QMessageBox.warning(self.MainWindow, "Error", "Please select a customer first!")
            return
            
        customer = self.data_connector.find_customer_by_id(customer_id)
        if not customer:
            return
            
        # Cập nhật thông tin khách hàng (chỉ cho phép sửa name, phone, address)
        customer.name = self.lineEditCustomerName.text()
        customer.phone = self.lineEditPhone.text()
        customer.address = self.lineEditAddress.text()
        
        try:
            # Lưu thông tin khách hàng vào file customers.json
            self.data_connector.save_customer(customer)
            
            # Lấy danh sách customers hiện tại từ file
            customers_file = os.path.join(self.data_connector.base_path, "customers.json")
            try:
                with open(customers_file, 'r', encoding='utf-8') as f:
                    customers = json.load(f)
            except:
                customers = []
            
            # Cập nhật thông tin khách hàng trong danh sách
            for i, cust in enumerate(customers):
                if cust.get('customer_id') == customer_id:
                    customers[i] = {
                        'customer_id': customer_id,
                        'name': customer.name,
                        'phone': customer.phone,
                        'address': customer.address
                    }
                    break
                
            # Ghi đè file customers.json
            with open(customers_file, 'w', encoding='utf-8') as f:
                json.dump(customers, f, indent=4, ensure_ascii=False)
            
            # Cập nhật lại danh sách trong bộ nhớ
            self.customers = self.data_connector.get_all_customers()
            
            # Nạp lại danh sách khách hàng trên UI
            self.loadCustomers()
            
            # Tìm và chọn lại item vừa cập nhật
            for i in range(self.listWidgetWarehouse.count()):
                item = self.listWidgetWarehouse.item(i)
                if item.text().startswith(customer_id):
                    self.listWidgetWarehouse.setCurrentItem(item)
                    break
            
            QMessageBox.information(self.MainWindow, "Success", "Customer information updated successfully!")
            
        except Exception as e:
            QMessageBox.warning(self.MainWindow, "Error", f"Failed to update data: {str(e)}")

    def removeCustomer(self):
        # Lấy khách hàng được chọn
        current_item = self.listWidgetWarehouse.currentItem()
        if not current_item:
            QMessageBox.warning(self.MainWindow, "Error", "Please select a customer to remove!")
            return
            
        customer_id = current_item.text().split(" - ")[0]
        
        # Xác nhận xóa
        reply = QMessageBox.question(self.MainWindow, "Confirm", 
                                   f"Are you sure you want to remove customer {customer_id}?",
                                   QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
                                   
        if reply == QMessageBox.StandardButton.Yes:
            try:
                # Xóa khách hàng khỏi file customers.json
                customers_file = os.path.join(self.data_connector.base_path, "customers.json")
                
                # Đọc danh sách customers hiện tại
                try:
                    with open(customers_file, 'r', encoding='utf-8') as f:
                        customers = json.load(f)
                except:
                    customers = []
                
                # Lọc bỏ customer cần xóa
                customers = [cust for cust in customers if cust.get('customer_id') != customer_id]
                
                # Ghi đè lại file customers.json
                with open(customers_file, 'w', encoding='utf-8') as f:
                    json.dump(customers, f, indent=4, ensure_ascii=False)
                
                # Xóa đơn hàng của khách hàng khỏi file orders.json
                orders_file = os.path.join(self.data_connector.base_path, "orders.json")
                
                # Đọc file orders.json
                try:
                    with open(orders_file, 'r', encoding='utf-8') as f:
                        orders = json.load(f)
                except:
                    orders = []
                
                # Lọc bỏ các đơn hàng của khách hàng bị xóa
                orders = [order for order in orders if order['customer_id'] != customer_id]
                
                # Lưu lại file orders.json
                with open(orders_file, 'w', encoding='utf-8') as f:
                    json.dump(orders, f, indent=4, ensure_ascii=False)
                
                # Cập nhật lại danh sách trong bộ nhớ
                self.orders = orders
                self.customers = self.data_connector.get_all_customers()  # Cập nhật lại danh sách customers
                
                # Xóa thông tin chi tiết và bảng sản phẩm
                self.clearCustomerDetails()
                self.tableWidgetProduct.setRowCount(0)
                
                # Xóa item được chọn khỏi listWidget
                row = self.listWidgetWarehouse.row(current_item)
                self.listWidgetWarehouse.takeItem(row)
                
                QMessageBox.information(self.MainWindow, "Success", "Customer and related orders removed successfully!")
                
            except Exception as e:
                QMessageBox.warning(self.MainWindow, "Error", f"Failed to remove customer: {str(e)}")

    def onDeleteButtonClicked(self):
        # Lấy dòng được chọn
        current_row = self.tableWidgetProduct.currentRow()
        if current_row < 0:
            QMessageBox.warning(self.MainWindow, "Lỗi", "Vui lòng chọn sản phẩm cần xóa!")
            return
        
        reply = QMessageBox.question(self.MainWindow, "Xác nhận", 
                                   "Bạn có chắc chắn muốn xóa sản phẩm này?",
                                   QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        
        if reply == QMessageBox.StandardButton.Yes:
            self.deleteProduct(current_row)

    def deleteProduct(self, row):
        try:
            # Lấy thông tin sản phẩm cần xóa
            product_id = self.tableWidgetProduct.item(row, 0).text()
            customer_id = self.lineEditCustomerID.text()
            order_id = self.lineEditOrderID.text()
            
            # Tìm order cần cập nhật
            for order in self.orders:
                if order['customer_id'] == customer_id and order['order_id'] == order_id:
                    # Lọc bỏ sản phẩm cần xóa
                    order['items'] = [item for item in order['items'] if item['product_id'] != product_id]
                    break
            
            # Lưu lại vào file orders.json
            orders_file = os.path.join(self.data_connector.base_path, "orders.json")
            with open(orders_file, 'w', encoding='utf-8') as f:
                json.dump(self.orders, f, indent=4, ensure_ascii=False)
            
            # Xóa dòng khỏi bảng
            self.tableWidgetProduct.removeRow(row)
            
            # Tính lại tổng giá trị
            total = 0
            for row in range(self.tableWidgetProduct.rowCount()):
                subtotal_str = self.tableWidgetProduct.item(row, 4).text().replace(',', '')
                total += float(subtotal_str)
            
            self.lineEditTotalValue.setText(f"{total:,} VND")
            
            QMessageBox.information(self.MainWindow, "Thành công", "Đã xóa sản phẩm thành công!")
            
        except Exception as e:
            QMessageBox.warning(self.MainWindow, "Lỗi", f"Không thể xóa sản phẩm: {str(e)}")
            # Nạp lại dữ liệu để đảm bảo tính nhất quán
            self.displayCustomerOrders(customer_id)

    def generateInvoice(self):
        # Lấy khách hàng được chọn
        current_item = self.listWidgetWarehouse.currentItem()
        if not current_item:
            QMessageBox.warning(self.MainWindow, "Lỗi", "Vui lòng chọn khách hàng để xem báo cáo!")
            return
            
        customer_id = current_item.text().split(" - ")[0]
        
        # Lấy thông tin khách hàng
        customer = self.data_connector.find_customer_by_id(customer_id)
        if not customer:
            QMessageBox.warning(self.MainWindow, "Lỗi", "Không tìm thấy thông tin khách hàng!")
            return
            
        # Lấy đơn hàng của khách hàng
        customer_orders = [order for order in self.orders if order['customer_id'] == customer_id]
        if not customer_orders:
            QMessageBox.warning(self.MainWindow, "Lỗi", "Không tìm thấy đơn hàng của khách hàng này!")
            return
            
        # Hiển thị cửa sổ báo cáo với đơn hàng đầu tiên
        dialog = InvoiceReportDialog(customer, customer_orders[0], self.MainWindow)
        dialog.exec()

    def onCellChanged(self, row, column):
        try:
            # Chỉ xử lý khi thay đổi cột Price (2) hoặc Quantity (3)
            if column not in [2, 3]:
                return
            
            # Lấy giá trị price và quantity
            price_str = self.tableWidgetProduct.item(row, 2).text().replace(',', '')
            quantity_str = self.tableWidgetProduct.item(row, 3).text()
            
            # Chuyển đổi sang số
            try:
                price = float(price_str)
                quantity = int(quantity_str)
            except ValueError:
                QMessageBox.warning(self.MainWindow, "Lỗi", "Giá trị không hợp lệ. Vui lòng nhập số.")
                self.displayCustomerOrders(self.lineEditCustomerID.text())
                return
            
            # Kiểm tra giá trị hợp lệ
            if price < 0 or quantity < 0:
                QMessageBox.warning(self.MainWindow, "Lỗi", "Giá trị không được âm.")
                self.displayCustomerOrders(self.lineEditCustomerID.text())
                return
            
            # Tính lại subtotal
            subtotal = price * quantity
            
            # Cập nhật subtotal trong bảng
            self.tableWidgetProduct.item(row, 4).setText(f"{subtotal:,}")
            
            # Cập nhật tổng giá trị
            total = 0
            for row in range(self.tableWidgetProduct.rowCount()):
                subtotal_str = self.tableWidgetProduct.item(row, 4).text().replace(',', '')
                total += float(subtotal_str)
            
            self.lineEditTotalValue.setText(f"{total:,} VND")
            
            # Cập nhật dữ liệu trong orders
            customer_id = self.lineEditCustomerID.text()
            order_id = self.lineEditOrderID.text()
            
            # Tìm order cần cập nhật
            for order in self.orders:
                if order['customer_id'] == customer_id and order['order_id'] == order_id:
                    # Cập nhật thông tin sản phẩm
                    product_id = self.tableWidgetProduct.item(row, 0).text()
                    for item in order['items']:
                        if item['product_id'] == product_id:
                            item['price'] = price
                            item['quantity'] = quantity
                            item['subtotal'] = subtotal
                    break
            
            # Lưu orders vào file
            try:
                orders_file = os.path.join(self.data_connector.base_path, "orders.json")
                with open(orders_file, 'w', encoding='utf-8') as f:
                    json.dump(self.orders, f, indent=4, ensure_ascii=False)
            except Exception as e:
                QMessageBox.warning(self.MainWindow, "Lỗi", f"Không thể lưu dữ liệu: {str(e)}")
            
        except Exception as e:
            QMessageBox.warning(self.MainWindow, "Lỗi", f"Đã xảy ra lỗi: {str(e)}")
            self.displayCustomerOrders(self.lineEditCustomerID.text())

    def showWindow(self):
        self.MainWindow.show()