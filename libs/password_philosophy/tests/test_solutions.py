# -*- coding: utf-8 -*-
import unittest
from libs.password_philosophy import PASSWORD_PHILOSOPHY_DEFAULT_INPUT, main


class TestSolution(unittest.TestCase):
    def test_part_1(self):
        expected = 418
        actual = main(input_file=PASSWORD_PHILOSOPHY_DEFAULT_INPUT, policy_type="count")
        assert expected == actual

    def test_part_2(self):
        expected = 616
        actual = main(input_file=PASSWORD_PHILOSOPHY_DEFAULT_INPUT, policy_type="index")
        assert expected == actual


if __name__ == "__main__":
    unittest.main()
