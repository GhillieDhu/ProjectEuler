from .tri_path_sum import read_tri, roll_up


def test_example():
    tri = read_tri('example_tri.txt')
    assert roll_up(tri) == 23
