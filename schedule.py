from Activity import Activity
from core_data import ACTIVITIES


class Schedule:
    def __init__(self, assignments=None, score=0):
        self.assignments = assignments if assignments is not None else {}
        self.score = score

    @classmethod
    def random_schedule(cls):
        assignments = {}

        for activity_name in ACTIVITIES:
            activity = Activity(activity_name)
            activity.roll()
            assignments[activity_name] = activity.to_dict()

        return cls(assignments=assignments)

    def items(self):
        return self.assignments.items()

    def values(self):
        return self.assignments.values()

    def to_dict(self):
        return dict(self.assignments)

    def set_score(self, score):
        self.score = score


def create_random_schedule():
    return Schedule.random_schedule()


def create_initial_population(size=500):
    if size < 1:
        raise ValueError("Population size must be at least 1.")

    population = []
    for _ in range(size):
        population.append(create_random_schedule())

    return population


def print_schedule(schedule):
    print("-" * 72)
    print(f"{'Activity':<10} {'Room':<12} {'Time':<6} {'Facilitator':<12}")
    print("-" * 72)

    for activity_name, assignment in schedule.items():
        print(
            f"{activity_name:<10} "
            f"{assignment['room']:<12} "
            f"{assignment['time']:<6} "
            f"{assignment['facilitator']:<12}"
        )

    print("-" * 72)


def print_population_summary(population):
    print("Population created successfully.")
    print(f"Total schedules: {len(population)}")

    if population:
        first_schedule = population[0]
        if hasattr(first_schedule, "assignments"):
            activity_count = len(first_schedule.assignments)
        else:
            activity_count = len(first_schedule)
        print(f"Activities per schedule: {activity_count}")


def sort_population_by_score(population, descending=True):
    return sorted(population, key=lambda schedule: schedule.score, reverse=descending)


if __name__ == "__main__":
    test_schedule = create_random_schedule()
    print_schedule(test_schedule)