from typing import Generator, Tuple
from itertools import takewhile


def fib(fs: Tuple[int, int]=(1, 1)) -> Generator[int, None, None]:
    a, b = fs
    while True:
        yield a
        a, b = b, a + b


def first_fib_len_n(n: int) -> int:
    fibs = list(takewhile(lambda f: len(str(f)) < n, fib()))
    return len(fibs) + 1


if __name__ == '__main__':
    '''
    The Fibonacci sequence is defined by the recurrence relation:

        F_n = F_n-1 + F_n-2, where F_1 = 1 and F_2 = 1.

    Hence the first 12 terms will be:

        F_1 = 1
        F_2 = 1
        F_3 = 2
        F_4 = 3
        F_5 = 5
        F_6 = 8
        F_7 = 13
        F_8 = 21
        F_9 = 34
        F_10 = 55
        F_11 = 89
        F_12 = 144

    The 12th term, F_12, is the first term to contain three digits.

    What is the first term in the Fibonacci sequence to contain 1000 digits?
    '''
    print(first_fib_len_n(1000))
