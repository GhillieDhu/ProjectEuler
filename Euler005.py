'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

import sys

if __name__ == '__main__':
    support = int(sys.argv[1])
    smallest_multiple = 1
    factors = []
    for base in range(1, support + 1):
        new_factor = base
        for factor in factors:
            if new_factor % factor == 0:
                new_factor //= factor
        if new_factor > 1:
            smallest_multiple *= new_factor
            factors.append(new_factor)
    print(smallest_multiple)