#!/usr/bin/python3
"""
rectangle module
"""


from models.base import Base


class Rectangle(Base):
    """
    Rectangle class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        init method
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        width getter method
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        width setter method
        """
        self.__width = value

    @property
    def height(self):
        """
        height getter method
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        height setter method
        """
        self.__height = value

    @property
    def x(self):
        """
        x getter method
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        x setter method
        """
        self.__x = value

    @property
    def y(self):
        """
        y getter method
        """
        return self.__x

    @y.setter
    def y(self, value):
        """
        y setter method
        """
        self.__y = value
