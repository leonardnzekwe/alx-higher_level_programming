#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv, exit
    argc = len(argv) - 1
    if argc != 3:
        print(f"Usage: {argv[0]} <a> <operator> <b>")
        exit(1)
    elif argc == 3:
        a = int(argv[1])
        b = int(argv[3])
        operator = argv[2]
        if operator not in ['+', '-', '*', '/']:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        elif operator == '+':
            print("{} + {} = {}".format(a, b, add(a, b)))
        elif operator == '-':
            print("{} - {} = {}".format(a, b, sub(a, b)))
        elif operator == '*':
            print("{} * {} = {}".format(a, b, mul(a, b)))
        elif operator == '/':
            print("{} / {} = {}".format(a, b, div(a, b)))
