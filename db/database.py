import sqlite3
import csv

# Connect to database
conn = sqlite3.connect('cigya.db')

# Create a cursor
c = conn.cursor()

# datatypes null, integer, real (float), text, blob

# Create tables

c.execute("""CREATE TABLE IF NOT EXISTS medical_clinic (
    clinic_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT
    )""")

c.execute("""CREATE TABLE IF NOT EXISTS insurance_carrier (
    carrier_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    address TEXT,
    status INTEGER
    )""")

# TODO
c.execute("""CREATE TABLE IF NOT EXISTS service (
    service_id INTEGER PRIMARY KEY AUTOINCREMENT,
    description TEXT,
    billable_cost INTEGER
    )""")

# TODO
c.execute("""CREATE TABLE IF NOT EXISTS vendor (
    vendor_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    address TEXT,
    is_preferred INTEGER
    )""")

# TODO
c.execute("""CREATE TABLE IF NOT EXISTS equipment (
    equipment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    type TEXT,
    description TEXT,
    department TEXT,
    vendor_id INT,
    FOREIGN KEY (vendor_id) REFERENCES vendor (vendor_id)
    )""")

# TODO
c.execute("""CREATE TABLE IF NOT EXISTS invoice (
    invoice_id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INT,
    FOREIGN KEY (patient_id) REFERENCES patient (patient_id)
    )""")

# TODO
c.execute("""CREATE TABLE IF NOT EXISTS user (
    employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    job_title TEXT,
    password TEXT,
    invoice_id INT,
    FOREIGN KEY (invoice_id) REFERENCES invoice (invoice_id)
    )""")

# TODO
c.execute("""CREATE TABLE IF NOT EXISTS physician (
    number INTEGER,
    schedule TEXT,
    employee_id INT,
    FOREIGN KEY (employee_id) REFERENCES user (employee_id)
    )""")

# TODO
c.execute("""CREATE TABLE IF NOT EXISTS pharmacist (
    is_fulltime INTEGER,
    employee_id INT,
    FOREIGN KEY (employee_id) REFERENCES user (employee_id)
    )""")

# TODO
c.execute("""CREATE TABLE IF NOT EXISTS lab_technician (
    is_fulltime INTEGER,
    employee_id INT,
    FOREIGN KEY (employee_id) REFERENCES user (employee_id)
    )""")

# TODO
c.execute("""CREATE TABLE IF NOT EXISTS nursing_staff (
    employee_id INT,
    FOREIGN KEY (employee_id) REFERENCES user (employee_id)
    )""")

# TODO
c.execute("""CREATE TABLE IF NOT EXISTS assistant (
    employee_id INT,
    FOREIGN KEY (employee_id) REFERENCES user (employee_id)
    )""")

# TODO
c.execute("""CREATE TABLE IF NOT EXISTS subsystem (
    subsystem_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    employee_id INT,
    FOREIGN KEY (employee_id) REFERENCES user (employee_id)
    )""")

# TODO
c.execute("""CREATE TABLE IF NOT EXISTS patient (
    patient_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    number INTEGER,
    address TEXT,
    birthdate TEXT,
    gender TEXT,
    carrier_id INT,
    primary_physician INT,
    FOREIGN KEY (carrier_id) REFERENCES carrier (carrier_id)
    FOREIGN KEY (primary_physician) REFERENCES physician (employee_id)
    )""")

# TODO
c.execute("""CREATE TABLE IF NOT EXISTS lab_test (
    type_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    normal_values TEXT,
    dangerous_values TEXT
    )""")

# TODO
c.execute("""CREATE TABLE IF NOT EXISTS lab_order (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    result TEXT,
    physician_id INT,
    patient_id INT,
    type_id INT,
    FOREIGN KEY (physician_id) REFERENCES physician (employee_id)
    FOREIGN KEY (patient_id) REFERENCES patient (patient_id)
    FOREIGN KEY (type_id) REFERENCES lab_test (type_id)
    )""")

# TODO
c.execute("""CREATE TABLE IF NOT EXISTS prescription (
    prescription_id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INT,
    physician_id INT,
    FOREIGN KEY (patient_id) REFERENCES patient (patient_id)
    FOREIGN KEY (physician_id) REFERENCES physician (employee_id)
    )""")

