from .product import product, max_subseq_product
from hypothesis import given
from hypothesis.strategies import integers, floats, one_of, lists, decimals


def test_example():
    assert max_subseq_product(4) == 5832


@given(one_of(integers(), floats(allow_nan=False)))
def test_empty(start):
    assert product([], start) == start


@given(one_of(integers(), floats(allow_nan=False)))
def test_singleton(x):
    assert product([x]) == x


@given(lists(integers()))
def test_associativity(xs):
    '''
    Fails for floats & decimals due to precision / rounding
    '''
    assert product(xs) == product(sorted(xs))
