import re
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QMessageBox


def verifyInformation(self):
    #TODO: Fix name and address patterns.
    name_pattern:str = ("""
                    [a-zA-Z ]{2,}\s[a-zA-Z ]{2,}|
                    [a-zA-Z ]{2,}-[a-zA-Z ]{2,}\s[a-zA-Z ]{2,}|
                    [a-zA-Z ]{2,}\s[a-zA-Z ]{2,}-[a-zA-Z ]{2,}|
                    [a-zA-Z ]{2,}-[a-zA-Z ]{2,}\s[a-zA-Z ]{2,}-[a-zA-Z ]{2,}
                    """)
    phone_pattern:str = "[0-9]{3}-[0-9]{3}-[0-9]{4}"
    address_pattern:str = "[0-9]{1,}\s[A-Z]{1}[a-z]*\s(Street|St.|St|Drive|Dr.|Dr|Place|Pl.|Pl|Lane|Ln.|Ln)"
    insurance_carrier_pattern:str = "[0-9]{1,}\s"

    good_name:bool = bool(re.search(name_pattern, self.patientnameInput.text()))
    if not good_name:
        pass # TODO: Do something here.

    good_phone_number:bool = bool(re.search(name_pattern, self.phoneInput.text()))
    if not good_phone_number:
        pass # TODO: Do something here

    good_address:bool = bool(re.search(name_pattern, self.addressInput.text()))
    if not good_address:
        pass # TODO: Do something here

    good_insurance_carrier:bool = bool(re.search(name_pattern, self.insuranceInput.text()))
    if not good_insurance_carrier:
        pass # TODO: Do something here


    # Use this below in order to highlight border for incorrect entries.
    #myEditField.setStyleSheet("QLineEdit { border : 2px solid green;}")

    if good_name and good_phone_number and good_address and good_insurance_carrier:
        commitPatient(self)


def id_input(self):
    cursor = self.conn.execute("SELECT patient_id, name, number, address, birthdate, gender FROM patient")
    for row in cursor:
        if str(row[0]) == self.patientIDInput.text():
            self.patientnameInput.setText(row[1])
            self.phoneInput.setText(str(row[2]))
            date = [int(out) for out in row[4].split("/")]
            self.dobInput.setDate(QDate(date[2], date[0], date[1]))
            self.addressInput.setText(row[3])
            self.genderInput.setCurrentText(row[5])
            # FIXME: Fix DB so that it has information for insurance and primary care physician.
            # self.insuranceInput.setText(row[6])
            # self.primaryphysicianInput.setCurrentText(row[7])
            return
    self.patientnameInput.clear()
    self.phoneInput.clear()
    self.dobInput.setDate(QDate(2000, 1, 1))
    self.addressInput.clear()
    self.insuranceInput.clear()
    self.primaryphysicianInput.clear()

def verifyCommit(self):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Question)
    msg.setText("Are you sure you want to update this patient?" if self.patientIDInput.text() else "Are you sure you want to commit a new patient?")
    msg.setWindowTitle("Update Patient" if self.patientIDInput.text() else "Confirm New Patient")
    msg.exec()
    # FIXME: Fix this button.
    msg.setStandardButtons(QMessageBox.Ok)
    msg.buttonClicked.connect(commitPatient)

def commitPatient(self):
    data = [
        str(self.patientnameInput.text()),
        str(self.phoneInput.text()),
        str(self.addressInput.text()),
        str(self.dobInput.date().toString("MM/dd/yyyy")),
        str(self.genderInput.currentText()),
        str(self.insuranceInput.text()),
        str(self.primaryphysicianInput.currentText())
    ]



    
    
    if self.patientIDInput.text():
        sql = "INSERT INTO patient (name, number, address, birthdate, gender, carrier_id, primary_physician) VALUES (?, ?, ?, ?, ?, ?, ?)"
    else:
        sql = "UPDATE patient SET name = ?, number = ?, address = ?, birthdate = ?, gender = ?, carrier_id = ?, primary_physician = ? WHERE patient_id = ?"
        data.append(int(self.patientIDInput.text()))

    c = self.conn.cursor()
    c.execute(sql, tuple(data))
    self.conn.commit()