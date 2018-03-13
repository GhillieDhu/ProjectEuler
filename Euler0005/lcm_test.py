from .lcm import lcm
from typing import Sequence, List


def test_example():
    assert lcm(range(1, 11)) == 2520
