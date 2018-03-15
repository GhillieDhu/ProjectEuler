from .primesbelow import prime_sum
from itertools import takewhile
from hypothesis import given
from hypothesis.strategies import integers


def test_example():
    assert prime_sum(10) == 17


@given(integers(2, 1000))
def test_sieve_vs_generator(n):
    from Euler0003.primes import primes
    ps = list(takewhile(lambda x: x <= n, primes()))
    for n in range(2, n):
        assert prime_sum(n) == sum(p for p in ps if p <= n)
