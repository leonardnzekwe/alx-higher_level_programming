#!/usr/bin/python3
"""
10-square Module
contains the Square class
a subclass of Rectangle
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    square class
    """
    def __init__(self, size):
        """
        Initialization method
        """
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        area function
        """
        return self.__size * self.__size

    def __str__(self):
        """
        str function
        """
        return f"[Square] {self.__size}/{self.__size}"
