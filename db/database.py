import sqlite3
import csv

# Connect to database
conn = sqlite3.connect('db/cigya.db')

# Create a cursor
c = conn.cursor()

# Create tables

c.execute("""CREATE TABLE IF NOT EXISTS medical_clinic (
    clinic_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT
    )""")

# Status INTEGER - 0 = pays on time, 1 = late with payments, 2 = difficult to get payment
c.execute("""CREATE TABLE IF NOT EXISTS insurance_carrier (
    carrier_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    address TEXT,
    status INTEGER
    )""")

c.execute("""CREATE TABLE IF NOT EXISTS service (
    service_id INTEGER PRIMARY KEY AUTOINCREMENT,
    description TEXT,
    billable_cost INTEGER
    )""")

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

c.execute("""CREATE TABLE IF NOT EXISTS user (
    employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    job_title TEXT,
    password TEXT,
    invoice_id INT,
    FOREIGN KEY (invoice_id) REFERENCES invoice (invoice_id)
    )""")

c.execute("""CREATE TABLE IF NOT EXISTS physician (
    number INTEGER,
    schedule TEXT,
    employee_id INT,
    FOREIGN KEY (employee_id) REFERENCES user (employee_id)
    )""")

c.execute("""CREATE TABLE IF NOT EXISTS pharmacist (
    is_fulltime INTEGER,
    employee_id INT,
    FOREIGN KEY (employee_id) REFERENCES user (employee_id)
    )""")

c.execute("""CREATE TABLE IF NOT EXISTS lab_technician (
    is_fulltime INTEGER,
    employee_id INT,
    FOREIGN KEY (employee_id) REFERENCES user (employee_id)
    )""")

c.execute("""CREATE TABLE IF NOT EXISTS nursing_staff (
    employee_id INT,
    FOREIGN KEY (employee_id) REFERENCES user (employee_id)
    )""")

c.execute("""CREATE TABLE IF NOT EXISTS assistant (
    employee_id INT,
    FOREIGN KEY (employee_id) REFERENCES user (employee_id)
    )""")

c.execute("""CREATE TABLE IF NOT EXISTS subsystem (
    subsystem_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    employee_id INT,
    FOREIGN KEY (employee_id) REFERENCES user (employee_id)
    )""")

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

c.execute("""CREATE TABLE IF NOT EXISTS lab_test (
    type_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    normal_values TEXT,
    dangerous_values TEXT
    )""")

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

c.execute("""CREATE TABLE IF NOT EXISTS prescription (
    prescription_id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INT,
    physician_id INT,
    FOREIGN KEY (patient_id) REFERENCES patient (patient_id)
    FOREIGN KEY (physician_id) REFERENCES physician (employee_id)
    )""")

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

c.execute("""CREATE TABLE IF NOT EXISTS performed_lab (
    date TEXT,
    technician_id INT,
    order_id INT,
    FOREIGN KEY (technician_id) REFERENCES lab_technician (employee_id),
    FOREIGN KEY (order_id) REFERENCES lab_order (order_id)
    )""")

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

c.execute("""CREATE TABLE IF NOT EXISTS service_provided (
    date TEXT,
    clinic_id INT,
    service_id INT,
    FOREIGN KEY (clinic_id) REFERENCES medical_clinic (clinic_id),
    FOREIGN KEY (service_id) REFERENCES service (service_id)
    )""")


# Insert into tables
# c.execute("INSERT INTO medical_clinic (name) VALUES ('Cigya')")
# c.execute("INSERT INTO insurance_carrier (name, address, status) VALUES ('Aetna', '10260 Meanley Dr.' , 0)")

# insurance_carriers = open("insurance_carriers.csv")
# rows_insurance_carriers = csv.reader(insurance_carriers)
# c.executemany(
#     "INSERT INTO insurance_carrier (name, address, status) VALUES (?,?,?)", rows)

# vendors = open("vendors.csv")
# rows_vendors = csv.reader(vendors)
# c.executemany(
#     "INSERT INTO vendor (name, address, is_preferred) VALUES (?,?,?)", rows_vendors)

# users = open("users.csv")
# rows_users = csv.reader(users)
# c.executemany(
#     "INSERT INTO user (name, job_title, password) VALUES (?,?,?)", rows_users)

# c.execute("INSERT INTO pharmacist (is_fulltime, employee_id) VALUES ('0', 7)")
# c.execute("INSERT INTO pharmacist (is_fulltime, employee_id) VALUES ('0', 9)")
# c.execute("UPDATE pharmacist SET is_fulltime = '1' WHERE employee_id = 9")

# c.execute("INSERT INTO lab_technician (is_fulltime, employee_id) VALUES ('0', 14)")
# c.execute("INSERT INTO lab_technician (is_fulltime, employee_id) VALUES ('1', 16)")

# c.execute("INSERT INTO nursing_staff (employee_id) VALUES (4)")
# c.execute("INSERT INTO nursing_staff (employee_id) VALUES (6)")
# c.execute("INSERT INTO nursing_staff (employee_id) VALUES (12)")
# c.execute("INSERT INTO nursing_staff (employee_id) VALUES (15)")
# c.execute("INSERT INTO nursing_staff (employee_id) VALUES (17)")
# c.execute("INSERT INTO nursing_staff (employee_id) VALUES (18)")
# c.execute("INSERT INTO nursing_staff (employee_id) VALUES (19)")
# c.execute("INSERT INTO nursing_staff (employee_id) VALUES (20)")

