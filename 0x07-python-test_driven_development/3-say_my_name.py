#!/usr/bin/python3
"""
This is 3-say_my_name Module
It contains the say_my_name(first_name, last_name="") function
The function prints - My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    if (
        first_name is None or
        not isinstance(first_name, str)
    ):
        raise TypeError("first_name must be a string")
    if (
        last_name is None or
        not isinstance(last_name, str)
    ):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
