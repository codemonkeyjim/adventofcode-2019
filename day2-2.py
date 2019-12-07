#!/usr/bin/env python


def run_program(noun: int, verb: int) -> int:
    with open("data/day2.txt") as data:
        inputs = [int(item) for item in data.readline().split(",")]
    inputs[1] = noun
    inputs[2] = verb
    i = 0
    while True:
        opcode = inputs[i]
        if opcode == 99:
            break
        a = inputs[i + 1]
        b = inputs[i + 2]
        dest = inputs[i + 3]

        if opcode == 1:
            inputs[dest] = inputs[a] + inputs[b]
        elif opcode == 2:
            inputs[dest] = inputs[a] * inputs[b]
        else:
            raise ValueError(f"Unknown opcode: {opcode}")
        i += 4
    return inputs[0]


if __name__ == "__main__":
    for noun in range(0, 100):
        for verb in range(0, 100):
            output = run_program(noun, verb)
            if output == 19690720:
                print(f"{noun:02}{verb:02}")
                exit()
    print("No solution found")
