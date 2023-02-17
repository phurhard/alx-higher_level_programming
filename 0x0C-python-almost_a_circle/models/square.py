#!/usr/bin/python3
from models.rectangle import Rectangle
"""
Square class that builds on rectangle
"""


class Square(Rectangle):
    """Square class with a size as width and height, 2D Position
    reference and also it has input validation."""
    def __init__(self, size, x=0, y=0, id=None):
        """Instantiate a Square with certain dimmensions:
        Arguments:
            size {int}  --  The dimmensions of the new Square.
        Keyword Arguments:
            x {int} --  The coordinate in the X axis of a square
                        in a 2D space(default: {0}).
            y {int} --  The coordinate in the Y axis of a square
                        in a 2D space(default: {0}).
            id {int} -- The integer number that represent the object
                        among other base objects (default: {None}).
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return (f'[Square] ({self.id}) {self.x}/{self.y} - {self.width}')

    @property
    def size(self):
        return super().width
    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates certain fields of the instance,
        which are specified by args or kwargs.
        Arguments:
            Args and Kwargs:
`                id {int}        --  The integer value that represents the new
                                    id of the instance.
                size {int}      --  The integer value that represents the new
                                    size of the instance.
                x {int}         --  The integer value that represents the new X
                                    coordinate of the instance.
                y {int}         --  The integer value that represents the new
                                    Y coordinate of the instance.
        """
        actual = [self.id, self.size, self.x, self.y]
        if args:
            new_args = list(args[:len(args)]) + actual[len(args):]
        if not args:
            parsed_kwargs = [
                kwargs.get('id'),
                kwargs.get('size'),
                kwargs.get('x'),
                kwargs.get('y')
            ]
            new_args = [
                parsed_kwargs[i] if parsed_kwargs[i] is not None else actual[i]
                for i in range(len(actual))
            ]
        if args or kwargs:
            (self.id, self.size, self.x, self.y) = new_args

    def to_dictionary(self):
        """Returns the dictionary represenation of Rectangle"""
        Dict = {
                'id':self.id, 'size':self.width, 'x':self.x, 'y':self.y
                }
        return Dict

