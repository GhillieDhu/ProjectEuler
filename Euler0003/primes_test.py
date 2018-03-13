from Euler0003.primes import prime_factors
from hypothesis import given
from hypothesis.strategies import integers
from functools import reduce
from operator import mul


def test_example():
    assert set(prime_factors(13195)) == {5, 7, 13, 29}


@given(integers(1))
def test_factor_product(n: int):
    assert n == reduce(mul, prime_factors(n), 1)
