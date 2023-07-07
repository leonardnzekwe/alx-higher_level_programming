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
    if type(a) not in (int, float):
        raise TypeError("a must be an integer or float")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer or float")

    a = int(a)
    b = int(b)

    return a + b
