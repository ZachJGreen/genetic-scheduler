import random
from schedule import Schedule
from core_data import FACILITATORS, ROOMS, TIMES


def pairs(population):

    # Create a copy and shuffle to randomize pairings
    shuffled = list(population)
    random.shuffle(shuffled)
    
    # Pair them sequentially: (0,1), (2,3), (4,5), etc.
    # If odd number of parents, the last one doesn't get a pair
    paired = []
    for i in range(0, len(shuffled) - 1, 2):
        paired.append((shuffled[i], shuffled[i + 1]))
    
    return paired


def reproduce(population, target_size=None):

    offspring = []

    parent_pairs = pairs(population)
    if not parent_pairs:
        return offspring

    if target_size is None:
        target_size = len(population) * 2

    pair_index = 0
    while len(offspring) < target_size:
        parent1, parent2 = parent_pairs[pair_index % len(parent_pairs)]
        pair_index += 1

        p1_assignments = parent1.to_dict()
        p2_assignments = parent2.to_dict()

        activity_names = list(p1_assignments.keys())
        midpoint = random.randint(1, len(activity_names) - 1)

        child1_assignments = {}
        child2_assignments = {}

        for i, activity in enumerate(activity_names):
            if i < midpoint:
                child1_assignments[activity] = dict(p1_assignments[activity])
                child2_assignments[activity] = dict(p2_assignments[activity])
            else:
                child1_assignments[activity] = dict(p2_assignments[activity])
                child2_assignments[activity] = dict(p1_assignments[activity])

        child1 = Schedule(assignments=child1_assignments)
        child2 = Schedule(assignments=child2_assignments)

        offspring.append(child1)
        if len(offspring) < target_size:
            offspring.append(child2)

    mutate_population(offspring)
    return offspring


def mutate_schedule(schedule, mutation_rate=0.01):
    if random.random() >= mutation_rate:
        return schedule

    activity_names = list(schedule.assignments.keys())
    if not activity_names:
        return schedule

    random_activity = random.choice(activity_names)
    random_attribute = random.choice(["room", "time", "facilitator"])

    if random_attribute == "room":
        schedule.assignments[random_activity]["room"] = random.choice(list(ROOMS.keys()))
    elif random_attribute == "time":
        schedule.assignments[random_activity]["time"] = random.choice(TIMES)
    else:
        schedule.assignments[random_activity]["facilitator"] = random.choice(FACILITATORS)

    return schedule


def mutate_population(population, mutation_rate=0.01):
    for schedule in population:
        mutate_schedule(schedule, mutation_rate)
    return population

