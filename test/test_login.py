from PyQt6.QtWidgets import QApplication, QMainWindow

from Ui_Cadty.Ui.LoginExt import LoginMainWindowExt

app = QApplication([])
mainwindow = QMainWindow()
ui = LoginMainWindowExt()
ui.setupUi(mainwindow)
ui.showWindow()
app.exec()
