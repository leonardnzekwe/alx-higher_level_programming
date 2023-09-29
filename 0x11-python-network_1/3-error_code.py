#!/usr/bin/python3
"""
a Python script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8)
"""
from urllib import request, error
from sys import argv


def main():
    """main program"""
    # Get URL paramter value
    url = argv[1]

    try:
        with request.urlopen(url) as response:
            # Read the response body and decode it in utf-8
            response_text = response.read().decode('utf-8')
            print(response_text)

    except error.HTTPError as err:
        # Handle HTTP errors and print the HTTP status code
        print("Error code:", err.code)


if __name__ == "__main__":
    main()
