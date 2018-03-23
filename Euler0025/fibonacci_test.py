from .fibonacci import fib, first_fib_len_n


def test_example_seq():
    fs = fib()
    fibs = [next(fs) for i in range(12)]
    assert fibs == [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]


def test_example_len():
    assert first_fib_len_n(3) == 12
