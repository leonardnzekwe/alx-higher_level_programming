#!/usr/bin/python3
"""This is 3-square Module"""


class Square:
    """This is Square class"""

    def __init__(self, size=0):
        """This is Initialization Method"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Public instance method
        that returns the current square area
        """
        return self.__size * self.__size
