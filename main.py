import pygame
import sys
from simulation import Simulation

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
            sys.exit() # User is able to quit if desired

        elif event.type == pygame.MOUSEBUTTONDOWN: # If user clicks on a cell, toggle its state
            pos = pygame.mouse.get_pos()
            row = pos[1] // CELL_SIZE
            column = pos[0] // CELL_SIZE
            simulation.toggle_cell(row, column)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN: # User presses Enter key to start simulation
                simulation.start()
                pygame.display.set_caption("Game of Life is running")
            elif event.key == pygame.K_SPACE: # User presses Spacebar to stop simulation
                simulation.stop()
                pygame.display.set_caption("Game of Life has stopped")
            elif event.key == pygame.K_f: # User presses f key to make simulation faster
                FPS += 2
            elif event.key == pygame.K_s: # User presses s key to make simulation slower
                if FPS > 5:
                    FPS -= 2
            elif event.key == pygame.K_r: # User presses r key for a random state
                simulation.create_random_state()
            elif event.key == pygame.K_c: # User presses c key to clear grid
                simulation.clear()

    # 2. Updating State
    simulation.update()

    # 3. Drawing Objects

    window.fill(GREY)
    simulation.draw(window)

    pygame.display.update()
    clock.tick(FPS) # Runs at 12 FPS maximum, not always 12 FPS