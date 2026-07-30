import random

class Cell:

    def __init__(self):

        if random.random() < 0.15:
            self.energy = random.randint(20,50)
        else:
            self.energy = 0

    def symbol(self):

        if self.energy > 0:
            return "E"

        return "."