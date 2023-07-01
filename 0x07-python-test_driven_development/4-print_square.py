#!/usr/bin/python3
"""
This is 4-print_square Module
It contains the print_square(size) function
The function prints a square with the character #
"""


def print_square(size):
    """
    A function that prints a square with the character #
    """
    if (
        size is None or
        not isinstance(size, int) or
        size < 0 and isinstance(size, float)
    ):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    i = 1
    while i <= size:
        print("#" * size)
        i += 1
