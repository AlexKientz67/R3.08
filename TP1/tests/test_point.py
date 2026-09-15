from src.exo1 import Point
import pytest


def test_point():
    point = Point(2, 3)

    assert point.get_x == 2
    assert point.get_y == 3


def test_distanceCord():
    point = Point(0, 0)
    assert point.distanceCord(3, 4) == 5

def test_distancePoint():
    p1 = Point(0, 0)
    p2 = Point(1, 0)

    assert p1.distancePoint(p2) == 1

def test_exception_type_y():
    with pytest.raises(TypeError):
        p1 = Point(0, ".")

def test_exception_type_x():
    with pytest.raises(TypeError):
        p1 = Point(".", 0)