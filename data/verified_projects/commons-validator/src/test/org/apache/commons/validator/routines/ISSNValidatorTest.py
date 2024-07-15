import pytest

import unittest
from random import Random
from src.main.org.apache.commons.validator.routines.ISSNValidator import *
from src.main.org.apache.commons.validator.routines.checkdigit.EAN13CheckDigit import *

class ISSNValidatorTest(unittest.TestCase):

    __VALIDATOR = ISSNValidator.getInstance()

    __validFormat = [
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

    __invalidFormat = [
        "",  # empty
        "   ",  # empty
        "ISBN 0317-8471",  # wrong prefix
        "'1050-124X",  # leading garbage
        "ISSN1562-6865",  # missing separator
        "10637710",  # missing separator
        "1748-7188'",  # trailing garbage
        "ISSN  0264-2875",  # extra space
        "1750 0095",  # invalid separator
        "1188_1534",  # invalid separator
        "1911-1478",  # invalid checkdigit
    ]

    
    @pytest.mark.test
    def testIsValidISSN(self) -> None:
        for f in self.__validFormat:
            self.assertTrue(
                ISSNValidatorTest.__VALIDATOR.isValid(f),
                f
            )

    
    @pytest.mark.test
    def testNull(self) -> None:
        self.assertFalse(
            ISSNValidatorTest.__VALIDATOR.isValid(None),
            "isValid"
        )

    
    @pytest.mark.test
    def testInvalid(self) -> None:
        for f in self.__invalidFormat:
            self.assertFalse(
                ISSNValidatorTest.__VALIDATOR.isValid(f),
                f
            )

    
    @pytest.mark.test
    def testIsValidISSNConvertNull(self) -> None:
        self.assertIsNone(
            ISSNValidatorTest.__VALIDATOR.convertToEAN13(None, "00")
        )

    
    @pytest.mark.test
    def testIsValidISSNConvertSuffix(self) -> None:
        for suffix in [None, "", "0", "A", "AA", "999"]:
            with self.assertRaises(
                ValueError,
                msg="Expected IllegalArgumentException"
            ):
                ISSNValidatorTest.__VALIDATOR.convertToEAN13(None, suffix)

    
    @pytest.mark.test
    def testIsValidISSNConvert(self) -> None:
        ean13cd = EAN13CheckDigit.EAN13_CHECK_DIGIT
        r = Random()
        for f in self.__validFormat:
            suffix = "{:02d}".format(r.randint(0, 99))
            ean13 = ISSNValidatorTest.__VALIDATOR.convertToEAN13(f, suffix)
            self.assertTrue(
                ean13cd.isValid(ean13),
                ean13
            )
        self.assertEqual(
            "9771144875007",
            ISSNValidatorTest.__VALIDATOR.convertToEAN13("1144-875X", "00")
        )
        self.assertEqual(
            "9770264359008",
            ISSNValidatorTest.__VALIDATOR.convertToEAN13("0264-3596", "00")
        )
        self.assertEqual(
            "9771234567003",
            ISSNValidatorTest.__VALIDATOR.convertToEAN13("1234-5679", "00")
        )

    
    @pytest.mark.test
    def testConversionErrors(self) -> None:
        inputs = ["9780072129519", "9791090636071", "03178471"]
        for input in inputs:
            with self.assertRaises(
                ValueError,
                msg="Expected IllegalArgumentException for '" + input + "'"
            ):
                ISSNValidatorTest.__VALIDATOR.extractFromEAN13(input)

    
    @pytest.mark.test
    def testValidCheckDigitEAN13(self) -> None:
        valideCodes = ["9771234567003"]
        invalideCodes = [
            "9771234567001",
            "9771234567002",
            "9771234567004",
            "9771234567005",
            "9771234567006",
            "9771234567007",
            "9771234567008",
            "9771234567009",
            "9771234567000"
        ]
        for code in valideCodes:
            self.assertIsNotNone(
                ISSNValidatorTest.__VALIDATOR.extractFromEAN13(code)
            )
        for code in invalideCodes:
            self.assertIsNone(
                ISSNValidatorTest.__VALIDATOR.extractFromEAN13(code)
            )

    
    @pytest.mark.test
    def testIsValidExtract(self) -> None:
        self.assertEqual(
            "12345679",
            ISSNValidatorTest.__VALIDATOR.extractFromEAN13("9771234567003")
        )
        self.assertEqual(
            "00014664",
            ISSNValidatorTest.__VALIDATOR.extractFromEAN13("9770001466006")
        )
        self.assertEqual(
            "03178471",
            ISSNValidatorTest.__VALIDATOR.extractFromEAN13("9770317847001")
        )
        self.assertEqual(
            "1144875X",
            ISSNValidatorTest.__VALIDATOR.extractFromEAN13("9771144875007")
        )
