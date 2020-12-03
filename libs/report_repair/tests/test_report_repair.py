# -*- coding: utf-8 -*-
import unittest
from libs.report_repair import _load_input, calc_repair_cost, main


class TestReportRepair(unittest.TestCase):
    def setUp(self):
        self.input = sorted([1721, 979, 366, 299, 675, 1456])

    def test_calc_repair_cost__2_addends(self):
        expected = 1721 * 299
        actual = calc_repair_cost(self.input, n_addends=2, sum_=2020)
        assert actual == expected

    def test_calc_repair_cost__3_addends(self):
        expected = 979 * 366 * 675
        actual = calc_repair_cost(self.input, n_addends=3, sum_=2020)
        assert actual == expected


if __name__ == "__main__":
    unittest.main()
