# content of test_sample.py
import pytest
from typing import Tuple
from src.game.board import Board


class TestCellNeighbor:
    @pytest.fixture(scope="function")
    def board(self):
        return Board(
            cells=[
                [0, 0, 0, 0, 0],
                [0, 1, 1, 1, 0],
                [0, 1, 1, 1, 0],
                [0, 0, 0, 0, 0],
            ]
        )

    def test_get_row_qty(self, board: Board):
        assert board.get_row_qty() == 4
        assert Board(cells=[[]]).get_row_qty() == 1

    def test_get_col_qty(self, board: Board):
        assert board.get_col_qty() == 5
        assert Board(cells=[[]]).get_col_qty() == 0

    def test_get_neighbors_for_cell(self, board: Board):
        # Corner cases
        neighbors_0_0: list[Tuple] = board.get_neighbors_for_cell(0, 0)
        neighbors_0_0.sort()
        neighbors_0_0_expected = [(0, 1), (1, 0), (1, 1)]
        neighbors_0_0_expected.sort()
        assert neighbors_0_0 == neighbors_0_0_expected

        neighbors_3_0: list[Tuple] = board.get_neighbors_for_cell(3, 0)
        neighbors_3_0.sort()
        neighbors_3_0_expected = [(2, 0), (2, 1), (3, 1)]
        neighbors_3_0_expected.sort()
        assert neighbors_3_0 == neighbors_3_0_expected

        neighbors_0_4: list[Tuple] = board.get_neighbors_for_cell(0, 4)
        neighbors_0_4.sort()
        neighbors_0_4_expected = [(0, 3), (1, 3), (1, 4)]
        neighbors_0_4_expected.sort()
        assert neighbors_0_4 == neighbors_0_4_expected

        neighbors_3_4: list[Tuple] = board.get_neighbors_for_cell(3, 4)
        neighbors_3_4.sort()
        neighbors_3_4_expected = [(2, 4), (2, 3), (3, 3)]
        neighbors_3_4_expected.sort()
        assert neighbors_3_4 == neighbors_3_4_expected

        # Middle case
        neighbors_1_2: list[Tuple] = board.get_neighbors_for_cell(1, 2)
        neighbors_1_2.sort()
        neighbors_1_2_expected = [
            (0, 1),
            (0, 2),
            (0, 3),
            (1, 1),
            (1, 3),
            (2, 1),
            (2, 2),
            (2, 3),
        ]
        neighbors_1_2_expected.sort()
        assert neighbors_1_2 == neighbors_1_2_expected

    def test_count_live_neighbors_for_cell(self, board: Board):
        # Corner cases
        assert board.count_live_neighbors_for_cell(0, 0) == 1
        assert board.count_live_neighbors_for_cell(3, 0) == 1
        assert board.count_live_neighbors_for_cell(0, 4) == 1
        assert board.count_live_neighbors_for_cell(3, 4) == 1
        # Middle cases
        assert board.count_live_neighbors_for_cell(0, 2) == 3
        assert board.count_live_neighbors_for_cell(3, 2) == 3
        assert board.count_live_neighbors_for_cell(1, 2) == 5

    def test_evolve_oscillators_blinker_pattern(self):
        blinker_pattern_off = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]
        blinker_pattern_on = [
            [0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0],
        ]

        board = Board(cells=blinker_pattern_off)
        board.evolve()
        assert board.cells == blinker_pattern_on
        board.evolve()
        assert board.cells == blinker_pattern_off

    def test_evolve_oscillators_still_pattern(self):
        block_pattern = [
            [0, 0, 0, 0],
            [0, 1, 1, 0],
            [0, 1, 1, 0],
            [0, 0, 0, 0],
        ]

        board = Board(cells=block_pattern)
        board.evolve()
        assert board.cells == block_pattern
        board.evolve()
        assert board.cells == block_pattern
