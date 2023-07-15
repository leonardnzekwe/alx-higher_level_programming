#!/usr/bin/python3
"""
base module
"""


import json


class Base:
    """
    Base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        init method
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        to_json_string method
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        save_to_file method
        """
        dict_list = []
        if list_objs is not None and len(list_objs) != 0:
            filename = type(list_objs[0]).__name__ + ".json"
            for obj in list_objs:
                dict_list.append(obj.to_dictionary())
        else:
            filename = type(list_objs).__name__ + ".json"

        with open(filename, "w", encoding="utf-8") as f:
            json_string = Base.to_json_string(dict_list)
            f.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """
        from_json_string method
        """
        py_list = []
        if json_string is None or len(json_string) == 0:
            return py_list
        return json.loads(json_string)
