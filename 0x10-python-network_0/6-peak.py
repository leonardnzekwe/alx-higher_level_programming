#!/usr/bin/python3
"""Find a peak Module"""


def find_peak(list_of_integers):
    """Find a peak Function"""
    if list_of_integers:
        list_of_integers.sort()
        return list_of_integers[-1]
