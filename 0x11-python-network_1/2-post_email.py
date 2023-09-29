#!/usr/bin/python3
"""
a Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""
from urllib import request, parse
from sys import argv


def main():
    """main program"""
    try:
        # Get URL and email parameter values
        url = argv[1]
        email = argv[2]

        # Encode the email parameter
        data = parse.urlencode({'email': email}).encode('utf-8')

        with request.urlopen(url, data=data) as response:
            # Read the response body and decode it in utf-8
            response_text = response.read().decode('utf-8')
            print(response_text)

    except Exception as err:
        print("Error:", err)


if __name__ == "__main__":
    main()
