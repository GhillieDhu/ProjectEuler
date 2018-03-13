from .lcm import lcm
from typing import Sequence, List
from hypothesis import given
from hypothesis.strategies import integers, lists


def test_example():
    assert lcm(range(1, 11)) == 2520


@given(integers(2))
def test_single(x: int):
    assert lcm([x]) == x


@given(integers(2), integers(1, 5))
def test_duplication_irrelevant(x: int, n: int):
    assert lcm([x] * n) == x


@given(lists(integers(2), min_size=2, max_size=10))
def test_divisibility(xs: List[int]):
    product = lcm(xs)
    assert all(product % x == 0 for x in xs)
