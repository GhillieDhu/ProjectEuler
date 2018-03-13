from primes import prime_factors
from hypothesis import given
from hypothesis.strategies import integers
from functools import reduce
from operator import mul


@given(integers(1))
def test_factor_product(n: int):
    assert n == reduce(mul, prime_factors(n), 1)
