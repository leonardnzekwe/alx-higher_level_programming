#!/usr/bin/python3
"""
This is 0-add_integer Module
It contains the add_integer(a, b=98) function
The function returns an integer: the addition of a and b
"""


def add_integer(a, b=98):
    """
    A function that adds 2 integers
    """
    if (
        a is None or
        type(a) != int and
        type(a) != float
    ):
        raise TypeError("a must be an integer")
    if (
        b is None or
        type(b) != int and
        type(b) != float
    ):
        raise TypeError("b must be an integer")

    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)

    return a + b
