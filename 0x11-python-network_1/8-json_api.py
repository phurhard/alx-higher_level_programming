#!/usr/bin/python3
'''Python script that takes in a letter and sends a POST re
quest to http://0.0.0.0:5000/search_user with the letter as
a parameter.'''
import sys
import requests
if __name__ == '__main__':
    if (len(sys.argv) == 2):
        q = sys.argv[1]
    else:
        q = ""
    req = requests.post("http://0.0.0.0:5000/search_user", data={'q': q})
    if (req.status_code == 200):
        try:
            jfile = req.json()
            if jfile:
                print(f"[{jfile['id']}] {jfile['name']}")
            else:
                print("No result")
        except Exception as e:
            print(f"Not a valid JSON")
    else:
        print(f'Error: {req.status_code}')
