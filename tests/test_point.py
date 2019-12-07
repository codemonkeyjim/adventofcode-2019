import pytest

from point import Point


def test_point_equivalence():
    assert Point(0, 0) == Point(0, 0)
    assert Point(1, 2) == Point(1, 2)
    assert Point(1, 2) != Point(2, 1)


@pytest.mark.parametrize(
    "source, vector, expected",
    [
        (Point(0, 0), Point(2, 3), Point(2, 3)),
        (Point(-1, -2), Point(2, 3), Point(1, 1)),
    ],
)
def test_point_point_addition(source, vector, expected):
    assert source + vector == expected


@pytest.mark.parametrize(
    "source, step, expected",
    [
        (Point(0, 0), "U10", Point(0, 10)),
        (Point(2, 3), "D5", Point(2, -2)),
        (Point(-2, 3), "L3", Point(-5, 3)),
        (Point(-2, 3), "R5", Point(3, 3)),
    ],
)
def test_point_string_addition(source, step, expected):
    assert source + step == expected


@pytest.mark.parametrize(
    "source, dest, expected",
    [
        (Point(0, 0), Point(0, 3), [Point(0, 1), Point(0, 2), Point(0, 3)],),
        (Point(0, 0), Point(3, 0), [Point(1, 0), Point(2, 0), Point(3, 0)],),
        (
            Point(2, 3),
            Point(2, -1),
            [Point(2, 2), Point(2, 1), Point(2, 0), Point(2, -1)],
        ),
        (Point(-1, 1), Point(1, 1), [Point(0, 1), Point(1, 1)]),
    ],
)
def test_points_between(source, dest, expected):
    result = source.points_between(dest)
    assert isinstance(result, list)
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
