'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

import sys

def is_palindrome(string):
    if string == '':
        return True
    elif string[0] == string[-1]:
        return is_palindrome(string[1:-1])
    else:
        return False

def max_palindrome(upper_bound, lower_bound):
    palindromes = {}
    for i in range(upper_bound, lower_bound, -1):
        for j in range(upper_bound, i, -1):
            if is_palindrome(str(i * j)):
                print(i*j, i, j)
                palindromes[i*j] = (i, j)
    return max(palindromes), palindromes[max(palindromes)]

if __name__ == '__main__':
    input = int(sys.argv[1])
    max_limit = 10**input - 1
    min_limit = 10**(input - 1)
    print(max_palindrome(max_limit, min_limit))