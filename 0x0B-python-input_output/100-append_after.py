#!/usr/bin/python3
"""
100-append_after Module
"""


def append_after(filename="", search_string="", new_string=""):
    """
    append_after function
    """
    with open(filename, "r+", encoding="utf-8") as f:
        lines = f.readlines()
        f.seek(0)
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
        f.truncate()
