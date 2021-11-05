from functions import login, mainmenu, er, sched
from PyQt5 import QtWidgets, uic
import sys
import sqlite3

# class cigyaApp():
#     def __init__(self):
#         self.login_UI = loginUI()
#         self.main_UI = mainUI()
#         self.er_UI = erUI()
#         self.sched_UI = schedUI()
#         self.lt_UI = ltUI()
#         self.pt_UI = ptUI()
#         self.ib_UI = ibUI()
#         self.eq_UI = eqUI()

class cigyaUI(QtWidgets.QMainWindow):
    conn = sqlite3.connect('db/cigya.db')

    def getUIObj(self):
        items = self.findChildren(QtWidgets.QWidget)
        [setattr(self, item.objectName(), item) for item in items]

class loginUI(cigyaUI):
    def __init__(self):
        super(cigyaUI, self).__init__()
        uic.loadUi('cigya/ui/login.ui', self)
        self.main_UI = mainUI()
        self.signalSetup()

    def signalSetup(self):
        self.loginBtn.clicked.connect(lambda: login.login_clicked(self))
        # self.loginBtn.setProperty()
        
class mainUI(cigyaUI):
    def __init__(self):
        super(cigyaUI, self).__init__()
        uic.loadUi('cigya/ui/main.ui', self)
        self.signalSetup()
        mainmenu.disable_unused(self)
    
    def signalSetup(self):
        self.ltlaunchBtn.clicked.connect(lambda: login.login_clicked(self))

class erUI(cigyaUI):
    def __init__(self):
        super(cigyaUI, self).__init__()
        uic.loadUi('cigya/ui/er.ui', self)
        self.signalSetup()
        mainmenu.disable_unused(self)
    
    def signalSetup(self):
        pass
class schedUI(cigyaUI):
    def __init__(self):
        super(cigyaUI, self).__init__()
        uic.loadUi('cigya/ui/sched.ui', self)
        self.signalSetup()
        mainmenu.disable_unused(self)
    
    def signalSetup(self):
        pass

class ltUI(cigyaUI):
    def __init__(self):
        super(cigyaUI, self).__init__()
        uic.loadUi('cigya/ui/lt.ui', self)
        self.signalSetup()
        mainmenu.disable_unused(self)
    
    def signalSetup(self):
        pass

class ptUI(cigyaUI):
    def __init__(self):
        super(cigyaUI, self).__init__()
        uic.loadUi('cigya/ui/pt.ui', self)
        self.signalSetup()
        mainmenu.disable_unused(self)
    
    def signalSetup(self):
        pass

class ibUI(cigyaUI):
    def __init__(self):
        super(cigyaUI, self).__init__()
        uic.loadUi('cigya/ui/ib.ui', self)
        self.signalSetup()
        mainmenu.disable_unused(self)
    
    def signalSetup(self):
        pass

class eqUI(cigyaUI):
    def __init__(self):
        super(cigyaUI, self).__init__()
        uic.loadUi('cigya/ui/eq.ui', self)
        self.signalSetup()
        mainmenu.disable_unused(self)
    
    def signalSetup(self):
        pass

if __name__ == '__main__':
    print("Trix Tesimon,Physician,dgXcWH")
    app = QtWidgets.QApplication(sys.argv)
    # window = cigyaApp()
    # window.login_UI.show()
    window = loginUI()
    window.show()
    app.exec_()
