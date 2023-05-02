#!/usr/bin/python
'''This python script returns the value of the
X-Requer-Id in the header of the request'''
import urllib.request as url
import sys
if __name__ == "__main__":
    '''Code is not executed wen imported'''
    with url.urlopen(sys.argv[1]) as req:
        header = req.info()
        print(header.get('X-Request-Id'))
