import psycopg2
from LoginUI import *
from InterfaceUI import *
import webbrowser
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

user_now = ""
class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        self.shadow.setOffset(5, 5)
        self.shadow.setBlurRadius(10)
        self.shadow.setColor(QtCore.Qt.black)
        self.ui.frame.setGraphicsEffect(self.shadow)

        self.ui.pushButton_login.clicked.connect(lambda :self.ui.stackedWidget_2.setCurrentIndex(0))
        self.ui.pushButton_register.clicked.connect(lambda :self.ui.stackedWidget_2.setCurrentIndex(1))
        self.ui.pushButton_l_sure.clicked.connect(self.login_in)
        self.ui.pushButton_d_sure.clicked.connect(self.register_in)

        self.show()
    def login_in(self):
        account = self.ui.lineEdit_l_account.text()
        password = self.ui.lineEdit_l_passward.text()
        print(account, password)
        # 数据库连接
        account_list = []
        password_list = []
        conn =psycopg2.connect(database="DataMy",user="postgres",password="123456",host="localhost",port="5432")
        cur = conn.cursor()
        cur.execute("select * from users")
        rows=cur.fetchall()
        for row in rows:
            account_list.append(row[0])
            password_list.append(row[1])
        print(account_list, password_list)
        conn.commit()
        cur.close()

        for i in range(len(account_list)):
            if len(account) == 0 or len(password) == 0:
                self.ui.stackedWidget.setCurrentIndex(1)

            elif account == account_list[i] and password == password_list[i]:
                global user_now
                user_now = account
                self.w=MyWindow()
                self.close()
            else:
                self.ui.stackedWidget.setCurrentIndex(2)
    def register_in(self):
        account = self.ui.lineEdit_d_account.text()
        password = self.ui.lineEdit_d_passward.text()
        password_sure = self.ui.lineEdit_d_rpassword.text()
        if len(account)==0 or len(password)==0 or len(password_sure)==0:
            self.ui.stackedWidget.setCurrentIndex(1)
        elif password != password_sure:
            self.ui.stackedWidget.setCurrentIndex(4)
        else:
            conn = psycopg2.connect(database="DataMy", user="postgres", password="123456", host="localhost", port="5432")
            cur = conn.cursor()
            cur.execute(f"insert into users values('{account}','{password}')")
            conn.commit()
            cur.close()
            self.ui.stackedWidget_2.setCurrentIndex(3)
            print("修改成功")



class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MyWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        self.shadow.setOffset(5, 5)
        self.shadow.setBlurRadius(20)
        # self.shadow.setColor(QtCore.Qt.black)
        self.ui.frame_6.setGraphicsEffect(self.shadow)

        self.ui.pushButton_home.clicked.connect(lambda :self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.pushButton_web.clicked.connect(self.gp_web)
        self.ui.pushButton_my.clicked.connect(lambda :self.ui.stackedWidget.setCurrentIndex(2))
        self.ui.pushButton_logout.clicked.connect(self.log_out)
        self.ui.pushButton_4.clicked.connect(self.change_password)
        self.show()
    def gp_web(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        self.ui.pushButton_bilibili.clicked.connect(lambda :webbrowser.open("https://www.bilibili.com/"))
        self.ui.pushButton_csdn.clicked.connect(lambda :webbrowser.open("https://blog.csdn.net/"))
        self.ui.pushButton_vedio.clicked.connect(lambda :webbrowser.open("https://www.iqiyi.com/"))
        self.ui.pushButton_apple.clicked.connect(lambda :webbrowser.open("https://www.apple.com/cn/"))

    def log_out(self):
        global user_now
        self.close()
        self.login = LoginWindow()
        user_now = ""

    def change_password(self):
        global user_now
        password=self.ui.lineEdit_m_pass.text()
        if len(self.ui.lineEdit_m_pass.text()) == 0 or len(self.ui.lineEdit_m_pass_sure.text()) == 0:
            self.ui.stackedWidget_2.setCurrentIndex(1)
        elif self.ui.lineEdit_m_pass.text() != self.ui.lineEdit_m_pass_sure.text():
            self.ui.stackedWidget_2.setCurrentIndex(2)
        elif self.ui.lineEdit_m_pass.text() == self.ui.lineEdit_m_pass_sure.text():
            conn = psycopg2.connect(database="DataMy", user="postgres", password="123456", host="localhost", port="5432")
            cur = conn.cursor()
            cur.execute(f"update users set passwords = '{password}' where accounts = '{user_now}'")
            conn.commit()
            cur.close()
            self.ui.stackedWidget_2.setCurrentIndex(3)
            print("修改成功")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = LoginWindow()
    # w = MyWindow()
    sys.exit(app.exec_())
