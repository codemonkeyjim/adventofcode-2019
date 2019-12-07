#!/usr/bin/env python

from pathlib import Path

from point import Point
from wire import wire_to_points


if __name__ == "__main__":
    with Path("data/day3.txt").open() as data:
        paths = [wire_to_points(wire.strip()) for wire in data.readlines()]
    joins = set(paths[0]).intersection(paths[1])  # HACK: Assumes only two wires!
    joins.remove(Point(0, 0))

    nearest = min(joins, key=lambda point: point.manhattan())
    print(f"Nearest by distance: {nearest.manhattan()}")

    path_lens = {
        point: paths[0].index(point) + paths[1].index(point) for point in joins
    }

    closest = min(path_lens, key=path_lens.get)
    print(f"Shortest total path: {path_lens[closest]}")
