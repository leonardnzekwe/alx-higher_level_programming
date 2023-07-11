#!/usr/bin/python3
"""
2-append_write Module
"""


def append_write(filename="", text=""):
    """
    append_write function
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
