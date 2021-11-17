import functions.mainmenu as mainmenu

def login_clicked(self):
    cursor = self.conn.execute("SELECT name, password, employee_id FROM user")
    for row in cursor:
        if row[0] == self.usernameInput.text():
            if row[1] == self.passwordInput.text():
                mainmenu.disable_restricted(self.cigyaApp.main_UI, row[2])
                self.cigyaApp.main_UI.show()
                self.hide()
                print("Login Under:\nName = {}, Password = {}".format(row[0], row[1]))
                return
    self.failLabel.setVisible(True)

