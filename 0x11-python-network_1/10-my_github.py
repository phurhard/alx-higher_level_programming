#!/usr/bin/python3
''' Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id
 * You must use Basic Authentication with a personal access
 token as password to access to your information
 (only read:user permission is needed)
 * The first argument will be your username
 * The second argument will be your password (in your case, a personal access token as password)
 * You must use the package requests and sys'''
import requests
import sys

if __name__ == "__main__":
    try:
        username = sys.argv[1]
        password = sys.argv[2]
        header = {"Authorization": "Basic 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"}
        req = requests.get("https://api.github.com/users/" + username, headers=header)
        jsonFile = req.json()
        print(jsonFile['id'])
    except Exception as e:
        print(e)
