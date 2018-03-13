import fibonacci
from hypothesis import given
from hypothesis.strategies import integers


def test_example():
    assert fibonacci.firstN(1, 2, 10) == \
           [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]


@given(integers(0))
def test_all_zeros(n):
    assert sum(fibonacci.firstN(0, 0, n)) == 0


@given(integers(), integers(), integers(1, 10))
def test_offset_matches(seed1, seed2, n):
    assert fibonacci.firstN(seed1, seed2, n)[1:] == \
           fibonacci.firstN(seed2, seed1 + seed2, n - 1)
