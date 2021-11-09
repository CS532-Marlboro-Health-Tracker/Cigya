import re
from PyQt5.QtCore import QDate

def verifyName(name:str) -> bool:
    '''
    Verifies the name provided to ensure it is alphabetic characters (and hyphens) only.
    '''
    name_pattern:str = "^[a-zA-z]+-?[a-zA-z]+$"
    return re.search(name_pattern, name)

def verifyPhone(phoneNumber:str) -> bool:
    # TODO: What is our pattern for phones numbers?
    phone_pattern:str = "[0-9]{10}"
    return re.search(phone_pattern, phoneNumber)

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
            return
    self.patientnameInput.clear()
    self.phoneInput.clear()
    self.dobInput.setDate(QDate(2000, 1, 1))
    self.addressInput.clear()
    
# def commitOrUpdatePatient(self):
#     if len(self.patientIDInput.text()) == 0:
#         commitPatient(self)
#     else:
#         updatePatient(self)


# def updatePatient(self):
#     pass


def commitPatient(self):
    '''
    Function commits new patient to the DB. If the patient ID field is completed in at the time of calling this function, this function will
    serve as "updatePatient" instead, where the information portions filled out will be updated for the repsective ID provided in the DB.
    '''

    #FIXME: Need to get a list of physicans for drop down?
    patient_name:str = self.patientnameInput.text()
    patient_phone_number:str = self.phoneInput.text()
    patient_address:str = self.addressInput.text()
    patient_dob:str = self.dobInput.date().toString("MM/dd/yyyy")
    patient_gender:str = self.genderInput.currentText()

    # FIXME: How does this connect with the DB?
    patient_insurance:str = self.insuranceInput.text()

    # FIXME: Primary physician is drop down in GUI, but integer field in the DB. Additionally, this field is queried from the DB. Need
    # to figure that out in order to populate these values.
    #primary_physician:int = int(self.primaryphysicianInput.currentText())
    primary_physician = 1

    # TODO: Primary physician needs to be identified from patient ID, then query needs to be made from DB for all matching physician IDs.

    data = [patient_name,
            patient_phone_number,
            patient_address,
            patient_dob, 
            patient_gender,
            patient_insurance,
            primary_physician]

    if self.patientIDInput.text():
        sql = "INSERT INTO patient (name, number, address, birthdate, gender, carrier_id, primary_physician) VALUES (?, ?, ?, ?, ?, ?, ?)"
    else:
        sql = "UPDATE patient SET name = ?, number = ?, address = ?, birthdate = ?, gender = ?, carrier_id = ?, primary_physician = ? WHERE patient_id = ?"
        data.append(int(self.patientIDInput.text()))

    c = self.conn.cursor()
    c.execute(sql, tuple(data))
    self.conn.commit()
    print("Executed")