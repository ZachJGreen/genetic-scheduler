import random
from schedule import Schedule


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


def reproduce(population):

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
                child1_assignments[activity] = p1_assignments[activity]
                child2_assignments[activity] = p2_assignments[activity]
            else:
                # After midpoint: child1 gets from parent2, child2 gets from parent1
                child1_assignments[activity] = p2_assignments[activity]
                child2_assignments[activity] = p1_assignments[activity]
        
        child1 = Schedule(assignments=child1_assignments)
        child2 = Schedule(assignments=child2_assignments)
        
        offspring.append(child1)
        offspring.append(child2)
    
    return offspring

