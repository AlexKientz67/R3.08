import math

class Point:
    def __init__(self, x : float, y : float):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def distanceCord(self, x : float, y : float) -> float:
        return math.dist((self.x, self.y), (x, y))

    def distancePoint(self, point) -> float:
        return math.dist((self.x, self.y), (point.x, point.y))

first = Point(1, 1)
second = Point(1, 1)

print(first.distancePoint(second))