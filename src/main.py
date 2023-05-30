from game.game import GameOfLife
from game.start_patterns import Random, Oscillators, StillLifes

cells = Random().generate(75, 75)
GameOfLife(cells=cells).run()
