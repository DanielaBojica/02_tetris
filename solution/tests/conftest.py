from _pytest.fixtures import fixture

from oop_5.exercise_2.solution.models import Shape, ShapeS, ShapeSquare, ShapeU


@fixture
def shape():
    return Shape(1, "triangle", "red")


@fixture
def shape_s():
    return ShapeS(1, "red")


@fixture
def shape_square():
    return ShapeSquare(1, "red")


@fixture
def shape_u():
    return ShapeU(1, "red")