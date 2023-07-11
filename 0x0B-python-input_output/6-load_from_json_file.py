#!/usr/bin/python3
"""
6-load_from_json_file Module
"""


import json


def load_from_json_file(filename):
    """
    load_from_json_file function
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
