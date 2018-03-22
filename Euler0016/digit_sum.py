def sum_digits(x: int) -> int:
    x_str = str(x)
    return sum(int(x_i) for x_i in x_str)


def binary_power_digit_sum(n: int) -> int:
    return sum_digits(2**n)


if __name__ == '__main__':
    '''
    2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

    What is the sum of the digits of the number 2^1000?
    '''
    print(binary_power_digit_sum(1000))
