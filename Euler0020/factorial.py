def fact(n: int) -> int:
    from Euler0008.product import product
    return product(range(1, n + 1))


def fact_digit_sum(n: int) -> int:
    from Euler0016.digit_sum import sum_digits
    return sum_digits(fact(n))


if __name__ == '__main__':
    import os
    import sys
    sys.path.append(os.path.dirname(os.pardir))
    '''
    n! means n x (n - 1) x ... x 3 x 2 x 1

    For example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800,
    and the sum of the digits in the number 10! is
    3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

    Find the sum of the digits in the number 100!
    '''
    print(fact_digit_sum(100))
