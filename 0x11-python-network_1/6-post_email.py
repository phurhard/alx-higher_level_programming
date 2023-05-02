#!/usr/bin/python3
'''This script sends a  email as a POST request and
prints the body decoded as utf-8
using requests'''
import sys
import requests as url
if __name__ == "__main__":
    email = {'email': sys.argv[2]}
    req = url.post(sys.argv[1], data = {'email': sys.argv[2]})
    print(req.text)
