import random

# =========================
# Core data from assignment
# =========================

FACILITATORS = [
    "Lock", "Glen", "Banks", "Richards", "Shaw",
    "Singer", "Uther", "Tyler", "Numen", "Zeldin"
]

TIMES = ["10 AM", "11 AM", "12 PM", "1 PM", "2 PM", "3 PM"]

ROOMS = {
    "Beach 201": 18,
    "Beach 301": 25,
    "Frank 119": 95,
    "Loft 206": 55,
    "Loft 310": 48,
    "James 325": 110,
    "Roman 201": 40,
    "Roman 216": 80,
    "Slater 003": 32
}

ACTIVITIES = {
    "SLA101A": {
        "expected_enrollment": 40,
        "preferred_facilitators": ["Glen", "Lock", "Banks"],
        "other_facilitators": ["Numen", "Richards", "Shaw", "Singer"]
    },
    "SLA101B": {
        "expected_enrollment": 35,
        "preferred_facilitators": ["Glen", "Lock", "Banks"],
        "other_facilitators": ["Numen", "Richards", "Shaw", "Singer"]
    },
    "SLA191A": {
        "expected_enrollment": 45,
        "preferred_facilitators": ["Glen", "Lock", "Banks"],
        "other_facilitators": ["Numen", "Richards", "Shaw", "Singer"]
    },
    "SLA191B": {
        "expected_enrollment": 40,
        "preferred_facilitators": ["Glen", "Lock", "Banks"],
        "other_facilitators": ["Numen", "Richards", "Shaw", "Singer"]
    },
    "SLA201": {
        "expected_enrollment": 60,
        "preferred_facilitators": ["Glen", "Banks", "Zeldin", "Lock", "Singer"],
        "other_facilitators": ["Richards", "Uther", "Shaw"]
    },
    "SLA291": {
        "expected_enrollment": 50,
        "preferred_facilitators": ["Glen", "Banks", "Zeldin", "Lock", "Singer"],
        "other_facilitators": ["Richards", "Uther", "Shaw"]
    },
    "SLA303": {
        "expected_enrollment": 25,
        "preferred_facilitators": ["Glen", "Zeldin"],
        "other_facilitators": ["Banks"]
    },
    "SLA304": {
        "expected_enrollment": 20,
        "preferred_facilitators": ["Singer", "Uther"],
        "other_facilitators": ["Richards"]
    },
    "SLA394": {
        "expected_enrollment": 15,
        "preferred_facilitators": ["Tyler", "Singer"],
        "other_facilitators": ["Richards", "Zeldin"]
    },
    "SLA449": {
        "expected_enrollment": 30,
        "preferred_facilitators": ["Tyler", "Zeldin", "Uther"],
        "other_facilitators": ["Zeldin", "Shaw"]
    },
    "SLA451": {
        "expected_enrollment": 90,
        "preferred_facilitators": ["Lock", "Banks", "Zeldin"],
        "other_facilitators": ["Tyler", "Singer", "Shaw", "Glen"]
    }
}


class Activity:
    """
    Represents one scheduled activity with a randomly assigned
    room, time, and facilitator.
    """

    def __init__(self, name: str):
        if name not in ACTIVITIES:
            raise ValueError(f"Unknown activity name: {name}")

        self.name = name
        self.room = None
        self.time = None
        self.facilitator = None

    def roll(self) -> None:
        """
        Randomly assign one valid room, time, and facilitator.
        """
        self.room = random.choice(list(ROOMS.keys()))
        self.time = random.choice(TIMES)
        self.facilitator = random.choice(FACILITATORS)

    def to_dict(self) -> dict:
        """
        Convert this Activity object into dictionary form.
        """
        return {
            "room": self.room,
            "time": self.time,
            "facilitator": self.facilitator
        }


def create_random_schedule() -> dict:
    """
    Create one full random schedule.
    
    Returns:
        dict: A schedule where each activity has a room, time, and facilitator.
    """
    schedule = {}

    for activity_name in ACTIVITIES:
        activity = Activity(activity_name)
        activity.roll()
        schedule[activity_name] = activity.to_dict()

    return schedule


def create_initial_population(size: int = 250) -> list:
    """
    Create the initial population of random schedules.

    Args:
        size (int): Number of schedules to generate. Assignment says N >= 250.

    Returns:
        list: A list of schedule dictionaries.
    """
    if size < 1:
        raise ValueError("Population size must be at least 1.")

    population = []
    for _ in range(size):
        population.append(create_random_schedule())

    return population


# =====================
# Display / test helpers
# =====================

def print_schedule(schedule: dict) -> None:
    """
    Print a schedule in a readable format.
    """
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


def print_population_summary(population: list) -> None:
    """
    Print a simple summary of the generated population.
    """
    print(f"Population created successfully.")
    print(f"Total schedules: {len(population)}")

    if population:
        print(f"Activities per schedule: {len(population[0])}")


# =========
# Test code
# =========

if __name__ == "__main__":
    # Test one random schedule
    sample_schedule = create_random_schedule()
    print("SAMPLE RANDOM SCHEDULE")
    print_schedule(sample_schedule)

    # Test initial population
    population = create_initial_population(250)
    print_population_summary(population)