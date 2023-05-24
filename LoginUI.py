# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoginUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(793, 663)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(60, 120, 271, 461))
        self.frame.setStyleSheet("#frame{\n"
"background-color: qlineargradient(spread:pad, x1:0.609195, y1:0.511, x2:1, y2:1, stop:0 rgba(48, 109, 119, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius:20\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(70, 70, 171, 41))
        self.label.setStyleSheet("font: 87 26pt \"Arial Black\";\n"
"font: 8pt \"Arial\";\n"
"font: 12pt \"Agency FB\";")
        self.label.setObjectName("label")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(330, 130, 301, 441))
        self.frame_2.setStyleSheet("#frame_2{\n"
"background-color: rgb(255, 255, 255);\n"
"border-top-right-radius：20px;\n"
"\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(210, 0, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setGeometry(QtCore.QRect(0, 60, 301, 371))
        self.frame_3.setMinimumSize(QtCore.QSize(301, 371))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_4 = QtWidgets.QFrame(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(6)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_6 = QtWidgets.QFrame(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.stackedWidget_2 = QtWidgets.QStackedWidget(self.frame_6)
        self.stackedWidget_2.setStyleSheet("QlineEdit{\n"
"\n"
"}")
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.page_login = QtWidgets.QWidget()
        self.page_login.setObjectName("page_login")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.page_login)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lineEdit_l_account = QtWidgets.QLineEdit(self.page_login)
        self.lineEdit_l_account.setMinimumSize(QtCore.QSize(0, 35))
        self.lineEdit_l_account.setObjectName("lineEdit_l_account")
        self.verticalLayout_3.addWidget(self.lineEdit_l_account)
        self.lineEdit_l_passward = QtWidgets.QLineEdit(self.page_login)
        self.lineEdit_l_passward.setMinimumSize(QtCore.QSize(0, 35))
        self.lineEdit_l_passward.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_l_passward.setObjectName("lineEdit_l_passward")
        self.verticalLayout_3.addWidget(self.lineEdit_l_passward)
        self.pushButton_l_sure = QtWidgets.QPushButton(self.page_login)
        self.pushButton_l_sure.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_l_sure.setObjectName("pushButton_l_sure")
        self.verticalLayout_3.addWidget(self.pushButton_l_sure)
        self.stackedWidget_2.addWidget(self.page_login)
        self.page_register = QtWidgets.QWidget()
        self.page_register.setObjectName("page_register")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.page_register)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lineEdit_d_account = QtWidgets.QLineEdit(self.page_register)
        self.lineEdit_d_account.setMinimumSize(QtCore.QSize(0, 35))
        self.lineEdit_d_account.setObjectName("lineEdit_d_account")
        self.verticalLayout_4.addWidget(self.lineEdit_d_account)
        self.lineEdit_d_passward = QtWidgets.QLineEdit(self.page_register)
        self.lineEdit_d_passward.setMinimumSize(QtCore.QSize(0, 35))
        self.lineEdit_d_passward.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_d_passward.setObjectName("lineEdit_d_passward")
        self.verticalLayout_4.addWidget(self.lineEdit_d_passward)
        self.lineEdit_d_rpassward = QtWidgets.QLineEdit(self.page_register)
        self.lineEdit_d_rpassward.setMinimumSize(QtCore.QSize(0, 35))
        self.lineEdit_d_rpassward.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_d_rpassward.setObjectName("lineEdit_d_rpassward")
        self.verticalLayout_4.addWidget(self.lineEdit_d_rpassward)
        self.pushButton_d_sure = QtWidgets.QPushButton(self.page_register)
        self.pushButton_d_sure.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_d_sure.setObjectName("pushButton_d_sure")
        self.verticalLayout_4.addWidget(self.pushButton_d_sure)
        self.stackedWidget_2.addWidget(self.page_register)
        self.horizontalLayout_3.addWidget(self.stackedWidget_2)
        self.verticalLayout_2.addWidget(self.frame_6)
        self.frame_7 = QtWidgets.QFrame(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_login = QtWidgets.QPushButton(self.frame_7)
        self.pushButton_login.setObjectName("pushButton_login")
        self.horizontalLayout_2.addWidget(self.pushButton_login)
        self.pushButton_register = QtWidgets.QPushButton(self.frame_7)
        self.pushButton_register.setObjectName("pushButton_register")
        self.horizontalLayout_2.addWidget(self.pushButton_register)
        self.verticalLayout_2.addWidget(self.frame_7)
        self.verticalLayout.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.page_2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.page_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.page_3)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.page_3)
        self.label_3.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.label_4 = QtWidgets.QLabel(self.page_4)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 297, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setStyleSheet("color: rgb(0, 170, 0);")
        self.label_4.setObjectName("label_4")
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.label_5 = QtWidgets.QLabel(self.page_5)
        self.label_5.setGeometry(QtCore.QRect(0, 0, 297, 51))
        self.label_5.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_5.setObjectName("label_5")
        self.stackedWidget.addWidget(self.page_5)
        self.horizontalLayout.addWidget(self.stackedWidget)
        self.verticalLayout.addWidget(self.frame_5)
        self.frame_2.raise_()
        self.frame.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget_2.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(0)
        self.pushButton.clicked.connect(MainWindow.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Welcome my world"))
        self.pushButton.setText(_translate("MainWindow", "退出"))
        self.lineEdit_l_account.setPlaceholderText(_translate("MainWindow", "账号："))
        self.lineEdit_l_passward.setPlaceholderText(_translate("MainWindow", "密码："))
        self.pushButton_l_sure.setText(_translate("MainWindow", "确认登陆"))
        self.lineEdit_d_account.setPlaceholderText(_translate("MainWindow", "账号："))
        self.lineEdit_d_passward.setPlaceholderText(_translate("MainWindow", "密码："))
        self.lineEdit_d_rpassward.setPlaceholderText(_translate("MainWindow", "再次输入密码："))
        self.pushButton_d_sure.setText(_translate("MainWindow", "确认注册"))
        self.pushButton_login.setText(_translate("MainWindow", "登录"))
        self.pushButton_register.setText(_translate("MainWindow", "注册"))
        self.label_2.setText(_translate("MainWindow", "         账号和密码不能为空"))
        self.label_3.setText(_translate("MainWindow", "         密码错误或账号不存在"))
        self.label_4.setText(_translate("MainWindow", "           账号注册成功"))
        self.label_5.setText(_translate("MainWindow", "             密码不一致"))