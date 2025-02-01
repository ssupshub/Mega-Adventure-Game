import random

class Location:
    def __init__(self):
        self.locations = ['Forest', 'Cave', 'Castle', 'Village']

    def random_location(self):
        return random.choice(self.locations)
