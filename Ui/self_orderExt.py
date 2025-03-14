from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem
from Ui.self_order import Ui_MainWindow

class SelfOrderExt(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.order_count = 0
        self.total_amount = 0.0

        # Mapping cho các nút Cookies (pushButton_add19 đến pushButton_add24)
        self.cookie_mapping = {
            "pushButton_add19": {"name": "Classic Choco Chip", "price": 35000},
            "pushButton_add20": {"name": "Dark Mix", "price": 40000},
            "pushButton_add21": {"name": "Cookies&Cream", "price": 45000},
            "pushButton_add22": {"name": "Creamy Matcha", "price": 45000},
            "pushButton_add23": {"name": "Twisted Love", "price": 45000},
            "pushButton_add24": {"name": "Oreo Chocolate", "price": 45000}
        }

        self.setupUi(self)
        self.setupSignalsAndSlots()
        self.setupTableHeaders()
        self.setupCookieButtons()

    def setupSignalsAndSlots(self):
        # Các nút chuyển giữa các trang menu
        self.pushButton_Mousse.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_Mousse))
        self.pushButton_Tart.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_Tart))
        self.pushButton_Croissant.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_Croissant))
        self.pushButton_Cookies.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_Cookies))
        self.pushButton_Drinks.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_Drinks))
        # Nếu có nút add cho các loại khác, bạn kết nối ở đây.

    def setupTableHeaders(self):
        # Nếu không có cột Size (sản phẩm không có size) thì đặt header 4 cột
        self.tableWidget_order.setColumnCount(4)
        headers = ["Item", "Price", "Quantity", "Subtotal"]
        self.tableWidget_order.setHorizontalHeaderLabels(headers)

    def setupCookieButtons(self):
        # Duyệt qua mapping và kết nối các nút tương ứng.
        # Chú ý: các đối tượng push button phải có tên trùng với tên trong mapping (ví dụ: pushButton_add19)
        for btn_name, cookie_info in self.cookie_mapping.items():
            btn = self.findChild(QtWidgets.QPushButton, btn_name)
            if btn:
                btn.cookie_info = cookie_info  # Lưu thông tin sản phẩm vào thuộc tính của button
                # Dùng lambda với đối số mặc định để tránh vấn đề late binding
                btn.clicked.connect(lambda checked, b=btn: self.onCookieButtonClicked(b))
            else:
                print(f"Button {btn_name} không được tìm thấy.")

    def onCookieButtonClicked(self, btn):
        info = btn.cookie_info
        self.addCookieToOrder(info)

    def addCookieToOrder(self, info):
        # Thêm món cookies vào giỏ hàng (table widget)
        item_name = info["name"]
        item_price = info["price"]
        item_quantity = 1  # Mặc định là 1; bạn có thể mở rộng cho người dùng chỉnh sửa sau
        item_subtotal = item_price * item_quantity
        self.total_amount += item_subtotal

        row_position = self.tableWidget_order.rowCount()
        self.tableWidget_order.insertRow(row_position)
        self.tableWidget_order.setItem(row_position, 0, QTableWidgetItem(item_name))
        self.tableWidget_order.setItem(row_position, 1, QTableWidgetItem(str(item_price)))
        self.tableWidget_order.setItem(row_position, 2, QTableWidgetItem(str(item_quantity)))
        self.tableWidget_order.setItem(row_position, 3, QTableWidgetItem(str(item_subtotal)))

        self.order_count += 1
        self.tableWidget_order.resizeColumnsToContents()
        print(f"Added cookie: {item_name} to order.")

    def clearOrderAndPushData(self):
        """
        Lấy dữ liệu từ tableWidget_order (giỏ hàng),
        xây dựng chuỗi tóm tắt đơn hàng và đẩy vào widget tóm tắt (order_summary_content),
        sau đó xóa sạch bảng giỏ hàng và reset các biến đếm.
        """
        order_summary = ""
        row_count = self.tableWidget_order.rowCount()
        col_count = self.tableWidget_order.columnCount()
        for row in range(row_count):
            row_data = []
            for col in range(col_count):
                item = self.tableWidget_order.item(row, col)
                row_data.append(item.text() if item else "")
            order_summary += "\t".join(row_data) + "\n"

        if hasattr(self, "order_summary_content"):
            self.order_summary_content.setPlainText(order_summary)
        else:
            print("Widget order_summary_content không tồn tại.")

        # Xóa dữ liệu trong bảng và reset biến đếm
        self.tableWidget_order.setRowCount(0)
        self.order_count = 0
        self.total_amount = 0.0
        print("Cleared order and updated summary.")

    def showWindow(self):
        self.show()
