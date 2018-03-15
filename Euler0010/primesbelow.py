from functools import reduce
from typing import Set


def primes_to(n: int) -> Set[int]:
    xs = range(n, 1, -1)
    cs: Set = reduce(lambda a, b: a | b,
                     [set(range(x**2, n + 1, x)) for x in xs])
    return set(xs) - cs


def prime_sum(n: int) -> int:
    return sum(primes_to(n))


if __name__ == '__main__':
    import os
    import sys
    sys.path.append(os.path.dirname(os.pardir))
    '''
    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

    Find the sum of all the primes below two million.
    '''
    print(prime_sum(2000000))
