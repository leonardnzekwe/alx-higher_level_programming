#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argc = len(argv) - 1
    result = 0
    if argc >= 2:
        i = 1
        while i - 1 < argc:
            result = result + int(argv[i])
            i = i + 1
    print(result)
