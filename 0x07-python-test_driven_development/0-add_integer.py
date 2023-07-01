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
        not isinstance(a, int) and
        not isinstance(a, float)
    ):
        raise TypeError("a must be an integer")
    if (
        b is None or
        not isinstance(b, int) and
        not isinstance(b, float)
    ):
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return a + b
