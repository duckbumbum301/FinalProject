# Form implementation generated from reading ui file 'D:\FinalProject\Ui\Login.ui'
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
        self.label_logo.setPixmap(QtGui.QPixmap("D:\\FinalProject\\Ui\\../images/cadty_logo.png"))
        self.label_logo.setScaledContents(True)
        self.label_logo.setObjectName("label_logo")
        self.pushButtoOrder = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtoOrder.setGeometry(QtCore.QRect(330, 420, 231, 91))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(20)
        self.pushButtoOrder.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("D:\\FinalProject\\Ui\\../images/ic_meo2.webp"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtoOrder.setIcon(icon)
        self.pushButtoOrder.setIconSize(QtCore.QSize(34, 34))
        self.pushButtoOrder.setObjectName("pushButtoOrder")
        self.pushButtonManage = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonManage.setGeometry(QtCore.QRect(590, 420, 231, 91))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(20)
        self.pushButtonManage.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("D:\\FinalProject\\Ui\\../images/ic_meobatluc.webp"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonManage.setIcon(icon1)
        self.pushButtonManage.setIconSize(QtCore.QSize(34, 34))
        self.pushButtonManage.setObjectName("pushButtonManage")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1085, 18))
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
