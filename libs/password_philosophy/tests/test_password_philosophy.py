# -*- coding: utf-8 -*-
import unittest
from libs.password_philosophy import (
    InvalidPasswordError,
    PasswordPolicy,
    main,
    validate_password,
)


class TestPasswordPolicy(unittest.TestCase):
    def test_from_string(self):
        expected = PasswordPolicy(char="a", min_=1, max_=3)
        actual = PasswordPolicy.from_string("1-3 a")
        assert expected == actual

    def test_validate(self):
        policy = PasswordPolicy(char="a", min_=1, max_=3)

        policy.validate("abcde")

        with self.assertRaises(InvalidPasswordError):
            policy.validate("bcde")

        with self.assertRaises(InvalidPasswordError):
            policy.validate("aaaabcde")


class TestPasswordPhilosophy(unittest.TestCase):
    def test_validate_password(self):
        validate_password("1-3 a: abcde")

        with self.assertRaises(InvalidPasswordError):
            validate_password("1-3 b: cdefg")

        validate_password("2-9 c: ccccccccc")


if __name__ == "__main__":
    unittest.main()
