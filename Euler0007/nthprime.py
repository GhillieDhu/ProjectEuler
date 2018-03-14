from itertools import islice


def prime_n(n: int) -> int:
    from Euler0003.primes import primes
    return list(islice(primes(), n))[-1]


if __name__ == '__main__':
    import os
    import sys
    sys.path.append(os.path.dirname(os.pardir))
    '''
    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
    we can see that the 6th prime is 13.

    What is the 10 001st prime number?
    '''
    print(prime_n(10001))
