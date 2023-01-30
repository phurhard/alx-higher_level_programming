#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0,0)):
        self.__size = size
        self.__position = position
    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self, value):
        self.__size = value
        if type(self.__size) != int:
            raise TypeError('size must be integer')
        if self.__size < 0:
            raise ValueError('size must be >= 0')
    @property
    def position(self):
        return self.__position
    @position.setter
    def position(self, value):
        self.__position = value
        if len(self.__position) < 2 or position[0] < 0 or position[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
    def area(self):
        """Public instance of method Area which returns the area of the square """
        return (self.__size)**2
    def my_print(self):
        """ Prints to the stdout the square with the character #"""
        area = self.__size
        position = self.__position
        if area == 0:
            print()
        for space in position:
            print(" ", end="")
            for row in range(area):
                for column in range(area):
                    print('#', end="")
                print()
            print()
