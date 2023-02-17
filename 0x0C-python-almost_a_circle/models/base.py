#!/usr/bin/python3
import json
"""
Base class of a python package
"""


class Base:
    """ Base class"""
    __nb_objects = 0
    def __init__(self, id=None):
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    def to_json_string(list_dictionaries):
        """Returns the JSON representation of list dictionaries"""
        if list_dictionaries == None or not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    def save_to_file(cls, list_objs):
        """Writes the JSON string representation to a file"""
        if list_objs is None:

