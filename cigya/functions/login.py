
def login_clicked(self):
    cursor = self.conn.execute("SELECT name, password FROM user")
    for row in cursor:
        print("Name = {}, Password = {}".format(row[0], row[1]))
    # print(cursor)
    # print(self.usernameInput.text())

