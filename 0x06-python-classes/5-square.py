#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        self.__size = size
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
    def area(self):
        return (self.__size)**2
    def my_print(self):
        area = self.__size
        if area == 0:
            print()
        for i in range(area):
            for j in range(area):
                print('#', end="")
            print()
