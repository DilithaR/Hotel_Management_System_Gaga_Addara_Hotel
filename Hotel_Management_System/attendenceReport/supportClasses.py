class EmpToday:
    def __init__(self , name , eId , date , timeIn , hrs):
        self.name = name
        self.eId = eId
        self.date = date
        self.timeIn = timeIn
        self.hrs = hrs


class EmpFull:
    def __init__(self, name, eId, expDays, totDays, leaves):
        self.name = name
        self.eId = eId
        self.expDays = expDays
        self.totDays = totDays
        self.leaves = leaves
