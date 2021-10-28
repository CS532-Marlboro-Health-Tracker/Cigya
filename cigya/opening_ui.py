from PyQt5 import QtWidgets, uic
import sys

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('cigya/ui/login.ui', self) # Load the .ui file
        self.button = self.findChild(QtWidgets.QPushButton, 'loginBtn')
        self.button.clicked.connect(login_clicked)
        self.show() # Show the GUI

    #function that may be able to store data fields?
    def import_data(self):
        #name, done1 = QtWidgets.QInputDialog.getText(self, 'Input Dialog', 'Enter your name.')
        pass

def login_clicked():
    print("Login Clicked")

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    app.exec_()

