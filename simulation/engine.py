import time

from environment.world import World
from agents.agent import Agent


class Engine:

    def __init__(self):

        self.world = World(10,10)

        self.agents = [
            Agent(5,5)
        ]

        self.step = 0

    def update(self):

        self.step += 1

        for agent in self.agents:

            if agent.alive:
                agent.move(self.world)

    def render(self):
        print("Alive:", self.agents[0].alive)
        print("\n"*2)

        print("="*40)
        print("ASE STEP", self.step)
        print("="*40)

        self.world.display(self.agents[0])

    def run(self):

        while True:

            self.update()

            self.render()

            time.sleep(0.4)