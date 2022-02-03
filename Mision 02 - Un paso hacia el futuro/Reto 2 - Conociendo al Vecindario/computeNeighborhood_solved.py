import sys

# Global variable that defines the number of cells per side the grid will have
CELLS_PER_SIDE = 32


# Define cell class
class Cell:

    NEIGHBORS_R    = [ [-1,-1], [-1,0], [-1,1], [0,-1], [0,1], [1,-1], [1,0], [1,1] ]
    NEIGHBORS_R_EX = [ [-1,0], [-1,1], [0,1], [1,1], [1,0], [1,-1], [0,-1], [-1,-1] ]

    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.neighbors = []  # Se utiliza vecindad a 8

    def updateNeighbors(self):  # Se utiliza vecindad a 8
        self.neighbors = []
        for r, c in self.NEIGHBORS_R_EX:
            if self.row + r in range(CELLS_PER_SIDE) and self.col + c in range(CELLS_PER_SIDE):
                self.neighbors.append([self.row + r, self.col + c])


# create grid
grid = []
for i in range(CELLS_PER_SIDE):
    grid.append([])
    for j in range(CELLS_PER_SIDE):
        cell = Cell(i, j)
        cell.updateNeighbors()
        grid[i].append(cell)


def get_neighbors_as_string(userIn):
    row, col = [int(i) for i in userIn.split(",")]
    if row not in range(CELLS_PER_SIDE) or col not in range(CELLS_PER_SIDE):
        return "cell index range error"
    return ''.join([str(element).replace(" ", "") for element in grid[row][col].neighbors])


if __name__ == "__main__":
    # Acquire cell position from user input
    string = get_neighbors_as_string(input())

    if "error" in string:
        sys.exit(string)
    print(string)

    # Check selected cell neighbors
    string = ''.join([''.join(str(element).split()) for element in grid[cellCol][cellRow].neighbors])
    print(string)
