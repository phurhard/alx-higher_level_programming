#!/usr/bin/python3
"""
5-square
Built on 4-square
Creates a class Square
return area of the square
"""


class Square:
    """ class Square """
    def __init__(self, size=0):
        """ Initializing the private attribute size """
        self.__size = size

    @property
    def size(self):
        """ Getter method, to get the size """
        return self.__size

    @size.setter
    def size(self, value):
        """ Setter method to set the square size """
        self.__size = value
        if type(self.__size) != int:
            raise TypeError('size must be integer')
        if self.__size < 0:
            raise ValueError('size must be >= 0')

    def area(self):
        """ Area method tp return the area of the square """
        return (self.__size)**2

    def my_print(self):
        """ my_print method, to print out the square using # """
        area = self.__size
        if area == 0:
            print()
        for i in range(area):
            for j in range(area):
                print('#', end="")
            print()
