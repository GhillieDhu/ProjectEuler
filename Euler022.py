'''
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 * 53 = 49714.

What is the total of all the name scores in the file?
'''

import sys
from functools import reduce
from operator import mul

def numerate(string):
    return sum([ord(s) - 64 for s in string])

if __name__ == '__main__':
    names = open(sys.argv[1]).readline().split(',')
    names = sorted([name.replace('"', '') for name in names])
    numerals = [numerate(name) for name in names]
    total = 0
    for i in range(len(numerals)):
        total += (i+1) * numerals[i]
    print(total)
