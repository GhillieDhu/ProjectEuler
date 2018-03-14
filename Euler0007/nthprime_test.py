from .nthprime import prime_n


def test_example():
    assert prime_n(1) == 2
    assert prime_n(2) == 3
    assert prime_n(3) == 5
    assert prime_n(4) == 7
    assert prime_n(5) == 11
    assert prime_n(6) == 13
