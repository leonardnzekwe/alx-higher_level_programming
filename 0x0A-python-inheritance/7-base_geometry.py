#!/usr/bin/python3
"""
6-base_geometry Module
contains BaseGeometry class
with its methods and attributes
"""


class BaseGeometry:
    """
    BaseGeometry class
    """
    def area(self):
        """
        area function
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        integer_validator function
        """
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
