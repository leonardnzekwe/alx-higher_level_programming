#!/usr/bin/python3
def uppercase(str):
    for c in str:
        c = ord(c)
        if 97 <= c and c <= 122:
            c = c - 32
        print("{}".format(chr(c)), end="")
    print()
