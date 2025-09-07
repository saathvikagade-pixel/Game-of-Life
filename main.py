import pygame
import sys
from simulation import Simulation
#from grid import Grid

pygame.init()

GREY = (29, 29, 29)
WINDOW_WIDTH = 750
WINDOW_HEIGHT = 750
CELL_SIZE = 25 # 750 x 750 grid. 750/25 = 30 pixels in both directions
FPS = 12 # Frames per second

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Game of Life")

clock = pygame.time.Clock() # Tracks how much time has passed
simulation = Simulation(WINDOW_WIDTH, WINDOW_HEIGHT, CELL_SIZE)
simulation.grid.cells[5][29] = 1
simulation.grid.cells[6][0] = 1
simulation.grid.cells[5][0] = 1
simulation.grid.cells[4][0] = 1

print(simulation.count_live_neighbours(simulation.grid, 5, 29))


'''
grid = Grid(WINDOW_WIDTH, WINDOW_HEIGHT, CELL_SIZE)
grid.cells[0][0] = 1
grid.cells[2][1] = 1 # 26:35 FOR RULES TO ADD TO README
'''

"""
Simulation Loop involves 3 stages:
    - Event Handling
    - Updating State
    - Drawing Objects
"""
# Simulation Loop
while True:

    # 1. Event Handling

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 2. Updating State

    # 3. Drawing Objects

    window.fill(GREY)
    simulation.draw(window)
    #grid.draw(window)

    pygame.display.update()
    clock.tick(FPS) # Runs at 12 FPS maximum, not always 12 FPS