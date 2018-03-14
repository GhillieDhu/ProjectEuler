from typing import Tuple, List


def is_triplet(x: int, y: int, z: int) -> bool:
    [a, b, c] = sorted([x, y, z])
    return a**2 + b**2 == c**2


def triplets_summing_to(x: int) -> List[Tuple[int, ...]]:
    return [tuple(sorted([a, b, x - (a + b)])) for a in range(1, x + 1) for b
            in range(a, x + 1 - a) if is_triplet(a, b, x - (a + b))]


if __name__ == '__main__':
    import os
    import sys
    sys.path.append(os.path.dirname(os.pardir))
    from Euler0008.product import product
    '''
    A Pythagorean triplet is a set of three natural numbers, a < b < c,
    for which,
    a^2 + b^2 = c^2

    For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

    There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    Find the product abc.
    '''
    print(product(triplets_summing_to(1000)[0]))
