#!/usr/bin/python3
"""
Defines a student class
"""


class Student:
    """ Student class """
    def __init__(self, first_name, last_name, age):
        """Instantiation of firstname, lastname and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Retrieves the dictionary representation of the Student class"""
        if not isinstance(attrs, list):
            return vars(self)
        return {k: v for k, v in self.__dict__.items() if k in attrs}
