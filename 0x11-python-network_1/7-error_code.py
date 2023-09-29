#!/usr/bin/python3
"""
a Python script that takes in a URL
sends a request to the URL and displays the body of the response
"""
from sys import argv
import requests


def main():
    """main program"""
    try:
        url = argv[1]
        response = requests.get(url)

        if response.status_code >= 400:
            print("Error code:", response.status_code)
        else:
            response_text = response.text
            print(response_text)

    except Exception as err:
        print("Error:", err)


if __name__ == "__main__":
    main()
