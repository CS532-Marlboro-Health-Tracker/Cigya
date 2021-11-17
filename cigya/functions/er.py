import re
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QMessageBox

def id_input(self):
    self.patientnameInput.clear()
    self.phoneInput.clear()
    self.dobInput.setDate(QDate(2000, 1, 1))
    self.addressInput.clear()
    self.insuranceInput.clear() 
    self.medicationList.clear()
    self.labList.clear()
    self.scheduleList.clear()
    cursor = self.conn.execute("SELECT patient_id, name, number, address, birthdate, gender, carrier_id, primary_physician FROM patient")
    for row in cursor:
        if str(row[0]) == self.patientIDInput.text():
            self.patientnameInput.setText(row[1])
            self.phoneInput.setText(str(row[2]))
            date = [int(out) for out in row[4].split("/")]
            self.dobInput.setDate(QDate(date[2], date[0], date[1]))
            self.addressInput.setText(row[3])
            self.genderInput.setCurrentText(row[5])
            self.insuranceInput.setText(str(row[6]))
            populateLabOrders(self)
            if row[7] == 1:
                self.primaryphysicianInput.setCurrentText("Trix Tesimon")
            elif row[7] == 3:
                self.primaryphysicianInput.setCurrentText("Bay Meneer")
            elif row[7] == 8:
                self.primaryphysicianInput.setCurrentText("Delphinia Millan")
            elif row[7] == 10:
                self.primaryphysicianInput.setCurrentText("Trisha Cummungs")
            else:
                self.primaryphysicianInput.setCurrentText("Cobby MacFle")

            query = f"SELECT prescription_id FROM prescription WHERE patient_id = {self.patientIDInput.text()}"
            med_query = self.conn.execute(query)
            for med in med_query:
                medication_query = f"SELECT name, dosage FROM medication WHERE medication_id = {med[0]}"
                medicines = self.conn.execute(medication_query)
                for medicine in medicines:
                    self.medicationList.addItem(medicine[0] + " " + medicine[1])

            query = f"SELECT scheduled_date FROM medical_encounter WHERE patient_id = {self.patientIDInput.text()}"
            appt_query = self.conn.execute(query)
            for appt in appt_query:
                self.scheduleList.addItem(appt[0])

def populateLabOrders(self):
        data = [int(self.patientIDInput.text()) if self.patientIDInput.text() else None]
        cursor = self.conn.execute("SELECT * FROM lab_order WHERE patient_id = ?",tuple(data))
        for row in cursor:
            self.labList.addItem(str(row[0]) + " - " + str(row[1]))

def commitPatient(self):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Question)
    msg.setText("Are you sure you want to update this patient?" if self.patientIDInput.text() else "Are you sure you want to commit a new patient?")
    msg.setWindowTitle("Update Patient" if self.patientIDInput.text() else "Confirm New Patient")
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
        ]

        if str(self.primaryphysicianInput.currentText()) == "Trix Tesimon":
            data.append(1)
        elif str(self.primaryphysicianInput.currentText()) == "Bay Meneer":
            data.append(3)
        elif str(self.primaryphysicianInput.currentText()) == "Delphinia Millan":
            data.append(8)
        elif str(self.primaryphysicianInput.currentText()) == "Trisha Cummungs":
            data.append(10)
        else:
            data.append(13)

        if self.patientIDInput.text():
            sql = "UPDATE patient SET name = ?, number = ?, address = ?, birthdate = ?, gender = ?, carrier_id = ?, primary_physician = ? WHERE patient_id = ?"
            data.append(int(self.patientIDInput.text()))
        else:
            sql = "INSERT INTO patient (name, number, address, birthdate, gender, carrier_id, primary_physician) VALUES (?, ?, ?, ?, ?, ?, ?)"

        c = self.conn.cursor()
        c.execute(sql, tuple(data))
        self.conn.commit()