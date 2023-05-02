#!/usr/bin/python3
'''This script sends a  email as a POST request and
prints the body decoded as utf-8'''
import sys
import urllib.request as url
from urllib.parse import urlencode
if __name__ == "__main__":
    email = {'email': sys.argv[2]}
    email = urlencode(email)
    email = email.encode('utf-8')
    reqq = url.Request(sys.argv[1], email)
    with url.urlopen(reqq) as req:
        print(req.read().decode('utf-8'))
