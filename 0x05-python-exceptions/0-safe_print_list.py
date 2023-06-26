#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    try:
        while i < x:
            print(f"{my_list[i]}", end="")
            i = i + 1
    except Exception:
        pass
    finally:
        print()
        return i
