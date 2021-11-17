import re
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QMessageBox

def id_input(self):
    data = [int(self.patientIDInput.text())]
    cursor = self.conn.execute("SELECT * FROM medical_encounter WHERE patient_id = ?",tuple(data))
    for row in cursor:
        if str(row[1]) == str(self.dateInput.date().toString("MM/dd/yyyy")):
            self.practitionernotesInput.setText(row[5])
            self.vitalInput.setText(row[3])
            self.diagnosisInput.setText(row[6])
            self.treatmentInput.setText(row[7])
            return
    # self.patientnameInput.clear()
    # self.phoneInput.clear()
    # self.dobInput.setDate(QDate(2000, 1, 1))
    # self.addressInput.clear()
    # self.insuranceInput.clear()
    # self.primaryphysicianInput.clear()

def verifyCommit(self):
    msg = QMessageBox()
    msg.setWindowTitle("Update Patient" if self.patientIDInput.text() else "Confirm New Patient")
    question = "Are you sure you want to update this patient?" if self.patientIDInput.text() else "Are you sure you want to commit a new patient?"
    rtn = msg.question(self,'', question, msg.Yes | msg.No)
    if rtn == msg.Yes:
        commitEncounter(self)

def commitEncounter(self):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Question)
    msg.setText("Are you sure you want to update this encounter?")
    msg.setWindowTitle("Update Encounter")
    msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    msg.setDefaultButton(QMessageBox.No)

    if msg.exec() == QMessageBox.Yes:
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