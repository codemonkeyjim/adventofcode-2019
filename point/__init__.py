from __future__ import annotations


class Point(object):
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __hash__(self):
        return hash((self.x, self.y))

    def __repr__(self):
        return f"Point{str(self)}"

    def __str__(self):
        return f"({self.x}, {self.y})"

    def points_between(self, other) -> Set[Point]:
        points = set()
        if self.x == other.x:
            y_range = (
                range(self.y, other.y + 1)
                if self.y < other.y
                else range(other.y, self.y + 1)
            )
            for y in y_range:
                points.add(Point(self.x, y))
        elif self.y == other.y:
            x_range = (
                range(self.x, other.x + 1)
                if self.x < other.x
                else range(other.x, self.x + 1)
            )
            for x in x_range:
                points.add(Point(x, self.y))
        else:
            raise ValueError("Points must lie on a line parallel with an axis")
        return points

    def manhattan(self, other=None) -> int:
        if other is None:
            other = Point(0, 0)
        return abs(self.x - other.x) + abs(self.y - other.y)
