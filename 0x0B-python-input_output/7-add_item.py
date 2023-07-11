#!/usr/bin/python3
"""
7-add_item Module
"""


from sys import argv
append_write = __import__('2-append_write').append_write
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def main():
    """
    main function
    """
    my_list = []
    content = ""
    filename = "add_item.json"
    try:
        content = load_from_json_file(filename)
    except Exception:
        append_write(filename, content)
    if len(content) != 0:
        for obj in content:
            my_list.append(obj)
    if len(argv) > 1:
        for args in argv:
            if args == argv[0]:
                continue
            my_list.append(args)
    save_to_json_file(my_list, filename)


main()
