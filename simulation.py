from grid import Grid

class Simulation:
    """
    Simulation class which uses methods from the Grid class
    """
    def __init__(self, width, height, cell_size):
        self.grid = Grid(width, height, cell_size)
        self.temp_grid = Grid(width, height, cell_size)
        self.rows = height // cell_size
        self.columns = width // cell_size
        self.run = False 

    def draw(self, window):
        """
        Draw grid
        """
        self.grid.draw(window)

    def count_live_neighbours(self, grid, row, column):
        """
        Each cell has 8 neighbours, directly above, below, left, to the right and in the 4 directions 
        diagonally. This method uses a list of tuples to calculate neighbouring cells, wrapping around 
        the grid for infinite space. 

        Takes as arguments the grid, row number and column number. Returns the number of live neighbours
        """
        live_neighbours = 0

        neighbour_offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for offset in neighbour_offsets:
            new_row = (row + offset[0]) % self.rows
            new_column = (column + offset[1]) % self.columns
            if self.grid.cells[new_row][new_column] == 1:
                live_neighbours += 1

        return live_neighbours
    
    def update(self):
        """
        Update the grid as it is running by using a temporary grid and then copying to the original
        grid
        """
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
        """
        Checks if simulation is running. Returns a Boolean value
        """
        return self.run
    
    def start(self):
        """
        Start simulation
        """
        self.run = True

    def stop(self):
        """
        Stop simulation
        """
        self.run = False
        
    def clear(self):
        """
        Clear grid
        """
        if self.is_running() == False:
            self.grid.clear()

    def create_random_state(self):
        """
        Create a random grid
        """
        if self.is_running() == False:
            self.grid.fill_random()

    def toggle_cell(self, row, column):
        """
        Toggle state of grid
        """
        if self.is_running() == False:
            self.grid.toggle_cell(row, column)