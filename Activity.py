import random

class Activity:
    rooms = ["Beach 201", "Beach 301", "Frank 119", "Loft 206", "Loft 310", "James 325", "Roman 201", "Roman 216", "Slater 003", "Loft 310"]
    times = [10, 11, 12, 1, 2, 3]
    facilitators = ["Lock", "Glen", "Banks", "Richards", "Shaw", "Singer", "Uther", "Tyler", "Numen", "Zeldin"]

    def __init__(self, activity):
        self.activity = activity

    def roll(self):
        self.room = random.choice(self.rooms)
        self.time = random.choice(self.times)
        self.facilitator = random.choice(self.facilitators)

    