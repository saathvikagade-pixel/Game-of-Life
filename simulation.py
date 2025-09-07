from grid import Grid

class Simulation:
    def __init__(self, width, height, cell_size):
        self.grid = Grid(width, height, cell_size)
        self.temp_grid = Grid(width, height, cell_size)
        self.rows = height // cell_size
        self.columns = width // cell_size
        self.grid.fill_random()
        self.run = False 

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
    
    def update(self):
        if self.is_running():
            for row in range(self.rows):
                for column in range(self.columns):
                    live_neighbours = self.count_live_neighbours(self.grid, row, column)
                    cell_value = self.grid.cells[row][column]

                    if cell_value == 1:
                        if live_neighbours > 3 or live_neighbours < 2:
                            self.temp_grid.cells[row][column] = 0
                        else:
                            self.temp_grid.cells[row][column] = 1
                    else:
                        if live_neighbours == 3:
                            self.temp_grid.cells[row][column] = 1
                        else:
                            self.temp_grid.cells[row][column] = 0

            for row in range(self.rows):
                for column in range(self.columns):
                    self.grid.cells[row][column] = self.temp_grid.cells[row][column]

    def is_running(self):
        return self.run
    
    def start(self):
        self.run = True

    def stop(self):
        self.run = False