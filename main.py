from schedule import Schedule

def main():
    schedule = Schedule()
    schedule.generate_schedule()

    for activity in schedule.schedule:
        print(f"Activity: {activity.name}, Room: {activity.room}, Time: {activity.time}, Facilitator: {activity.facilitator}")

if __name__ == "__main__":
    main()