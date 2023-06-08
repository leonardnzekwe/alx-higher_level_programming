#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argc = len(argv) - 1
    if argc == 0:
        print(f"{argc:d} arguments.")
    elif argc == 1:
        print(f"{argc:d} argument:")
        print(f"{argc:d}: {argv[1]}")
    else:
        print(f"{argc:d} arguments:")
        i = 1
        while i < argc + 1:
            print(f"{i}: {argv[i]}")
            i = i + 1
