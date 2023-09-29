#!/usr/bin/python3
"""a Python script that fetches https://alx-intranet.hbtn.io/status"""
from urllib import request


def main():
    """main program"""
    url = 'https://alx-intranet.hbtn.io/status'
    try:
        with request.urlopen(url) as response:
            # Read the response body as bytes
            response_bytes = response.read()

            # Decode the response bytes into UTF-8
            response_text = response_bytes.decode('utf-8')

            print("Body response:")
            print("\t- type:", type(response_bytes))
            print("\t- content:", response_bytes)
            print("\t- utf8 content:", response_text)

    except Exception as err:
        print("Error:", err)


if __name__ == "__main__":
    main()
