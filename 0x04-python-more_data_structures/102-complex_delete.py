#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys_to_delete = []
    for k, v in a_dictionary.items():
        if v is value:
            keys_to_delete.append(k)
    for key in keys_to_delete:
        del a_dictionary[key]
    return a_dictionary