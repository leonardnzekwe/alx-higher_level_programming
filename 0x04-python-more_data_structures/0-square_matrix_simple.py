#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    pow_matrix = []
    for row in matrix:
        pow_matrix.append(list(map(lambda x : x**2, row)))
    return pow_matrix
