from utility import FACILITATORS

# Issue 6 https://github.com/ZachJGreen/genetic-scheduler/issues/6

# Count number of times a facilitator is scheduled for activities in a schedule.
def count_facilitator_activities(schedule, facilitator):
    count = 0
    for activity in schedule.schedule:
        if activity.facilitator == facilitator:
            count += 1
    return count

def fitness_facilitator_load_check(schedule):
    for activity in schedule.schedule:
        for facilitator in FACILITATORS:
            score = 0
            count = count_facilitator_activities(schedule, facilitator)
            if count == 1:
                score += 0.2
            