# -*- coding: utf-8 -*-
import unittest
from libs.password_philosophy import (
    InvalidPasswordError,
    CountCharacterPolicy,
    IndexCharacterPolicy,
    main,
    validate_password,
)


class TestCountCharacterPolicy(unittest.TestCase):
    def test_from_string(self):
        expected = CountCharacterPolicy(char="a", min_=1, max_=3)
        actual = CountCharacterPolicy.from_string("1-3 a")
        assert expected == actual

    def test_validate(self):
        policy = CountCharacterPolicy(char="a", min_=1, max_=3)

        policy.validate("abcde")

        with self.assertRaises(InvalidPasswordError):
            policy.validate("bcde")

        with self.assertRaises(InvalidPasswordError):
            policy.validate("aaaabcde")


class TestIndexCharacterPolicy(unittest.TestCase):
    def test_from_string(self):
        expected = IndexCharacterPolicy(char="a", indices=(0, 2))
        actual = IndexCharacterPolicy.from_string("1-3 a")
        print(expected)
        print(actual)
        assert expected == actual

    def test_validate(self):
        policy = IndexCharacterPolicy(char="a", indices=(0, 2))
        policy.validate("abcde")

        with self.assertRaises(InvalidPasswordError):
            policy = IndexCharacterPolicy(char="b", indices=(0, 2))
            policy.validate("cdefg")

        with self.assertRaises(InvalidPasswordError):
            policy = IndexCharacterPolicy(char="c", indices=(1, 8))
            policy.validate("ccccccccc")


class TestPasswordPhilosophy(unittest.TestCase):
    def test_validate_password__count(self):
        validate_password("1-3 a: abcde", policy_type="count")

        with self.assertRaises(InvalidPasswordError):
            validate_password("1-3 b: cdefg", policy_type="count")

        validate_password("2-9 c: ccccccccc", policy_type="count")

    def test_validate_password__index(self):
        validate_password("1-3 a: abcde", policy_type="index")

        with self.assertRaises(InvalidPasswordError):
            validate_password("1-3 b: cdefg", policy_type="index")

        with self.assertRaises(InvalidPasswordError):
            validate_password("2-9 c: ccccccccc", policy_type="index")


if __name__ == "__main__":
    unittest.main()
