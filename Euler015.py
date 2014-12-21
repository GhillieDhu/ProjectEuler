'''
Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20x20 grid?
'''

import sys

def lattice(height, width, lattices):
    if height == 1:
        lattices[height, width] = width + 1
    elif width == 1:
        lattices[height, width] = height + 1
    else:
        if (height - 1, width) not in lattices:
            lattices = lattice(height - 1, width, lattices)
        if (height, width - 1) not in lattices:
            lattices = lattice(height, width - 1, lattices)
        lattices[height, width] = lattices[height - 1, width] + lattices[height, width - 1]
    return lattices

if __name__ == '__main__':
    size = int(sys.argv[1])
    print(lattice(size, size, {})[size, size])