# TODO
c.execute("""CREATE TABLE IF NOT EXISTS medical_encounter (
    encounter_id INTEGER PRIMARY KEY AUTOINCREMENT,
    scheduled_date TEXT,
    date_created TEXT,
    patient_complaint TEXT,
    vital_signs TEXT,
    notes TEXT,
    diagnosis TEXT,
    treatment_plan TEXT,
    referral TEXT,
    follow_up TEXT,
    patient_id INT,
    S_employee_id INT,
    W_employee_id INT,
    FOREIGN KEY (patient_id) REFERENCES patient (patient_id),
    FOREIGN KEY (S_employee_id) REFERENCES user (employee_id),
    FOREIGN KEY (W_employee_id) REFERENCES user (employee_id)
    )""")

# TODO
c.execute("""CREATE TABLE IF NOT EXISTS medication (
    medication_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    description TEXT,
    reactions TEXT,
    side_effects TEXT,
    dosage TEXT,
    frequency_of_use TEXT,
    prescription_id INT,
    FOREIGN KEY (prescription_id) REFERENCES prescription (prescription_id)
    )""")

# TODO
c.execute("""CREATE TABLE IF NOT EXISTS performed_lab (
    date TEXT,
    technician_id INT,
    order_id INT,
    FOREIGN KEY (technician_id) REFERENCES lab_technician (employee_id),
    FOREIGN KEY (order_id) REFERENCES lab_order (order_id)
    )""")

# TODO
c.execute("""CREATE TABLE IF NOT EXISTS filled_prescription (
    date TEXT,
    pharmacist_id INT,
    prescription_id INT,
    FOREIGN KEY (pharmacist_id) REFERENCES pharmacist (employee_id)
    FOREIGN KEY (prescription_id) REFERENCES prescription (prescription_id)
    )""")

# TODO
c.execute("""CREATE TABLE IF NOT EXISTS maintenance (
    maintenance_id INTEGER PRIMARY KEY AUTOINCREMENT,
    resolution TEXT,
    problem_type TEXT,
    status TEXT,
    description TEXT,
    equipment_id INT,
    FOREIGN KEY (equipment_id) REFERENCES equipment (equipment_id)
    )""")

# TODO
c.execute("""CREATE TABLE IF NOT EXISTS invoice_item (
    item_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_invoiced TEXT,
    last_invoiced TEXT,
    date_paid TEXT,
    days_overdue INTEGER,
    invoice_id INT,
    service_id INT,
    FOREIGN KEY (invoice_id) REFERENCES invoice (invoice_id),
    FOREIGN KEY (service_id) REFERENCES service (service_id)
    )""")

# TODO
c.execute("""CREATE TABLE IF NOT EXISTS bought_equipment (
    date TEXT,
    warranty TEXT,
    clinic_id INT,
    equipment_id INT,
    FOREIGN KEY (clinic_id) REFERENCES medical_clinic (clinic_id),
    FOREIGN KEY (equipment_id) REFERENCES equipment (equipment_id)
    )""")

# TODO
c.execute("""CREATE TABLE IF NOT EXISTS leased_equipment (
    start_date TEXT,
    end_date TEXT,
    clinic_id INT,
    equipment_id INT,
    FOREIGN KEY (clinic_id) REFERENCES medical_clinic (clinic_id),
    FOREIGN KEY (equipment_id) REFERENCES equipment (equipment_id)
    )""")

# TODO
c.execute("""CREATE TABLE IF NOT EXISTS service_provided (
    date TEXT,
    clinic_id INT,
    service_id INT,
    FOREIGN KEY (clinic_id) REFERENCES medical_clinic (clinic_id),
    FOREIGN KEY (service_id) REFERENCES service (service_id)
    )""")


# Insert into tables
#c.execute("INSERT INTO medical_clinic (name) VALUES ('Cigya')")
#c.execute("INSERT INTO insurance_carrier (name, address, status) VALUES ('Aetna', '10260 Meanley Dr.' , 0)")


# insurance_carriers = open("insurance_carriers.csv")
# rows = csv.reader(insurance_carriers)
# c.executemany(
#     "INSERT INTO insurance_carrier (name, address, status) VALUES (?,?,?)", rows)

c.execute("SELECT * FROM medical_clinic")
c.execute("SELECT * FROM insurance_carrier")

print(c.fetchall())

conn.commit()

conn.close()
