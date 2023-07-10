#!/usr/bin/python3
"""
3-is_kind_of_class Module
contains is_kind_of_class(obj, a_class) function
that returns True if the object is an instance of
or if the object is an instance of a class that was inherited
otherwise False
"""


def is_kind_of_class(obj, a_class):
    """
    is_kind_of_class function
    """
    return isinstance(obj, a_class)
