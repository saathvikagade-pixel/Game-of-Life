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
        cells = grid.cells
        rows, cols = self.rows, self.columns
        cnt = 0
        for dr, dc in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
            cnt += 1 if cells[(row+dr)%rows][(column+dc)%cols] == 1 else 0
        return cnt
    
    def update(self):
        """
        Update the grid as it is running by using a temporary grid and then swapping it with the original
        grid
        """
        if not self.is_running():
            return

        cells = self.grid.cells
        temp  = self.temp_grid.cells
        rows, cols = self.rows, self.columns

        for row in range(rows):
            for column in range(cols):
                ln = self.count_live_neighbours(self.grid, row, column)
                value = cells[row][column]
                temp[row][column] = 1 if (value == 1 and 2 <= ln <= 3) or (value == 0 and ln == 3) else 0

        self.grid, self.temp_grid = self.temp_grid, self.grid

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