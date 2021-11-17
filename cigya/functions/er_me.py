import re
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QMessageBox

def id_input(self):
    data = [int(self.patientIDInput.text())]
    cursor = self.conn.execute("SELECT * FROM medical_encounter WHERE patient_id = ?",tuple(data))
    for row in cursor:
        if str(row[1]) == str(self.dateInput.date().toString("MM/dd/yyyy")):
            query = f"SELECT name FROM user WHERE employee_id = {row[12]}"
            physicians_list = self.conn.execute(query)
            for physician in physicians_list:
                self.practitionerseenInput.setCurrentText(str(physician[0]))
                self.referralInput.setCurrentText(str(physician[0]))
            date = [int(out) for out in row[9].split("/")]
            self.followupInput.setDate(QDate(date[2], date[0], date[1]))
            self.practitionernotesInput.setText(row[5])
            self.vitalInput.setText(row[3])
            self.diagnosisInput.setText(row[6])
            self.treatmentInput.setText(row[7])
            return
    self.practitionerseenInput.setCurrentText("Trix Tesimon")
    self.followupInput.setDate(QDate(2000, 1, 1))
    self.referralInput.setCurrentText("Trix Tesimon")
    self.practitionernotesInput.clear()
    self.vitalInput.clear()
    self.diagnosisInput.clear()
    self.treatmentInput.clear()

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
            str(self.practitionernotesInput.toPlainText()),
            str(self.vitalInput.toPlainText()),
            str(self.diagnosisInput.toPlainText()),
            str(self.treatmentInput.toPlainText())
        ]  
        
        # if self.patientIDInput.text():
        #     sql = "INSERT INTO medical_encounter (name, number, address, birthdate, gender, carrier_id, primary_physician) VALUES (?, ?, ?, ?, ?, ?, ?)"
        # else:
        sql = """UPDATE medical_encounter SET notes = ?, vital_signs = ?, diagnosis = ?, treatment_plan = ? WHERE patient_id = ? AND scheduled_date = ?"""
        data.append(int(self.patientIDInput.text()))
        data.append(str(self.dateInput.date().toString("MM/dd/yyyy")))

        c = self.conn.cursor()
        c.execute(sql, tuple(data))
        self.conn.commit()