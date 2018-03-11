from functools import partial
from typing import List, Callable


def filtered_range(pred: Callable[[int], bool], cap: int) -> List[int]:
    """"""
    return [i for i in range(1, cap) if pred(i)]


def multiple_of_any(multiplicands, i):
    return any([i % m == 0 for m in multiplicands])


def sum_of_multiples(multiplicands, cap):
    return sum(filtered_range(partial(multiple_of_any, multiplicands), cap))
