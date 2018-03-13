from itertools import takewhile, islice
from typing import Generator
import typing


def series(seed1: int, seed2: int) -> Generator[int, None, None]:
    while True:
        yield seed1
        seed1, seed2 = seed2, seed1 + seed2


def firstN(seed1: int, seed2: int, n: int):
    return list(islice(series(seed1, seed2), n))


def allBelow(seed1: int, seed2: int, limit: int):
    return list(takewhile(lambda x: x <= limit, series(seed1, seed2)))


if __name__ == '__main__':
    '''
    Each new term in the Fibonacci sequence is generated by adding the
    previous two terms. By starting with 1 and 2, the first 10 terms will be:

    1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

    By considering the terms in the Fibonacci sequence whose values do not
    exceed four million, find the sum of the even-valued terms.
    '''
    print(sum(filter(lambda x: x % 2 == 0, allBelow(1, 2, 4000000))))
