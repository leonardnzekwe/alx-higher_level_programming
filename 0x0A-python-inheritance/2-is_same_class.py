#!/usr/bin/python3
"""
2-is_same_class Module
a function that returns True if the object
is exactly an instance of the specified class
otherwise False
"""


def is_same_class(obj, a_class):
    """
    is_same_class function
    """
    return type(obj) == a_class
