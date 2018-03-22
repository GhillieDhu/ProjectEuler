from typing import List, Set, Dict
from itertools import combinations


def all_factors(n: int) -> Set[int]:
    from Euler0003.primes import prime_factors
    from Euler0008.product import product
    pfs: List[int] = prime_factors(n)
    return {product(pfc) for c in range(max(1, len(pfs)))
            for pfc in combinations(pfs, c)}


def sum_of_fs(n: int) -> int:
    return sum(all_factors(n))


if __name__ == '__main__':
    import os
    import sys
    sys.path.append(os.path.dirname(os.pardir))
    '''
    Let d(n) be defined as the sum of proper divisors of n (numbers less than
    n which divide evenly into n).
    If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair
    and each of a and b are called amicable numbers.

    For example, the proper divisors of 220 are
    1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
    The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

    Evaluate the sum of all the amicable numbers under 10000.
    '''
    f_sums: Dict[int, int] = {i: sum_of_fs(i) for i in range(1, 10000)}
    print(sum(i for i in f_sums if f_sums[i] != i and f_sums[i] in f_sums and
              f_sums[f_sums[i]] == i))
