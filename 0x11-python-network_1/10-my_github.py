#!/usr/bin/python3
"""
a Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""
from sys import argv
import requests


def main():
    """main program"""
    try:
        username = argv[1]
        token = argv[2]

        auth = (username, token)
        url = 'https://api.github.com/user'

        response = requests.get(url, auth=auth)

        if response.status_code == 200:
            user_data = response.json()
            user_id = user_data.get('id')
            print(user_id)
        else:
            print(None)
    except Exception as err:
        print("Error:", err)


if __name__ == "__main__":
    main()
