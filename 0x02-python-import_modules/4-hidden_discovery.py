#!/usr/bin/python3
if __name__ == "__main__":
    module = __import__("hidden_4")
    module_names = dir(module)
    for name in module_names:
        if not name.startswith('__'):
            print(name)
