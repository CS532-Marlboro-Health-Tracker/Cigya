import re

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
    cursor = self.conn.execute("SELECT patient_id, name FROM patient")
    for row in cursor:
        print(row[0], row[1])
        # if row[0] == self.patientIDInput.text():
        #     print(self.patientIDInput.text())
        #     # return
    
def commitPatient(self):
    '''
    Function commits new patient to the DB. If the patient ID field is completed in at the time of calling this function, this function will
    serve as "updatePatient" instead, where the information portions filled out will be updated for the repsective ID provided in the DB.
    '''
    query = """
            INSERT INTO patient ('name', 'number', 'address', 'birthdate', 'gender', 'carrier_id', 'primary_physician') 
            VALUES (%s, %s, %s, %s, %s, %s, %s);
            """

    if len(self.patientIDInput.text()) == 0:
        patient_name:str = self.patientnameInput.text()
        patient_phone_number:str = self.phoneInput.text()
        patient_address:str = self.addressInput.text()
        patient_dob:str = self.dobInput.date()

        # FIXME: Genders are not available in the dropdown.
        patient_gender:str = self.genderInput.currentText()

        # FIXME: How does this connect with the DB?
        patient_insurance:str = self.insuranceInput.text()

        # FIXME: Primary physician is drop down in GUI, but integer field in the DB. Additionally, this field is queried from the DB. Need
        # to figure that out in order to populate these values.
        primary_physician:int = int(self.primaryphysicianInput.currentText())

        self.conn.cursor().executemany(query, (patient_name, patient_phone_number,patient_address,patient_dob,patient_gender,patient_insurance,primary_physician))
        self.conn.commit()
        print("Executed")