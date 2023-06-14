#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    max_value = 0
    max_value_key = None
    for key, value in a_dictionary.items():
        if value > max_value:
            max_value = value
            max_value_key = key
    return max_value_key
