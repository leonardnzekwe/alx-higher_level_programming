#!/usr/bin/python3
"""
This is 2-matrix_divided Module
It contains matrix_divided(matrix, div) function
The function returns a new matrix
"""


def matrix_divided(matrix, div):
    """
    A function that divides all elements of a matrix
    """
    if (
        matrix is None or
        not matrix or
        not isinstance(matrix, list) or
        any(not isinstance(row, list) for row in matrix) or
        any(not isinstance(item, int) for row in matrix for item in row) and
        any(not isinstance(item, float) for row in matrix for item in row)
    ):
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
    if (
        div is None or
        not isinstance(div, int) and
        not isinstance(div, float)
    ):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    row = 0
    while row < len(matrix):
        if len(matrix[0]) != len(matrix[row]):
            raise TypeError("Each row of the matrix must have the same size")
        new_row = []
        for item in matrix[row]:
            new_row.append(round(item / div, 2))
        new_matrix.append(new_row)
        row += 1
    return new_matrix
