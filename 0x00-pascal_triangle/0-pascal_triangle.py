#!/usr/bin/python3
'''pascal_triangle
'''


def pascal_triangle(n):
    '''
    function def pascal_triangle(n):
    that returns a list of lists of integers
    representing the Pascal’s triangle of n:
    Returns an empty list if n <= 0
    You can assume n will be always an integer
    '''
    triangle = []
    if n <= 0:
        triangle
    else:
        for i in range(n):
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = triangle[i-1][j-1] + triangle[i-1][j]
            triangle.append(row)
    return triangle
