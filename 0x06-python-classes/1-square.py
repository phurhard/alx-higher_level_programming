#!/usr/bin/python3
"""
1-square
Built on 0-square
defines a square class and
initializes a private instance attribute named size
return class with instance attribute
"""


class Square:
    """
    Creates a square class and initailizes a private instance attribute
    """
    def __init__(self, size):
        """
        Initializes the size attribute
        """
        self.__size = size
