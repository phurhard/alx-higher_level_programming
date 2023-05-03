#!/usr/bin/python3
''' Python script that takes a Github credentials and print the first 10 commits from newest to oldest
 * You must use the package requests and sys'''
import requests
import sys

if __name__ == "__main__":
    try:
        repoName = sys.argv[1]
        ownerName = sys.argv[2]
        url = f"https://api.github.com/repos/{ownerName}/{repoName}/commits?author=rails"
        req = requests.get(url)
        jsonFile = req.json()
        for commit in jsonFile[:10]:
            sha = commit['sha']
            authorName = commit['commit']['author']['name']
            print(f'{sha}: {authorName}')
    except Exception as e:
        print(e)
