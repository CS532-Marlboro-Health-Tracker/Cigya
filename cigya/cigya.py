from functions import menu, login, mainmenu, er, sched, lt, ib, lt
from PyQt5 import QtWidgets, uic
import sys
import sqlite3
from platform import system

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

class cigyaUI(QtWidgets.QMainWindow):
    conn = sqlite3.connect('../db/cigya.db') if (system() == "Darwin") else sqlite3.connect('db/cigya.db')

    def __init__(self, cls):
        super(cigyaUI, self).__init__()
        self.cigyaApp = cls
        menu.setup(self)

class loginUI(cigyaUI):
    def __init__(self, cls):
        super(loginUI, self).__init__(cls)
        ui = 'ui/login.ui' if (system() == "Darwin") else 'cigya/ui/login.ui'
        uic.loadUi(ui, self)
        self.signalSetup()

    def signalSetup(self):
        self.loginBtn.clicked.connect(lambda: login.login_clicked(self))
        
class mainUI(cigyaUI):
    def __init__(self, cls):
        super(mainUI, self).__init__(cls)
        ui = 'ui/main.ui' if system() == "Darwin" else 'cigya/ui/main.ui'
        uic.loadUi(ui, self)
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
        ui = 'ui/er.ui' if (system() == "Darwin") else 'cigya/ui/er.ui'
        uic.loadUi(ui, self)
        self.signalSetup()
    
    def signalSetup(self):
        self.commitpatientBtn.clicked.connect(lambda: er.verifyCommit(self))
        self.patientIDInput.textChanged.connect(lambda: er.id_input(self))
        self.genderInput.addItem("Male")
        self.genderInput.addItem("Female")
        cursor = self.conn.execute("SELECT employee_id FROM physician")
        for row in cursor:
            query = f"SELECT name FROM user WHERE employee_id = {row[0]}"
            physicians_list = self.conn.execute(query)
            for physician in physicians_list:
                self.primaryphysicianInput.addItem(str(physician[0]))

class schedUI(cigyaUI):
    def __init__(self, cls):
        super(schedUI, self).__init__(cls)
        ui = 'ui/sched.ui' if (system() == "Darwin") else 'cigya/ui/sched.ui'
        uic.loadUi(ui, self)
        self.signalSetup()
    
    def signalSetup(self):
        pass

class ltUI(cigyaUI):
    def __init__(self, cls):
        super(ltUI, self).__init__(cls)
        ui = 'ui/lt.ui' if (system() == "Darwin") else 'cigya/ui/lt.ui'
        uic.loadUi(ui, self)
        self.signalSetup()
    
    def signalSetup(self):
        pass

class ptUI(cigyaUI):
    def __init__(self, cls):
        super(ptUI, self).__init__(cls)
        ui = 'ui/pt.ui' if (system() == "Darwin") else 'cigya/ui/pt.ui'
        uic.loadUi(ui, self)
        self.signalSetup()
    
    def signalSetup(self):
        pass

class ibUI(cigyaUI):
    def __init__(self, cls):
        super(ibUI, self).__init__(cls)
        ui = 'ui/ib.ui' if (system() == "Darwin") else 'cigya/ui/ib.ui'
        uic.loadUi(ui, self)
        self.signalSetup()
    
    def signalSetup(self):
        pass

class eqUI(cigyaUI):
    def __init__(self, cls):
        super(eqUI, self).__init__(cls)
        ui = 'ui/eq.ui' if (system() == "Darwin") else 'cigya/ui/eq.ui'
        uic.loadUi(ui, self)
        self.signalSetup()
    
    def signalSetup(self):
        pass

if __name__ == '__main__':
    print("Trix Tesimon, dgXcWH")
    app = QtWidgets.QApplication(sys.argv)
    window = cigyaApp()
    window.login_UI.show()
    app.exec_()