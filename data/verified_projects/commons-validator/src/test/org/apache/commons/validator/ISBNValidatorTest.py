import pytest

import unittest
from src.main.org.apache.commons.validator.ISBNValidator import *

class ISBNValidatorTest(unittest.TestCase):

    __VALID_ISBN_RAW = "1930110995"
    __VALID_ISBN_DASHES = "1-930110-99-5"
    __VALID_ISBN_SPACES = "1 930110 99 5"
    __VALID_ISBN_X = "0-201-63385-X"
    __INVALID_ISBN = "068-556-98-45"
    

    @pytest.mark.test
    def testIsValid(self) -> None:
        try:
            validator = ISBNValidator()
            self.assertFalse(validator.isValid(None))
            self.assertFalse(validator.isValid(""))
            self.assertFalse(validator.isValid("1"))
            self.assertFalse(validator.isValid("12345678901234"))
            self.assertFalse(validator.isValid("dsasdsadsads"))
            self.assertFalse(validator.isValid("535365"))
            self.assertFalse(validator.isValid("I love sparrows!"))
            self.assertFalse(validator.isValid("--1 930110 99 5"))
            self.assertFalse(validator.isValid("1 930110 99 5--"))
            self.assertFalse(validator.isValid("1 930110-99 5-"))

            self.assertTrue(validator.isValid(ISBNValidatorTest.__VALID_ISBN_RAW))
            self.assertTrue(validator.isValid(ISBNValidatorTest.__VALID_ISBN_DASHES))
            self.assertTrue(validator.isValid(ISBNValidatorTest.__VALID_ISBN_SPACES))
            self.assertTrue(validator.isValid(ISBNValidatorTest.__VALID_ISBN_X))
            self.assertFalse(validator.isValid(ISBNValidatorTest.__INVALID_ISBN))
        except Exception as e:
            self.fail(f"An exception occurred: {e}")
