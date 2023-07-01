#!/usr/bin/python3
"""
This is 5-text_indentation Module
It contains the text_indentation(text) function
Prints a text with 2 new lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    A function that prints a text parameter
    """
    if text is None or not isinstance(text, str):
        raise TypeError("text must be a string")

    spec_chars = ['.', '?', ':']
    lines = ""
    line = ""

    for char in text:
        line += char
        if char in spec_chars:
            lines += line.strip()
            lines += "\n\n"
            line = ""

    lines += line.strip()
    print(lines, end="")
