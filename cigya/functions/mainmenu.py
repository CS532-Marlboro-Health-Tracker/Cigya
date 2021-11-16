def disable_restricted(self, id):
    en_table = {'Electronic Patient Record':self.eprlaunchBtn.setEnabled,
                'Physician Scheduler':self.schedlaunchBtn.setEnabled,
                'Lab Order Tracking':self.ltlaunchBtn.setEnabled,
                'Pharmacy Order Tracking':self.ptlaunchBtn.setEnabled,
                'Insurance Billing':self.iblaunchBtn.setEnabled,
                'Equipment Inventory and Maintenance':self.eqlaunchBtn.setEnabled}
    cursor = self.conn.execute("SELECT * FROM subsystem WHERE employee_id=:id", {"id":id})
    for row in cursor:
        en_table[row[1]](True)

def launch_ui(self, ui):
    if (ui == "er"):
        self.cigyaApp.er_UI.show()
    elif (ui == "sched"):
        self.cigyaApp.sched_UI.show()
    elif (ui == "lt"):
        self.cigyaApp.lt_UI.show()
    elif (ui == "pt"):
        self.cigyaApp.pt_UI.show()
    elif (ui == "ib"):
        self.cigyaApp.ib_UI.show()
    elif (ui == "eq"):
        self.cigyaApp.eq_UI.show()