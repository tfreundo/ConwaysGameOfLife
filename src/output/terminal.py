import os
from game.board import Board
from output.output import XOutput


class TerminalOutput(XOutput):
    def __init__(self, cells_width=10, cells_height=10) -> None:
        super().__init__(cells_width, cells_height)

    def clear_screen(self) -> None:
        os.system("cls" if os.name == "nt" else "clear")

    def update(self, board: Board) -> None:
        self.clear_screen()
        print(f"=== Epoch: {board.epoch} ===")
        for row in board.cells:
            for cell in row:
                cell = "-" if cell == 0 else "X"
                print(f" {cell} ", end="")
            print("\n")
