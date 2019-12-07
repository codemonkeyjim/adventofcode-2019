#!/usr/bin/env python

if __name__ == "__main__":
    with open("data/day2.txt") as data:
        inputs = [int(item) for item in data.readline().split(",")]
    inputs[1] = 12
    inputs[2] = 2
    # inputs = [int(item) for item in '1,9,10,3,2,3,11,0,99,30,40,50'.split(',')]
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
    print(inputs[0])
