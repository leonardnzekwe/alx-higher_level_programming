#!/usr/bin/python3
"""
9-student Module
"""


class Student:
    """
    student class
    """
    def __init__(self, first_name, last_name, age):
        """
        initialization method
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        to_json method
        """
        stu_dict = {}
        for key, value in self.__dict__.items():
            stu_dict.update({key: value})
        return stu_dict
