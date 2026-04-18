from Activity import Activity


class Schedule:
    activities = [
        "SLA101A", "SLA101B",
        "SLA191A", "SLA191B",
        "SLA201", "SLA291",
        "SLA303", "SLA304",
        "SLA394", "SLA449",
        "SLA451"
    ]

    def __init__(self):
        self.schedule = []

    def generate_schedule(self):
        self.schedule = []  

        for activity_name in self.activities:
            new_activity = Activity(activity_name)
            new_activity.roll()
            self.schedule.append(new_activity)

        return self.schedule

    def print_schedule(self):
        print("-" * 70)
        print(f"{'Activity':<10} {'Room':<12} {'Time':<6} {'Facilitator':<12}")
        print("-" * 70)

        for activity in self.schedule:
            print(
                f"{activity.name:<10} "
                f"{activity.room:<12} "
                f"{str(activity.time):<6} "
                f"{activity.facilitator:<12}"
            )

        print("-" * 70)

    def get_schedule(self):
        return self.schedule


if __name__ == "__main__":
    test_schedule = Schedule()
    test_schedule.generate_schedule()
    test_schedule.print_schedule()