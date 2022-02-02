import sys

# Global variable that defines the number of cells per side the grid will have
CELLS_PER_SIDE = 32


# Define cell class
class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.neighbors = []  # Se utiliza vecindad a 8

    def updateNeighbors  # Se utiliza vecindad a 8



# create grid
grid = []
for i in range(CELLS_PER_SIDE):
    grid.append([])
    for j in range(CELLS_PER_SIDE):
        cell = Cell(i, j)
        cell.updateNeighbors()
        grid[i].append(cell)

# Acquire cell position from user input
cell_position = input()
cellRow_str, cellCol_str = cell_position.split(",")
cellRow, cellCol = int(cellRow_str), int(cellCol_str)
if cellRow not in range(CELLS_PER_SIDE) or cellCol not in range(CELLS_PER_SIDE):
    sys.exit('cell index range error')

# Check selected cell neighbors
string = ''.join([str(element) for element in grid[cellRow][cellCol].neighbors])
string = ''.join(string.split())
print(string)


# #############################################################################################################
# Este fragmento de codigo sirve unicamente para la visualizacion del resultado. No interviene de ninguna forma
# Puede ser completamente ignorado para la resolución del reto
# ATENCION: COMENTAR O ELIMINAR ESTA SECCION UNA VEZ SE VAYA A SUBIR EL SCRIPT COMO SOLUCION
# #############################################################################################################
# Visualization (COMMENT ALL OR ERASE IF UPLOADING THIS SCRIPT AS SOLUTION)
import pygame

WINDOW_SIDE = 512  # Window is a square
WINDOW = pygame.display.set_mode((WINDOW_SIDE, WINDOW_SIDE))
pygame.display.set_caption("Neighbors")
CELL_SIDE = WINDOW_SIDE // CELLS_PER_SIDE
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
TURQUOISE = (64, 224, 208)
GREY = (128, 128, 128)
while True:
    # Fill window with white color
    WINDOW.fill(WHITE)

    # Draw current cell and its neighbors
    pygame.draw.rect(WINDOW, YELLOW, (cellRow * CELL_SIDE, cellCol * CELL_SIDE, CELL_SIDE, CELL_SIDE))
    for neighbor in grid[cellRow][cellCol].neighbors:
        pygame.draw.rect(WINDOW, TURQUOISE,
                         (neighbor[0] * CELL_SIDE, neighbor[1] * CELL_SIDE, CELL_SIDE, CELL_SIDE))

    # Draw grid lines
    for i in range(CELLS_PER_SIDE):
        pygame.draw.line(WINDOW, GREY, (0, i * CELL_SIDE), (WINDOW_SIDE, i * CELL_SIDE))
        for j in range(CELLS_PER_SIDE):
            pygame.draw.line(WINDOW, GREY, (j * CELL_SIDE, 0), (j * CELL_SIDE, WINDOW_SIDE))

    pygame.display.update()  # refresh game window

    # Close game window if X window button clicked
    for event in pygame.event.get():  # For each event (key pressed/mouse clicked, etc) into the game screen
        if event.type == pygame.QUIT:  # if detected click on game window "X" button
            pygame.quit()  # quit pygame
            exit()  # end code
