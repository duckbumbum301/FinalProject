# Form implementation generated from reading ui file 'E:\Git_TDLT\FinalProject\Ui\Login.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1085, 784)
        MainWindow.setStyleSheet("background-color: rgb(245, 245, 220);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_logo = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_logo.setGeometry(QtCore.QRect(270, 220, 521, 191))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        self.label_logo.setFont(font)
        self.label_logo.setStyleSheet("background-color:transparent;")
        self.label_logo.setText("")
        self.label_logo.setPixmap(QtGui.QPixmap("E:\\Git_TDLT\\FinalProject\\Ui\\../images/cadty_logo.png"))
        self.label_logo.setScaledContents(True)
        self.label_logo.setObjectName("label_logo")
        self.pushButtoOrder = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtoOrder.setGeometry(QtCore.QRect(330, 420, 191, 71))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(20)
        self.pushButtoOrder.setFont(font)
        self.pushButtoOrder.setObjectName("pushButtoOrder")
        self.pushButtonManage = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonManage.setGeometry(QtCore.QRect(590, 420, 241, 71))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(20)
        self.pushButtonManage.setFont(font)
        self.pushButtonManage.setObjectName("pushButtonManage")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1085, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButtoOrder.setText(_translate("MainWindow", "Tap to order"))
        self.pushButtonManage.setText(_translate("MainWindow", "Manage System"))
