# Issue 2 https://github.com/ZachJGreen/genetic-scheduler/issues/2
def fitness_calculate_final_score():
    return 0

# Issue 6 https://github.com/ZachJGreen/genetic-scheduler/issues/6
def fitness_facilitator_load_check():
    return 0


# Issue 5 https://github.com/ZachJGreen/genetic-scheduler/issues/5
def fitness_activity_facilitator_check():
    return 0

def facilitator_check(activity, facilitator, preferred, other):
    
    if facilitator in preferred.get(activity, []):
        return 0.5
    if facilitator in other.get(activity, []):
        return 0.2
    return -0.1

# Issue 4 https://github.com/ZachJGreen/genetic-scheduler/issues/4
def fitness_room_capacity_check():
    return 0

# Issue 3 https://github.com/ZachJGreen/genetic-scheduler/issues/3
def fitness_time_conflict_check():
    return 0


