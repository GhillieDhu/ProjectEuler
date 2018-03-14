from itertools import takewhile
from typing import List


def primes_to(n: int):
    from Euler0003.primes import primes
    ps = primes()
    return takewhile(lambda x: x <= n, ps)


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
