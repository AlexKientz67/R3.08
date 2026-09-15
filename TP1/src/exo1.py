import math


class Point:
    """
    Classe pour la création d'un point

    :param x: Coordonnée x
    :param y: Coordonnée y
    """
    def __init__(self, x: float = 0.0, y: float = 0.0):
        if not isinstance(x, (int, float)):
            raise TypeError("La coordonnée x doit être un nombre")

        if not isinstance(y, (int, float)):
            raise TypeError("La coordonnée y doit être un nombre")

        self.__x = x
        self.__y = y

    def __str__(self) -> str:
        return f"({self.__x}, {self.__y})"

    @property
    def get_x(self) -> float:
        return self.__x

    @property
    def get_y(self) -> float:
        return self.__y

    def distanceCord(self, x: float, y: float) -> float:
        if not isinstance(x, (int, float)):
            raise TypeError("x doit être un nombre")

        if not isinstance(y, (int, float)):
            raise TypeError("y doit être un nombre")

        return math.dist((self.__x, self.__y), (x, y))

    def distancePoint(self, point) -> float:
        if not isinstance(point, Point):
            raise TypeError("Le paramètre doit être un Point")

        return math.dist(
            (self.__x, self.__y),
            (point.get_x, point.get_y)
        )


class Cercle:
    """
    Classe pour la création d'un cercle

    :param centre: Point qui définit le centre
    :param rayon: float qui définit le rayon du cercle
    """
    def __init__(self, centre: Point, rayon: float):

        if not isinstance(centre, Point):
            raise TypeError("Le centre doit être un Point")

        if not isinstance(rayon, (int, float)):
            raise TypeError("Le rayon doit être un nombre")

        if rayon <= 0:
            raise ValueError("Le rayon doit être supérieur à 0")

        self.__centre = centre
        self.__rayon = rayon

    def get_centre(self) -> Point:
        return self.__centre

    def get_rayon(self) -> float:
        return self.__rayon

    def calc_diametre(self) -> float:
        return self.__rayon * 2

    def perimetre(self) -> float:
        return 2 * math.pi * self.__rayon

    def surface(self) -> float:
        return math.pi * self.__rayon ** 2

    def check_intersection(self, cercle2) -> int:
        if not isinstance(cercle2, Cercle):
            raise TypeError("Le paramètre doit être un Cercle")

        distance = self.__centre.distancePoint(cercle2.get_centre())

        if distance <= self.__rayon + cercle2.get_rayon():
            return 1
        else:
            return 0

    def check_point_in_cercle(self, point2: Point) -> int:
        if not isinstance(point2, Point):
            raise TypeError("Le paramètre doit être un Point")

        distance = self.__centre.distancePoint(point2)

        if distance < self.__rayon:
            return 1
        else:
            return 0


class Rectangle:
    """
    Classe pour la création d'un rectangle

    :param point: Point de départ du cercle
    :param longuer: Longueur du rectangle
    :param largeur: Largeur du rectangle
    """
    def __init__(
        self,
        point_bas_gauche: Point = None,
        hauteur: float = 1,
        largeur: float = 1,
        point_haut_droit: Point = None
    ):

        if point_bas_gauche is None:
            point_bas_gauche = Point(0, 0)

        if not isinstance(point_bas_gauche, Point):
            raise TypeError(
                "Le point bas gauche doit être un Point"
            )

        if not isinstance(hauteur, (int, float)):
            raise TypeError("La hauteur doit être un nombre")

        if not isinstance(largeur, (int, float)):
            raise TypeError("La largeur doit être un nombre")

        if hauteur <= 0:
            raise ValueError("La hauteur doit être supérieure à 0")

        if largeur <= 0:
            raise ValueError("La largeur doit être supérieure à 0")

        if point_haut_droit is not None:

            if not isinstance(point_haut_droit, Point):
                raise TypeError(
                    "Le point haut droit doit être un Point"
                )

            largeur = (point_haut_droit.get_x - point_bas_gauche.get_x)

            hauteur = (point_haut_droit.get_y- point_bas_gauche.get_y)

            if largeur <= 0:
                raise ValueError("Le point haut droit doit être à droite du point bas gauche")

            if hauteur <= 0:
                raise ValueError("Le point haut droit doit être au-dessus du point bas gauche")

        self.__point_bas_gauche = point_bas_gauche
        self.__hauteur = hauteur
        self.__largeur = largeur

    def calcul_surface(self) -> float:
        return self.__largeur * self.__hauteur

    def calcul_perimetre(self) -> float:
        return 2 * (self.__largeur + self.__hauteur)

    def position_bas_gauche(self) -> Point:
        return self.__point_bas_gauche

    def position_bas_droit(self) -> Point:
        return Point(self.__point_bas_gauche.get_x + self.__largeur, self.__point_bas_gauche.get_y)

    def position_haut_gauche(self) -> Point:
        return Point(self.__point_bas_gauche.get_x, self.__point_bas_gauche.get_y + self.__hauteur)

    def position_haut_droit(self) -> Point:
        return Point(self.__point_bas_gauche.get_x + self.__largeur, self.__point_bas_gauche.get_y + self.__hauteur)

    def check_point_in_rectangle(self, point: Point) -> int:

        if not isinstance(point, Point):
            raise TypeError("Le paramètre doit être un Point")

        x = point.get_x
        y = point.get_y

        x_min = self.position_bas_gauche().get_x
        x_max = self.position_bas_droit().get_x

        y_min = self.position_bas_gauche().get_y
        y_max = self.position_haut_gauche().get_y

        if x_min <= x <= x_max and y_min <= y <= y_max:
            return 1

        return 0

"""
def main():
    print("point")
    point = Point(0, 0)
    p1 = Point(0, 0)
    p2 = Point(1, 1)

    print(p1.distanceCord(2, 2))
    print(p1.distancePoint(p2))

    print("cercle")
    c1 = Cercle(p1, 5)
    c2 = Cercle(p2, 5)

    print(c1.perimetre())
    print(c1.check_point_in_cercle(p2))
    print(c1.calc_diametre())
    print(c1.check_intersection(c2))
    
    try:
        c1 = Cercle(p1, -5)
    except (TypeError, ValueError) as e:
        print(f"Erreur : {e}")

    print("rectangle")

    r1 = Rectangle(p1, 5, 10)
    print(r1.calcul_surface())
    print(r1.calcul_perimetre())
    print(r1.position_bas_gauche())
    print(r1.position_bas_droit())
    print(r1.position_haut_gauche())
    print(r1.position_haut_droit())
    print(r1.check_point_in_rectangle(p2))



if __name__ == "__main__":
    main()
"""