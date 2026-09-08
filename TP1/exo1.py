import math

import math

class Point:
    """
    Représente un point dans un plan cartésien.

    Un point est défini par deux coordonnées x et y.
    La classe permet également de calculer la distance
    entre deux points.
    """

    def __init__(self, x: float = 0.0, y: float = 0.0):
        """
        Initialise un point avec ses coordonnées.

        Args:
            x (float): Coordonnée horizontale du point.
            y (float): Coordonnée verticale du point.
        """
        self.x = x
        self.y = y

    def __str__(self) -> str:
        """Retourne les coordonnées du point sous forme de chaîne de caractères."""
        return f"({self.x}, {self.y})"

    def distanceCord(self, x: float, y: float) -> float:
        """
        Calcule la distance entre le point courant et des coordonnées données.

        Args:
            x (float): Coordonnée x de l'autre point.
            y (float): Coordonnée y de l'autre point.

        Returns:
            float: Distance entre les deux points.
        """
        return math.dist((self.x, self.y), (x, y))

    def distancePoint(self, point) -> float:
        """
        Calcule la distance entre le point courant et un autre point.

        Args:
            point (Point): Autre point avec lequel calculer la distance.

        Returns:
            float: Distance entre les deux points.
        """
        return math.dist((self.x, self.y), (point.x, point.y))


class Cercle:
    """
    Représente un cercle défini par un centre et un rayon.
    """

    def __init__(self, centre: Point, rayon: float):
        """
        Initialise un cercle.

        Args:
            centre (Point): Centre du cercle.
            rayon (float): Rayon du cercle.
        """
        self.centre = centre
        self.rayon = rayon

    def __str__(self) -> str:
        """Retourne les informations du cercle sous forme de chaîne de caractères."""
        return f"({self.centre.x}, {self.centre.y}, {self.rayon})"

    def calc_diametre(self) -> float:
        """
        Calcule le diamètre du cercle.

        Returns:
            float: Diamètre du cercle.
        """
        return self.rayon * 2

    def perimetre(self) -> float:
        """
        Calcule le périmètre du cercle.

        Returns:
            float: Périmètre du cercle.
        """
        return 2 * math.pi * self.rayon

    def surface(self) -> float:
        """
        Calcule la surface du cercle.

        Returns:
            float: Surface du cercle.
        """
        return math.pi * self.rayon ** 2

    def check_intersection(self, cercle2) -> int:
        """
        Vérifie si deux cercles se touchent ou se chevauchent.

        Args:
            cercle2 (Cercle): Deuxième cercle à tester.

        Returns:
            int: 1 si les cercles se touchent ou se chevauchent,
                 0 sinon.
        """
        distance = self.centre.distancePoint(cercle2.centre)

        if distance <= self.rayon + cercle2.rayon:
            return 1
        else:
            return 0

    def check_point_in_cercle(self, point2: Point) -> int:
        """
        Vérifie si un point se trouve à l'intérieur du cercle.

        Args:
            point2 (Point): Point à tester.

        Returns:
            int: 1 si le point est à l'intérieur,
                 0 sinon.
        """
        distance = self.centre.distancePoint(point2)

        if distance < self.rayon:
            return 1
        else:
            return 0

class Rectangle:


def main():
    point1 = Point(0, 0)
    point2 = Point(1, 1)

    cercle = Cercle(point1, 2)

    cercle2 = Cercle(point2, 2)
    print(cercle.calc_diametre())
    print(cercle.perimetre())
    print(cercle.surface())
    print(cercle.check_intersection(cercle2))

    print(cercle.check_point_in_cercle(point2))

if __name__ == "__main__":
    main()