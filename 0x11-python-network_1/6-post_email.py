#!/usr/bin/python3
"""
a Python script that takes in a URL and an email address
sends a POST request to the passed URL with the email as a parameter
and finally displays the body of the response
"""
from sys import argv
import requests


def main():
    """main program"""
    try:
        url = argv[1]
        email = argv[2]

        # Create a dictionary containing the email parameter
        data = {'email': email}

        response = requests.post(url, data=data)
        response_text = response.text
        print(response_text)

    except Exception as err:
        print("Error:", err)


if __name__ == "__main__":
    main()
