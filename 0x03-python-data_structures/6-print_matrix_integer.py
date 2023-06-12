#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for value in row:
            print("{:d}".format(value), end="")
            if row.index(value) < len(row) - 1:
                print(" ", end="")
        print(end="\n")
