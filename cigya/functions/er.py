def id_input(self):
    cursor = self.conn.execute("SELECT patient_id, name FROM patient")
    for row in cursor:
        print(row[0], row[1])
        # if row[0] == self.patientIDInput.text():
        #     print(self.patientIDInput.text())
        #     # return
    
def commitPatient(self):
    cursor = self.conn.cursor()
    values_to_insert = [(self.patientIDInput.text(), "Mary Lane")]
    cursor.executemany("""INSERT INTO patient
                       (name, address) VALUES (?, ?)""", values_to_insert)
    self.conn.commit()
    print("Executed")