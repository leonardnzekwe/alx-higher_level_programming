#!/usr/bin/python3
def max_integer(my_list=[]):
    list_len = len(my_list) - 1
    if list_len == 0:
        return None
    my_list.sort()
    return my_list[list_len]
