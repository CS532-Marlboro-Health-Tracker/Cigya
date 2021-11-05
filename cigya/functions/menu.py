from PyQt5 import QtWidgets

def setup(self):
    self.menu = self.menuBar()
    self.setMenuBar(self.menu)

    exitAction = QtWidgets.QAction('&Close App', self)        
    exitAction.setShortcut('Ctrl+E')
    exitAction.setStatusTip('Close all applications')
    # exitAction.triggered.connect(lambda: close(self))

    self.fileMenu = self.menu.addMenu("&File")
    self.editMenu = self.menu.addMenu("&Edit")

    self.fileMenu.addAction(exitAction)

# def login_setup(self):


# def close(self):
#     #need to add confirmation here
#     self.cigyaApp.exit_app()