from output.output import XOutput
from output.terminal import TerminalOutput
from output.screen import ScreenOutput
from game.board import Board
import time


# Rules taken from: https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
class GameOfLife:
    output: XOutput

    # The amount of seconds to delay between epochs
    delay = 0.5

    def __init__(self, cells: list[list]) -> None:
        self.board = Board(cells=cells)
        self.output = ScreenOutput(
            cells_width=self.board.get_col_qty(), cells_height=self.board.get_row_qty()
        )

    def run(self) -> None:
        self.output.update(board=self.board)
        while True:
            time.sleep(self.delay)
            self.board.evolve()
            self.output.update(board=self.board)
