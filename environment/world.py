from environment.cell import Cell

class World:

    def __init__(self,width,height):

        self.width = width
        self.height = height

        self.grid=[]

        for y in range(height):

            row=[]

            for x in range(width):
                row.append(Cell())

            self.grid.append(row)

    def display(self,agent):

        print()

        for y in range(self.height):

            row=[]

            for x in range(self.width):

                if x==agent.x and y==agent.y:
                    row.append("A")
                else:
                    row.append(self.grid[y][x].symbol())

            print(" ".join(row))

        print()