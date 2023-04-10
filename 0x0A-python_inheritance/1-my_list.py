#!/usr/bin/python3
"""
Creates a class my list that inherits from list
"""


class MyList(list):
    """ My list class
        with a public instance of sorted list,
        that prints the list but in a sorted way
    """
    def __init__(self):
        super().__init__(self)

    def print_sorted(self):
        new_list = self
        return new_list.sort()

