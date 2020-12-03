# -*- coding: utf-8 -*-
from typing import Tuple
import unittest
from libs.tobaggan_trajectory import (
    TOBAGGAN_TRAJECTORY_DEFAULT_INPUT,
    InvalidCoordinateError,
    Point,
    count_trees_on_path,
    get_path,
    lookup,
)


TOBAGGAN_TRAJECTORY_DEFAULT_INPUT: str = "libs/report_repair/data/input.txt"

BASEMAP: Tuple[str] = (
    "..##.......",
    "#...#...#..",
    ".#....#..#.",
    "..#.#...#.#",
    ".#...##..#.",
    "..#.##.....",
    ".#.#.#....#",
    ".#........#",
    "#.##...#...",
    "#...##....#",
    ".#..#...#.#",
)


class TestTobagganTrajectory(unittest.TestCase):
    def test_lookup(self):
        assert lookup(Point(x=0, y=1), basemap=BASEMAP) == "#"
        assert lookup(Point(x=11, y=1), basemap=BASEMAP) == "#"

        assert lookup(Point(x=0, y=10), basemap=BASEMAP) == "."
        assert lookup(Point(x=11, y=10), basemap=BASEMAP) == "."

        with self.assertRaises(InvalidCoordinateError):
            lookup(Point(x=0, y=100), basemap=BASEMAP)

    def test_get_path(self):
        generator = get_path(x=1, y=3)
        # print(next(generator))
        assert next(generator) == Point(0, 0)
        assert next(generator) == Point(1, 3)
        assert next(generator) == Point(2, 6)

    def test_count_trees_on_path(self):
        path = get_path(x=3, y=1)
        assert count_trees_on_path(path, BASEMAP) == 7


if __name__ == "__main__":
    unittest.main()
