#!/usr/bin/python3
"""
100-my_int
"""


class MyInt(int):
    """
    MyInt class
    """
    def __init__(self, value):
        """
        Initialization method
        """
        self.value = value

    def __eq__(self, other):
        """
        equality inversion method
        """
        if self.value == other:
            return False
        return True

    def __ne__(self, other):
        """
        not equal inversion method
        """
        if self.value != other:
            return False
        return True
