#!/usr/bin/python3
"""This is 6-square Module"""


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
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            for num in value:
                if isinstance(num, int) and num >= 0:
                    continue
                else:
                    raise TypeError("position must be a \
                            tuple of 2 positive integers")
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
        else:
            i = 0
            while i < self.size:
                if self.position[1] >= 0:
                    k = 0
                    while k < self.position[0]:
                        print(" ", end="")
                        k += 1
                j = 0
                while j < self.size:
                    print("#", end="")
                    j += 1
                print()
                i += 1
