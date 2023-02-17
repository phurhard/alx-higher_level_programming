#!/usr/bin/python3
import json
"""
Base class of a python package
"""


class Base:
    """ Base class"""
    __nb_objects = 0
    def __init__(self, id=None):
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON representation of list dictionaries"""
        if list_dictionaries == None or not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Saves a list of instance objects in a JSON formatted file.
        Arguments:
            list_objs {list[dict]}  --  The list of Base object instances
                                        (with its properties)
                                        that will be processed.
        """
        with open('{}.json'.format(cls.__name__), 'w') as file:
            if not list_objs:
                file.write(cls.to_json_string([]))
            else:
                instances_list = [obj.to_dictionary() for obj in list_objs]
                file.write(cls.to_json_string(instances_list))

    @staticmethod
    def from_json_string(json_string):
        """Parses a JSON formatted string to a list of its python
        representation.
        Arguments:
            json_string {str}   --  The JSON formatted string that will be
                                    processed.
        Returns:
            {list[dict]}  --    The list with dictionaries of
                                Base object instances
                                (with its properties).
        """
        if not json_string:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Creates an instance of a certain Base subclass and fill it with
        specific values for its fields.
        Returns:
            {cls}   --  The new instance of a @cls initialized with the values
                        stored in @dictionary.
        """
        if cls.__name__ == 'Rectangle':
            response = cls(1, 1, 0, 0)
        if cls.__name__ == 'Square':
            response = cls(1, 0, 0)
        response.update(**dictionary)
        return response

    @classmethod
    def load_from_file(cls):
        """Creates a list of Base subclass objects
        based on the content of a JSON formatted file.
        Returns:
            {list[cls]}     --  The list with the instances of the objects
                                stored in the JSON file.
        """
        try:
            with open('{}.json'.format(cls.__name__), 'r') as file:
                data = file.read()
                json_data = cls.from_json_string(data)
                list_instances = [cls.create(**ins) for ins in json_data]
                return list_instances
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Prints a rectangle in a turtle canvas.
        Arguments:
            list_rectangles {list[Rectangle]}   --  A list with Rectangles
                                                    to print.
            list_squares {list[Square]}         --  A list with Squares
                                                    to print.
        """
        drawer = turtle.Turtle()
        drawer.shape("turtle")

        def draw_figure(x, y, width, height, pen):
            """Helper function to print any figure.
            """
            color = ('green', 'blue', 'yellow',
                     'red', 'black', 'orange', 'pink')

            pen.penup()
            pen.speed(5)
            pen.goto(x, y)
            pen.pendown()
            pen.begin_fill()
            pen.color(random.choice(color))
            for i in range(4):
                pen.forward(width if i % 2 == 0 else height)
                pen.left(90)
            pen.end_fill()

        for rectangle in list_rectangles:
            draw_figure(rectangle.x, rectangle.y, rectangle.width,
                        rectangle.height, drawer)
        for square in list_squares:
            draw_figure(square.x, square.y, square.size, square.size, drawer)

        drawer.hideturtle()
        screen = turtle.Screen()
        screen.exitonclick()

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Saves a list of instance objects in a CSV formatted file.
        Arguments:
            list_objs {list[dict]}  --  The list of Base object instances
                                        (with its properties)
                                        that will be processed.
        """
        with open('{}.csv'.format(cls.__name__), "w") as file:
            instances_list = [
                instance.to_dictionary() for instance in list_objs
            ]
            if cls.__name__ == "Rectangle":
                fields = ["id", "width", "height", "x", "y"]
            else:
                fields = ["id", "size", "x", "y"]
            data_writer = csv.DictWriter(file, fields)
            data_writer.writeheader()
            data_writer.writerows(instances_list)

    @classmethod
    def load_from_file_csv(cls):
        """Creates a list of Base subclass objects
        based on the content of a CSV formatted file.
        Returns:
            {list[cls]}     --  The list with the instances of the objects
                                stored in the CSV file.
        """
        try:
            with open('{}.csv'.format(cls.__name__), 'r') as file:
                data = csv.DictReader(file)
                lines = [dict(line) for line in data]
                props = [{
                    key: int(value)
                    for (key, value) in dictionary.items()
                } for dictionary in lines]
                instances = [cls.create(**prop) for prop in props]
            return instances
        except FileNotFoundError:
            return []

