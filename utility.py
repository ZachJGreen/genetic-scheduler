#Shared constants and helper functions for scheduling.

import random

ACTIVITIES = ["SLA101A", "SLA101B", "SLA191A", "SLA191B", "SLA201", "SLA291", "SLA303", "SLA304", "SLA394", "SLA449", "SLA451"]
ROOMS = ["Beach 201", "Beach 301", "Frank 119", "Loft 206", "Loft 310", "James 325", "Roman 201", "Roman 216", "Slater 003", "Loft 310"]
TIMES = [10, 11, 12, 1, 2, 3]
FACILITATORS = ["Lock", "Glen", "Banks", "Richards", "Shaw", "Singer", "Uther", "Tyler", "Numen", "Zeldin"]


def random_room():
	return random.choice(ROOMS)


def random_time():
	return random.choice(TIMES)


def random_facilitator():
	return random.choice(FACILITATORS)