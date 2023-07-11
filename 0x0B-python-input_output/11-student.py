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

    def to_json(self, attrs=None):
        """
        to_json method
        """
        stu_dict = {}
        for key, value in self.__dict__.items():
            if attrs is not None:
                for attr_key in attrs:
                    if attr_key == key:
                        stu_dict.update({attr_key: value})
            else:
                stu_dict.update({key: value})
        return stu_dict

    def reload_from_json(self, json):
        """
        reload_from_json function
        """
        for key, value in json.items():
            setattr(self, key, value)
