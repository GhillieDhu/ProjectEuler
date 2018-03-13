from fizzbuzz import sum_of_multiples
from hypothesis import given
from hypothesis.strategies import integers


def test_example():
    assert sum_of_multiples([3, 5], 10) == 23


@given(integers(1), integers(1), integers(0))
def test_order_invariant(a, b, cap):
    assert sum_of_multiples([a, b], cap) == sum_of_multiples([b, a], cap)


@given(integers(1), integers(1), integers(0))
def test_duplicates_irrelevant(a, n, cap):
    assert sum_of_multiples([a], cap) == sum_of_multiples([a] * n, cap)
