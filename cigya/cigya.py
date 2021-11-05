from functions import menu, login, mainmenu, er, sched, lt, ib, lt
from PyQt5 import QtWidgets, uic
import sys
import sqlite3

class cigyaApp():
    def __init__(self):
        self.login_UI = loginUI(self)
        self.main_UI = mainUI(self)
        self.er_UI = erUI(self)
        self.sched_UI = schedUI(self)
        self.lt_UI = ltUI(self)
        self.pt_UI = ptUI(self)
        self.ib_UI = ibUI(self)
        self.eq_UI = eqUI(self)
    
    # def exit_app(self):
    #     print("Shortcut pressed") #verification of shortcut press
    #     self.close()

class cigyaUI(QtWidgets.QMainWindow):
    conn = sqlite3.connect('db/cigya.db')

    def __init__(self, cls):
        super(cigyaUI, self).__init__()
        self.cigyaApp = cls
        menu.setup(self)

    def getUIObj(self):
        items = self.findChildren(QtWidgets.QWidget)
        [setattr(self, item.objectName(), item) for item in items]

class loginUI(cigyaUI):
    def __init__(self, cls):
        super(loginUI, self).__init__(cls)
        uic.loadUi('cigya/ui/login.ui', self)
        self.signalSetup()

    def signalSetup(self):
        self.loginBtn.clicked.connect(lambda: login.login_clicked(self))
        
class mainUI(cigyaUI):
    def __init__(self, cls):
        super(mainUI, self).__init__(cls)
        uic.loadUi('cigya/ui/main.ui', self)
        self.signalSetup()
        mainmenu.disable_restricted(self)
    
    def signalSetup(self):
        self.eprlaunchBtn.clicked.connect(lambda: mainmenu.launch_ui(self,"er"))
        self.schedlaunchBtn.clicked.connect(lambda: mainmenu.launch_ui(self,"sched"))
        self.ltlaunchBtn.clicked.connect(lambda: mainmenu.launch_ui(self,"lt"))
        self.ptlaunchBtn.clicked.connect(lambda: mainmenu.launch_ui(self,"pt"))
        self.iblaunchBtn.clicked.connect(lambda: mainmenu.launch_ui(self,"ib"))
        self.eqlaunchBtn.clicked.connect(lambda: mainmenu.launch_ui(self,"eq"))

class erUI(cigyaUI):
    def __init__(self, cls):
        super(erUI, self).__init__(cls)
        uic.loadUi('cigya/ui/er.ui', self)
        self.signalSetup()
    
    def signalSetup(self):
        self.commitpatientBtn.clicked.connect(lambda: er.commitPatient(self))
        self.patientIDInput.textChanged.connect(lambda: er.id_input(self))

class schedUI(cigyaUI):
    def __init__(self, cls):
        super(schedUI, self).__init__(cls)
        uic.loadUi('cigya/ui/sched.ui', self)
        self.signalSetup()
    
    def signalSetup(self):
        pass

class ltUI(cigyaUI):
    def __init__(self, cls):
        super(ltUI, self).__init__(cls)
        uic.loadUi('cigya/ui/lt.ui', self)
        self.signalSetup()
    
    def signalSetup(self):
        pass

class ptUI(cigyaUI):
    def __init__(self, cls):
        super(ptUI, self).__init__(cls)
        uic.loadUi('cigya/ui/pt.ui', self)
        self.signalSetup()
    
    def signalSetup(self):
        pass

class ibUI(cigyaUI):
    def __init__(self, cls):
        super(ibUI, self).__init__(cls)
        uic.loadUi('cigya/ui/ib.ui', self)
        self.signalSetup()
    
    def signalSetup(self):
        pass

class eqUI(cigyaUI):
    def __init__(self, cls):
        super(eqUI, self).__init__(cls)
        uic.loadUi('cigya/ui/eq.ui', self)
        self.signalSetup()
    
    def signalSetup(self):
        pass

if __name__ == '__main__':
    print("Trix Tesimon,Physician,dgXcWH")
    app = QtWidgets.QApplication(sys.argv)
    window = cigyaApp()
    window.login_UI.show()
    app.exec_()
