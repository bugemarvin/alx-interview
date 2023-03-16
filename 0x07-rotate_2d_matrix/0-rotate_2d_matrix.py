#!/usr/bin/python3
"""Rotate matrix in reverse
"""


def rotate_2d_matrix(matrix):
    """Rotate 90%

    Keyword arguments:
    matrix -- a list as an argument
    Return: reversed list
    """

    matrix_3 = []
    matrix_2 = []
    matrix_1 = []

    for value in matrix:
        """_summary_
        """
        matrix_3.append(value[2])
        matrix_2.append(value[1])
        matrix_1.append(value[0])

    matrix[:] = [matrix_1[::-1], matrix_2[::-1], matrix_3[::-1]]
    return matrix
