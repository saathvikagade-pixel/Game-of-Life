from grid import Grid

class Simulation:
    def __init__(self, width, height, cell_size):
        self.grid = Grid(width, height, cell_size)
        self.rows = height // cell_size
        self.columns = width // cell_size

    def draw(self, window):
        self.grid.draw(window)

    def count_live_neighbours(self, grid, row, column):
        """
        Each cell has 8 neighbours, directly above, below, left, to the right and in the 4 directions diagonally.
        This method uses a list of tuples to calculate neighbouring cells, wrapping around the grid
        """
        live_neighbours = 0

        neighbour_offsets = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for offset in neighbour_offsets:
            new_row = (row + offset[0]) % self.rows
            new_column = (column + offset[1]) % self.columns
            if self.grid.cells[new_row][new_column] == 1:
                live_neighbours += 1

        return live_neighbours