#!/usr/bin/python3
"""
a python script that list 10 commits
(from the most recent to oldest)
of the repository “rails” by the user “rails”
"""
from sys import argv
import requests


def main():
    """main program"""
    try:
        repo = argv[1]
        owner = argv[2]

        url = f"https://api.github.com/repos/{owner}/{repo}/commits"
        response = requests.get(url)

        if response.status_code == 200:
            commits_data = response.json()
            first_10_recent_commits = commits_data[0:10]

            for commit in first_10_recent_commits:
                sha = commit.get('sha')
                author_name = commit.get('commit').get('author').get('name')
                print(f"{sha}: {author_name}")
        else:
            print("Error:", response.status_code)
    except Exception as err:
        print("Error:", err)


if __name__ == "__main__":
    main()
