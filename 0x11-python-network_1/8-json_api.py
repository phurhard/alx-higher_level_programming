#!/usr/bin/python3
'''Python script that takes in a letter and sends a POST re
quest to http://0.0.0.0:5000/search_user with the letter as
a parameter.'''

import sys
import requests
if __name__ == '__main__':
    q = sys.argv[1] if (len(sys.argv) == 2) else ""
    req = requests.post("http://0.0.0.0:5000/search_user", data={'q': q})
    if (req.status_code == 200):
        try:
            if jfile := req.json():
                print(f"[{jfile['id']}] {jfile['name']}")
            else:
                print("No result")
        except Exception as e:
            print("Not a valid JSON")
    else:
        print(f'Error: {req.status_code}')
