# Form implementation generated from reading ui file 'D:\FinalProject\Ui\ManagerLogin.ui'
#
# Created by: PyQt6 UI code generator 6.8.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_LoginMainWindow(object):
    def setupUi(self, LoginMainWindow):
        LoginMainWindow.setObjectName("LoginMainWindow")
        LoginMainWindow.resize(439, 291)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        LoginMainWindow.setFont(font)
        LoginMainWindow.setStyleSheet("QWidget {\n"
"    background-color: #FFF8E7; \n"
"    font-size: 12pt;\n"
"    color: #4E342E; \n"
"}")
        self.centralwidget = QtWidgets.QWidget(parent=LoginMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutMain = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayoutMain.setObjectName("verticalLayoutMain")
        self.groupBoxLoginInfo = QtWidgets.QGroupBox(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBoxLoginInfo.sizePolicy().hasHeightForWidth())
        self.groupBoxLoginInfo.setSizePolicy(sizePolicy)
        self.groupBoxLoginInfo.setMaximumSize(QtCore.QSize(16777215, 16777205))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBoxLoginInfo.setFont(font)
        self.groupBoxLoginInfo.setStyleSheet("QGroupBox {\n"
"    border: 2px solid #E6B89C; /* Soft brown */\n"
"    border-radius: 10px;\n"
"    margin-top: 10px;\n"
"    padding: 10px;\n"
"    font-weight: bold;\n"
"    color: #4E342E;\n"
"    background-color: #FFF3EB; \n"
"}\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding: 4px 12px;\n"
"    background-color: #FFE5B4; \n"
"    border-radius: 5px;\n"
"    font-size: 13pt;\n"
"    color: #4E342E;\n"
"}")
        self.groupBoxLoginInfo.setObjectName("groupBoxLoginInfo")
        self.formLayoutLogin = QtWidgets.QFormLayout(self.groupBoxLoginInfo)
        self.formLayoutLogin.setObjectName("formLayoutLogin")
        self.labelUsername = QtWidgets.QLabel(parent=self.groupBoxLoginInfo)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(62)
        self.labelUsername.setFont(font)
        self.labelUsername.setStyleSheet("QLabel {\n"
"    font-weight: 500;\n"
"    color: #5E3C28;\n"
"    background-color:transparent;\n"
"}")
        self.labelUsername.setObjectName("labelUsername")
        self.formLayoutLogin.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.labelUsername)
        self.lineEditUsername = QtWidgets.QLineEdit(parent=self.groupBoxLoginInfo)
        self.lineEditUsername.setStyleSheet("QLineEdit {\n"
"    background-color: #FFFDEB;\n"
"    border: 1px solid #D7A86E;\n"
"    border-radius: 6px;\n"
"    padding: 4px;\n"
"    min-height: 24px; \n"
"    max-height: 28px; \n"
"}")
        self.lineEditUsername.setObjectName("lineEditUsername")
        self.formLayoutLogin.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEditUsername)
        self.labelPassword = QtWidgets.QLabel(parent=self.groupBoxLoginInfo)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(62)
        self.labelPassword.setFont(font)
        self.labelPassword.setStyleSheet("QLabel {\n"
"    font-weight: 500;\n"
"    color: #5E3C28;\n"
"    background-color:transparent;\n"
"}")
        self.labelPassword.setObjectName("labelPassword")
        self.formLayoutLogin.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.labelPassword)
        self.lineEditPassword = QtWidgets.QLineEdit(parent=self.groupBoxLoginInfo)
        self.lineEditPassword.setStyleSheet("QLineEdit {\n"
"    background-color: #FFFDEB;\n"
"    border: 1px solid #D7A86E;\n"
"    border-radius: 6px;\n"
"    padding: 4px;\n"
"    min-height: 24px; \n"
"    max-height: 28px; \n"
"}")
        self.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.formLayoutLogin.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEditPassword)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.formLayoutLogin.setItem(0, QtWidgets.QFormLayout.ItemRole.LabelRole, spacerItem)
        self.verticalLayoutMain.addWidget(self.groupBoxLoginInfo)
        self.horizontalLayoutButtons = QtWidgets.QHBoxLayout()
        self.horizontalLayoutButtons.setObjectName("horizontalLayoutButtons")
        self.pushButtonLogin = QtWidgets.QPushButton(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonLogin.setFont(font)
        self.pushButtonLogin.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    padding: 8px 20px;\n"
"    border-radius: 10px;\n"
"    font-weight: bold;\n"
"    color: #4E342E;\n"
"    font-size: 11pt;\n"
"}\n"
"\n"
"QPushButton{\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #FFD1BA, stop:1 #FFB085);\n"
"    border: 2px solid #E6B89C;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #FBAF90;\n"
"    color: white;\n"
"}")
        self.pushButtonLogin.setObjectName("pushButtonLogin")
        self.horizontalLayoutButtons.addWidget(self.pushButtonLogin)
        self.pushButtonExit = QtWidgets.QPushButton(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonExit.setFont(font)
        self.pushButtonExit.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    padding: 8px 20px;\n"
"    border-radius: 10px;\n"
"    font-weight: bold;\n"
"    color: #4E342E;\n"
"    font-size: 11pt;\n"
"}\n"
"QPushButton {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"                                      stop:0 #FAD6A5, stop:1 #EAC084);\n"
"    border: 2px solid #D7A86E;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #EAB676;\n"
"    color: white;\n"
"}")
        self.pushButtonExit.setObjectName("pushButtonExit")
        self.horizontalLayoutButtons.addWidget(self.pushButtonExit)
        self.verticalLayoutMain.addLayout(self.horizontalLayoutButtons)
        LoginMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=LoginMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 439, 24))
        self.menubar.setObjectName("menubar")
        LoginMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=LoginMainWindow)
        self.statusbar.setObjectName("statusbar")
        LoginMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(LoginMainWindow)
        self.pushButtonExit.clicked.connect(LoginMainWindow.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(LoginMainWindow)

    def retranslateUi(self, LoginMainWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginMainWindow.setWindowTitle(_translate("LoginMainWindow", "Login System"))
        self.groupBoxLoginInfo.setTitle(_translate("LoginMainWindow", "Manager Login Information"))
        self.labelUsername.setText(_translate("LoginMainWindow", "Username:"))
        self.labelPassword.setText(_translate("LoginMainWindow", "Password:"))
        self.pushButtonLogin.setText(_translate("LoginMainWindow", "Login"))
        self.pushButtonExit.setText(_translate("LoginMainWindow", "Exit"))
