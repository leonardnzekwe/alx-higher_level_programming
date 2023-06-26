#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as err_msg:
        print("Exception: {}".format(err_msg), file=stderr)
        return None
