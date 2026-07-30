import random
from agents.brain import Brain
class Agent:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.energy = 100
        self.age = 0
        self.alive = True
        self.brain = Brain()

    def move(self, world):

        self.x, self.y = self.brain.decide(self, world)

        self.energy -= 1
        self.age += 1

        cell = world.grid[self.y][self.x]

        if cell.energy > 0:
           self.energy += cell.energy
           cell.energy = 0
        if self.energy <= 0:
           self.alive = False