import pygame
import random

class Grid:
    """
    Grid class
    """
    def __init__(self, width, height, cell_size):
        self.rows = height // cell_size
        self.columns = width // cell_size
        self.cell_size = cell_size
        self.cells = [[0 for _ in range(self.columns)] for _ in range(self.rows)]

    def draw(self, window):
        """
        Draw grid. Cell is green - alive - if cell's value is 1. Otherwise it is grey as it is 0
        """
        for row in range(self.rows):
            for column in range(self.columns):
                colour = (0, 255, 0) if self.cells[row][column] else (55, 55, 55)
                pygame.draw.rect(window, colour, (column * self.cell_size, row * self.cell_size, self.cell_size - 1, self.cell_size - 1)) # rect values consists of 4 values: x, y, width and height

    def fill_random(self):
        """
        Fill grid with random state of cells
        """
        for row in range(self.rows):
            for column in range(self.columns):
                self.cells[row][column] = random.choice([1, 0, 0, 0]) # 25% of cell being alive

    def clear(self):
        """
        Clear grid by assinging every cell's value to 0
        """
        for row in range(self.rows):
            for column in range(self.columns):
                self.cells[row][column] = 0

    def toggle_cell(self, row, column):
        """
        Toggle state of cell
        """
        if 0 <= row < self.rows and 0 <= column < self.columns: 
            self.cells[row][column] = not self.cells[row][column]