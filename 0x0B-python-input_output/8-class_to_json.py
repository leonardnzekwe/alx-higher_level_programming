#!/usr/bin/python3
"""
8-class_to_json Module
"""


def class_to_json(obj):
    """
    class_to_json function
    """
    my_dict = {}
    if hasattr(obj, "__dict__"):
        for key, value in obj.__dict__.items():
            my_dict.update({key: value})
        return my_dict
