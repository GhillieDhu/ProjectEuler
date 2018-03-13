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


def prime_factors(cap: int) -> List[int]:
    candidates = primes()
    candidate = next(candidates)
    pfs: List[int] = []
    while candidate < cap:
        while cap % candidate == 0:
            cap = cap // candidate
            pfs.append(candidate)
        candidate = next(candidates)
    if cap > 1:
        pfs.append(cap)
    return pfs

if __name__ == '__main__':
    # cap = 600851475143
    for i in range(1000):
        print(str(i) + ": " + str(prime_factors(i)))
