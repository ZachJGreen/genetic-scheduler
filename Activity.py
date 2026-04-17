from utility import random_facilitator, random_room, random_time

class Activity:

    def __init__(self, activity):
        self.name = activity

    def roll(self):
        self.room = random_room()
        self.time = random_time()
        self.facilitator = random_facilitator()

    