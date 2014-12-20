'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

import sys

def is_coprime(candidate, primes):
    for prime in primes:
        if candidate % prime == 0:
            return False
    return True

def prime(n):
    primes = []
    candidate = 2
    while len(primes) < n:
        if is_coprime(candidate, primes):
            primes.append(candidate)
        candidate += 1
    return primes[n-1]

if __name__ == '__main__':
    nth = int(sys.argv[1])
    print(prime(nth))