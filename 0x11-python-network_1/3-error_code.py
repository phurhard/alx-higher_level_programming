#!/usr/bin/python3
'''This python script sends a GET request
and prints the error code in cases of error'''
import urllib
from urllib.request import Request, urlopen
from urllib.error import HTTPError
import sys
try:
    with urlopen(sys.argv[1]) as req:
        print(req.read().decode('utf-8'))
except HTTPError as e:
    print(f"Error code: {e.code}")
