from .grid_routes import generate_grid, corner_paths


def test_example():
    assert corner_paths(2, 2) == 6
