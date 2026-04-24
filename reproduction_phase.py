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


def reproduce(population, target_size=None, mutation_rate=0.01):

    offspring = []
    
    parent_pairs = pairs(population)
    
    for parent1, parent2 in parent_pairs:
        # Get the assignments as dicts
        p1_assignments = parent1.to_dict()
        p2_assignments = parent2.to_dict()
        
        # Get list of activity names (same for both parents)
        activity_names = list(p1_assignments.keys())
        
        # Select a random crossover point (midpoint)
        # randint(1, n-1) ensures at least one activity from each parent
        midpoint = random.randint(1, len(activity_names) - 1)
        
        # Create two children by crossover
        child1_assignments = {}
        child2_assignments = {}
        
        for i, activity in enumerate(activity_names):
            if i < midpoint:
                # Before midpoint: child1 gets from parent1, child2 gets from parent2
                child1_assignments[activity] = dict(p1_assignments[activity])
                child2_assignments[activity] = dict(p2_assignments[activity])
            else:
                # After midpoint: child1 gets from parent2, child2 gets from parent1
                child1_assignments[activity] = dict(p2_assignments[activity])
                child2_assignments[activity] = dict(p1_assignments[activity])
        
        child1 = Schedule(assignments=child1_assignments)
        child2 = Schedule(assignments=child2_assignments)
        
        offspring.append(child1)
        offspring.append(child2)

    if target_size is not None:
        if target_size < 1:
            return []

        while len(offspring) < target_size and len(population) >= 2:
            extra_pair = pairs(population)
            if not extra_pair:
                break

            parent1, parent2 = extra_pair[0]
            p1_assignments = parent1.to_dict()
            p2_assignments = parent2.to_dict()
            activity_names = list(p1_assignments.keys())
            midpoint = random.randint(1, len(activity_names) - 1)

            child_assignments = {}
            for i, activity in enumerate(activity_names):
                if i < midpoint:
                    child_assignments[activity] = dict(p1_assignments[activity])
                else:
                    child_assignments[activity] = dict(p2_assignments[activity])

            offspring.append(Schedule(assignments=child_assignments))

        offspring = offspring[:target_size]

    mutate_population(offspring, mutation_rate)
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

