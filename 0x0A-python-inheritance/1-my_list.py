#!/usr/bin/python3
"""
1-my_list Module
contains print_sorted(self) function
that prints the list, but sorted (ascending sort)
"""

try:
    class MyList(list):
        """
        MyList class
        """
        def print_sorted(self):
            """
            print_sorted function
            """
            new_list = []
            new_list = sorted(self)
            print(new_list)
except Exception as err:
    raise type(err)(str(err))
