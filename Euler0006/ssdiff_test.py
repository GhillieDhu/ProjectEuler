from .ssdiff import sumsq, sqsum, ssdiff
from hypothesis import given
from hypothesis.strategies import integers


def test_example():
    sumsqrange = sumsq(range(1, 11))
    assert sumsqrange == 385
    sqsumrange = sqsum(range(1, 11))
    assert sqsumrange == 3025
    assert sqsumrange - sumsqrange == 2640


@given(integers())
def test_single_item_diff_zero(x: int):
    assert ssdiff([x]) == 0
