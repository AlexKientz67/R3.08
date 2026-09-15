from src.exo1 import Point, Cercle
import pytest

def test_cercle_centre():
    p1 = Point(0,0)
    c1 = Cercle(p1, 5)

    assert c1.get_centre() == p1

def test_cercle_rayon():
    p1 = Point(0,0)
    c1 = Cercle(p1, 5)
    assert c1.get_rayon() == 5

def test_cercle_diametres():
    p1 = Point(0,0)
    c1 = Cercle(p1, 5)

    assert c1.calc_diametre() == 10

def test_cercle_perimetres():
    p1 = Point(0,0)
    c1 = Cercle(p1, 5)

    assert c1.perimetre() == 31.41592653589793

def test_cercle_surface():
    p1 = Point(0,0)
    c1 = Cercle(p1, 5)

    assert c1.surface() == 78.53981633974483

def test_check_intersection():
    p1 = Point(0,0)
    c1 = Cercle(p1, 5)
    p2 = Point(2,2)
    c2 = Cercle(p2, 5)

    assert c1.check_intersection(c2) == 1

def test_point_in_cercle():
    p1 = Point(0,0)
    c1 = Cercle(p1, 5)

    p2 = Point(2,2)
    assert c1.check_point_in_cercle(p2) == 1

def test_type_error_not_point():
    with pytest.raises(TypeError):
        Cercle(".", 5)

def test_type_error_not_rayon():
    with pytest.raises(TypeError):
        Cercle(Point(0,0), ".")

def test_rayon_inferieur_zero():
    with pytest.raises(ValueError):
        Cercle(Point(0,0), 0)

def test_check_intersection_not_cercle():
    with pytest.raises(TypeError):
        p1 = Point(0,0)
        c1 = Cercle(p1, 5)

        c1.check_point_in_cercle(".")

def test_check_check_point_not_point():
    with pytest.raises(TypeError):
        p1 = Point(0,0)
        c1 = Cercle(p1, 5)
        c1.check_point_in_cercle(".")