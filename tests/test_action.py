import unittest
import sqlite3
from platform import system

class TestStringMethods(unittest.TestCase):
    conn = sqlite3.connect('../db/cigya.db') if (system() == "Darwin") else sqlite3.connect('db/cigya.db')

    def test_users(self):
        en_table = ['Electronic Patient Record', 'Physician Scheduler', 'Lab Order Tracking',
                'Pharmacy Order Tracking', 'Insurance Billing', 'Equipment Inventory and Maintenance']
        cursor = self.conn.execute("SELECT * FROM subsystem WHERE employee_id=:id", {"id":1})
        for i, row in enumerate(cursor):
            self.assertEqual(row[1],en_table[i])
    
if __name__ == '__main__':
    unittest.main()