#!/usr/bin/python3
"""
a Python script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter
"""
from sys import argv
import requests


def main():
    """main program"""
    if len(argv) == 2:
        q = argv[1]
    else:
        q = ""

    url = 'http://0.0.0.0:5000/search_user'
    data = {'q': q}

    try:
        response = requests.post(url, data=data)
        response_json = response.json()

        if response_json:
            print(f"[{response_json['id']}] {response_json['name']}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
    except requests.RequestException as err:
        print("Error:", err)


if __name__ == "__main__":
    main()
