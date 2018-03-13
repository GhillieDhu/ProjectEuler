'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

import sys
from math import sqrt
from typing import List


def multiples(prime, cap):
    return [prime * i for i in range(cap // prime)]


def is_coprime(candidate, primes):
    return all([candidate % prime != 0 for prime in primes])


if __name__ == '__main__':
    cap = 600851475143
    primes: List[int] = []
    candidate = 2
    while candidate < cap:
        if is_coprime(candidate, primes):
            primes.append(candidate)
            while cap % candidate == 0:
                cap = cap // candidate
                print(str(cap) + ', ' + str(candidate))
        candidate += 1
