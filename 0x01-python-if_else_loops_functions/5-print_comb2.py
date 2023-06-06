#!/usr/bin/python3
for i in range(0, 100):
    if i <= 9:
        print("0{}, ".format(i), end="")
    if i > 9 and i <= 98:
        print("{}, ".format(i), end="")
    if i  == 99:
        print("{}".format(i))
