#!/usr/bin/python3
"""Rotate matrix in reverse
"""


def rotate_2d_matrix(matrix):
    """Rotate 90%

    Keyword arguments:
    matrix -- a list as an argument
    Return: reversed list
    """
    new_matrix = []
    for i in range(len(matrix[0])):
        new_row = []
        for j in range(len(matrix)):
            new_row.append(matrix[j][i])
        new_matrix.append(new_row[::-1])

    return new_matrix
