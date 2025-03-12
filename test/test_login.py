from PyQt6.QtWidgets import QApplication, QMainWindow

from Ui.LoginExt import LoginMainWindowExt

app = QApplication([])
mainwindow = QMainWindow()
ui = LoginMainWindowExt()
ui.setupUi(mainwindow)
ui.showWindow()
app.exec()
