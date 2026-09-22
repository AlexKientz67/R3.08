import pytest
from src.main import Personnage

def test_pseudo():
    p1 = Personnage("Mage1")
    assert p1.pseudo == "Mage1"

def test_niveau():
    p1 = Personnage("Mage1")
    assert p1.niveau == 1

def test_initiative():
    p1 = Personnage("Mage1")
    assert p1.initiative == 1

def test_nbr_point_de_vie():
    p1 = Personnage("Mage1")
    assert p1.nbr_point_de_vie == 1

def test_set_point_de_vie():
    p1 = Personnage("Mage1")
    p1.nbr_point_de_vie = 5
    assert p1.nbr_point_de_vie == 5

def test_typeerror_pseudo():
    with pytest.raises(TypeError):
        p1 = Personnage(5)

def test_typeerror_niveau():
    with pytest.raises(TypeError):
        p1 = Personnage("Mage1", "1")

def test_typeerror_nbr_point_de_vie():
    with pytest.raises(TypeError):
        p1 = Personnage("Mage1", 1, "1")

def test_typeerrror_initiative():
    with pytest.raises(TypeError):
        p1 = Personnage("Mage1", 1, 1, "4")

def test_attaque():
    p1 = Personnage("test1")
    p2 = Personnage("test2")
    p1.attaque(p2)
    assert p1.nbr_point_de_vie == 0

def test_combat():
    p1 = Personnage("test1", 5, 50, 1)
    p2 = Personnage("test2", 5, 20, 1)

    p1.combat(p2)
    assert p1.nbr_point_de_vie == 30


def test_soigner():
    p1 = Personnage("test1", 5, 50, 1)
    p2 = Personnage("test2", 5, 1, 1)
    p1.soigner(p2)

    assert p2.nbr_point_de_vie == 5