# -*- coding: utf-8 -*-
"""--- Day 3: Toboggan Trajectory ---

With the toboggan login problems resolved, you set off toward the airport. 
While travel by toboggan might be easy, it's certainly not safe: 
there's very minimal steering and the area is covered in trees. 
You'll need to see which angles will take you near the fewest trees.

Due to the local geology, trees in this area only grow on exact integer 
coordinates in a grid. You make a map (your puzzle input) 
of the open squares (.) and trees (#) you can see. For example:

..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#

These aren't the only trees, though; due to something you read about once
involving arboreal genetics and biome stability, the same pattern repeats
to the right many times:

..##.........##.........##.........##.........##.........##.......  --->
#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
.#....#..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
.#...##..#..#...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
..#.##.......#.##.......#.##.......#.##.......#.##.......#.##.....  --->
.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
.#........#.#........#.#........#.#........#.#........#.#........#
#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...
#...##....##...##....##...##....##...##....##...##....##...##....#
.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#  --->

You start on the open square (.) in the top-left corner and need to reach the
bottom (below the bottom-most row on your map).

The toboggan can only follow a few specific slopes (you opted for a cheaper
model that prefers rational numbers); start by counting all the trees you
would encounter for the slope right 3, down 1:

From your starting position at the top-left, check the position that is right
3 and down 1. Then, check the position that is right 3 and down 1 from there,
and so on until you go past the bottom of the map.

The locations you'd check in the above example are marked here with O where
there was an open square and X where there was a tree:

..##.........##.........##.........##.........##.........##.......  --->
#..O#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
.#....X..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
..#.#...#O#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
.#...##..#..X...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
..#.##.......#.X#.......#.##.......#.##.......#.##.......#.##.....  --->
.#.#.#....#.#.#.#.O..#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
.#........#.#........X.#........#.#........#.#........#.#........#
#.##...#...#.##...#...#.X#...#...#.##...#...#.##...#...#.##...#...
#...##....##...##....##...#X....##...##....##...##....##...##....#
.#..#...#.#.#..#...#.#.#..#...X.#.#..#...#.#.#..#...#.#.#..#...#.#  --->

In this example, traversing the map using this slope would cause you to
encounter 7 trees.

Starting at the top-left corner of your map and following a slope of
right 3 and down 1, how many trees would you encounter?
"""
from dataclasses import dataclass
from typing import Iterable, Tuple


TOBAGGAN_TRAJECTORY_DEFAULT_INPUT: str = "libs/tobaggan_trajectory/data/input.txt"


class InvalidCoordinateError(Exception):
    pass


@dataclass
class Point:
    x: int
    y: int

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        return Point(x=self.x + other.x, y=self.y + other.y)


def lookup(point: Point, basemap: Tuple[str]) -> bool:
    max_x = len(basemap[0])
    max_y = len(basemap)
    if point.y >= max_y:
        raise InvalidCoordinateError("y coordinate is longer than map")
    if point.x >= max_x:
        point = Point(x=point.x % max_x, y=point.y)

    return basemap[point.y][point.x]


def get_path(
    x: int, y: int, *, starting_point: Point = Point(x=0, y=0)
) -> Iterable[Tuple[int]]:
    point = starting_point
    while True:
        yield point
        point += Point(x, y)


def count_trees_on_path(path: Iterable[Point], basemap: str):
    results = []
    for point in path:
        try:
            results.append(lookup(point, basemap))
        except InvalidCoordinateError:
            return "".join(results).count("#")


def main(x: int, y: int, input_file: str = TOBAGGAN_TRAJECTORY_DEFAULT_INPUT):
    with open(input_file, "r") as ifile:
        basemap = tuple(line.strip() for line in ifile.readlines())
    path = get_path(x, y)
    return count_trees_on_path(path, basemap)
