from __future__ import annotations
import re
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
        "",
        "   ",
        "1",
        "978123456789",
        "97812345678901",
        "978-123456-1234567-123456-1",
        "978-12345-12345678-123456-1",
        "978-12345-1234567-1234567-1",
        "978-12345-1234567-123456-12",
        "--978 1 930110 99 1",
        "978 1 930110 99 1--",
        "978 1 930110-99 1-",
        "123-4-567890-12-8",
        "978.1.2.3.4",
        "978=1=2=3=4",
        "978_1_2_3_4",
        "978123456789X",
        "978-0-201-63385-X",
        "dsasdsadsadsa",
        "I love sparrows!",
        "979-1-234-567-89-6",
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
    __invalidISBN10Format: typing.List[str] = []
    __validISBN10Format: typing.List[str] = [
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
            self.fail("Expected ValueError for '" + input + "'")
        except ValueError as e:
            pass
        try:
            input = "12345678901"
            validator.convertToISBN13(input)
            self.fail("Expected ValueError for '" + input + "'")
        except ValueError as e:
            pass
        try:
            input = ""
            validator.convertToISBN13(input)
            self.fail("Expected ValueError for '" + input + "'")
        except ValueError as e:
            pass
        try:
            input = "X234567890"
            validator.convertToISBN13(input)
            self.fail("Expected ValueError for '" + input + "'")
        except ValueError as e:
            pass

    def testInvalid(self) -> None:
        validator: ISBNValidator = ISBNValidator.getInstance0()
        baseCode: str = "193011099"
        self.assertFalse("ISBN10-0", validator.isValid(baseCode + "0"))
        self.assertFalse("ISBN10-1", validator.isValid(baseCode + "1"))
        self.assertFalse("ISBN10-2", validator.isValid(baseCode + "2"))
        self.assertFalse("ISBN10-3", validator.isValid(baseCode + "3"))
        self.assertFalse("ISBN10-4", validator.isValid(baseCode + "4"))
        self.assertTrue(
            "ISBN10-5", validator.isValid(baseCode + "5")
        )  # valid check digit
        self.assertFalse("ISBN10-6", validator.isValid(baseCode + "6"))
        self.assertFalse("ISBN10-7", validator.isValid(baseCode + "7"))
        self.assertFalse("ISBN10-8", validator.isValid(baseCode + "8"))
        self.assertFalse("ISBN10-9", validator.isValid(baseCode + "9"))
        self.assertFalse("ISBN10-X", validator.isValid(baseCode + "X"))

        baseCode = "978193011099"
        self.assertFalse("ISBN13-0", validator.isValid(baseCode + "0"))
        self.assertTrue(
            "ISBN13-1", validator.isValid(baseCode + "1")
        )  # valid check digit
        self.assertFalse("ISBN13-2", validator.isValid(baseCode + "2"))
        self.assertFalse("ISBN13-3", validator.isValid(baseCode + "3"))
        self.assertFalse("ISBN13-4", validator.isValid(baseCode + "4"))
        self.assertFalse("ISBN13-5", validator.isValid(baseCode + "5"))
        self.assertFalse("ISBN13-6", validator.isValid(baseCode + "6"))
        self.assertFalse("ISBN13-7", validator.isValid(baseCode + "7"))
        self.assertFalse("ISBN13-8", validator.isValid(baseCode + "8"))
        self.assertFalse("ISBN13-9", validator.isValid(baseCode + "9"))

    def testNull(self) -> None:
        validator = ISBNValidator.getInstance0()
        self.assertFalse("isValid", validator.isValid(None))
        self.assertFalse("isValidISBN10", validator.isValidISBN10(None))
        self.assertFalse("isValidISBN13", validator.isValidISBN13(None))
        self.assertIsNone("validate", validator.validate(None))
        self.assertIsNone("validateISBN10", validator.validateISBN10(None))
        self.assertIsNone("validateISBN13", validator.validateISBN13(None))
        self.assertIsNone("convertToISBN13", validator.convertToISBN13(None))

    def testValidateISBN13(self) -> None:
        validator = ISBNValidator.getInstance0()
        self.assertEqual(
            "validateISBN13-1",
            "9781930110991",
            validator.validateISBN13("9781930110991"),
        )
        self.assertEqual(
            "validateISBN13-2",
            "9781930110991",
            validator.validateISBN13("978-1-930110-99-1"),
        )
        self.assertEqual(
            "validateISBN13-3",
            "9781930110991",
            validator.validateISBN13("978 1 930110 99 1"),
        )
        self.assertEqual(
            "validateISBN13-4",
            "9780201633856",
            validator.validateISBN13("9780201633856"),
        )
        self.assertEqual(
            "validateISBN13-5",
            "9780201633856",
            validator.validateISBN13("978-0-201-63385-6"),
        )
        self.assertEqual(
            "validateISBN13-6",
            "9780201633856",
            validator.validateISBN13("978 0 201 63385 6"),
        )

        self.assertEqual(
            "validate-1", "9781930110991", validator.validate("9781930110991")
        )
        self.assertEqual(
            "validate-2", "9781930110991", validator.validate("978-1-930110-99-1")
        )
        self.assertEqual(
            "validate-3", "9781930110991", validator.validate("978 1 930110 99 1")
        )
        self.assertEqual(
            "validate-4", "9780201633856", validator.validate("9780201633856")
        )
        self.assertEqual(
            "validate-5", "9780201633856", validator.validate("978-0-201-63385-6")
        )
        self.assertEqual(
            "validate-6", "9780201633856", validator.validate("978 0 201 63385 6")
        )

    def testValidateISBN10Convert(self) -> None:
        validator = ISBNValidator.getInstance0()
        self.assertEqual(
            "validate-1", "9781930110991", validator.validate("1930110995")
        )
        self.assertEqual(
            "validate-2", "9781930110991", validator.validate("1-930110-99-5")
        )
        self.assertEqual(
            "validate-3", "9781930110991", validator.validate("1 930110 99 5")
        )
        self.assertEqual(
            "validate-4", "9780201633856", validator.validate("020163385X")
        )
        self.assertEqual(
            "validate-5", "9780201633856", validator.validate("0-201-63385-X")
        )
        self.assertEqual(
            "validate-6", "9780201633856", validator.validate("0 201 63385 X")
        )

    def testValidateISBN10(self) -> None:
        validator = ISBNValidator.getInstance1(False)
        self.assertEqual(
            "validateISBN10-1", "1930110995", validator.validateISBN10("1930110995")
        )
        self.assertEqual(
            "validateISBN10-2", "1930110995", validator.validateISBN10("1-930110-99-5")
        )
        self.assertEqual(
            "validateISBN10-3", "1930110995", validator.validateISBN10("1 930110 99 5")
        )
        self.assertEqual(
            "validateISBN10-4", "020163385X", validator.validateISBN10("020163385X")
        )
        self.assertEqual(
            "validateISBN10-5", "020163385X", validator.validateISBN10("0-201-63385-X")
        )
        self.assertEqual(
            "validateISBN10-6", "020163385X", validator.validateISBN10("0 201 63385 X")
        )

        self.assertEqual("validate-1", "1930110995", validator.validate("1930110995"))
        self.assertEqual(
            "validate-2", "1930110995", validator.validate("1-930110-99-5")
        )
        self.assertEqual(
            "validate-3", "1930110995", validator.validate("1 930110 99 5")
        )
        self.assertEqual("validate-4", "020163385X", validator.validate("020163385X"))
        self.assertEqual(
            "validate-5", "020163385X", validator.validate("0-201-63385-X")
        )
        self.assertEqual(
            "validate-6", "020163385X", validator.validate("0 201 63385 X")
        )

    def testIsValidISBN13(self) -> None:
        validator: ISBNValidator = ISBNValidator.getInstance0()
        self.assertTrue("isValidISBN13-1", validator.isValidISBN13("9781930110991"))
        self.assertTrue("isValidISBN13-2", validator.isValidISBN13("978-1-930110-99-1"))
        self.assertTrue("isValidISBN13-3", validator.isValidISBN13("978 1 930110 99 1"))
        self.assertTrue("isValidISBN13-4", validator.isValidISBN13("9780201633856"))
        self.assertTrue("isValidISBN13-5", validator.isValidISBN13("978-0-201-63385-6"))
        self.assertTrue("isValidISBN13-6", validator.isValidISBN13("978 0 201 63385 6"))

        self.assertTrue("isValid-1", validator.isValid("9781930110991"))
        self.assertTrue("isValid-2", validator.isValid("978-1-930110-99-1"))
        self.assertTrue("isValid-3", validator.isValid("978 1 930110 99 1"))
        self.assertTrue("isValid-4", validator.isValid("9780201633856"))
        self.assertTrue("isValid-5", validator.isValid("978-0-201-63385-6"))
        self.assertTrue("isValid-6", validator.isValid("978 0 201 63385 6"))

    def testIsValidISBN10(self) -> None:
        validator: ISBNValidator = ISBNValidator.getInstance0()
        self.assertTrue("isValidISBN10-1", validator.isValidISBN10("1930110995"))
        self.assertTrue("isValidISBN10-2", validator.isValidISBN10("1-930110-99-5"))
        self.assertTrue("isValidISBN10-3", validator.isValidISBN10("1 930110 99 5"))
        self.assertTrue("isValidISBN10-4", validator.isValidISBN10("020163385X"))
        self.assertTrue("isValidISBN10-5", validator.isValidISBN10("0-201-63385-X"))
        self.assertTrue("isValidISBN10-6", validator.isValidISBN10("0 201 63385 X"))

        self.assertTrue("isValid-1", validator.isValid("1930110995"))
        self.assertTrue("isValid-2", validator.isValid("1-930110-99-5"))
        self.assertTrue("isValid-3", validator.isValid("1 930110 99 5"))
        self.assertTrue("isValid-4", validator.isValid("020163385X"))
        self.assertTrue("isValid-5", validator.isValid("0-201-63385-X"))
        self.assertTrue("isValid-6", validator.isValid("0 201 63385 X"))

    def testInvalidISBN13Format(self) -> None:
        pattern = re.compile(ISBNValidator.ISBN13_REGEX)
        validator = ISBNValidator.getInstance0()
        for i in range(len(self.__invalidISBN13Format)):
            self.assertFalse(
                "Pattern[" + str(i) + "]=" + self.__invalidISBN13Format[i],
                pattern.match(self.__invalidISBN13Format[i]) is not None,
            )
            self.assertFalse(
                "isValidISBN13[" + str(i) + "]=" + self.__invalidISBN13Format[i],
                validator.isValidISBN13(self.__invalidISBN13Format[i]),
            )
            self.assertIsNone(
                "validateISBN13[" + str(i) + "]=" + self.__invalidISBN13Format[i],
                validator.validateISBN13(self.__invalidISBN13Format[i]),
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
        for i in range(len(self.__invalidISBN10Format)):
            self.assertFalse(
                "Pattern[" + str(i) + "]=" + self.__invalidISBN10Format[i],
                pattern.match(self.__invalidISBN10Format[i]) is not None,
            )
            self.assertFalse(
                "isValidISBN10[" + str(i) + "]=" + self.__invalidISBN10Format[i],
                validator.isValidISBN10(self.__invalidISBN10Format[i]),
            )
            self.assertIsNone(
                "validateISBN10[" + str(i) + "]=" + self.__invalidISBN10Format[i],
                validator.validateISBN10(self.__invalidISBN10Format[i]),
            )

    def testValidISBN10Format(self) -> None:
        pattern = Pattern.compile(ISBNValidator.ISBN10_REGEX)
        for i in range(len(self.__validISBN10Format)):
            self.assertTrue(
                "Pattern[" + str(i) + "]=" + self.__validISBN10Format[i],
                pattern.matcher(self.__validISBN10Format[i]).matches(),
            )

    def __init__(self, name: str) -> None:
        super().__init__(name)
