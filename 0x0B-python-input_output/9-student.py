#!/usr/bin/python3
"""
Defines a student class
"""


class Student:
    """ Student class """
    def __init__(self, first_name, last_name, age):
        """Instantiation of the firstname, lastname, age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves the dictionary representation of the Student instance"""
        return vars(self)
