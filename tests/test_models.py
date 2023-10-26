import pytest
from pygame import Rect


class TestShape:

    def test_contains_required_properties(self, shape):

        assert shape.num == 1
        assert shape.name == "triangle"
        assert shape.color == "red"

    def test_rota90_raise_not_implemented_exception(self, shape):
        with pytest.raises(NotImplementedError):
            shape.rota180()

    def test_rota180_raise_not_implemented_exception(self, shape):
        with pytest.raises(NotImplementedError):
            shape.rota180()

    def test_rota270_raise_not_implemented_exception(self, shape):
        with pytest.raises(NotImplementedError):
            shape.rota270()

    def test_rota360_raise_not_implemented_exception(self, shape):
        with pytest.raises(NotImplementedError):
            shape.rota360()


class TestShapeS:

    def test_inherit_from_shape_parent(self, shape_s):
        assert shape_s.color == "red"

    def test_contains_default_type_s(self, shape_s):
        assert shape_s.name == "s"

    def test_contains_property_shape_list(self, shape_s):
        assert shape_s.shape_list == [
            Rect(50, 0, 50, 50),
            Rect(100, 0, 50, 50),
            Rect(0, 50, 50, 50),
            Rect(50, 50, 50, 50),
        ]

    def test_rota180_shape(self, shape_s):

        shape_s.rota180()

        assert shape_s.shape_list == [
            Rect(0, 0, 50, 50),
            Rect(50, 100, 50, 50),
            Rect(0, 50, 50, 50),
            Rect(50, 50, 50, 50),
        ]

    def test_rota360_shape(self, shape_s):

        shape_s.rota360()

        assert shape_s.shape_list == [
            Rect(100, 0, 50, 50),
            Rect(150, -100, 50, 50),
            Rect(0, 50, 50, 50),
            Rect(50, 50, 50, 50),
        ]

    def test_move_shape_180deg(self, shape_s):

        assert shape_s.shape_list == [
            Rect(50, 0, 50, 50),
            Rect(100, 0, 50, 50),
            Rect(0, 50, 50, 50),
            Rect(50, 50, 50, 50),
        ]

        up_push_count = shape_s.move(1)

        assert up_push_count == 1
        assert shape_s.shape_list == [
            Rect(0, 0, 50, 50),
            Rect(50, 100, 50, 50),
            Rect(0, 50, 50, 50),
            Rect(50, 50, 50, 50),
        ]

    def test_move_shape_360deg(self, shape_s):

        # If no key is selected, the shape keep
        # his position while falling

        assert shape_s.shape_list == [
            Rect(50, 0, 50, 50),
            Rect(100, 0, 50, 50),
            Rect(0, 50, 50, 50),
            Rect(50, 50, 50, 50),
        ]

        up_push_count = shape_s.move(0)

        assert up_push_count == 0
        assert shape_s.shape_list == [
            Rect(100, 0, 50, 50),
            Rect(150, -100, 50, 50),
            Rect(0, 50, 50, 50),
            Rect(50, 50, 50, 50),
        ]


class TestShapeSquare:

    def test_inherit_from_shape_parent(self, shape_square):
        assert shape_square.color == "red"

    def test_contains_default_type_s(self, shape_square):
        assert shape_square.name == "square"

    def test_contains_property_shape_list(self, shape_square):
        assert shape_square.shape_list == [
            Rect(0, 50, 50, 50)
        ]

    def test_do_not_move_since_a_square(self, shape_square):

        assert shape_square.shape_list == [
            Rect(0, 50, 50, 50)
        ]

        shape_square.move(1)
        shape_square.move(0)

        assert shape_square.shape_list == [
            Rect(0, 50, 50, 50)
        ]


class TestShapeU:

    def test_inherit_from_shape_parent(self, shape_u):
        assert shape_u.color == "red"

    def test_contains_default_type_u(self, shape_u):
        assert shape_u.name == "u"

    def test_contains_property_shape_list(self, shape_u):
        assert shape_u.shape_list == [
            Rect(0, 0, 50, 50),
            Rect(100, 0, 50, 50),
            Rect(0, 50, 50, 50),
            Rect(50, 50, 50, 50),
            Rect(100, 50, 50, 50),
        ]

    def test_rota_90(self, shape_u):
        assert shape_u.shape_list == [
            Rect(0, 0, 50, 50),
            Rect(100, 0, 50, 50),
            Rect(0, 50, 50, 50),
            Rect(50, 50, 50, 50),
            Rect(100, 50, 50, 50),
        ]

        shape_u.rota90()

        assert shape_u.shape_list == [
            Rect(0, 0, 50, 50),
            Rect(50, 0, 50, 50),
            Rect(0, 50, 50, 50),
            Rect(0, 100, 50, 50),
            Rect(50, 100, 50, 50),
        ]

    def test_rota_180(self, shape_u):
        assert shape_u.shape_list == [
            Rect(0, 0, 50, 50),
            Rect(100, 0, 50, 50),
            Rect(0, 50, 50, 50),
            Rect(50, 50, 50, 50),
            Rect(100, 50, 50, 50),
        ]

        shape_u.rota180()

        assert shape_u.shape_list == [
            Rect(0, 0, 50, 50),
            Rect(100, 0, 50, 50),
            Rect(0, 50, 50, 50),
            Rect(150, -50, 50, 50),
            Rect(150, 0, 50, 50),
        ]

    def test_rota_270(self, shape_u):
        assert shape_u.shape_list == [
            Rect(0, 0, 50, 50),
            Rect(100, 0, 50, 50),
            Rect(0, 50, 50, 50),
            Rect(50, 50, 50, 50),
            Rect(100, 50, 50, 50),
        ]

        shape_u.rota270()

        assert shape_u.shape_list == [
            Rect(0, 0, 50, 50),
            Rect(100, 0, 50, 50),
            Rect(0, 100, 50, 50),
            Rect(0, 100, 50, 50),
            Rect(50, 100, 50, 50),
        ]

    def test_rota_360(self, shape_u):
        assert shape_u.shape_list == [
            Rect(0, 0, 50, 50),
            Rect(100, 0, 50, 50),
            Rect(0, 50, 50, 50),
            Rect(50, 50, 50, 50),
            Rect(100, 50, 50, 50),
        ]

        shape_u.rota360()

        assert shape_u.shape_list == [
            Rect(0, 0, 50, 50),
            Rect(150, 0, 50, 50),
            Rect(0, 0, 50, 50),
            Rect(50, 50, 50, 50),
            Rect(150, 0, 50, 50),
        ]
