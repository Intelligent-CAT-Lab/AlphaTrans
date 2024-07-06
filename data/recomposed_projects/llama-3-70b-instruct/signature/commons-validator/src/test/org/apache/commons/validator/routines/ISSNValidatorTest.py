from __future__ import annotations
import re
import unittest
import pytest
import io
import typing
from typing import *
import unittest
from src.main.org.apache.commons.validator.routines.ISSNValidator import *
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.EAN13CheckDigit import *


class ISSNValidatorTest(unittest.TestCase):

    __invalidFormat: typing.List[str] = [
        "",
        "   ",
        "ISBN 0317-8471",
        "'1050-124X",
        "ISSN1562-6865",
        "10637710",
        "1748-7188'",
        "ISSN  0264-2875",
        "1750 0095",
        "1188_1534",
        "1911-1478",
    ]
    __validFormat: typing.List[str] = [
        "ISSN 0317-8471",
        "1050-124X",
        "ISSN 1562-6865",
        "1063-7710",
        "1748-7188",
        "ISSN 0264-2875",
        "1750-0095",
        "1188-1534",
        "1911-1479",
        "ISSN 1911-1460",
        "0001-6772",
        "1365-201X",
        "0264-3596",
        "1144-875X",
    ]
    __VALIDATOR: ISSNValidator = ISSNValidator.getInstance()

    def testIsValidExtract(self) -> None:
        self.assertEqual("12345679", self.__VALIDATOR.extractFromEAN13("9771234567003"))
        self.assertEqual("00014664", self.__VALIDATOR.extractFromEAN13("9770001466006"))
        self.assertEqual("03178471", self.__VALIDATOR.extractFromEAN13("9770317847001"))
        self.assertEqual("1144875X", self.__VALIDATOR.extractFromEAN13("9771144875007"))

    def testValidCheckDigitEan13(self) -> None:
        self.assertIsNone(self.__VALIDATOR.extractFromEAN13("9771234567001"))
        self.assertIsNone(self.__VALIDATOR.extractFromEAN13("9771234567002"))
        self.assertIsNotNone(
            self.__VALIDATOR.extractFromEAN13("9771234567003")
        )  # valid check digit
        self.assertIsNone(self.__VALIDATOR.extractFromEAN13("9771234567004"))
        self.assertIsNone(self.__VALIDATOR.extractFromEAN13("9771234567005"))
        self.assertIsNone(self.__VALIDATOR.extractFromEAN13("9771234567006"))
        self.assertIsNone(self.__VALIDATOR.extractFromEAN13("9771234567007"))
        self.assertIsNone(self.__VALIDATOR.extractFromEAN13("9771234567008"))
        self.assertIsNone(self.__VALIDATOR.extractFromEAN13("9771234567009"))
        self.assertIsNone(self.__VALIDATOR.extractFromEAN13("9771234567000"))

    def testConversionErrors(self) -> None:
        input: str = None
        try:
            input = "9780072129519"
            self.__VALIDATOR.extractFromEAN13(input)
            self.fail("Expected ValueError for '" + input + "'")
        except ValueError as e:
            pass
        try:
            input = "9791090636071"
            self.__VALIDATOR.extractFromEAN13(input)
            self.fail("Expected ValueError for '" + input + "'")
        except ValueError as e:
            pass
        try:
            input = "03178471"
            self.__VALIDATOR.extractFromEAN13(input)
            self.fail("Expected ValueError for '" + input + "'")
        except ValueError as e:
            pass

    def testIsValidISSNConvert(self) -> None:
        ean13cd: CheckDigit = EAN13CheckDigit.EAN13_CHECK_DIGIT
        r: Random = Random()
        for f in self.__validFormat:
            suffix: str = String.format("%02d", r.nextInt(100))
            ean13: str = self.__VALIDATOR.convertToEAN13(f, suffix)
            assertTrue(ean13, ean13cd.isValid(ean13))
        assertEquals(
            "9771144875007", self.__VALIDATOR.convertToEAN13("1144-875X", "00")
        )
        assertEquals(
            "9770264359008", self.__VALIDATOR.convertToEAN13("0264-3596", "00")
        )
        assertEquals(
            "9771234567003", self.__VALIDATOR.convertToEAN13("1234-5679", "00")
        )

    def testIsValidISSNConvertSuffix(self) -> None:

        pass  # LLM could not translate this method

    def testIsValidISSNConvertNull(self) -> None:
        self.assertIsNone(self.__VALIDATOR.convertToEAN13(None, "00"))

    def testInvalid(self) -> None:
        for f in self.__invalidFormat:
            self.assertFalse(f, self.__VALIDATOR.isValid(f))

    def testNull(self) -> None:
        self.assertFalse("isValid", self.__VALIDATOR.isValid(None))

    def testIsValidISSN(self) -> None:
        for f in self.__validFormat:
            self.assertTrue(f, self.__VALIDATOR.isValid(f))

    def __init__(self, name: str) -> None:
        super().__init__(name)
