#!/usr/bin/python3
"""
4-square
Built on 3-square
Creates a class Square
return area of the square
"""


class Square:
    """ Class Square """
    def __init__(self, size=0):
        """ Initializing the private attribute size """
        self.__size = size

    @property
    def size(self):
        """ A getter to get the size of the square """
        return self.__size

    @size.setter
    def size(self, value):
        """ A setter to set the value of the square size """
        self.__size = value
        if type(self.__size) != int:
            raise TypeError('size must be integer')
        if self.__size < 0:
            raise ValueError('size must be >= 0')

    def area(self):
        """ Method to calculate and return the area of the square """
        return (self.__size)**2
