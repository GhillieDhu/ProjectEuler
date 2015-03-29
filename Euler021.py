'''
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''

import sys
from math import sqrt
from itertools import product
from functools import reduce
from operator import mul

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

def prime_factors(integer, primes):
    counts = {}
    if integer > 0:
        for i in primes:
            count = 0
            while integer % i == 0:
                count += 1
                integer //= i
            if count > 0:
                counts[i] = count
        if integer > 1:
            counts[integer] = 1
    return counts

def factors(integer, primes):
    pf_dict = prime_factors(integer, primes)
    f = []
    factor_count = 1
    for pf in pf_dict:
        factor_count *= pf_dict[pf]
        ff = []
        for count in range(pf_dict[pf]+1):
            ff.append(pf**count)
        f.append(ff)
    if len(list(product(f))) > 1:
        factor_list = [reduce(mul, primy, 1) for primy in list(product(*f))]
    else:
        try:
            factor_list = list(product(f))[0][0]
        except IndexError:
            factor_list = [1, integer]
    return sum(factor_list) - integer

if __name__ == '__main__':
    limit = int(sys.argv[1])
    primes = []
    for count in range(int(sqrt(34560))):
        primes = prime(count, primes)
    pairs = {}
    for count in range(limit):
        facts = factors(count, primes)
        if facts >= limit:
            pairs[facts] = factors(facts, primes)
        pairs[count] = facts
    amicables = []
    for pair in pairs:
        if pair < limit and pairs[pairs[pair]] == pair and pairs[pair] != pair:
            amicables.append(pair)
    print(sum(amicables))
