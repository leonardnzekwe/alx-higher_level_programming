#!/usr/bin/python3
"""
4-inherits_from Module
contains a function
that returns True if the object is an instance of a class
that inherited (directly or indirectly)
4rm the specified class
otherwise False
"""


def inherits_from(obj, a_class):
    """
    an inheritance check function
    """
    return type(obj) != a_class and issubclass(type(obj), a_class)
