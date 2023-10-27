#!/usr/bin/python3
"""
Defines a student class
"""


class Student:
    """ Student class """
    def __init__(self, first_name, last_name, age):
        """ initializing the firstname, lastname and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves a dictionary representation of a student instance"""
        if not isinstance(attrs, list):
            return vars(self)
        return {k: v for k, v in self.__dict__.items() if k in attrs}

    def reload_from_json(self, json):
        """ Replaces all attributes of the student instnce"""
        self.__dict__ = json
