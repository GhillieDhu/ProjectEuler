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


def primesTo(n: int) -> List[int]:
    return list(takewhile(lambda x: x <= n, primes()))


if __name__ == '__main__':
    cap = 600851475143
    candidates = primes()
    candidate = next(candidates)
    while candidate < cap:
        while cap % candidate == 0:
            cap = cap // candidate
            print(str(cap) + ', ' + str(candidate))
        candidate = next(candidates)
