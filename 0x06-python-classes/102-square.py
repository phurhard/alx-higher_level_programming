#!/usr/bin/python3
"""
102-square
Built on 4-square and 101-square
Creates a class Square
has an instance of Square
Can perform multiple comparators
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

    def __repr__(self):
        """ Prints to the stdout the square with the character #
        Can be used as an instance of itself without
        neccessarily calling the my_print method
        """
        area = self.__size
        string = ""
        position = self.__position
        if area == 0:
            return ""
        for _ in range(position[1]):
            """in the range of the last value go to a new line"""
            string += "\n"
        for _ in range(area):
            """ range of the area """
            for _ in range(position[0]):
                string += " "
            for _ in range(area):
                string += '#'
            string += "\n"
        return string[:-1]
    def __gt__(self, other):
        return self.__size > other.__size
    def __lt__(self, other):
        return self.__size < other.__size
    def __le__(self, other):
        return self.__size <= other.__size
    def __ge__(self, other):
        return self.__size >= other.__size
    def __eq__(self, other):
        return self.__size == other.__size
    def __ne__(self, other):
        return self.__size != other.__size
