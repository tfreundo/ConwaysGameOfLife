from typing import Tuple
from enum import Enum
from copy import deepcopy


class CellDirection(Enum):
    NORTH = 0
    NORTH_EAST = 1
    EAST = 2
    SOUTH_EAST = 3
    SOUTH = 4
    SOUTH_WEST = 5
    WEST = 6
    NORTH_WEST = 7


class CellStatus(Enum):
    DEAD = 0
    LIVE = 1


class Board:
    # The current board status
    cells = [[]]

    # Current epoch counter
    epoch = 0

    def __init__(self, cells=list[list]) -> None:
        self.cells = cells

    def evolve(self):
        """Executes the rules of this game and calculates the state of the next epoch"""

        new_cells = deepcopy(self.cells)

        for row in range(len(self.cells)):
            for col in range(len(self.cells[row])):
                cell_current_status = self.cells[row][col]
                cell_new_status = None
                live_neighbors_cells = self.get_live_neighbors_for_cell(row, col)
                live_neighbors = self.count_live_neighbors_for_cell(row, col)

                if cell_current_status == CellStatus.LIVE.value:
                    # Rule 1: Any live cell with two or three live neighbours survives
                    if (live_neighbors == 2) or (live_neighbors == 3):
                        cell_new_status = CellStatus.LIVE.value
                    # Rule 3.1: All other live cells die in the next generation
                    else:
                        cell_new_status = CellStatus.DEAD.value
                elif cell_current_status == CellStatus.DEAD.value:
                    # Rule 2: Any dead cell with three live neighbours becomes a live cell
                    if live_neighbors == 3:
                        cell_new_status = CellStatus.LIVE.value
                    # Rule 3.2: All other dead cells stay dead
                    else:
                        cell_new_status = CellStatus.DEAD.value

                # Update cell status
                new_cells[row][col] = cell_new_status

        self.cells = new_cells
        self.epoch += 1

    def get_row_qty(self) -> int:
        return len(self.cells)

    def get_col_qty(self) -> int:
        return len(self.cells[0])

    def count_live_neighbors_for_cell(self, row: int, col: int) -> list[Tuple]:
        return len(self.get_live_neighbors_for_cell(row, col))

    def get_live_neighbors_for_cell(self, row: int, col: int) -> list[Tuple]:
        """Returns the index as Tuple (row, col) of all neighbors around the given cell that are live

        Args:
            row (int): The row index to return the neighbors to
            col (int): The column index to return the neighbors to

        Returns:
            list[Tuple]: A list of Tuples containing all neighbors of the given cell that are live
        """
        live_neighbors = []
        neighbors = self.get_neighbors_for_cell(row, col)
        for neighbor in neighbors:
            cell_status = self.cells[neighbor[0]][neighbor[1]]
            if cell_status == CellStatus.LIVE.value:
                live_neighbors.append(neighbor)

        return live_neighbors

    def get_neighbors_for_cell(self, row: int, col: int) -> list[Tuple]:
        """Returns the index as Tuple (row, col) of all neighbors around the given cell

        Args:
            row (int): The row index to return the neighbors to
            col (int): The column index to return the neighbors to

        Returns:
            list[Tuple]: A list of Tuples containing all neighbors of the given cell
        """
        neighbors = []

        for direction in list(CellDirection):
            neighbor = self.__get_neighbor_at_direction(row, col, direction)
            if neighbor != None:
                neighbors.append(neighbor)

        return neighbors

    def __get_neighbor_at_direction(self, row, col, direction: CellDirection) -> Tuple:
        """Returns the neighbor index as Tuple (row, col) at the given direction

        Args:
            row (_type_): The row index to return the neighbors to
            col (_type_): The column index to return the neighbors to
            direction (CellDirection): The direction to look for the neighbor

        Returns:
            Tuple: Tuple containing the row and column of the neighbor or None if there is no neighbor
        """
        # Directions like south_east combine south and east checks
        if direction == CellDirection.NORTH:
            if row > 0:
                return (row - 1, col)
            return None
        if direction == CellDirection.NORTH_EAST:
            if (row > 0) and (col < (self.get_col_qty() - 1)):
                return (row - 1, col + 1)
            return None
        elif direction == CellDirection.EAST:
            if col < (self.get_col_qty() - 1):
                return (row, col + 1)
            return None
        elif direction == CellDirection.SOUTH_EAST:
            if (row < (self.get_row_qty() - 1)) and col < (self.get_col_qty() - 1):
                return (row + 1, col + 1)
            return None
        elif direction == CellDirection.SOUTH:
            if row < (self.get_row_qty() - 1):
                return (row + 1, col)
            return None
        elif direction == CellDirection.SOUTH_WEST:
            if (row < (self.get_row_qty() - 1)) and (col > 0):
                return (row + 1, col - 1)
            return None
        elif direction == CellDirection.WEST:
            if col > 0:
                return (row, col - 1)
            return None
        elif direction == CellDirection.NORTH_WEST:
            if (row > 0) and (col > 0):
                return (row - 1, col - 1)
            return None
