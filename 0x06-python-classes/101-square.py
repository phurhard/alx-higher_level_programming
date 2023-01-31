#!/usr/bin/python3
"""
101-square
Built on 6-square
Creates a class Square
return area of the square
"""


class Square:
    """ class Square """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes the size and position of the square """
        self.__size = size
        self.__position = position

    """ Setting up the size of the square """
    @property
    def size(self):
        """ Getter for the size attribute """
        return self.__size

    @size.setter
    def size(self, value):
        """ Setter for the size attribute"""
        self.__size = value
        if type(self.__size) != int:
            raise TypeError('size must be integer')
        if self.__size < 0:
            raise ValueError('size must be >= 0')

        """ Setting up geter and setter for the position attribute """
    @property
    def position(self):
        """ Getter for the position attribute"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for the position attribute"""
        if len(value) != 2 or not isinstance(value, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        if any(num < 0 for num in value):
            raise TypeError('position must be a tuple of 2 positive integers')
        if any(not isinstance(num, int) for num in value):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """Public instance of method Area
        which returns the area of the square """
        return (self.__size)**2

    def my_print(self):
        """ Prints to the stdout the square with the character #"""
        area = self.__size
        position = self.__position
        if area == 0:
            print()
            return
        for end in range(position[1]):
            """in the range of the last value go to a new line"""
            print()
        for i in range(area):
            """ range of the area """
            for space in range(position[0]):
                print(" ", end="")
            for row in range(area):
                print('#', end="")
            print()

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
        for end in range(position[1]):
            """in the range of the last value go to a new line"""
            string += "\n"
        for i in range(area):
            """ range of the area """
            for space in range(position[0]):
                string += " "
            for row in range(area):
                string += '#'
            string += "\n"
        return string[:-1]
