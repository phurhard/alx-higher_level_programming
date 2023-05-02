#!/usr/bin/python
import urllib.request as url
import sys
'''This python script return the value of X-Request-Id
in the header of the request'''
if __name__ == "__main__":
    '''Code is not executed wen imported'''
    with url.urlopen(sys.argv[1]) as req:
        header = req.info()
        print(header.get('X-Request-Id'))
