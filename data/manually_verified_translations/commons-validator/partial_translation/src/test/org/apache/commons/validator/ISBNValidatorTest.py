from __future__ import annotations
import re
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.validator.ISBNValidator import *
from src.main.org.apache.commons.validator.routines.ISBNValidator import *


class ISBNValidatorTest(unittest.TestCase):

    __INVALID_ISBN: str = "068-556-98-45"
    __VALID_ISBN_X: str = "0-201-63385-X"
    __VALID_ISBN_SPACES: str = "1 930110 99 5"
    __VALID_ISBN_DASHES: str = "1-930110-99-5"
    __VALID_ISBN_RAW: str = "1930110995"

    def testIsValid(self) -> None:

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

        self.assertTrue(validator.isValid(self.__VALID_ISBN_RAW))
        self.assertTrue(validator.isValid(self.__VALID_ISBN_DASHES))
        self.assertTrue(validator.isValid(self.__VALID_ISBN_SPACES))
        self.assertTrue(validator.isValid(self.__VALID_ISBN_X))
        self.assertFalse(validator.isValid(self.__INVALID_ISBN))

    def __init__(self, name: str) -> None:
        super().__init__(name)
