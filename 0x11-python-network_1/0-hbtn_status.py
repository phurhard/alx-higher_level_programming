#!/usr/bin/python3
import urllib.request as url
'''This python file displays the status of the webpage accessed using urllib'''
if __name__ == "__main__":
    with url.urlopen("https://alx-intranet.hbtn.io/status") as req:
        status = req.read()
        print('Body response:')
        print(f"\t - type: {type(status)}")
        print(f"\t - content: {status}")
        print(f"\t - utf content: {status.decode('utf-8')}")
