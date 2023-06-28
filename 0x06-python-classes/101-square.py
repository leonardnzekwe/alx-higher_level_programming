#!/usr/bin/python3
"""This is 101-square Module"""


class Square:
    """This is Square class"""

    def __init__(self, size=0, position=(0, 0)):
        """This is Initialization Method"""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """This is position getter method"""
        return self.__position

    @position.setter
    def position(self, value):
        """This is position setter method"""
        if (
            not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(num, int) for num in value) or
            not all(num >= 0 for num in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        Public instance method
        that returns the current square area
        """
        return self.size * self.size

    def my_print(self):
        """
        Public instance method
        that prints in stdout the square with the character #
        """
        if self.size == 0:
            print()
            return

        for _ in range(self.position[1]):
            print()

        for _ in range(self.size):
            print((" " * self.position[0]) + ("#" * self.size))

    def __str__(self):
        """Special method that returns a string representation of an object"""
        obj_str_rep = ""
        if self.size == 0:
            obj_str_rep += "\n"
            return obj_str_rep

        for _ in range(self.position[1]):
            obj_str_rep += "\n"

        for _ in range(self.size):
            obj_str_rep += (" " * self.position[0]) + ("#" * self.size) + "\n"

        return obj_str_rep
