from typing import Sequence
from functools import reduce


def sumsq(xs: Sequence[int]) -> int:
    return sum(x**2 for x in xs)


def sqsum(xs: Sequence[int]) -> int:
    return (sum(xs))**2


def ssdiff(xs: Sequence[int]) -> int:
    return sqsum(xs) - sumsq(xs)


if __name__ == '__main__':
    '''
    The sum of the squares of the first ten natural numbers is,
    12 + 22 + ... + 102 = 385

    The square of the sum of the first ten natural numbers is,
    (1 + 2 + ... + 10)2 = 552 = 3025

    Hence the difference between the sum of the squares of the first ten
    natural numbers and the square of the sum is 3025 - 385 = 2640.

    Find the difference between the sum of the squares of the first one hundred
    natural numbers and the square of the sum.
    '''
    print(ssdiff(range(1, 101)))
