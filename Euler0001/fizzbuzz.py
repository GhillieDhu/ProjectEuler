from typing import Sequence
import typing


def sum_of_multiples(multiplicands: Sequence[int], cap: int):
    return sum({x for m in multiplicands for x in range(0, cap, m)})


if __name__ == '__main__':
    '''
    If we list all the natural numbers below 10 that are multiples of 3 or 5,
    we get 3, 5, 6 and 9. The sum of these multiples is 23.

    Find the sum of all the multiples of 3 or 5 below 1000.
    '''
    print(sum_of_multiples([3, 5], 1000))
