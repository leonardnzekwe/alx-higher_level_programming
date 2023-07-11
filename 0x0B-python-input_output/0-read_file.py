#!/usr/bin/python3
"""
0-read_file Module
"""


def read_file(filename=""):
    """
    read_file function
    """
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
    print(content, end="")
