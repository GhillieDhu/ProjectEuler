import fibonacci
from hypothesis import given
import hypothesis.strategies


@given(hypothesis.strategies.integers())
def test_dummy(x):
    assert False
