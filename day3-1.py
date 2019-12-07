#!/usr/bin/env python

from pathlib import Path
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


if __name__ == "__main__":
    with Path("data/day3.txt").open() as data:
        paths = [wire_to_points(wire.strip()) for wire in data.readlines()]
    joins = set(paths[0]).intersection(paths[1])  # HACK: Assumes only two wires!
    joins.remove(Point(0, 0))
    nearest = min(joins, key=lambda point: point.manhattan())
    print(nearest.manhattan())
