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

    def area(self):
        """
        implementation of the area method in the super class
        """
        return self.__width * self.__height

    def __str__(self):
        """
        str function
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
