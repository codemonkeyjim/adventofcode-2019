from typing import List


class Intcode(object):
    INSTRUCTION_LEN = 5
    OPCODE_LEN = 2
    PARAM_LEN = INSTRUCTION_LEN - OPCODE_LEN

    def __init__(self, program: str, inputs=[]):
        self.program = [int(value) for value in program.split(",")]
        self.inputs = inputs
        self.inputs.reverse()  # Since we're going to pop
        self.pointer = 0

    def _interpret(self) -> (int, List[bool]):
        instruction = str(self.next()).zfill(self.INSTRUCTION_LEN)
        opcode = int(instruction[self.OPCODE_LEN + 1 :])
        # Parameter modes are specified from n to 1, so we reverse them
        modes = list(
            reversed([bool(int(mode)) for mode in instruction[: self.PARAM_LEN]])
        )
        return opcode, modes

    def next(self) -> int:
        if self.pointer > len(self.program):
            raise StopIteration
        val = self.program[self.pointer]
        self.pointer += 1
        return val

    def get_value(self, val_or_loc: int, immediate: bool) -> int:
        return val_or_loc if immediate else self.program[val_or_loc]

    def execute(self):
        retval = None  # Return the last value outputted for testing purposes
        while True:
            opcode, modes = self._interpret()
            if opcode == 99:
                break
            elif opcode == 1:  # Addition
                a = self.get_value(self.next(), modes[0])
                b = self.get_value(self.next(), modes[1])
                dest = self.next()
                self.program[dest] = a + b
            elif opcode == 2:  # Multiplication
                a = self.get_value(self.next(), modes[0])
                b = self.get_value(self.next(), modes[1])
                dest = self.next()
                self.program[dest] = a * b
            elif opcode == 3:  # Input
                loc = self.next()
                try:
                    val = self.inputs.pop()
                except IndexError:
                    val = int(input(f"Line {self.pointer - 1}: Location {loc}? "))
                self.program[loc] = val
            elif opcode == 4:  # Output
                val = self.get_value(self.next(), modes[0])
                print(f"Line {self.pointer - 1}: {val}")
                retval = val
            elif opcode in (5, 6):  # Jump if...
                cond = self.get_value(self.next(), modes[0])
                loc = self.get_value(self.next(), modes[1])
                if (opcode == 5 and cond != 0) or (opcode == 6 and cond == 0):
                    self.pointer = loc
            elif opcode in (7, 8):  # Compare
                a = self.get_value(self.next(), modes[0])
                b = self.get_value(self.next(), modes[1])
                loc = self.next()
                self.program[loc] = int(
                    (opcode == 7 and a < b) or (opcode == 8 and a == b)
                )
            else:
                raise ValueError(f"Unknown opcode {opcode} at {self.pointer - 1}")
        return retval
