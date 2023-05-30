from abc import ABC, abstractmethod
from game.board import Board


class XOutput(ABC):
    def __init__(self, cells_width=10, cells_height=10) -> None:
        self.cells_width = cells_width
        self.cells_height = cells_height

    @abstractmethod
    def update(self, board: Board):
        pass
