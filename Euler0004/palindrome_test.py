from .palindrome import max_palindrome, is_palindrome
from hypothesis import given
from hypothesis.strategies import characters


def test_example():
    assert max_palindrome(2) == 9009


def test_empty_string():
    assert is_palindrome('')


@given(characters())
def test_single_character(c):
    assert is_palindrome(c)
