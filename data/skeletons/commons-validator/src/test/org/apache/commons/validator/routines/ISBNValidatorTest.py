from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.validator.routines.ISBNValidator import *
from src.main.org.apache.commons.validator.ISBNValidator import *
import unittest
import typing
from typing import *
import io

# Imports End


class ISBNValidatorTest(unittest.TestCase):

    # Class Fields Begin
    __validISBN10Format: typing.List[typing.List[str]] = None
    __invalidISBN10Format: typing.List[typing.List[str]] = None
    __validISBN13Format: typing.List[typing.List[str]] = None
    __invalidISBN13Format: typing.List[typing.List[str]] = None
    # Class Fields End

    # Class Methods Begin
    def testConversionErrors(self) -> None:
        pass

    def testInvalid(self) -> None:
        pass

    def testNull(self) -> None:
        pass

    def testValidateISBN13(self) -> None:
        pass

    def testValidateISBN10Convert(self) -> None:
        pass

    def testValidateISBN10(self) -> None:
        pass

    def testIsValidISBN13(self) -> None:
        pass

    def testIsValidISBN10(self) -> None:
        pass

    def testInvalidISBN13Format(self) -> None:
        pass

    def testValidISBN13Format(self) -> None:
        pass

    def testInvalidISBN10Format(self) -> None:
        pass

    def testValidISBN10Format(self) -> None:
        pass

    def __init__(self, name: str) -> None:
        pass

    # Class Methods End
