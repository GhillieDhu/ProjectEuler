'''
The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

     1: 1
     3: 1,3
     6: 1,2,3,6
    10: 1,2,5,10
    15: 1,3,5,15
    21: 1,3,7,21
    28: 1,2,4,7,14,28

We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
'''

import sys
from math import sqrt

def triangle_number(sequence):
    return [1] if sequence == [] else sequence + [(len(sequence)+1) + sequence[-1]]

def is_coprime(candidate, primes):
    for prime in primes:
        if candidate % prime == 0:
            return False
    return True

def prime(n, primes):
    if primes == []:
        primes = [2]
    candidate = max(primes) + 1 
    while max(primes) < n:
        if is_coprime(candidate, primes):
            primes.append(candidate)
        candidate += 1
    return primes

def factors(integer, primes):
    counts = {}
    for i in primes:
        count = 0
        while integer % i == 0:
            count += 1
            integer //= i
        if count > 0:
            counts[i] = count
    factors = 1
    for i in counts:
        factors *= counts[i]+1
    return factors

if __name__ == '__main__':
    primes = []
    triangle_numbers = []
    tri_facts = 0
    while tri_facts < int(sys.argv[1]):
        triangle_numbers = triangle_number(triangle_numbers)
        tri = triangle_numbers[-1]
        primes = prime(tri, primes)
        tri_facts = factors(tri, primes)
        print((tri, tri_facts))
