from typing import Sequence, List
from Euler0003.primes import prime_factors


def lcm(support: Sequence[int]) -> int:
    print(support)
    return 0


if __name__ == '__main__':
    '''
    2520 is the smallest number that can be divided by each of the numbers
    from 1 to 10 without any remainder.

    What is the smallest positive number that is evenly divisible by all of
    the numbers from 1 to 20?
    '''
    support = 0
    smallest_multiple = 1
    factors: List[int] = []
    for base in range(1, support + 1):
        new_factor = base
        for factor in factors:
            if new_factor % factor == 0:
                new_factor //= factor
        if new_factor > 1:
            smallest_multiple *= new_factor
            factors.append(new_factor)
    print(smallest_multiple)
