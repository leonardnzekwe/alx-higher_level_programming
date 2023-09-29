#!/usr/bin/python3
"""
a Python script that takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id variable
found in the header of the response
"""
from urllib import request
from sys import argv


def main():
    """main program"""
    try:
        # Get the URL paramter value
        url = argv[1]

        with request.urlopen(url) as response:
            # Check if the 'X-Request-Id' header is present in the response
            if 'X-Request-Id' in response.headers:
                request_id = response.headers['X-Request-Id']
                print(request_id)

    except Exception as err:
        print("Error:", err)


if __name__ == "__main__":
    main()