# c.execute("INSERT INTO assistant (employee_id) VALUES (2)")
# c.execute("INSERT INTO assistant (employee_id) VALUES (5)")
# c.execute("INSERT INTO assistant (employee_id) VALUES (11)")

# services = open("services.csv")
# rows_services = csv.reader(services)
# c.executemany(
#     "INSERT INTO service (description, billable_cost) VALUES (?,?)", rows_services)

# subsystems = open("subsystems.csv")
# rows_subsystems = csv.reader(subsystems)
# c.executemany(
#     "INSERT INTO subsystem (name) VALUES (?)", rows_subsystems)

# patients = open("patients.csv")
# rows_patients = csv.reader(patients)
# c.executemany(
#     "INSERT INTO patient (name, number, address, birthdate, gender) VALUES (?,?,?,?,?)", rows_patients)

# c.execute("INSERT INTO physician (number, employee_id) VALUES ('950-136-9177', 1)")
# c.execute("INSERT INTO physician (number, employee_id) VALUES ('958-186-9607', 3)")
# c.execute("INSERT INTO physician (number, employee_id) VALUES ('440-423-9937', 8)")
# c.execute("INSERT INTO physician (number, employee_id) VALUES ('950-324-2639', 10)")
# c.execute("INSERT INTO physician (number, employee_id) VALUES ('958-322-2234', 13)")

# c.execute("INSERT INTO prescription (patient_id, physician_id) VALUES (2, 13)")
# c.execute("INSERT INTO prescription (patient_id, physician_id) VALUES (4, 1)")
# c.execute("INSERT INTO prescription (patient_id, physician_id) VALUES (3, 1)")
# c.execute("INSERT INTO prescription (patient_id, physician_id) VALUES (5, 8)")

# c.execute("INSERT INTO medication (name, description, side_effects, dosage, frequency_of_use, prescription_id) VALUES ('Vicodin', 'Used to relieve moderate to severe pain','Nausea, vomiting, dizziness', '10 mg/300 mg', '1-2 tablets taken every 4-6 hours as needed', 1)")
# c.execute("INSERT INTO medication (name, description, side_effects, dosage, frequency_of_use, prescription_id) VALUES ('Vicodin', 'Used to relieve moderate to severe pain', 'Nausea, vomiting, dizziness', '10 mg/300 mg', '1-2 tablets taken every 4-6 hours as needed', 4)")
# c.execute("INSERT INTO medication (name, description, side_effects, dosage, frequency_of_use, prescription_id) VALUES ('Atorvastatin', 'Used reduce the risk of heart attack and stroke', 'Joint pain, insomnia, nausea, lost of appetite', '20 mg', 'Once a day', 2)")
# c.execute("INSERT INTO medication (name, description, side_effects, dosage, frequency_of_use, prescription_id) VALUES ('Metformin', 'Helps control blood sugar levels','Bloating, stomach pain, headache, muscle pain', '500 mg', 'Twice a day', 3)")

# c.execute("INSERT INTO filled_prescription (date, pharmacist_id, prescription_id) VALUES ('3/4/2021', 7, 1)")
# c.execute("INSERT INTO filled_prescription (date, pharmacist_id, prescription_id) VALUES ('9/9/2021', 7, 2)")
# c.execute("INSERT INTO filled_prescription (date, pharmacist_id, prescription_id) VALUES ('5/4/2021', 9, 3)")
# c.execute("INSERT INTO filled_prescription (date, pharmacist_id, prescription_id) VALUES ('10/8/2021', 7, 4)")

# encounters = open("db/medical_encounters.csv")
# rows_encounters = csv.reader(encounters)
# c.executemany(
#     "INSERT INTO medical_encounter (scheduled_date, date_created, patient_id, S_employee_id, W_employee_id) VALUES (?,?,?,?,?)", rows_encounters)

# c.execute("INSERT INTO lab_test (name, normal_values) VALUES ('White blood cells (WBCs)', '4.500-10.000 cells/mcL')")
# c.execute("INSERT INTO lab_test (name, normal_values) VALUES ('Red blood cell count (RBC)', 'Men: 14-17 gm/dL, Women: 12-15 gm/dL')")
# c.execute(
#     "INSERT INTO lab_test (name, normal_values) VALUES ('Mean corpuscular volume (MCV)', '70-95')")
# c.execute("INSERT INTO lab_test (name, normal_values) VALUES ('Hemoglobin (Hbg)', 'Men: 13-18 g/dL, Women: 12-16 g/dL')")

# lab_orders = open("db/lab_orders.csv")
# rows_lab_orders = csv.reader(lab_orders)
# c.executemany(
#     "INSERT INTO lab_order (result, physician_id, patient_id, type_id) VALUES (?,?,?,?)", rows_lab_orders)

# performed_labs = open("db/performed_lab.csv")
# rows_performed_labs = csv.reader(performed_labs)
# c.executemany(
#     "INSERT INTO performed_lab (date, technician_id, order_id) VALUES (?,?,?)", rows_performed_labs)

c.execute("SELECT * FROM performed_lab")

print(c.fetchall())

conn.commit()

conn.close()
