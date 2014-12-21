'''
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
'''

import sys

if __name__ == '__main__':
    exponent = int(sys.argv[1])
    number = str(2**exponent)
    print(sum(int(number[i]) for i in range(len(number))))
