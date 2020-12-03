# -*- coding: utf-8 -*-
"""--- Day 1: Report Repair ---

After saving Christmas five years in a row, you've decided to take a vacation
at a nice resort on a tropical island. Surely, Christmas will go on without
you.

The tropical island has its own currency and is entirely cash-only. The gold
coins used there have a little picture of a starfish; the locals just call
them stars. None of the currency exchanges seem to have heard of them, but
somehow, you'll need to find fifty of these coins by the time you arrive so
you can pay the deposit on your room.

To save your vacation, you need to get all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each
day in the Advent calendar; the second puzzle is unlocked when you complete
the first. Each puzzle grants one star. Good luck!

Before you leave, the Elves in accounting just need you to fix your expense
report (your puzzle input); apparently, something isn't quite adding up.

Specifically, they need you to find the two entries that sum to 2020 and then
multiply those two numbers together.

For example, suppose your expense report contained the following:

1721
979
366
299
675
1456

In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying
them together produces 1721 * 299 = 514579, so the correct answer is 514579.

Of course, your expense report is much larger. Find the two entries that sum
to 2020; what do you get if you multiply them together?
"""
from typing import List, Tuple


def _load_input(p: str) -> Tuple:
    """Load list of integers from a newline file of integers.

    Args:
        p (str): A file containing newline delimited integers.

    Returns:
        Tuple: A sorted tuple of integers found in the given file.
    """
    with open(p, "r") as ifile:
        numbers = sorted(int(line) for line in ifile.readlines())

    return tuple(numbers)

def _get_addends(L: List) -> Tuple[int]:
    """Lookup two addends that sum to 2020.

    Args:
        L (List): A list of integers.

    Returns:
        Tuple[int]: A tuple of two addends that sum to 2020.
    """
    for i in L:
        for j in L[i+1:]:
            if i + j == 2020:
                return i, j

def calc_repair_cost(L: Tuple[int]) -> int:
    """Search tuple for two numbers that sum to 2020 and return the 
    product of the resulting two numbers.

    Args:
        L (Tuple[int]): A file of newline separated numbers.

    Returns:
        int: The product of two numbers summing to 2020.
    """
    x, y = _get_addends(L)

    return x * y

def main(*, input_file: str) -> None:
    """Search the input file for two numbers that sum to 2020 and return the 
    product of the resulting two numbers.

    Args:
        input_file (str): A file of newline separated numbers.
    """
    L = _load_input(input_file)
    repair_cost = calc_repair_cost(L)

    print(repair_cost)

    return repair_cost
