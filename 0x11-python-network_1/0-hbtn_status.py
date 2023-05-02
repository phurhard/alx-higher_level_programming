#!/usr/bin/python3
"""This module is not executed when imported,
and it prints the status of the webpage
https://alx-intranet.hbtn.io/status"""
import urllib.request as url

"""This python file displays the status of the webpage accessed using urllib"""

if __name__ == "__main__":
    """Starting out, making sure the module is not executed when imported"""

    with url.urlopen("https://alx-intranet.hbtn.io/status") as req:
        status = req.read()
        print('Body response:')
        print(f"\t- type: {type(status)}")
        print(f"\t- content: {status}")
        print(f"\t- utf content: {status.decode('utf-8')}")

