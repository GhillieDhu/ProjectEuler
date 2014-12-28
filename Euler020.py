'''
n! means n x (n - 1) x ... x 3 x 2 x 1

For example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
'''

import sys

def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

if __name__ == '__main__':
    argument = int(sys.argv[1])
    number = str(fact(argument))
    print(sum(int(number[i]) for i in range(len(number))))
