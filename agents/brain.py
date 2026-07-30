import random

class Brain:

    def decide(self, agent, world):

        best_x = agent.x
        best_y = agent.y
        best_energy = -1

        directions = [
            (0,0),
            (0,1),
            (0,-1),
            (1,0),
            (-1,0)
        ]

        for dx, dy in directions:

            nx = agent.x + dx
            ny = agent.y + dy

            if 0 <= nx < world.width and 0 <= ny < world.height:

                cell = world.grid[ny][nx]

                if cell.energy > best_energy:
                    best_energy = cell.energy
                    best_x = nx
                    best_y = ny

        if best_energy == 0:

            random.shuffle(directions)

            for dx, dy in directions:

                nx = agent.x + dx
                ny = agent.y + dy

                if 0 <= nx < world.width and 0 <= ny < world.height:
                    best_x = nx
                    best_y = ny
                    break

        return best_x, best_y