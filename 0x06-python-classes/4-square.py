#!/usr/bin/python3
"""This is 4-square Module"""


class Square:
    """This is Square class"""

    def __init__(self, size=0):
        """This is Initialization Method"""
        self.size = size

    @property
    def size(self):
        """This is size property"""
        return self.__size

    @size.setter
    def size(self, value):
        """This is size setter method"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Public instance method
        that returns the current square area
        """
        return self.size * self.size
