from Activity import Activity

class Schedule:
    activities = ["SLA101A", "SLA101B", "SLA191A", "SLA191B", "SLA201", "SLA291", "SLA303", "SLA304", "SLA394", "SLA449", "SLA451"]
    def __init__(self):
        self.schedule = []

    def generate_schedule(self):
        for activity in self.activities:
            new_activity = Activity(activity)
            new_activity.roll()
            self.schedule.append(new_activity)
        