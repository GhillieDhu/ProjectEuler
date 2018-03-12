from typing import Sequence
import typing


def sum_of_multiples(multiplicands: Sequence[int], cap: int):
    return sum({x for m in multiplicands for x in range(0, cap, m)})
