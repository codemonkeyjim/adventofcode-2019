import mock
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


@pytest.mark.parametrize("input_str", ["1", "5", "-1"])
def test_input_output_instruction(input_str):
    program = "3,0,4,0,99"  # Output the input
    interpreter = Intcode(program)
    with mock.patch("builtins.input", side_effect=[input_str]):
        assert interpreter.execute() == int(input_str)


@pytest.mark.parametrize(
    "program,input_str,output_int",
    [
        ("3,9,8,9,10,9,4,9,99,-1,8", 8, 1),  # Is input equal to 8 (positional)
        ("3,9,8,9,10,9,4,9,99,-1,8", 7, 0),
        ("3,9,7,9,10,9,4,9,99,-1,8", 7, 1),  # Is input less than 8 (positional)
        ("3,9,7,9,10,9,4,9,99,-1,8", 9, 0),
        ("3,3,1108,-1,8,3,4,3,99", 8, 1),  # Is input equal to 8 (immediate)
        ("3,3,1108,-1,8,3,4,3,99", 7, 0),
        ("3,3,1107,-1,8,3,4,3,99", 7, 1),  # Is input less than 8 (immediate)
        ("3,3,1107,-1,8,3,4,3,99", 9, 0),
        # Is input equal to 0 (positional, jumps)
        ("3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9", 0, 0),
        ("3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9", 3, 1),
        # Is input equal to 0 (immediate, jumps)
        ("3,3,1105,-1,9,1101,0,0,12,4,12,99,1", 0, 0),
        ("3,3,1105,-1,9,1101,0,0,12,4,12,99,1", 3, 1),
    ],
)
def test_comparison_instructions(program, input_str, output_int):
    interpreter = Intcode(program)
    with mock.patch("builtins.input", side_effect=[input_str]):
        assert interpreter.execute() == output_int


@pytest.mark.parametrize(
    "input_str,output_int", [(3, 999), (8, 1000), (10, 1001)],
)
def test_longer_program(input_str, output_int):
    program = "3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99"
    interpreter = Intcode(program)
    with mock.patch("builtins.input", side_effect=[input_str]):
        assert interpreter.execute() == output_int
    interpreter = Intcode(program, inputs=[int(input_str)])
    assert interpreter.execute() == output_int
