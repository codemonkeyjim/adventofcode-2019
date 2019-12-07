from typing import List


class Intcode(object):
    INSTRUCTION_LEN = 5
    OPCODE_LEN = 2
    PARAM_LEN = INSTRUCTION_LEN - OPCODE_LEN

    def __init__(self, program: str):
        self.program = [int(value) for value in program.split(",")]
        self.pointer = 0

    def _interpret(self, loc) -> (int, List[bool]):
        instruction = str(self.program[loc]).zfill(self.INSTRUCTION_LEN)
        opcode = int(instruction[self.OPCODE_LEN + 1 :])
        # Parameter modes are specified from n to 1, so we reverse them
        modes = list(
            reversed([bool(int(mode)) for mode in instruction[: self.PARAM_LEN]])
        )
        return opcode, modes
