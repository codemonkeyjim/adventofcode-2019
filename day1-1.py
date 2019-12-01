#!/usr/bin/env python

from math import trunc


def fuel_needed(mass: int) -> int:
    return trunc(mass / 3) - 2


if __name__ == "__main__":
    with open("data/day1.txt") as data:
        total = sum([fuel_needed(int(line)) for line in data])
    print(total)
