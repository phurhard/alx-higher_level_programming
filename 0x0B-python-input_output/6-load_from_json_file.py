#!/usr/bin/python3
import json
"""
Creates an object file from a JSON file
"""


def load_from_json_file(filename):
    """Loads object from a json file"""
    with open(filename, 'r') as f:
        return json.load(f)
