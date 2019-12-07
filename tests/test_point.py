import pytest

from point import Point


def test_point_equivalence():
    assert Point(0, 0) == Point(0, 0)
    assert Point(1, 2) == Point(1, 2)
    assert Point(1, 2) != Point(2, 1)


@pytest.mark.parametrize(
    "source, dest, expected",
    [
        (
            Point(0, 0),
            Point(0, 3),
            {Point(0, 0), Point(0, 1), Point(0, 2), Point(0, 3)},
        ),
        (
            Point(0, 0),
            Point(3, 0),
            {Point(0, 0), Point(1, 0), Point(2, 0), Point(3, 0)},
        ),
        (Point(-1, 1), Point(1, 1), {Point(-1, 1), Point(0, 1), Point(1, 1)}),
    ],
)
def test_points_between(source, dest, expected):
    result = source.points_between(dest)
    assert isinstance(result, set)
    assert result == expected


@pytest.mark.parametrize(
    "source, dest, distance",
    [
        (Point(3, 4), None, 7),
        (Point(-3, 4), None, 7),
        (Point(3, 4), Point(-1, -2), 10),
    ],
)
def test_manhattan_distance(source, dest, distance):
    assert source.manhattan(dest) == distance
