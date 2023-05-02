#!/usr/bin/python3
import urllib
from urllib.request import Request, urlopen
from urllib.error import HTTPError
import sys
try:
    with urlopen(sys.argv[1]) as req:
        print(req.read().decode('utf-8'))
except HTTPError as e:
    if isinstance(e, urllib.error.HTTPError):
        print(f"Error code: {e.code}")
