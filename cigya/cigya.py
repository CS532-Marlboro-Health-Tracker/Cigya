from functions import login
from PyQt5 import QtWidgets, uic
import sys
import sqlite3

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('cigya/ui/login.ui', self) # Load the .ui file
        self.conn = sqlite3.connect('cigya.db')
        self.signalSetup()
        self.show() # Show the GUI

    def signalSetup(self):
        self.loginBtn = self.findChild(QtWidgets.QPushButton, 'loginBtn')
        self.loginBtn.clicked.connect(lambda: login.login_clicked(self))

        self.usernameInput = self.findChild(QtWidgets.QLineEdit, 'usernameInput')

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    app.exec_()
