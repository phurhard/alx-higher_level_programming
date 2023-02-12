#!/usr/bin/python3
import json
"""
Writes an object to a text file
using json representation
"""


def save_to_json_file(my_obj, filename):
    """ Save python obj to text file"""
    with open(filename, 'w') as f:
        written = f.write(json.dumps(my_obj))
    return written
