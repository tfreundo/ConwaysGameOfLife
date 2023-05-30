import pygame
from game.board import Board
from output.output import XOutput
import sys


class ScreenOutput(XOutput):
    cells_width: int
    cells_height: int

    screen_width: int
    screen_height: int
    cell_size: int
    screen: pygame.Surface
    clock: pygame.time.Clock

    color_bg = pygame.Color("white")
    color_fg = pygame.Color("black")

    def __init__(self, cells_width=10, cells_height=10) -> None:
        super().__init__(cells_width, cells_height)
        self.__derive_cell_size(cells_width, cells_height)
        self.screen_width = self.cells_width * self.cell_size
        self.screen_height = self.cells_height * self.cell_size
        pygame.init()
        pygame.display.set_caption("Conways Game of Life")
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.clock = pygame.time.Clock()
        self.running = True

    def __derive_cell_size(self, cells_width, cells_height):
        self.cell_size = 50
        if (cells_width > 25) or (cells_height > 25):
            self.cell_size = 15
        if (cells_width > 50) or (cells_height > 50):
            self.cell_size = 5

    def quit(self):
        self.running = False
        pygame.quit()
        sys.exit(0)

    def update(self, board: Board) -> None:
        if self.running:
            try:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False
                # wipe away everything from last iteration
                self.screen.fill(self.color_bg)

                # RENDER
                for ri, row in enumerate(board.cells):
                    for ci, cell in enumerate(row):
                        rect = (
                            ci * self.cell_size,
                            ri * self.cell_size,
                            self.cell_size,
                            self.cell_size,
                        )
                        color = self.color_bg if cell == 0 else self.color_fg
                        pygame.draw.rect(self.screen, color, rect)

                pygame.display.update()
            except Exception:
                self.quit()
        else:
            self.quit()
