#!/usr/bin/env python

from pathlib import Path

from intcode import Intcode


if __name__ == "__main__":
    with Path("data/day5.txt").open() as data:
        program = data.readline().strip()
    interpreter = Intcode(program)
    interpreter.execute()
