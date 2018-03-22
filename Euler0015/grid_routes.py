from typing import DefaultDict, Tuple, Set
from collections import defaultdict


def generate_grid(h: int, w: int) -> DefaultDict[Tuple[int, int], int]:
    grid: DefaultDict[Tuple[int, int], int] = defaultdict(int)
    grid[0, 0] = 1
    pts: Set[Tuple[int, int]] = {(0, 0)}
    while len(pts) > 0:
        up_pts = {(a + 1, b) for (a, b) in pts if a < h}
        left_pts = {(a, b + 1) for (a, b) in pts if b < w}
        pts = up_pts.union(left_pts)
        for a, b in pts:
            grid[a, b] = grid[a - 1, b] + grid[a, b - 1]
    return grid


def corner_paths(h: int, w: int) -> int:
    return generate_grid(h, w)[h, w]


if __name__ == '__main__':
    '''
    Starting in the top left corner of a 2x2 grid,
    and only being able to move to the right and down,
    there are exactly 6 routes to the bottom right corner.

    How many such routes are there through a 20x20 grid?
    '''
    print(corner_paths(20, 20))
