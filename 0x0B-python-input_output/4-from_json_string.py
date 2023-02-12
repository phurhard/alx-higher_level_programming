#!/usr/bin/python3
import json
"""
Converts from json strings to python objects
deserialization
"""


def from_json_string(my_str):
    """ Converts json to python obj"""
    return json.loads(my_str)
