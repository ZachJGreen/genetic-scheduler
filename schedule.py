from Activity import Activity
from utility import ACTIVITIES

class Schedule:
    
    def __init__(self):
        self.schedule = []

    def generate_schedule(self):
        for activity in ACTIVITIES:
            new_activity = Activity(activity)
            new_activity.roll()
            self.schedule.append(new_activity)
        