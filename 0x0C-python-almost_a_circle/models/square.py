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
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        size getter method
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        size setter method
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        obj str rep method
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """
        update method
        """
        no_of_args = len(args)

        if no_of_args != 0:
            if no_of_args >= 1:
                self.id = args[0]
            if no_of_args >= 2:
                self.size = args[1]
            if no_of_args >= 3:
                self.x = args[2]
            if no_of_args >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """
        to_dictionary method
        """
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
