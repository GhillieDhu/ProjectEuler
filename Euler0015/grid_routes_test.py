from .grid_routes import generate_grid, corner_paths
from hypothesis import given
from hypothesis.strategies import integers


def test_example():
    assert corner_paths(2, 2) == 6


@given(integers(0, 100), integers(0, 100))
def test_symmetry(m: int, n: int):
    assert corner_paths(m, n) == corner_paths(n, m)


@given(integers(0, 100), integers(0, 100), integers(0, 100), integers(0, 100))
def test_interior(i: int, j: int, k: int, l: int):
    a = max(i, j)
    b = max(k, l)
    c = min(i, j)
    d = min(k, l)
    assert corner_paths(c, d) == generate_grid(a, b)[c, d]
