#!/usr/bin/python3
'''This python script returns the value of the
X-Requer-Id in the header of the request
using requests'''
import requests as url
import sys
if __name__ == "__main__":
    '''Code is not executed wen imported'''
    req = url.get(sys.argv[1])
    header = req.headers
    print(header.get('X-Request-Id'))
