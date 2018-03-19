'''
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
'''

import sys

number_names = {0: '',
                1: 'one',
                2: 'two',
                3: 'three',
                4: 'four',
                5: 'five',
                6: 'six',
                7: 'seven',
                8: 'eight',
                9: 'nine',
                10: 'ten',
                11: 'eleven',
                12: 'twelve',
                13: 'thirteen',
                14: 'fourteen',
                15: 'fifteen',
                16: 'sixteen',
                17: 'seventeen',
                18: 'eighteen',
                19: 'nineteen',
                20: 'twenty',
                30: 'thirty',
                40: 'forty',
                50: 'fifty',
                60: 'sixty',
                70: 'seventy',
                80: 'eighty',
                90: 'ninety',
                100: 'hundred',
                1000: 'thousand'}

def name_a_number(number):
    number_string = str(number)
    if len(number_string) == 1:
        return number_names[int(number_string)]
    if len(number_string) == 2:
        if int(number_string) in number_names:
            return number_names[int(number_string)]
        else:
            return number_names[int(number_string[0] + '0')] + name_a_number(int(number_string[1]))
    if len(number_string) == 3:
        number_name = number_names[int(number_string[0])] + number_names[100]
        remainder = name_a_number(int(number_string[1:]))
        if len(remainder) > 0:
            number_name += 'and' + remainder
        return number_name
    if len(number_string) == 4:
        number_name = number_names[int(number_string[0])] + number_names[1000]
        remainder = name_a_number(int(number_string[1:]))
        if len(remainder) > 0:
            number_name += 'and' + remainder
        return number_name

if __name__ == '__main__':
    print(sum(len(name_a_number(i)) for i in range(int(sys.argv[1])+1)))
