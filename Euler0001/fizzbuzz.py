from functools import partial
from typing import Callable, Set, Sequence
import typing


def filtered_range(pred: Callable[[int], bool], cap: int) -> Set[int]:
    """"""
    return {i for i in range(1, cap) if pred(i)}


def multiple_of_any(multiplicands: Sequence[int], i: int):
    return any({i % m == 0 for m in multiplicands})


def sum_of_multiples(multiplicands: Sequence[int], cap: int):
    return sum(filtered_range(partial(multiple_of_any, multiplicands), cap))
