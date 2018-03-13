from itertools import takewhile, count, dropwhile
from typing import Generator, List


def primes() -> Generator[int, None, None]:
    ps = [2, 3]
    for p in ps:
        yield p
    while True:
        n = next(dropwhile(lambda x:
                           any(x % p == 0 for p in ps), count(ps[-1], 2)))
        yield n
        ps.append(n)


def primes_to(n: int) -> List[int]:
    return list(takewhile(lambda x: x <= n, primes()))


def prime_factors(n: int) -> List[int]:
    ps = primes()
    p = next(ps)
    pfs: List[int] = []
    while p < n:
        while n % p == 0:
            n = n // p
            pfs.append(p)
        p = next(ps)
    if n > 1:
        pfs.append(n)
    return pfs


if __name__ == '__main__':
    '''
    The prime factors of 13195 are 5, 7, 13 and 29.

    What is the largest prime factor of the number 600851475143 ?
    '''
    print(prime_factors(600851475143))
