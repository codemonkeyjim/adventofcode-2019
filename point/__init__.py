from __future__ import annotations
from typing import List


class Point(object):
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        if isinstance(other, str):
            return self._string_add(other)
        raise TypeError(f"Cannot add type {type(other)} to {type(self)}")

    def __hash__(self):
        return hash((self.x, self.y))

    def __repr__(self):
        return f"Point{str(self)}"

    def __str__(self):
        return f"({self.x}, {self.y})"

    def points_between(self, other) -> List[Point]:
        if self.x == other.x:
            step = 1 if self.y < other.y else -1
            return [
                Point(self.x, y) for y in range(self.y + step, other.y + step, step)
            ]
        elif self.y == other.y:
            step = 1 if self.x < other.x else -1
            return [
                Point(x, self.y) for x in range(self.x + step, other.x + step, step)
            ]
        else:
            raise ValueError("Points must lie on a line parallel with an axis")

    def manhattan(self, other=None) -> int:
        if other is None:
            other = Point(0, 0)
        return abs(self.x - other.x) + abs(self.y - other.y)

    def _string_add(self, step):
        direction = step[0]
        magnitude = int(step[1:])
        if "U" == direction:
            vector = Point(0, magnitude)
        elif "D" == direction:
            vector = Point(0, -magnitude)
        elif "L" == direction:
            vector = Point(-magnitude, 0)
        elif "R" == direction:
            vector = Point(magnitude, 0)
        else:
            raise ValueError(f"Unknown direction '{direction}'")
        return self + vector
