from core_data import ACTIVITIES, FACILITATORS, ROOMS, TIMES

# Issue 2 https://github.com/ZachJGreen/genetic-scheduler/issues/2
def fitness_calculate_final_score(population):
    schedule_scores = []
    for schedule in population:
        score = 0
        score += fitness_facilitator_load_check(schedule)

        score += fitness_activity_facilitator_check(schedule)

        score += fitness_room_capacity_check(schedule)

        score += fitness_activity_specific_adjustments(schedule)

        score += fitness_time_conflict_check(schedule)

        if hasattr(schedule, "set_score"):
            schedule.set_score(score)
        elif hasattr(schedule, "score"):
            schedule.score = score

        schedule_scores.append(score)
    return schedule_scores


def fitness_activity_specific_adjustments(schedule):
    score = 0
    assignments = schedule.assignments if hasattr(schedule, "assignments") else schedule

    time_index = {time_slot: idx for idx, time_slot in enumerate(TIMES)}

    sla101_sections = ["SLA101A", "SLA101B"]
    sla191_sections = ["SLA191A", "SLA191B"]

    def get_assignment(activity_name):
        return assignments[activity_name]

    def is_roman_or_beach(room_name):
        return room_name.startswith("Roman") or room_name.startswith("Beach")

    sla101a = get_assignment(sla101_sections[0])
    sla101b = get_assignment(sla101_sections[1])
    time_diff_101 = abs(time_index[sla101a["time"]] - time_index[sla101b["time"]])
    if time_diff_101 > 4:
        score += 0.5
    elif time_diff_101 == 0:
        score -= 0.5

    sla191a = get_assignment(sla191_sections[0])
    sla191b = get_assignment(sla191_sections[1])
    time_diff_191 = abs(time_index[sla191a["time"]] - time_index[sla191b["time"]])
    if time_diff_191 > 4:
        score += 0.5
    elif time_diff_191 == 0:
        score -= 0.5

    for activity_191 in sla191_sections:
        assignment_191 = get_assignment(activity_191)
        for activity_101 in sla101_sections:
            assignment_101 = get_assignment(activity_101)

            if assignment_191["facilitator"] != assignment_101["facilitator"]:
                continue

            diff = abs(
                time_index[assignment_191["time"]] - time_index[assignment_101["time"]]
            )

            if diff == 1:
                score += 0.5
                room_191_is_roman_or_beach = is_roman_or_beach(assignment_191["room"])
                room_101_is_roman_or_beach = is_roman_or_beach(assignment_101["room"])
                if room_191_is_roman_or_beach != room_101_is_roman_or_beach:
                    score -= 0.4
            elif diff == 2:
                score += 0.25
            elif diff == 0:
                score -= 0.25

    return score

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

