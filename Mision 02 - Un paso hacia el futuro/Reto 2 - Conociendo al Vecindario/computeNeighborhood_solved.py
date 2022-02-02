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
        for i in self.NEIGHBORS_R_EX:
            if self.row + i[0] >= 0 and self.col + i[1] >= 0:
                self.neighbors.append([self.row + i[0], self.col + i[1]])


# create grid
grid = []
for i in range(CELLS_PER_SIDE):
    grid.append([])
    for j in range(CELLS_PER_SIDE):
        cell = Cell(i, j)
        cell.updateNeighbors()
        grid[i].append(cell)


if __name__ == "__main__":
    # Acquire cell position from user input
    cell_position = input()
    cellCol, cellRow = [int(i) for i in cell_position.split(",")]
    if cellRow not in range(CELLS_PER_SIDE) or cellCol not in range(CELLS_PER_SIDE):
        sys.exit('cell index range error')

    # Check selected cell neighbors
    string = ''.join([''.join(str(element).split()) for element in grid[cellCol][cellRow].neighbors])
    print(string)
