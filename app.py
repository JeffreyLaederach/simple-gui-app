# Copyright 2023, Jeffrey Laederach, All rights reserved.
########################################################################################################################

# LOGIN CREDENTIALS:
# Username: JLaederach
# Password: BikeAdillo

########################################################################################################################

import sys
import hashlib

from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QTabWidget,
    QVBoxLayout,
    QGridLayout,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton
)

from PySide6.QtWidgets import *
from PySide6.QtGui import QPixmap

class Dashboard(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        self.setFixedSize(1200, 628)
        self.resize(1200, 628)
        self.label = QLabel(self)
        self.pixmap = QPixmap('background.png')
        self.label.setPixmap(self.pixmap)
        self.label.resize(self.pixmap.width(),
                          self.pixmap.height())
        
        self.s = None

        """
        # Create a top-level layout
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.s = None 
        # Create the tab widget with two tabs
        tabs = QTabWidget()
        tabs.setFixedSize(350, 500)
        tabs.setTabPosition(QTabWidget.North)
        tabs.setStyleSheet("QTabBar::tab { height: 30px; width: 100px}")
        tabs.addTab(self.generalTabUI(), "Home")
        tabs.addTab(self.networkTabUI(), "Network")
        tabs.addTab(self.solutionsTabUI(), "Solutions")
        layout.addWidget(tabs)
        """

        btn = QPushButton(self)
        btn.setText('Sign Up')
        btn.move(1120,5)
        btn.clicked.connect(self.signup)
        btn.show()

        self.label = QLabel(self)
        self.label.setText("<font size='5'> <font color=White> © 2023 Jeffrey Laederach. All rights reserved. </font>")
        self.label.adjustSize()
        self.label.move(835, 600)
        self.show

        # Create a top-level layout
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        # Create the tab widget with two tabs
        self.layout.tabs = QTabWidget()
        t = self.layout.tabs
        t.setTabShape(QTabWidget.Rounded)
        t.setFixedSize(300, 400)
        t.setTabPosition(QTabWidget.North)
        t.setStyleSheet("QTabBar::tab { height: 30px; width: 100px}")
        t.addTab(self.generalTabUI(), "Home")
        t.addTab(self.networkTabUI(), "Network")
        t.addTab(self.solutionsTabUI(), "Solutions")
        self.layout.addWidget(t)
        t.setVisible(False)

        self.button = QPushButton("Menu", self)
        #self.button.setFixedSize()
        self.button.move(20, 20)
        self.button.setCheckable(True)
        self.button.clicked.connect(self.menu)
        self.update()
        self.show()

    def menu(self):
        if self.button.isChecked():
            self.layout.tabs.setVisible(True)
            
        else:
            self.layout.tabs.setVisible(False)

    def signup(self):
        if self.s is None:
            self.s = SignupForm()
        self.s.show()

    def generalTabUI(self):
        """Create the General page UI."""
        generalTab = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(QCheckBox("General Option 1"))
        layout.addWidget(QCheckBox("General Option 2"))
        generalTab.setLayout(layout)
        return generalTab

    def networkTabUI(self):
        """Create the Network page UI."""
        networkTab = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(QCheckBox("Network Option 1"))
        layout.addWidget(QCheckBox("Network Option 2"))
        networkTab.setLayout(layout)
        return networkTab

    def solutionsTabUI(self):
        """Create the Solutions page UI."""
        solutionsTab = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(QCheckBox("Solution Option 1"))
        layout.addWidget(QCheckBox("Solution Option 2"))
        layout.addWidget(QCheckBox("Solution Option 3"))
        solutionsTab.setLayout(layout)
        return solutionsTab

class LoginForm(QWidget):
    def __init__(self):
        super().__init__()
 
        self.acceptDrops()
        self.setWindowTitle("Login")
        self.setFixedSize(400, 400)
        self.resize(400, 400)

        layout = QGridLayout()

        label_name = QLabel("<font size='5'> <font color='black'> Username: </font>")
        self.lineEdit_username = QLineEdit()
        self.lineEdit_username.setPlaceholderText("Please enter your username")
        self.lineEdit_username.setStyleSheet(
                """QLineEdit { background-color: gray; color: white }""")
        layout.addWidget(label_name, 0, 0)
        layout.addWidget(self.lineEdit_username, 0, 1)

        label_password = QLabel("<font size='5'> <font color='black'> Password: </font>")
        self.lineEdit_password = QLineEdit()
        self.lineEdit_password.setPlaceholderText("Please enter your password")
        self.lineEdit_password.setEchoMode(QLineEdit.Password)
        self.lineEdit_password.setStyleSheet(
                """QLineEdit { background-color: gray; color: white }""")
        layout.addWidget(label_password, 1, 0)
        layout.addWidget(self.lineEdit_password, 1, 1)

        button_login = QPushButton('Login')
        button_login.clicked.connect(self.login_clicked)
        layout.addWidget(button_login, 2, 0, 1, 2)

        self.label = QLabel(self)
        self.pixmap = QPixmap('')
        self.label.setPixmap(self.pixmap)
        self.label.resize(self.pixmap.width(),
                          self.pixmap.height())
        
        self.d = None 
        self.setLayout(layout)
        self.show()

    def login_clicked(self):
        username = self.lineEdit_username.text()
        password = self.lineEdit_password.text()
        auth = password.encode()
        auth_hash = hashlib.md5(auth).hexdigest()
        with open("credentials.txt", "r") as f:
            stored_username, stored_password = f.read().split("\n")
        f.close()
        if username == stored_username and auth_hash == stored_password:
            if self.d is None:
                self.d = Dashboard()
            self.hide()
            self.d.show()
            
        else:
            mbox = QMessageBox()
            mbox.setIcon(QMessageBox.Critical)
            mbox.setWindowTitle("Login Failed")
            mbox.setText("Username or Password is incorrect!")
            mbox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            mbox.exec_()

class SignupForm(QWidget):
    def __init__(self):
        super().__init__()
 
        self.acceptDrops()
        self.setWindowTitle("Signup")
        self.setFixedSize(400,400)
        self.resize(400,400)

        layout = QGridLayout()

        label_name = QLabel("<font size='4'> <font color='black'> Username: </font>")
        self.lineEdit_username = QLineEdit()
        self.lineEdit_username.setPlaceholderText("Please enter your username")
        self.lineEdit_username.setStyleSheet(
                """QLineEdit { background-color: gray; color: white }""")
        layout.addWidget(label_name, 0, 0)
        layout.addWidget(self.lineEdit_username, 0, 1)

        label_password = QLabel("<font size='4'> <font color='black'> Password: </font>")
        self.lineEdit_password = QLineEdit()
        self.lineEdit_password.setPlaceholderText("Please enter your password")
        self.lineEdit_password.setEchoMode(QLineEdit.Password)
        self.lineEdit_password.setStyleSheet(
                """QLineEdit { background-color: gray; color: white }""")
        layout.addWidget(label_password, 1, 0)
        layout.addWidget(self.lineEdit_password, 1, 1)

        label_confirm_password = QLabel("<font size='4'> <font color='black'> Confirm Pwd: </font>")
        self.lineEdit_confirmpassword = QLineEdit()
        self.lineEdit_confirmpassword.setPlaceholderText("Please re-enter your password")
        self.lineEdit_confirmpassword.setEchoMode(QLineEdit.Password)
        self.lineEdit_confirmpassword.setStyleSheet(
                """QLineEdit { background-color: gray; color: white }""")
        layout.addWidget(label_confirm_password, 2, 0)
        layout.addWidget(self.lineEdit_confirmpassword, 2, 1)

        button_signup = QPushButton('Sign Up')
        layout.addWidget(button_signup, 3, 1, 1, 2)
        button_signup.clicked.connect(self.signup_clicked)

        self.label = QLabel(self)
        self.pixmap = QPixmap('')
        self.label.setPixmap(self.pixmap)
        self.label.resize(self.pixmap.width(),
                          self.pixmap.height())

        self.widget = QLabel("<font size='7'> <font color=gray> Create Credentials: </font>", self)
        self.widget.move(105, 10)
        self.show()
        
        self.setLayout(layout)
        self.show()

    def signup_clicked(self):

        print(self.lineEdit_username.text())
        print(self.lineEdit_password.text())
        print(self.lineEdit_confirmpassword.text())

        username = self.lineEdit_username.text()
        password = self.lineEdit_password.text()
        password_confirm = self.lineEdit_confirmpassword.text()

        if password_confirm == password:
            enc = password_confirm.encode()
            hash1 = hashlib.md5(enc).hexdigest()
            with open("credentials.txt", "w") as f:
                 f.write(username + "\n")
                 f.write(hash1)
            f.close()
            
            print("You have registered successfully!")

            mbox = QMessageBox()
            mbox.setWindowTitle("Signup Successful")
            mbox.setText("Credentials saved successfully!")
            mbox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            mbox.exec_()

        else:
            print("Password is not same as above! \n")

            mbox = QMessageBox()
            mbox.setWindowTitle("Signup Failed")
            mbox.setText("Passwords do not match!")
            mbox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            mbox.exec_()

#
if __name__ == "__main__":
   app = QApplication(sys.argv)
   app.setStyle('WindowsVista')
   
   login_form = LoginForm()
   login_form.show
   
   sys.exit(app.exec())
#

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Dashboard()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
   app = QApplication(sys.argv)
   app.setStyle('WindowsVista')
   
   signup_form = SignupForm()
   signup_form.show
   
   sys.exit(app.exec())
