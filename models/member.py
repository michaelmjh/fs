class Member:

    def __init__(self, first_name, last_name, active = True, member_id = None):
        self.first_name = first_name
        self.last_name = last_name
        self.active = active
        self.member_id = member_id
        

    def change_active_status(self):
        if self.active == True:
            self.active = False
        else:
            self.active = True

