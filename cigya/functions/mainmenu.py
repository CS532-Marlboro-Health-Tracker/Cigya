def disable_restricted(self):
    pass

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