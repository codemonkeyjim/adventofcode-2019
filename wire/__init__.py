from typing import List

from point import Point


def wire_to_points(wire: str) -> List[Point]:
    current = Point(0, 0)
    points = [current]

    for step in wire.split(","):
        next_point = current + step
        points += current.points_between(next_point)
        current = next_point
    return points
