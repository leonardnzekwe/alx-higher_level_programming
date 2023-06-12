#!/usr/bin/python3
def max_integer(my_list=[]):
    my_list.sort()
    list_len = len(my_list) - 1
    return my_list[list_len]
