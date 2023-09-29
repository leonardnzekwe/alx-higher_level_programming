#!/usr/bin/python3
"""
a Python script that fetches https://alx-intranet.hbtn.io/status
"""
import requests


def main():
    """main program"""
    url = 'https://alx-intranet.hbtn.io/status'
    try:
        response = requests.get(url)
        response_text = response.text

        print("Body response:")
        print("\t- type:", type(response_text))
        print("\t- content:", response_text)

    except requests.RequestException as err:
        print("Error:", err)


if __name__ == "__main__":
    main()
