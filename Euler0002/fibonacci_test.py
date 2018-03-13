import fibonacci
from hypothesis import given
import hypothesis.strategies


def test_example():
    assert list(fibonacci.firstN(1, 2, 10)) == \
           [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
