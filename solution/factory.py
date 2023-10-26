import random

from oop_5.exercise_2.solution.models import ShapeS, ShapeU, ShapeSquare, ShapeBar, Shape


class ShapeFactory:

    shapes = [
        ShapeBar,
        ShapeS,
        ShapeU,
        ShapeSquare,
    ]

    colors = [
        "green",
        "red",
        "yellow",
        "blue"
    ]

    @classmethod
    def generate_new_shape(cls):
        shape_class = random.choice(cls.shapes)
        shape_color = random.choice(cls.colors)

        shape = shape_class(1, shape_color)

        for shape_rect in shape.shape_list:
            shape_rect.x = 300 - shape_rect.width / 2 - shape_rect.x

        print(type(shape))
        return shape

    @staticmethod
    def generate_combined_shape(shape1, shape2):
        new_shape_list = shape1.shape_list + shape2.shape_list

        new_shape = Shape(1, "custom", "white")
        new_shape.shape_list = new_shape_list

        return new_shape
