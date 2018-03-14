from .pythagoras import is_triplet, triplets_summing_to


def test_example():
    assert is_triplet(3, 4, 5)


def test_implicit_example():
    assert triplets_summing_to(12)[0] == (3, 4, 5)
