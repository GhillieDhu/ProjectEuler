from .tri_path_sum import read_tri, roll_up


def test_example():
    import os.path
    scriptpath = os.path.dirname(__file__)
    tri_file = os.path.join(scriptpath, 'example_tri.txt')
    tri = read_tri(tri_file)
    assert roll_up(tri) == 23
