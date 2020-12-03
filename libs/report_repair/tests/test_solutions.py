# -*- coding: utf-8 -*-
import unittest
from libs.report_repair import REPORT_REPAIR_DEFAULT_INPUT, main


class TestSolution(unittest.TestCase):
    def test_part_1(self):
        expected = 270144
        actual = main(input_file=REPORT_REPAIR_DEFAULT_INPUT)
        assert expected == actual

    def test_part_2(self):
        expected = 261342720
        actual = main(input_file=REPORT_REPAIR_DEFAULT_INPUT, n_addends=3)
        assert expected == actual


if __name__ == "__main__":
    unittest.main()
