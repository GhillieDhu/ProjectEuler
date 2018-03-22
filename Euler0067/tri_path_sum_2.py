if __name__ == '__main__':
    import os
    import sys
    sys.path.append(os.path.dirname(os.pardir))
    from Euler0018.tri_path_sum import read_tri, roll_up
    '''
    By starting at the top of the triangle below and moving to
    adjacent from top to bottom is 23.

    3
    7 4
    2 4 6
    8 5 9 3

    That is, 3 + 7 + 4 + 9 = 23.

    Find the maximum total from top to bottom in triangle.txt (right click and
    'Save Link/Target As...'), a 15K text file containing a triangle with
    one-hundred rows.

    NOTE: This is a much more difficult version of Problem 18. It is not
    possible to try every route to solve this problem, as there are 2^99
    altogether! If you could check one trillion (10^12) routes every second it
    would take over twenty billion years to check them all. There is an
    efficient algorithm to solve it. ;o)
    '''
    import os.path
    scriptpath = os.path.dirname(__file__)
    tri_file = os.path.join(scriptpath, 'p067_triangle.txt')
    prod = read_tri(tri_file)
    print(roll_up(prod))
