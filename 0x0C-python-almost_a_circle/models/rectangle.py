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
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
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
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
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
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        y getter method
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        y setter method
        """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        area method
        """
        return self.width * self.height

    def display(self):
        """
        display method
        """
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def __str__(self):
        """
        str method
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """
        update method
        """
        no_of_args = len(args)

        if no_of_args != 0:
            if no_of_args >= 1:
                self.id = args[0]
            if no_of_args >= 2:
                self.width = args[1]
            if no_of_args >= 3:
                self.height = args[2]
            if no_of_args >= 4:
                self.x = args[3]
            if no_of_args >= 5:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.width = value
                if key == "height":
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """
        to_dictionary method
        """
        return {
            'x': self.x, 'y': self.y, 'id': self.id,
            'height': self.height, 'width': self.width
            }
