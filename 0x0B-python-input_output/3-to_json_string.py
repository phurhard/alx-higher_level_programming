#!/usr/bin/python3
import json
"""
Converts a python object into a json string
"""


def to_json_string(my_obj):
    """ Returns the converted object"""
    return json.dumps(my_obj)
