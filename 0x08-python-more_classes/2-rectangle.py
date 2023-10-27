#!/usr/bin/python3
"""
2-rectangle
Built on 1-rectangle
defines a rectangle class and
initializes a private instance attribute named width and height
calculates the area and the perimeter
return class with instance attribute
"""


class Rectangle:
    """
    Creates a Rectangle class and initailizes two private instance attribute
    with both setters and getters
    """
    def __init__(self, width=0, height=0):
        """
        Initializes the width and height attribute
        """
        self.__width = width
        self.__height = height

    """ setters and getters"""

    @property
    def width(self):
        """ Retrieves the value of the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the value for the width
        conforming to the pree-requiaites"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """ Retrieves the value of the height"""
        return self.__height
    
    @height.setter
    def height(self, value):
        """Sets the value for the height
        conforming to the pree-requiaites"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """Calculates the Area of the Rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """ Calculates the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        length = 2 * self.__height
        breadth = 2 * self.__width
        return length + breadth
