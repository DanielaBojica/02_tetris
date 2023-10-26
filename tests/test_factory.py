from oop_5.exercise_2.factory import ShapeFactory
from oop_5.exercise_2.models import (
    Shape, ShapeBar, ShapeS,
    ShapeU, ShapeSquare
)


class TestShapeFactory:

    def test_contains_property_colors(self):

        assert ShapeFactory.colors == [
            "green",
            "red",
            "yellow",
            "blue"
        ]

    def test_contains_property_shapes(self):

        assert ShapeFactory.shapes == [
            ShapeBar,
            ShapeS,
            ShapeU,
            ShapeSquare,
        ]

    def test_generate_new_shape(self):

        shape = ShapeFactory.generate_new_shape()
        assert isinstance(shape, Shape)
        assert shape.name in ["square", "s", "u", "bar"]

    def test_generate_combined_shape(self):
        shape1 = ShapeFactory.generate_new_shape()
        shape2 = ShapeFactory.generate_new_shape()
        shape = ShapeFactory.generate_combined_shape(shape1, shape2)
        assert isinstance(shape, Shape)
        assert shape.name == "custom"
