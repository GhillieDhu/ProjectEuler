'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

import sys

def is_coprime(candidate, primes):
    for prime in primes:
        if prime**2 > candidate:
            return True
        if candidate % prime == 0:
            return False
    return True

def primes_below_n(n):
    primes = [2]
    candidate = 3
    while candidate < n:
        if is_coprime(candidate, primes):
            primes.append(candidate)
        candidate += 2
    return primes

if __name__ == '__main__':
    nth = int(sys.argv[1])
    print(sum(primes_below_n(nth)))