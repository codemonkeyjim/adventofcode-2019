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
    assert interpreter._interpret(0) == (opcode, modes)
