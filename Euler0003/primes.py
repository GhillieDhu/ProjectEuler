from itertools import count
from typing import Generator, List, Optional


def primes(ps: List[int] = [2, 3]) -> Generator[int, None, None]:
    for p in ps:
        yield p
    while True:
        n = next(x for x in count(ps[-1], 2) if all(x % p != 0 for p in ps))
        yield n
        ps.append(n)


def prime_factors(n: int, known_ps: Optional[List[int]] = None) -> List[int]:
    ps = primes(known_ps) if known_ps else primes()
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
