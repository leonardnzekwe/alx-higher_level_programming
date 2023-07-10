#!/usr/bin/python3
"""
101-add_attribute Module
"""


def add_attribute(obj, attr_name, attr_value):
    """
    add_attribute function
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    obj.__setattr__(attr_name, attr_value)
