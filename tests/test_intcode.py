import pytest

from intcode import Intcode


def test_init():
    program = "1101,100,-1,4,0"
    interpreter = Intcode(program)
    assert interpreter.program == [1101, 100, -1, 4, 0]


@pytest.mark.parametrize(
    "program,opcode,modes",
    [
        ("1002,4,3,4", 2, [False, True, False]),
        ("11001,4,3,4", 1, [False, True, True]),
        ("3,10", 3, [False, False, False]),
    ],
)
def test_instruction_interpretation(program, opcode, modes):
    interpreter = Intcode(program)
    assert interpreter._interpret() == (opcode, modes)


@pytest.mark.parametrize(
    "program,location,value",
    [
        ("1,5,6,7,99,2,3,0", 7, 5),  # Indirect addition
        ("1101,2,4,5,99,0", 5, 6),  # Direct addition
        ("2,5,6,7,99,2,3,0", 7, 6),  # Indirect multiplication
        ("1102,2,4,5,99,0", 5, 8),  # Direct multiplication
        ("1,5,6,7,99,-5,8,0", 7, 3),  # Indirect subtraction
        ("1002,4,3,4,33", 4, 99),  # Write stop instruction
        ("1101,100,-1,4,0", 4, 99),  # Write stop instruction
    ],
)
def test_program_execution(program, location, value):
    interpreter = Intcode(program)
    interpreter.execute()
    assert interpreter.program[location] == value
