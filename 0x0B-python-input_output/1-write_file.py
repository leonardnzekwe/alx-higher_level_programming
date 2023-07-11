#!/usr/bin/python3
"""
1-write_file Module
"""


def write_file(filename="", text=""):
    """
    write_file function
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
