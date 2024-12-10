from __future__ import annotations
import re
import enum
import unittest
import pytest
import io
import typing
from typing import *
import unittest
from src.main.org.apache.commons.validator.ISBNValidator import *
from src.main.org.apache.commons.validator.routines.ISBNValidator import *


class ISBNValidatorTest(unittest.TestCase):

    __invalidISBN13Format: typing.List[str] = [
        "",  # empty
        "   ",  # empty
        "1",  # too short
        "978123456789",  # too short
        "97812345678901",  # too long
        "978-123456-1234567-123456-1",  # Group too long
        "978-12345-12345678-123456-1",  # Publisher too long
        "978-12345-1234567-1234567-1",  # Title too long
        "978-12345-1234567-123456-12",  # Check Digit too long
        "--978 1 930110 99 1",  # format
        "978 1 930110 99 1--",  # format
        "978 1 930110-99 1-",  # format
        "123-4-567890-12-8",  # format
        "978.1.2.3.4",  # Invalid Separator
        "978=1=2=3=4",  # Invalid Separator
        "978_1_2_3_4",  # Invalid Separator
        "978123456789X",  # invalid character
        "978-0-201-63385-X",  # invalid character
        "dsasdsadsadsa",  # invalid characters
        "I love sparrows",  # invalid characters
        "979-1-234-567-89-6",  # format
    ]
    __validISBN13Format: typing.List[str] = [
        "9781234567890",
        "9791234567890",
        "978-12345-1234567-123456-1",
        "979-12345-1234567-123456-1",
        "978 12345 1234567 123456 1",
        "979 12345 1234567 123456 1",
        "978-1-2-3-4",
        "979-1-2-3-4",
        "978 1 2 3 4",
        "979 1 2 3 4",
    ]
    __invalidISBN10Format: typing.List[str] = [
        "",  # empty
        "   ",  # empty
        "1",  # too short
        "123456789",  # too short
        "12345678901",  # too long
        "12345678X0",  # X not at end
        "123456-1234567-123456-X",  # Group too long
        "12345-12345678-123456-X",  # Publisher too long
        "12345-1234567-1234567-X",  # Title too long
        "12345-1234567-123456-X2",  # Check Digit too long
        "--1 930110 99 5",  # format
        "1 930110 99 5--",  # format
        "1 930110-99 5-",  # format
        "1.2.3.4",  # Invalid Separator
        "1=2=3=4",  # Invalid Separator
        "1_2_3_4",  # Invalid Separator
        "123456789Y",  # Other character at the end
        "dsasdsadsa",  # invalid characters
        "I love sparrows!",  # invalid characters
        "068-556-98-45"  # format
    ]
    __validISBN10Format: List[str] = [
        "1234567890",
        "123456789X",
        "12345-1234567-123456-X",
        "12345 1234567 123456 X",
        "1-2-3-4",
        "1 2 3 4",
    ]

    def testConversionErrors(self) -> None:

        validator = ISBNValidator.getInstance0()
        input = None
        try:
            input = "123456789 "
            validator.convertToISBN13(input)
            pytest.fail("Expected ValueError for '" + input + "'")
        except ValueError:
            pass
        try:
            input = "12345678901"
            validator.convertToISBN13(input)
            pytest.fail("Expected ValueError for '" + input + "'")
        except ValueError:
            pass
        try:
            input = ""
            validator.convertToISBN13(input)
            pytest.fail("Expected ValueError for '" + input + "'")
        except ValueError:
            pass
        try:
            input = "X234567890"
            validator.convertToISBN13(input)
            pytest.fail("Expected ValueError for '" + input + "'")
        except ValueError:
            pass

    def testInvalid(self) -> None:

        validator = ISBNValidator.getInstance0()
        baseCode = "193011099"
        self.assertFalse(validator.isValid(baseCode + "0"), "ISBN10-0", )
        self.assertFalse(validator.isValid(baseCode + "1"), "ISBN10-1")
        self.assertFalse(validator.isValid(baseCode + "2"), "ISBN10-2")
        self.assertFalse(validator.isValid(baseCode + "3"), "ISBN10-3")
        self.assertFalse(validator.isValid(baseCode + "4"), "ISBN10-4")
        self.assertTrue(
            validator.isValid(baseCode + "5"), "ISBN10-5"
        )  # valid check digit
        self.assertFalse(validator.isValid(baseCode + "6"), "ISBN10-6")
        self.assertFalse(validator.isValid(baseCode + "7"), "ISBN10-7")
        self.assertFalse(validator.isValid(baseCode + "8"), "ISBN10-8")
        self.assertFalse(validator.isValid(baseCode + "9"), "ISBN10-9")
        self.assertFalse(validator.isValid(baseCode + "X"), "ISBN10-X")

        baseCode = "978193011099"
        self.assertFalse(validator.isValid(baseCode + "0"), "ISBN13-0")
        self.assertTrue(
            validator.isValid(baseCode + "1"), "ISBN13-1"
        )  # valid check digit
        self.assertFalse(validator.isValid(baseCode + "2"), "ISBN13-2")
        self.assertFalse(validator.isValid(baseCode + "3"), "ISBN13-3")
        self.assertFalse(validator.isValid(baseCode + "4"), "ISBN13-4")
        self.assertFalse(validator.isValid(baseCode + "5"), "ISBN13-5")
        self.assertFalse(validator.isValid(baseCode + "6"), "ISBN13-6")
        self.assertFalse(validator.isValid(baseCode + "7"), "ISBN13-7")
        self.assertFalse(validator.isValid(baseCode + "8"), "ISBN13-8")
        self.assertFalse(validator.isValid(baseCode + "9"), "ISBN13-9")

    def testNull(self) -> None:

        validator = ISBNValidator.getInstance0()
        self.assertFalse(validator.isValid(None))
        self.assertFalse(validator.isValidISBN10(None))
        self.assertFalse(validator.isValidISBN13(None))
        self.assertIsNone(validator.validate(None))
        self.assertIsNone(validator.validateISBN10(None))
        self.assertIsNone(validator.validateISBN13(None))
        self.assertIsNone(validator.convertToISBN13(None))

    def testValidateISBN13(self) -> None:

        validator = ISBNValidator.getInstance0()

        self.assertEqual("9781930110991", validator.validateISBN13("9781930110991"))
        self.assertEqual("9781930110991", validator.validateISBN13("978-1-930110-99-1"))
        self.assertEqual("9781930110991", validator.validateISBN13("978 1 930110 99 1"))
        self.assertEqual("9780201633856", validator.validateISBN13("9780201633856"))
        self.assertEqual("9780201633856", validator.validateISBN13("978-0-201-63385-6"))
        self.assertEqual("9780201633856", validator.validateISBN13("978 0 201 63385 6"))

        self.assertEqual("9781930110991", validator.validate("9781930110991"))
        self.assertEqual("9781930110991", validator.validate("978-1-930110-99-1"))
        self.assertEqual("9781930110991", validator.validate("978 1 930110 99 1"))
        self.assertEqual("9780201633856", validator.validate("9780201633856"))
        self.assertEqual("9780201633856", validator.validate("978-0-201-63385-6"))
        self.assertEqual("9780201633856", validator.validate("978 0 201 63385 6"))

    def testValidateISBN10Convert(self) -> None:

        validator = ISBNValidator.getInstance0()

        self.assertEqual("9781930110991", validator.validate("1930110995"))
        self.assertEqual("9781930110991", validator.validate("1-930110-99-5"))
        self.assertEqual("9781930110991", validator.validate("1 930110 99 5"))
        self.assertEqual("9780201633856", validator.validate("020163385X"))
        self.assertEqual("9780201633856", validator.validate("0-201-63385-X"))
        self.assertEqual("9780201633856", validator.validate("0 201 63385 X"))

    def testValidateISBN10(self) -> None:

        validator = ISBNValidator.getInstance1(False)
        self.assertEqual("1930110995", validator.validateISBN10("1930110995"))
        self.assertEqual("1930110995", validator.validateISBN10("1-930110-99-5"))
        self.assertEqual("1930110995", validator.validateISBN10("1 930110 99 5"))
        self.assertEqual("020163385X", validator.validateISBN10("020163385X"))
        self.assertEqual("020163385X", validator.validateISBN10("0-201-63385-X"))
        self.assertEqual("020163385X", validator.validateISBN10("0 201 63385 X"))

        self.assertEqual("1930110995", validator.validate("1930110995"))
        self.assertEqual("1930110995", validator.validate("1-930110-99-5"))
        self.assertEqual("1930110995", validator.validate("1 930110 99 5"))
        self.assertEqual("020163385X", validator.validate("020163385X"))
        self.assertEqual("020163385X", validator.validate("0-201-63385-X"))
        self.assertEqual("020163385X", validator.validate("0 201 63385 X"))

    def testIsValidISBN13(self) -> None:

        validator = ISBNValidator.getInstance0()

        self.assertTrue(validator.isValidISBN13("9781930110991"))
        self.assertTrue(validator.isValidISBN13("978-1-930110-99-1"))
        self.assertTrue(validator.isValidISBN13("978 1 930110 99 1"))
        self.assertTrue(validator.isValidISBN13("9780201633856"))
        self.assertTrue(validator.isValidISBN13("978-0-201-63385-6"))
        self.assertTrue(validator.isValidISBN13("978 0 201 63385 6"))

        self.assertTrue(validator.isValid("9781930110991"))
        self.assertTrue(validator.isValid("978-1-930110-99-1"))
        self.assertTrue(validator.isValid("978 1 930110 99 1"))
        self.assertTrue(validator.isValid("9780201633856"))
        self.assertTrue(validator.isValid("978-0-201-63385-6"))
        self.assertTrue(validator.isValid("978 0 201 63385 6"))

    def testIsValidISBN10(self) -> None:

        validator = ISBNValidator.getInstance0()

        self.assertTrue(validator.isValidISBN10("1930110995"))
        self.assertTrue(validator.isValidISBN10("1-930110-99-5"))
        self.assertTrue(validator.isValidISBN10("1 930110 99 5"))
        self.assertTrue(validator.isValidISBN10("020163385X"))
        self.assertTrue(validator.isValidISBN10("0-201-63385-X"))
        self.assertTrue(validator.isValidISBN10("0 201 63385 X"))

        self.assertTrue(validator.isValid("1930110995"))
        self.assertTrue(validator.isValid("1-930110-99-5"))
        self.assertTrue(validator.isValid("1 930110 99 5"))
        self.assertTrue(validator.isValid("020163385X"))
        self.assertTrue(validator.isValid("0-201-63385-X"))
        self.assertTrue(validator.isValid("0 201 63385 X"))

    def testInvalidISBN13Format(self) -> None:

        pattern = re.compile(ISBNValidator.ISBN13_REGEX)
        validator = ISBNValidator.getInstance0()

        for i, code in enumerate(self.__invalidISBN13Format):
            self.assertFalse(pattern.match(code) is not None, f"Pattern[{i}]={code}", )
            self.assertFalse(
                validator.isValidISBN13(code), f"isValidISBN13[{i}]={code}"
            )
            self.assertIsNone(
                validator.validateISBN13(code), f"validateISBN13[{i}]={code}"
            )

    def testValidISBN13Format(self) -> None:

        pattern = re.compile(ISBNValidator.ISBN13_REGEX)
        for i in range(len(self.__validISBN13Format)):
            self.assertTrue(
                "Pattern[" + str(i) + "]=" + self.__validISBN13Format[i],
                pattern.match(self.__validISBN13Format[i]) is not None,
            )

    def testInvalidISBN10Format(self) -> None:

        validator = ISBNValidator.getInstance0()
        pattern = re.compile(ISBNValidator.ISBN10_REGEX)

        for i, code in enumerate(self.__invalidISBN10Format):
            self.assertFalse(pattern.match(code), f"Pattern[{i}]={code}")
            self.assertFalse(
                validator.isValidISBN10(code), f"isValidISBN10[{i}]={code}"
            )
            self.assertIsNone(
                validator.validateISBN10(code), f"validateISBN10[{i}]={code}"
            )

    def testValidISBN10Format(self) -> None:

        pattern = re.compile(ISBNValidator.ISBN10_REGEX)
        for i in range(len(self.__validISBN10Format)):
            self.assertTrue(
                pattern.match(self.__validISBN10Format[i]) is not None,
                "Pattern[" + str(i) + "]=" + self.__validISBN10Format[i]
            )

    def __init__(self, name: str) -> None:
        super().__init__(name)
