from typing import Sequence, Tuple


def is_palindrome(candidate: Sequence) -> bool:
    return candidate == candidate[::-1]


def max_palindrome(digits: int) -> int:
    upper_bound = 10**digits - 1
    lower_bound = 10**(digits - 1)
    palindromes = filter(lambda k: is_palindrome(str(k)),
                         {i * j
                          for i in range(upper_bound, lower_bound, -1)
                          for j in range(upper_bound, i, -1)})
    return max(palindromes)


if __name__ == '__main__':
    '''
    A palindromic number reads the same both ways. The largest palindrome made
    from the product of two 2-digit numbers is 9009 = 91 x 99.

    Find the largest palindrome made from the product of two 3-digit numbers.
    '''
    print(max_palindrome(3))
