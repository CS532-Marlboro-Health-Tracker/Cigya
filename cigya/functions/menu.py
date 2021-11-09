from PyQt5 import QtWidgets
import sys
import webbrowser

url = "https://github.com/CS532-Marlboro-Health-Tracker/Cigya"

def setup(self):
    self.menu = self.menuBar()
    self.setMenuBar(self.menu)

    printAction = QtWidgets.QAction('&Print', self)        
    printAction.setStatusTip('Print Current Screen')
    # exitAction.triggered.connect(lambda: close(self))

    exitAction = QtWidgets.QAction('&Close App', self)        
    exitAction.setShortcut('Ctrl+E')
    exitAction.setStatusTip('Close all applications')
    exitAction.triggered.connect(lambda: sys.exit())

    userAction = QtWidgets.QAction('&User Management', self)
    userAction.setStatusTip('Manage Users')
    # exitAction.triggered.connect(lambda: close(self))

    docAction = QtWidgets.QAction('&Documentation', self)
    docAction.setStatusTip('Get Online Documentation')
    docAction.triggered.connect(lambda: webbrowser.open(url))

    self.fileMenu = self.menu.addMenu("&File")
    self.menuMenu = self.menu.addMenu("&Menu")
    self.settingsMenu = self.menu.addMenu("&Settings")
    self.helpMenu = self.menu.addMenu("&Help")

    self.fileMenu.addAction(printAction)
    self.fileMenu.addAction(exitAction)
    self.settingsMenu.addAction(userAction)
    self.helpMenu.addAction(docAction)

    menu_setup(self)

def menu_setup(self):
    erAction = QtWidgets.QAction('&Electronic Patient Record', self)        
    erAction.setStatusTip('Open Electronic Patient Record GUI')
    erAction.triggered.connect(lambda: self.cigyaApp.er_UI.show())

    schedAction = QtWidgets.QAction('&Physician Scheduler', self)        
    schedAction.setStatusTip('Open Physician Scheduler GUI')
    schedAction.triggered.connect(lambda: self.cigyaApp.sched_UI.show())

    ltAction = QtWidgets.QAction('&Lab Order Tracking', self)        
    ltAction.setStatusTip('Open Lab Order Tracking GUI')
    ltAction.triggered.connect(lambda: self.cigyaApp.lt_UI.show())

    ptAction = QtWidgets.QAction('&Pharmacy Order Tracking', self)        
    ptAction.setStatusTip('Open Pharmacy Order Tracking GUI')
    ptAction.triggered.connect(lambda: self.cigyaApp.pt_UI.show())

    ibAction = QtWidgets.QAction('&Insurance Billing', self)        
    ibAction.setStatusTip('Open Insurance Billing GUI')
    ibAction.triggered.connect(lambda: self.cigyaApp.ib_UI.show())

    eqAction = QtWidgets.QAction('&Equipment Inventory', self)        
    eqAction.setStatusTip('Open Equipment Inventory Management GUI')
    eqAction.triggered.connect(lambda: self.cigyaApp.eq_UI.show())

    self.menuMenu.addAction(erAction)
    self.menuMenu.addAction(schedAction)
    self.menuMenu.addAction(ltAction)
    self.menuMenu.addAction(ptAction)
    self.menuMenu.addAction(ibAction)
    self.menuMenu.addAction(eqAction)