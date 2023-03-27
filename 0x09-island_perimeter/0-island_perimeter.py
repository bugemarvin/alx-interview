#!/usr/bin/python3
'''
finding the perimeter of an island
'''


def island_perimeter(grid):
    '''Island perimeter
    argument
      - grid: lists
    Returns:
      - total number of islands
    '''

    total = 0

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:
                total += 4
                if row > 0 and grid[row-1][col] == 1:
                    total -= 2
                if col > 0 and grid[row][col-1] == 1:
                    total -= 2

    return total
