from typing import Sequence, List
from collections import Counter
from functools import reduce
from operator import mul


def lcm(support: Sequence[int]) -> int:
    from Euler0003.primes import prime_factors
    factors: List[Counter] = [Counter(prime_factors(x)) for x in support]
    common_factors: Counter = reduce(lambda a, b: a | b, factors)
    return reduce(mul, [k**common_factors[k] for k in common_factors.keys()])


if __name__ == '__main__':
    import os
    import sys
    sys.path.append(os.path.dirname(os.pardir))
    '''
    2520 is the smallest number that can be divided by each of the numbers
    from 1 to 10 without any remainder.

    What is the smallest positive number that is evenly divisible by all of
    the numbers from 1 to 20?
    '''
    print(lcm(range(1, 21)))
