#!/usr/bin/python3
"""1-rectangle Module"""


class Rectangle:
    """Rectangle Class"""
    def __init__(self, width=0, height=0):
        """initialization method"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """width getter method"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter method"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height getter method"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter method"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """area() method that returns the rectangle area"""
        return self.width * self.height

    def perimeter(self):
        """perimeter() method that returns the rectangle perimeter"""
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """
        returns an “informal” and nicely printable
        string representation of an instance
        """
        text = ""
        if self.width == 0 or self.height == 0:
            return text
        i = 1
        while i <= self.height:
            text += ("#" * self.width)
            if i + 1 <= self.height:
                text += "\n"
            i += 1
        return text

    def __repr__(self):
        """
        Instance method that returns an “official”
        string representation of an instance
        """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """
        Instance method called when an instance is deleted
        """
        print("Bye rectangle...")
