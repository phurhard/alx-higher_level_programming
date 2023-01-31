#!/usr/bin/python3
"""
3-square
Built on 2-square
Creates a class Square
return area of the square
"""


class Square:
    """
    Class Square created """
    def __init__(self, size=0):
        """ Initializing the size private attribute
        and setting the initial value to 0 """
        self.__size = size
        if type(self.__size) != int:
            """ Checking if the type of size input is int """
            raise TypeError('size must be integer')
        if self.__size < 0:
            """ Checking if input is greater than 0 """
            raise ValueError('size must be >= 0')

    def area(self):
        """ A function to calculate and return the area
        of the square """
        return (self.__size)**2
