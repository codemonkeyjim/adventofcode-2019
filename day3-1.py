#!/usr/bin/env python

from pathlib import Path
from typing import Set

from point import Point


def wire_to_points(wire: str) -> Set[Point]:
    current = Point(0, 0)
    points = {current}

    for step in wire.split(","):
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
        next_point = current + vector
        points.update(current.points_between(next_point))
        current = next_point
    return points


if __name__ == "__main__":
    with Path("data/day3.txt").open() as data:
        paths = [wire_to_points(wire.strip()) for wire in data.readlines()]
    joins = paths[0].intersection(paths[1])  # HACK: Assumes only two wires!
    joins.remove(Point(0, 0))
    nearest = min(joins, key=lambda point: point.manhattan())
    print(nearest.manhattan())
