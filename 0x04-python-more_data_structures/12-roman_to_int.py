#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str or roman_string is None:
        return 0
    roman_num_spec = {
            'I': 1, 'V': 5, 'X': 10,
            'L': 50, 'C': 100,
            'D': 500, 'M': 1000
            }
    roman_int = 0
    prev_value = 0
    for char in reversed(roman_string):
        for key, value in roman_num_spec.items():
            if char == key:
                if value < prev_value:
                    roman_int = roman_int - value
                else:
                    roman_int = roman_int + value
                    prev_value = value
    return roman_int
