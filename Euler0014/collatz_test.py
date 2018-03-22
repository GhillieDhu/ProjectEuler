from .collatz import collatz_seq, collatzes_upto_n, collatz_lengths
from hypothesis import given
from hypothesis.strategies import integers, just


def test_example():
    assert collatz_seq(13) == [13, 40, 20, 10, 5, 16, 8, 4, 2, 1]


@given(integers(2, 10000))
def test_collatz_length(n: int):
    czs = collatzes_upto_n(n)
    cz_ls = collatz_lengths(czs)
    assert cz_ls[n - 1] == len(collatz_seq(n - 1))
