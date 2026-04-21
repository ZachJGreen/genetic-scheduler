import random
from core_data import *
class Activity:


    def __init__(self, name: str):
        if name not in ACTIVITIES:
            raise ValueError(f"Unknown activity name: {name}")

        self.name = name
        self.room = None
        self.time = None
        self.facilitator = None

    def roll(self) -> None:
       
        self.room = random.choice(list(ROOMS.keys()))
        self.time = random.choice(TIMES)
        self.facilitator = random.choice(FACILITATORS)

    def to_dict(self) -> dict:
      
        return {
            "room": self.room,
            "time": self.time,
            "facilitator": self.facilitator
        }


