from typing import Dict, List, Optional, DefaultDict, TypeVar
from collections import defaultdict
from itertools import tee


def next_collatz(n: int) -> int:
    return n // 2 if n % 2 == 0 else 3 * n + 1


def collatz_seq(n: int, czs: Dict[int, int]={}) -> List[int]:
    cz: List[int] = [n]
    while n not in czs and n != 1:
        nc = next_collatz(n)
        cz.append(nc)
        n = nc
    return cz


def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def collatzes_upto_n(n: int, czs: Dict[int, int]={}) -> Dict[int, int]:
    for i in range(1, n):
        cz = collatz_seq(i, czs)
        cz_pairs = pairwise(cz)
        czs.update(cz_pairs)
    return czs


KT = TypeVar("KT")
VT = TypeVar("VT")


def invert_dict(kv: Dict[KT, VT]) -> DefaultDict[VT, List[KT]]:
    vk: DefaultDict[VT, List[KT]] = defaultdict(list)
    for k, v in kv.items():
        vk[v].append(k)
    return vk


def collatz_lengths(czs: Dict[int, int]) -> Dict[int, int]:
    i_czs = invert_dict(czs)
    cz_ls = {1: 1}
    length = 1
    ks = [1]
    while len(ks) > 0:
        cz_ls.update({k: length for k in ks})
        length += 1
        ks = [v for k in ks for v in i_czs[k]]
    return cz_ls


def longest_collatz_under_n(n: int) -> int:
    czs = collatzes_upto_n(n)
    cz_ls = collatz_lengths(czs)
    ls = {v: k for k, v in cz_ls.items()}
    return ls[max(ls)]


if __name__ == '__main__':
    '''
    The following iterative sequence is defined for the set of positive
    integers:

    n -> n/2 (n is even)
    n -> 3n + 1 (n is odd)

    Using the rule above and starting with 13, we generate the following
    sequence:

    13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

    It can be seen that this sequence (starting at 13 and finishing at 1)
    contains 10 terms. Although it has not been proved yet (Collatz Problem),
    it is thought that all starting numbers finish at 1.

    Which starting number, under one million, produces the longest chain->

    NOTE: Once the chain starts the terms are allowed to go above one million.
    '''
    print(longest_collatz_under_n(1000000))
