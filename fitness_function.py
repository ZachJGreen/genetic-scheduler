from core_data import ACTIVITIES, FACILITATORS, ROOMS, TIMES

# Issue 2 https://github.com/ZachJGreen/genetic-scheduler/issues/2
def fitness_calculate_final_score(population):
    schedule_scores = []
    for schedule in population:
        score = 0
        score += fitness_facilitator_load_check(schedule)

        score += fitness_activity_facilitator_check(schedule)

        score += fitness_room_capacity_check(schedule)

        score += fitness_time_conflict_check(schedule)

        if hasattr(schedule, "set_score"):
            schedule.set_score(score)
        elif hasattr(schedule, "score"):
            schedule.score = score

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
def fitness_activity_facilitator_check(schedule):
    score = 0

    for activity_name, assignment in schedule.items():
        facilitator = assignment["facilitator"]
        preferred = ACTIVITIES[activity_name]["preferred_facilitators"]
        other = ACTIVITIES[activity_name]["other_facilitators"]

        if facilitator in preferred:
            score += 0.5
        elif facilitator in other:
            score += 0.2
        else:
            score -= 0.1

    return score

# Issue 4 https://github.com/ZachJGreen/genetic-scheduler/issues/4
def fitness_room_capacity_check(schedule):
    score = 0

    for activity_name, assignment in schedule.items():
        expected_enrollment = ACTIVITIES[activity_name]["expected_enrollment"]
        room_capacity = ROOMS[assignment["room"]]

        if room_capacity < expected_enrollment:
            score -= 0.5
        elif room_capacity > expected_enrollment * 3:
            score -= 0.4
        elif room_capacity > expected_enrollment * 1.5:
            score -= 0.2
        else:
            score += 0.3

    return score

# Issue 3 https://github.com/ZachJGreen/genetic-scheduler/issues/3
def fitness_time_conflict_check(schedule):
    seen_time_room_pairs = set()

    for assignment in schedule.values():
        time_room_pair = (assignment["time"], assignment["room"])

        if time_room_pair in seen_time_room_pairs:
            return -0.5

        seen_time_room_pairs.add(time_room_pair)

    return 0

