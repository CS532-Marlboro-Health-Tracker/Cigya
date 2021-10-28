
def login_clicked(self):
    cursor = self.conn.execute("SELECT name, password FROM user")
    for row in cursor:
        if row[0] == self.usernameInput.text():
            if row[1] == self.passwordInput.text():
                self.main.show()
                print("Login Under:\nName = {}, Password = {}".format(row[0], row[1]))
                return
    print("Invalid Username/Password Combination")

