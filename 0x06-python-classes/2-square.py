#!/usr/bin/python3
"""
2-square
Creates a square class based on 1-square
Returns {}
"""


class Square:

    """
    A class of Square with initialzed datas
    """
    def __init__(self, size=0):
        """
        Initializing the size attribute
        """
        self.__size = size
        if type(self.__size) != int:
            """ Ensuring size type is int """
            raise TypeError('size must be integer')
        if self.__size < 0:
            """ Checking that the input of size is not less than 0 """
            raise ValueError('size must be >= 0')
