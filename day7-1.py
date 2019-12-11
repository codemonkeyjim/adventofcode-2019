#!/usr/bin/env python

from itertools import permutations
from pathlib import Path

from intcode import Intcode

AMP_COUNT = 5


if __name__ == "__main__":
    with Path("data/day7.txt").open() as data:
        program = data.readline().strip()
    results = {}
    for order in permutations(range(0, AMP_COUNT), AMP_COUNT):
        output = 0
        for phase in order:
            interpreter = Intcode(program, inputs=[phase, output])
            output = interpreter.execute()
        results[str(order)] = output
    max_seq = max(results, key=results.get)
    print(f"{max_seq}: {results[max_seq]}")
