"""
This is the grid module. It contains the Grid class and its associated methods.
"""
import matplotlib.pyplot as plt

import random

class Grid():
    """
    A class representing the grid from the swap puzzle. It supports rectangular grids. 

    Attributes: 
    -----------
    m: int
        Number of lines in the grid
    n: int
        Number of columns in the grid
    state: list[list[int]]
        The state of the grid, a list of list such that state[i][j] is the number in the cell (i, j), i.e., in the i-th line and j-th column. 
        Note: lines are numbered 0..m and columns are numbered 0..n.
    """
    
    def __init__(self, m, n, initial_state = []):
        """
        Initializes the grid.

        Parameters: 
        -----------
        m: int
            Number of lines in the grid
        n: int
            Number of columns in the grid
        initial_state: list[list[int]]
            The intiail state of the grid. Default is empty (then the grid is created sorted).
        """
        self.m = m
        self.n = n
        if not initial_state:
            initial_state = [list(range(i*n+1, (i+1)*n+1)) for i in range(m)]            
        self.state = initial_state

    def __str__(self): 
        """
        Prints the state of the grid as text.
        """
        output = f"The grid is in the following state:\n"
        for i in range(self.m): 
            output += f"{self.state[i]}\n"
        return output

    def __repr__(self): 
        """
        Returns a representation of the grid with number of rows and columns.
        """
        fig, ax = plt.subplots(1, 1)
        column_labels
        ax.axis("tight")
        ax.axis("off")
        ax.table(cellText=self.state, loc="center")

        plt.show()

    def is_sorted(self):
        """
        Checks is the current state of the grid is sorte and returns the answer as a boolean.
        """
        bon_tab = Grid(self.m,self.n)

        return bon_tab.state == self.state

    def swap(self, cell1, cell2):
        """
        Implements the swap operation between two cells. Raises an exception if the swap is not allowed.

        Parameters: 
        -----------
        cell1, cell2: tuple[int]
            The two cells to swap. They must be in the format (i, j) where i is the line and j the column number of the cell. 
        """
        (i_1,j_1) = cell1
        (i_2,j_2) = cell2
        if (i_1 < n and i_2 < n and j_1 < m and j_2 < m):
            if (i_1 == i_2) and ( (j_1 == j_2 + 1) or (j_1 == j_2 - 1) ):
                    temp = self.state[i_1][j_1]
                    self.state[i_1][j_1] = self.state[i_2][j_2]
                    self.state[i_2][j_2]=temp

            elif (j_1 == j_2) and ( (i_1 == i_2 + 1) or (i_1 == i_2 - 1) ) :
                    temp = self.state[i_1][j_1]
                    self.state[i_1][j_1] = self.state[i_2][j_2]
                    self.state[i_2][j_2]=temp

            else:
                raise ValueError
        else:
            raise ValueError

    def swap_seq(self, cell_pair_list):
        """
        Executes a sequence of swaps. 

        Parameters: 
        -----------
        cell_pair_list: list[tuple[tuple[int]]]
            List of swaps, each swap being a tuple of two cells (each cell being a tuple of integers). 
            So the format should be [((i1, j1), (i2, j2)), ((i1', j1'), (i2', j2')), ...].
        """
        #Fonction récursive
        if cell_pair_list == []:
            return 0
        else:
            (couple_1,couple_2) = cell_pair_list[0]
            self.swap(couple_1,couple_2)
            self.swap_seq(cell_pair_list[1:])


    @classmethod
    def grid_from_file(cls, file_name): 
        """
        Creates a grid object from class Grid, initialized with the information from the file file_name.
        
        Parameters: 
        -----------
        file_name: str
            Name of the file to load. The file must be of the format: 
            - first line contains "m n" 
            - next m lines contain n integers that represent the state of the corresponding cell

        Output: 
        -------
        grid: Grid
            The grid
        """
        with open(file_name, "r") as file:
            m, n = map(int, file.readline().split())
            initial_state = [[] for i_line in range(m)]
            for i_line in range(m):
                line_state = list(map(int, file.readline().split()))
                if len(line_state) != n: 
                    raise Exception("Format incorrect")
                initial_state[i_line] = line_state
            grid = Grid(m, n, initial_state)
        return grid


