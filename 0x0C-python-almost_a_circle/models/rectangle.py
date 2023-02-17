#!/usr/bin/python3
from models.base import Base
"""
Rectangle class that inherits from base
it has width and height, and private attributes x and y
"""


class Rectangle(Base):
    """Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Instantiation of the class attributes
        and validation of its iput values
        """
        super().__init__(id)
        self.__width = self.validate('width', width)
        self.__height = self.validate('height', height)
        self.__x = self.validate('x', x)
        self.__y = self.validate('y', y)

    def validate(self, name, value):
        """ Validation of the input values to the rectangle class"""
        if type(value) != int:
            raise TypeError(f'{name} must be an integer')
        if name in ['width', 'height']:
            if value <= 0:
                raise ValueError(f'{name} must be > 0')
            else:
                return value
        if name in ('x', 'y') and value < 0:
            raise ValueError(f'{name} must be >= 0')
        else:
            return value

    @property
    def width(self):
        """Getter for the width property of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the rectangle width attribute"""
        self.validate('width', value)
        self.__width = value

    @property
    def height(self):
        """Getter for the rectangle height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the rectagle height attribute"""
        self.validate('height', value)
        self.__height = value

    @property
    def x(self):
        """Getter for the x value """
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for the x value"""
        self.validate('x', value)
        self.__x = value

    @property
    def y(self):
        """Getter for the y value"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for the y value"""
        self.validate('y', value)
        self.__y = value

    def area(self):
        """ Returns area of the rectangle instance"""
        area = self.width * self.height
        return area

    def display(self):
        """ Displays the shape of a rectangle using #"""
        for space in range(self.y):
            print("\n", end="")
        for row in range(self.height):
            print(f'{" " * self.x} {"#" * self.width}')
            
    def __str__(self):
        """Overides the initial method and returns a new way of printing
        Returns:
            {str} -- The string representation of the rectangle and its attributes
        """
        return (f'[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}')
    
    def update(self, *args, **kwargs):
        """Assigns an rgument to each attribute"""
        
        actual = [self.id, self.width, self.height, self.x, self.y]
        if args:
            new_args = list(args[:len(args)]) + actual[len(args):]
        if not args:
            parsed_kwargs = [
                kwargs.get('id'),
                kwargs.get('width'),
                kwargs.get('height'),
                kwargs.get('x'),
                kwargs.get('y')
            ]
            new_args = [
                parsed_kwargs[i] if parsed_kwargs[i] is not None else actual[i]
                for i in range(len(actual))
            ]
        if args or kwargs:
            (self.id, self.width, self.height, self.x, self.y) = new_args
        """
        try:
            if len(args) != 0:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            else:
                for key, value in kwargs.items():
                    print(f'{key}')
        except Exception as e:
            pass
        """

    def to_dictionary(self):
        """Returns the dictionary represenation of Rectangle"""
        Dict = {
                'id':self.id, 'width':self.width, 'height':self.height, 'x':self.x, 'y':self.y
                }
        return Dict
