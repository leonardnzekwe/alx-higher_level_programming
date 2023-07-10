#!/usr/bin/python3
"""
8-rectangle Module
contains Rectangle class
which is a subclass of BaseGeometry class
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class
    """
    def __init__(self, width, height):
        """
        Initilization
        """
        super().integer_validator("height", height)
        super().integer_validator("width", width)
        self.__width = width
        self.__height = height
