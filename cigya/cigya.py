from functions import login
from PyQt5 import QtWidgets, uic
import sys
import sqlite3

class loginUI(QtWidgets.QMainWindow):
    def __init__(self):
        super(loginUI, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('cigya/ui/login.ui', self) # Load the .ui file
        self.conn = sqlite3.connect('cigya.db')
        self.main = mainUI()
        self.signalSetup()
        self.show()

    def signalSetup(self):
        self.loginBtn = self.findChild(QtWidgets.QPushButton, 'loginBtn')
        self.loginBtn.clicked.connect(lambda: login.login_clicked(self))

        self.usernameInput = self.findChild(QtWidgets.QLineEdit, 'usernameInput')
        self.passwordInput = self.findChild(QtWidgets.QLineEdit, 'passwordInput')

class mainUI(QtWidgets.QMainWindow):
    def __init__(self):
        super(mainUI, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('cigya/ui/main.ui', self) # Load the .ui file
        self.signalSetup()

    def signalSetup(self):
        pass


if __name__ == '__main__':
    print("Trix Tesimon,Physician,dgXcWH")
    app = QtWidgets.QApplication(sys.argv)
    window = loginUI()
    app.exec_()
