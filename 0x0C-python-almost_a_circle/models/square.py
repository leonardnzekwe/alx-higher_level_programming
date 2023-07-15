#!/usr/bin/python3
"""
square module
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    square class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        init method
        """
        self.size = size
        super().__init__(self.size, self.size, x, y, id)

    @property
    def size(self):
        """
        size getter method
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        size setter method
        """
        self.width = value
        self.height = value
        self.__size = self.width

    def __str__(self):
        """
        obj str rep method
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
