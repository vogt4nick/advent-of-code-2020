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

--- Part Two ---

The Elves in accounting are thankful for your help; one of them even offers
you a starfish coin they had left over from a past vacation. They offer you a
second one if you can find three numbers in your expense report that meet the
same criteria.

Using the above example again, the three entries that sum to 2020 are 979,
366, and 675. Multiplying them together produces the answer, 241861950.

In your expense report, what is the product of the three entries that sum to
2020?
"""
from functools import reduce
from typing import List, Tuple


REPORT_REPAIR_DEFAULT_INPUT: str = "libs/report_repair/data/input.txt"


class NoValidSumError(Exception):
    """Raise when no valid sums are found."""


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


def _get_addends(L: List[int], n: int = 2, sum_: int = 2020) -> Tuple[int]:
    """Lookup `n` addends that sum to `sum_`.

    Args:
        L (List): A list of integers.
        n (int): The number of addends to calculate sum.
        sum_ (int): The desired sum of addends.

    Returns:
        Tuple[int]: A tuple of `n` addends that sum to `sum_`.
    """
    L = sorted(L)
    for xi, x in enumerate(L):
        addends = [x]
        subset = L[xi + 1 :]
        if n == 2:
            try:
                yi = subset.index(sum_ - x)
            except ValueError:
                raise NoValidSumError
            else:
                y = subset[yi]
                addends.append(y)
                return addends
        else:
            try:
                new_n, new_sum = n - 1, sum_ - x
                addends += _get_addends(subset, n=new_n, sum_=new_sum)
            except NoValidSumError:
                continue
            else:
                return addends


def calc_repair_cost(L: Tuple[int], *, n_addends: int = 2, sum_: int = 2020) -> int:
    """Search tuple for two numbers that sum to 2020 and return the
    product of the resulting two numbers.

    Args:
        L (Tuple[int]): A file of newline separated numbers.

    Returns:
        int: The product of two numbers summing to 2020.
    """
    addends = _get_addends(L, n=n_addends, sum_=sum_)
    return reduce((lambda x, y: x * y), addends)


def main(*, input_file, n_addends: int = 2, sum_: int = 2020) -> int:
    """Search the input file for two numbers that sum to 2020 and return the
    product of the resulting two numbers.

    Args:
        input_file (str): A file of newline separated numbers.
        n_addends (int):
    """
    L = _load_input(input_file)
    addends = _get_addends(L, n=n_addends, sum_=sum_)
    repair_cost = calc_repair_cost(L, n_addends=n_addends, sum_=sum_)

    print(f"{addends} multiply to {repair_cost} and sum to {sum_}")

    return repair_cost
