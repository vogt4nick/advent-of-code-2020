# -*- coding: utf-8 -*-
import unittest
from libs.report_repair import calc_repair_cost, main


REPORT_REPAIR_DEFAULT_INPUT: str = "libs/report_repair/data/input.txt"


class TestReportRepair(unittest.TestCase):

    def test_calc_repair_cost(self):
        L = sorted((2020, 0, 1, 2))
        expected = 0
        assert calc_repair_cost(L) == expected

    def test_main(self):
        result = main(input_file=REPORT_REPAIR_DEFAULT_INPUT)
        assert result == 144 * 1876


if __name__ == "__main__":
    unittest.main()
