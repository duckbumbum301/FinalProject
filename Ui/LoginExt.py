from PyQt6.QtWidgets import QMainWindow

from Ui.Login import Ui_MainWindow
from Ui.self_orderExt import SelfOrderExt


class LoginMainWindowExt(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalsAndSlots()

    def setupSignalsAndSlots(self):
        self.pushButtoOrder.clicked.connect(self.openSelfOrderWindow)

    def openSelfOrderWindow(self):
        # Tạo thuộc tính self.self_order_window và self.self_order_ui
        self.self_order_window = QMainWindow()
        self.self_order_ui = SelfOrderExt()
        self.self_order_ui.setupUi(self.self_order_window)

        self.self_order_window.show()
        self.MainWindow.close()  # Đóng cửa sổ login

    def showWindow(self):
        self.MainWindow.show()