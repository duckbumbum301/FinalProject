from PyQt6.QtWidgets import QApplication, QMainWindow

from Ui.LoginExt import LoginExt

app = QApplication([])
mainwindow = QMainWindow()
ui = LoginExt()
ui.setupUi(mainwindow)
ui.showWindow()
app.exec()
