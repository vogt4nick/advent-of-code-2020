# -*- coding: utf-8 -*-
import unittest
from libs.tobaggan_trajectory import TOBAGGAN_TRAJECTORY_DEFAULT_INPUT, main


class TestSolution(unittest.TestCase):
    def test_part_1(self):
        expected = 216
        actual = main(x=3, y=1, input_file=TOBAGGAN_TRAJECTORY_DEFAULT_INPUT)
        assert actual == expected


if __name__ == "__main__":
    unittest.main()
