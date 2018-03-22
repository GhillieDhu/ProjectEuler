from typing import Dict


names: Dict[str, str] = {
    '0': '',
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine',
    '10': 'ten',
    '11': 'eleven',
    '12': 'twelve',
    '13': 'thirteen',
    '14': 'fourteen',
    '15': 'fifteen',
    '16': 'sixteen',
    '17': 'seventeen',
    '18': 'eighteen',
    '19': 'nineteen',
    '20': 'twenty',
    '30': 'thirty',
    '40': 'forty',
    '50': 'fifty',
    '60': 'sixty',
    '70': 'seventy',
    '80': 'eighty',
    '90': 'ninety',
    '100': 'hundred',
    '1000': 'thousand'}


def name_number(num: int) -> str:
    num_str = str(num)[::-1]
    num_name = ''
    if len(num_str) == 4:
        num_name += names[num_str[3]] + names['1000']
        num_str = num_str[:-1]
    if len(num_str) == 3:
        if num_str[2] != '0':
            num_name += names[num_str[2]] + names['100']
        if any([i != '0' for i in num_str[:2]]):
            num_name += 'and'
        num_str = num_str[:-1]
    if len(num_str) == 2:
        if num_str[1] + num_str[0] in names:
            num_name += names[num_str[1] + num_str[0]]
            num_str = ''
        elif num_str[1] + '0' in names:
            num_name += names[num_str[1] + '0']
            num_str = num_str[:-1]
        else:
            num_str = num_str[:-1]
    if len(num_str) == 1:
        num_name += names[num_str[0]]
    return num_name

if __name__ == '__main__':
    '''
    If the nums 1 to 5 are written out in words: one, two, three, four,
    five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

    If all the nums from 1 to 1000 (one thousand) inclusive were written
    out in words, how many letters would be used?

    NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
    forty-two) contains 23 letters and 115 (one hundred and fifteen) contains
    20 letters. The use of "and" when writing out nums is in compliance
    with British usage.
    '''
    for i in range(1000, 0, -1):
        print(str(i) + ': ' + name_number(i))
    print(sum([len(name_number(i)) for i in range(1, 1001)]))
