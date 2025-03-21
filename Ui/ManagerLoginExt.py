from PyQt6.QtWidgets import QMessageBox, QMainWindow

from Ui.ManagerLogin import Ui_LoginMainWindow
from Ui.WarehouseManagementExt import WarehouseManagementExt
from libs.DataConnector import DataConnector

class ManagerLoginExt(Ui_LoginMainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.data_connector = DataConnector()
        self.setupSignalsAndSlots()

    def setupSignalsAndSlots(self):
        self.pushButtonLogin.clicked.connect(self.process_login)

    def showWindow(self):
        self.MainWindow.show()

    def process_login(self):
        # Lấy thông tin đăng nhập
        username = self.lineEditUsername.text()
        password = self.lineEditPassword.text()
        
        # Danh sách manager (trong thực tế nên lưu trong database hoặc file riêng)
        managers = [
            {"username": "ilovetranduythanh", "password": "10diem10diem"},
        ]
        
        # Kiểm tra thông tin đăng nhập
        login_successful = False
        for manager in managers:
            if manager["username"] == username and manager["password"] == password:
                login_successful = True
                break
        
        if login_successful:
            # Đóng cửa sổ đăng nhập
            self.MainWindow.close()
            
            # Mở cửa sổ quản lý đơn hàng
            self.warehouse_window = QMainWindow()
            self.warehouse_manager = WarehouseManagementExt()
            self.warehouse_manager.setupUi(self.warehouse_window)
            self.warehouse_manager.showWindow()
        else:
            # Hiển thị thông báo lỗi
            QMessageBox.warning(
                self.MainWindow,
                "Login Failed",
                "Invalid username or password!"
            ) 