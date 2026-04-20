from Activity import *
from core_data import FACILITATORS, TIMES

# Issue 2 https://github.com/ZachJGreen/genetic-scheduler/issues/2
def fitness_calculate_final_score(population):
    schedule_scores = []
    for schedule in population:
        score = 0
        score += fitness_facilitator_load_check(schedule)

        schedule_scores.append(score)
    return schedule_scores

# Issue 6 https://github.com/ZachJGreen/genetic-scheduler/issues/6
def fitness_facilitator_load_check(schedule):
    score = 0
    facilitator_counts = {facilitator: 0 for facilitator in FACILITATORS}
    facilitator_time_counts = {
        facilitator: {time_slot: 0 for time_slot in TIMES}
        for facilitator in FACILITATORS
    }

    for activity in schedule.values():
        facilitator = activity["facilitator"]
        time_slot = activity["time"]
        facilitator_counts[facilitator] += 1
        facilitator_time_counts[facilitator][time_slot] += 1

    for facilitator in FACILITATORS:
        # Per-time-slot load checks.
        for time_slot in TIMES:
            count_in_slot = facilitator_time_counts[facilitator][time_slot]
            if count_in_slot == 1:
                score += 0.2
            elif count_in_slot > 1:
                score -= 0.2

        # Overall facilitator load checks.
        total_count = facilitator_counts[facilitator]
        if total_count > 4:
            score -= 0.5
        elif total_count < 3:
            if facilitator == "Tyler" and total_count < 2:
                pass
            else:
                score -= 0.4

    return score

# Issue 5 https://github.com/ZachJGreen/genetic-scheduler/issues/5
def fitness_activity_facilitator_check():
    return 0

# Issue 4 https://github.com/ZachJGreen/genetic-scheduler/issues/4
def fitness_room_capacity_check():
    return 0

# Issue 3 https://github.com/ZachJGreen/genetic-scheduler/issues/3
def fitness_time_conflict_check():
    return 0


