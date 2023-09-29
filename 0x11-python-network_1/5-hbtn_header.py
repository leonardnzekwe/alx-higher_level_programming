#!/usr/bin/python3
"""
a Python script that takes in a URL
sends a request to the URL and
displays the value of the variable X-Request-Id in the response header
"""
from sys import argv
import requests


def main():
    """main program"""
    try:
        url = argv[1]
        response = requests.get(url)

        # Check if the 'X-Request-Id' header is present in the response
        if 'X-Request-Id' in response.headers:
            request_id = response.headers['X-Request-Id']
            print(request_id)

    except Exception as err:
        print("Error:", err)


if __name__ == "__main__":
    main()
