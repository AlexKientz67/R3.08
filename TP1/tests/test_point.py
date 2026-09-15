from src.exo1 import Point


def test_creation_point():
    point = Point(2, 3)

    assert point.get_x == 2
    assert point.get_y == 3


def test_distance():
    point = Point(0, 0)
    assert point.distanceCord(3, 4) == 5