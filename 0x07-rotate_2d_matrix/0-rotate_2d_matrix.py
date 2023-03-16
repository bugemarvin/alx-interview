#!/usr/bin/python3
"""Rotate matrix in reverse
"""


def rotate_2d_matrix(matrix):
    """transpose a matrix by swaping the cols
    """
    for a in range(len(matrix)):
        for b in range(a, len(matrix)):
            matrix[a][b], matrix[b][a] = matrix[b][a], matrix[a][b]
    for value in range(len(matrix)):
        matrix[value].reverse()
    return matrix
