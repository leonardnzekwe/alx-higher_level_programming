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
        filename = cls.__name__ + ".json"
        if list_objs is not None:
            for obj in list_objs:
                dict_list.append(obj.to_dictionary())
        with open(filename, "w", encoding="utf-8") as f:
            json_string = cls.to_json_string(dict_list)
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

    @classmethod
    def create(cls, **dictionary):
        """
        create method
        """
        cls.dummy = cls(5, 5)
        cls.dummy.update(**dictionary)
        return cls.dummy

    @classmethod
    def load_from_file(cls):
        """
        load_from_file method
        """
        instances = []
        filename = cls.__name__ + ".json"
        with open(filename, "r", encoding="utf-8") as f:
            json_string = f.read()
            list_objs = cls.from_json_string(json_string)
        for obj in list_objs:
            instances.append(cls.create(**obj))
        return instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        save_to_file_csv method
        """
        dict_list = []
        filename = cls.__name__ + ".csv"
        if list_objs is not None:
            for obj in list_objs:
                dict_list.append(obj.to_dictionary())
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(dict_list, f)

    @classmethod
    def load_from_file_csv(cls):
        """
        load_to_file_csv method
        """
        instances = []
        filename = cls.__name__ + ".csv"
        with open(filename, "r", encoding="utf-8") as f:
            list_objs = json.load(f)
        for obj in list_objs:
            instances.append(cls.create(**obj))
        return instances
