#!/usr/bin/python3
"""
Adds all arguments to a python list and save it to a json file
"""


import json
import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
"""
Add all arguments to a python list and then save them to a file
"""
filename = "add_item.json"
new = []
args = sys.argv[1:]
try:
    new = load_from_json_file(filename)
except Exception as e:
    pass
finally:
    save_to_json_file(new + args, filename)
