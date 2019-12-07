import pytest

from point import Point
from wire import *


@pytest.mark.parametrize(
    "wire,points",
    [
        (
            "U1,L2,D2,R3",
            [
                Point(0, 0),
                Point(0, 1),
                Point(-1, 1),
                Point(-2, 1),
                Point(-2, 0),
                Point(-2, -1),
                Point(-1, -1),
                Point(0, -1),
                Point(1, -1),
            ],
        )
    ],
)
def test_wire_to_points(wire, points):
    assert wire_to_points(wire) == points
