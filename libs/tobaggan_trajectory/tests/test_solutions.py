# -*- coding: utf-8 -*-
from functools import reduce
import unittest
from libs.tobaggan_trajectory import TOBAGGAN_TRAJECTORY_DEFAULT_INPUT, main


class TestSolution(unittest.TestCase):
    def test_part_1(self):
        expected = 216
        actual = main(x=3, y=1, input_file=TOBAGGAN_TRAJECTORY_DEFAULT_INPUT)
        assert actual == expected

    def test_part_2(self):
        expected = 6708199680
        results = [
            main(x=1, y=1, input_file=TOBAGGAN_TRAJECTORY_DEFAULT_INPUT),
            main(x=3, y=1, input_file=TOBAGGAN_TRAJECTORY_DEFAULT_INPUT),
            main(x=5, y=1, input_file=TOBAGGAN_TRAJECTORY_DEFAULT_INPUT),
            main(x=7, y=1, input_file=TOBAGGAN_TRAJECTORY_DEFAULT_INPUT),
            main(x=1, y=2, input_file=TOBAGGAN_TRAJECTORY_DEFAULT_INPUT),
        ]
        actual = reduce((lambda x, y: x * y), results)
        assert actual == expected


if __name__ == "__main__":
    unittest.main()
