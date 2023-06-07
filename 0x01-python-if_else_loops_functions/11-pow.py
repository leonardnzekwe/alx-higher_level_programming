#!/usr/bin/python3
def pow(a, b):
    result = 1
    if b >= 0:
        for i in range(b):
            result = result * a
    else:
        for i in range(-b):
            result = result / a
    return round(result, 20)
