from typing import List
from itertools import count


def read_names() -> List[str]:
    import os.path
    scriptpath = os.path.dirname(__file__)
    name_file_path = os.path.join(scriptpath, 'p022_names.txt')
    with open(name_file_path) as name_file:
        names: str = name_file.read()
        ns: List[str] = [n.replace('"', '') for n in names.split(',')]
        return sorted(ns)


def numerate(string):
    return sum([ord(s) - 64 for s in string])


if __name__ == '__main__':
    '''
    Using names.txt (right click and 'Save Link/Target As...'), a 46K text
    file containing over five-thousand first names, begin by sorting it into
    alphabetical order. Then working out the alphabetical value for each name,
    multiply this value by its alphabetical position in the list to obtain a
    name score.

    For example, when the list is sorted into alphabetical order, COLIN, which
    is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
    So, COLIN would obtain a score of 938 * 53 = 49714.

    What is the total of all the name scores in the file?
    '''
    names = read_names()
    numerals = [numerate(name) for name in names]
    print(sum(n * c for n, c in zip(numerals, count(1))))
