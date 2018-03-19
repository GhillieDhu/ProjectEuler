from .gridproduct import grid_product, read_grid, max_grid_product
import numpy as np


def test_example():
    grid = read_grid()
    assert grid_product(grid, [(6, 8), (7, 9), (8, 10), (9, 11)]) == 1788696


def test_degenerate():
    grid = read_grid()
    assert max_grid_product(grid, 1) == np.amax(grid)
