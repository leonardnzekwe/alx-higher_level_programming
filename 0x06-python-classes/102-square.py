#!/usr/bin/python3
"""This is 102-square Module"""


class Square:
    """This is Square class"""

    def __init__(self, size=0):
        """This is Initialization Method"""
        self.size = size

    @property
    def size(self):
        """This is size getter method"""
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

    def __eq__(self, other):
        """Override the equality operator (==)"""
        if isinstance(other, Square):
            return self.area() == other.area()

    def __ne__(self, other):
        """Override the is not equal operator (!=)"""
        if isinstance(other, Square):
            return self.area() != other.area()

    def __gt__(self, other):
        """Override the greater than operator (>)"""
        if isinstance(other, Square):
            return self.area() > other.area()

    def __ge__(self, other):
        """Override the greater than or equal operator (>=)"""
        if isinstance(other, Square):
            return self.area() >= other.area()

    def __lt__(self, other):
        """Override the less than operator (<)"""
        if isinstance(other, Square):
            return self.area() < other.area()

    def __le__(self, other):
        """Override the less than or equal operator (<=)"""
        if isinstance(other, Square):
            return self.area() <= other.area()
