from .ssdiff import sumsq, sqsum


def test_example():
    sumsqrange = sumsq(range(1, 11))
    assert sumsqrange == 385
    sqsumrange = sqsum(range(1, 11))
    assert sqsumrange == 3025
    assert sqsumrange - sumsqrange == 2640
