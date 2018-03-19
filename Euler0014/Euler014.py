'''
The following iterative sequence is defined for the set of positive integers:

n -> n/2 (n is even)
n -> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain->

NOTE: Once the chain starts the terms are allowed to go above one million.
'''

import sys

def next_collatz(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1

def collatz(n, collatzes):
    if n == 1:
        collatzes[1] = 1
        return collatzes
    nc = next_collatz(n)
    if nc not in collatzes:
        collatzes = collatz(nc, collatzes)
    collatzes[n] = collatzes[nc] + 1
    return collatzes

if __name__ == '__main__':
    limit = int(sys.argv[1])
    collatzes = {}
    for i in range(1, limit):
        collatzes = collatz(i, collatzes)
    max_start, max_chain = 1, 1
    for i in collatzes:
        if collatzes[i] > max_chain:
            max_start, max_chain = i, collatzes[i]
    print((max_start, max_chain))
