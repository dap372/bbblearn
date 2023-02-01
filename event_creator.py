from datetime import datetime, timedelta

class event:
    def __init__(self, name, date, summary):
        self.NAME = name
        self.DATE = date
        self.SUMMARY = summary
    
    def get_week_num(self):
        return (self.DATE - datetime.today()).days // 7