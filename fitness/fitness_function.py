

# Issue 2 https://github.com/ZachJGreen/genetic-scheduler/issues/2
def fitness_calculate_final_score(schedule):
    sum = 0
    sum += fitness_time_conflict_check(schedule)
    sum += fitness_room_capacity_check(schedule)
    sum += fitness_activity_facilitator_check(schedule)
    sum += fitness_facilitator_load_check(schedule)
    return sum



# Issue 5 https://github.com/ZachJGreen/genetic-scheduler/issues/5
def fitness_activity_facilitator_check(schedule):
    return 0

# Issue 4 https://github.com/ZachJGreen/genetic-scheduler/issues/4
def fitness_room_capacity_check(schedule):
    return 0

# Issue 3 https://github.com/ZachJGreen/genetic-scheduler/issues/3
def fitness_time_conflict_check(schedule):
    return 0


