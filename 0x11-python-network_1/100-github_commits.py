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
        repoName = sys.argv[1]
        ownerName = sys.argv[2]
        req = requests.get(f"https://api.github.com/repos/{ownerName}/{repoName}/commits?author=rails")
        jsonFile = req.json()
        for commit in jsonFile[:10]:
            sha = commit.get('sha', 'unknown')
            authorName = commit.get('commit', {}).get('author', {}).get('name', 'unknown')
            print(f'{sha}: {authorName}')
    except Exception as e:
        print(e)
