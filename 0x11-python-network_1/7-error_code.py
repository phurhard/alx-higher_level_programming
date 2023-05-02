#!/usr/bin/python3
'''This python script sends a GET request
and prints the error code in cases of error
usig requests'''
import requests
import sys
try:
    req = requests.get(sys.argv[1])
    print(req.text)
except HTTPError as e:
    print(f"Error code: {e.code}")
