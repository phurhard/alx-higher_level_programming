#!/usr/bin/python3
'''This module is not executed when imported,
and it prints the status of the webpage
https://alx-intranet.hbtn.io/status
using the requests package'''
import requests as url
'''This python file displays the status of the webpage accessed using urllib'''
if __name__ == "__main__":
    '''Starting out, making sure the module is not executed ehen imported'''
    response = url.get("https://alx-intranet.hbtn.io/status")
    print('Body response:')
    print(f"\t - type: {type(response.text)}")
    print(f"\t - content: {response.text}")
