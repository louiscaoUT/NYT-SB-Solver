from NYT_Spelling_Bee_Solver import *
import unittest
from unittest.mock import patch


class Test_NYT(unittest.TestCase):
    def test_validate_letters(self):
        # less than 7 letters
        with self.assertRaises(Exception):
            validate_letters("a")

        # greater than 7 letters
        with self.assertRaises(Exception):
            validate_letters("aaaaaaa")

        # contains number
        with self.assertRaises(Exception):
            validate_letters("aaaa7")

        # correct input
        self.assertEqual(validate_letters("inkblot"), "inkblot")

    def test_validate_required_letter(self):
        # not a letter
        with self.assertRaises(Exception):
            validate_required_letter(letter="10", letters="i n k b l o t".split())

        # not in letters
        with self.assertRaises(Exception):
            validate_required_letter(letter="a", letters="i n k b l o t".split())

        # not in letters
        with self.assertRaises(Exception):
            validate_required_letter(letter="a", letters="i n k b l o t".split())

        # correct input
        self.assertEqual(
            validate_required_letter(letter="i", letters="i n k b l o t".split()), "i"
        )

    def test_validate_length(self):
        # length is less than 4
        with self.assertRaises(Exception):
            validate_length(3)

        # length is greater than 7
        with self.assertRaises(Exception):
            validate_length(8)

        # length is not a length and not "all"
        with self.assertRaises(Exception):
            validate_length("everything")

        # length is the exit command
        self.assertEqual(validate_length(length=""), "")

        # length is a correct input
        self.assertEqual(validate_length(length="7"), "7")


if __name__ == "__main__":
    unittest.main()
