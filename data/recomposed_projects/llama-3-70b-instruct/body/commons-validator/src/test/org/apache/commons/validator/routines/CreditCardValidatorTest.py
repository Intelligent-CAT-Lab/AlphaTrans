from __future__ import annotations
import re
import numbers
import unittest
import pytest
import io
import typing
from typing import *
import unittest
from src.main.org.apache.commons.validator.CreditCardValidator import *
from src.main.org.apache.commons.validator.routines.CodeValidator import *
from src.main.org.apache.commons.validator.routines.CreditCardValidator import *
from src.main.org.apache.commons.validator.routines.RegexValidator import *
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.LuhnCheckDigit import *


class CreditCardValidatorTest(unittest.TestCase):

    __ERROR_CARDS: typing.List[str] = [
        "ERROR_VISA",
        "ERROR_SHORT_VISA",
        "ERROR_AMEX",
        "ERROR_MASTERCARD",
        "ERROR_DISCOVER",
        "ERROR_DISCOVER65",
        "ERROR_DINERS",
        "ERROR_VPAY",
        "",
        "12345678901",
        "12345678901234567890",
        "4417123456789112",
    ]
    __VALID_CARDS: typing.List[str] = [
        "VALID_VISA",
        "VALID_SHORT_VISA",
        "VALID_AMEX",
        "VALID_MASTERCARD",
        "VALID_DISCOVER",
        "VALID_DISCOVER65",
        "VALID_DINERS",
        "VALID_VPAY",
        "VALID_VPAY2",
        "60115564485789458",
    ]
    __ERROR_VPAY: str = "4370000000000069"
    __VALID_VPAY2: str = "4370000000000012"
    __VALID_VPAY: str = "4370000000000061"
    __ERROR_DINERS: str = "30569309025901"
    __VALID_DINERS: str = "30569309025904"
    __ERROR_DISCOVER65: str = "6534567890123450"
    __VALID_DISCOVER65: str = "6534567890123458"
    __ERROR_DISCOVER: str = "6011000990139421"
    __VALID_DISCOVER: str = "6011000990139424"
    __ERROR_MASTERCARD: str = "5105105105105105"
    __VALID_MASTERCARD: str = "5105105105105100"
    __ERROR_AMEX: str = "378282246310001"
    __VALID_AMEX: str = "378282246310005"
    __ERROR_SHORT_VISA: str = "4222222222229"
    __VALID_SHORT_VISA: str = "4222222222222"
    __ERROR_VISA: str = "4417123456789112"
    __VALID_VISA: str = "4417123456789113"

    def testDisjointRange(self) -> None:
        ccv = CreditCardValidator(
            2, 0, [CreditCardRange(1, "305", "4", 0, 0, [13, 16])], None
        )
        self.assertEqual(13, len(self.__VALID_SHORT_VISA))
        self.assertEqual(16, len(self.__VALID_VISA))
        self.assertEqual(14, len(self.__VALID_DINERS))
        self.assertTrue(ccv.isValid(self.__VALID_SHORT_VISA))
        self.assertTrue(ccv.isValid(self.__VALID_VISA))
        self.assertFalse(ccv.isValid(self.__ERROR_SHORT_VISA))
        self.assertFalse(ccv.isValid(self.__ERROR_VISA))
        self.assertFalse(ccv.isValid(self.__VALID_DINERS))
        ccv = CreditCardValidator(
            2, 0, [CreditCardRange(1, "305", "4", 0, 0, [13, 14, 16])], None
        )
        self.assertTrue(ccv.isValid(self.__VALID_DINERS))

    def testValidLength(self) -> None:

        pass  # LLM could not translate this method

    def testRangeGenerator(self) -> None:
        ccv = CreditCardValidator(
            3,
            0,
            [
                CreditCardRange(0, "300", "305", 14, 14, None),
                CreditCardRange(0, "3095", None, 14, 14, None),
                CreditCardRange(0, "36", None, 14, 14, None),
                CreditCardRange(0, "38", "39", 14, 14, None),
            ],
            [
                CreditCardValidator.AMEX_VALIDATOR,
                CreditCardValidator.VISA_VALIDATOR,
                CreditCardValidator.MASTERCARD_VALIDATOR,
                CreditCardValidator.DISCOVER_VALIDATOR,
            ],
        )
        for s in self.__VALID_CARDS:
            self.assertTrue(s, ccv.isValid(s))
        for s in self.__ERROR_CARDS:
            self.assertFalse(s, ccv.isValid(s))

    def testRangeGeneratorNoLuhn(self) -> None:
        cv: CodeValidator = CreditCardValidator.createRangeValidator(
            [
                CreditCardRange(0, "1", None, 6, 7, None),
                CreditCardRange(0, "644", "65", 8, 8, None),
            ],
            None,
        )
        self.assertTrue(cv.isValid("1990000"))
        self.assertTrue(cv.isValid("199000"))
        self.assertFalse(cv.isValid("000000"))
        self.assertFalse(cv.isValid("099999"))
        self.assertFalse(cv.isValid("200000"))

        self.assertFalse(cv.isValid("64399999"))
        self.assertTrue(cv.isValid("64400000"))
        self.assertTrue(cv.isValid("64900000"))
        self.assertTrue(cv.isValid("65000000"))
        self.assertTrue(cv.isValid("65999999"))
        self.assertFalse(cv.isValid("66000000"))

    def testGeneric(self) -> None:
        ccv: CreditCardValidator = CreditCardValidator.genericCreditCardValidator2()
        for s in self.__VALID_CARDS:
            self.assertTrue(s, ccv.isValid(s))
        for s in self.__ERROR_CARDS:
            self.assertFalse(s, ccv.isValid(s))

    def testMastercardUsingSeparators(self) -> None:
        MASTERCARD_REGEX_SEP = (
            "^(5[1-5]\\d{2})(?:[- ])?(\\d{4})(?:[- ])?(\\d{4})(?:[- ])?(\\d{4})$"
        )
        validator = CodeValidator.CodeValidator5(
            MASTERCARD_REGEX_SEP, LuhnCheckDigit.LUHN_CHECK_DIGIT
        )
        regex = validator.getRegexValidator()

        self.assertEqual(
            "Number", "5134567890123456", regex.validate("5134567890123456")
        )
        self.assertEqual(
            "Hyphen", "5134567890123456", regex.validate("5134-5678-9012-3456")
        )
        self.assertEqual(
            "Space", "5134567890123456", regex.validate("5134 5678 9012 3456")
        )
        self.assertEqual(
            "MixedA", "5134567890123456", regex.validate("5134-5678 9012-3456")
        )
        self.assertEqual(
            "MixedB", "5134567890123456", regex.validate("5134 5678-9012 3456")
        )

        self.assertFalse("Invalid Separator A", regex.isValid("5134.5678.9012.3456"))
        self.assertFalse("Invalid Separator B", regex.isValid("5134_5678_9012_3456"))
        self.assertFalse("Invalid Grouping A", regex.isValid("513-45678-9012-3456"))
        self.assertFalse("Invalid Grouping B", regex.isValid("5134-567-89012-3456"))
        self.assertFalse("Invalid Grouping C", regex.isValid("5134-5678-901-23456"))

        self.assertEqual(
            "Valid-A", "5500000000000004", validator.validate("5500-0000-0000-0004")
        )
        self.assertEqual(
            "Valid-B", "5424000000000015", validator.validate("5424 0000 0000 0015")
        )
        self.assertEqual(
            "Valid-C", "5301250070000191", validator.validate("5301-250070000191")
        )
        self.assertEqual(
            "Valid-D", "5123456789012346", validator.validate("5123456789012346")
        )

    def testVPayOption(self) -> None:
        validator = CreditCardValidator(0, CreditCardValidator.VPAY, None, None)
        self.assertTrue("Valid", validator.isValid(self.__VALID_VPAY))
        self.assertTrue("Valid", validator.isValid(self.__VALID_VPAY2))
        self.assertFalse("Invalid", validator.isValid(self.__ERROR_VPAY))
        self.assertEqual(self.__VALID_VPAY, validator.validate(self.__VALID_VPAY))
        self.assertEqual(self.__VALID_VPAY2, validator.validate(self.__VALID_VPAY2))

        self.assertFalse("Amex", validator.isValid(self.__VALID_AMEX))
        self.assertFalse("Diners", validator.isValid(self.__VALID_DINERS))
        self.assertFalse("Discover", validator.isValid(self.__VALID_DISCOVER))
        self.assertFalse("Mastercard", validator.isValid(self.__VALID_MASTERCARD))
        self.assertTrue("Visa", validator.isValid(self.__VALID_VISA))
        self.assertTrue("Visa Short", validator.isValid(self.__VALID_SHORT_VISA))

    def testVisaOption(self) -> None:
        validator = CreditCardValidator(0, CreditCardValidator.VISA, None, None)
        self.assertFalse("Invalid", validator.isValid(self.__ERROR_VISA))
        self.assertFalse("Invalid-S", validator.isValid(self.__ERROR_SHORT_VISA))
        self.assertIsNone("validate()", validator.validate(self.__ERROR_VISA))
        self.assertEqual(self.__VALID_VISA, validator.validate(self.__VALID_VISA))
        self.assertEqual(
            self.__VALID_SHORT_VISA, validator.validate(self.__VALID_SHORT_VISA)
        )

        self.assertFalse("Amex", validator.isValid(self.__VALID_AMEX))
        self.assertFalse("Diners", validator.isValid(self.__VALID_DINERS))
        self.assertFalse("Discover", validator.isValid(self.__VALID_DISCOVER))
        self.assertFalse("Mastercard", validator.isValid(self.__VALID_MASTERCARD))
        self.assertTrue("Visa", validator.isValid(self.__VALID_VISA))
        self.assertTrue("Visa Short", validator.isValid(self.__VALID_SHORT_VISA))

    def testVisaValidator(self) -> None:
        validator: CodeValidator = CreditCardValidator.VISA_VALIDATOR
        regex: RegexValidator = validator.getRegexValidator()

        self.assertFalse("Length 12", regex.isValid("423456789012"))
        self.assertTrue("Length 13", regex.isValid("4234567890123"))
        self.assertFalse("Length 14", regex.isValid("42345678901234"))
        self.assertFalse("Length 15", regex.isValid("423456789012345"))
        self.assertTrue("Length 16", regex.isValid("4234567890123456"))
        self.assertFalse("Length 17", regex.isValid("42345678901234567"))
        self.assertFalse("Length 18", regex.isValid("423456789012345678"))
        self.assertFalse("Invalid Pref-A", regex.isValid("3234567890123"))
        self.assertFalse("Invalid Pref-B", regex.isValid("3234567890123456"))
        self.assertFalse("Invalid Char-A", regex.isValid("4234567x90123"))
        self.assertFalse("Invalid Char-B", regex.isValid("4234567x90123456"))

        self.assertTrue("Valid regex", regex.isValid(self.__ERROR_VISA))
        self.assertTrue("Valid regex-S", regex.isValid(self.__ERROR_SHORT_VISA))
        self.assertFalse("Invalid", validator.isValid(self.__ERROR_VISA))
        self.assertFalse("Invalid-S", validator.isValid(self.__ERROR_SHORT_VISA))
        self.assertIsNone("validate()", validator.validate(self.__ERROR_VISA))
        self.assertEqual(self.__VALID_VISA, validator.validate(self.__VALID_VISA))
        self.assertEqual(
            self.__VALID_SHORT_VISA, validator.validate(self.__VALID_SHORT_VISA)
        )

        self.assertFalse("Amex", validator.isValid(self.__VALID_AMEX))
        self.assertFalse("Diners", validator.isValid(self.__VALID_DINERS))
        self.assertFalse("Discover", validator.isValid(self.__VALID_DISCOVER))
        self.assertFalse("Mastercard", validator.isValid(self.__VALID_MASTERCARD))
        self.assertTrue("Visa", validator.isValid(self.__VALID_VISA))
        self.assertTrue("Visa Short", validator.isValid(self.__VALID_SHORT_VISA))

        self.assertTrue("Valid-A", validator.isValid("4111111111111111"))
        self.assertTrue("Valid-C", validator.isValid("4543059999999982"))
        self.assertTrue("Valid-B", validator.isValid("4462000000000003"))
        self.assertTrue("Valid-D", validator.isValid("4508750000000009"))  # Electron
        self.assertTrue("Valid-E", validator.isValid("4012888888881881"))

    def testMastercardOption(self) -> None:
        validator = CreditCardValidator(0, CreditCardValidator.MASTERCARD, None, None)
        self.assertFalse("Invalid", validator.isValid(self.__ERROR_MASTERCARD))
        self.assertIsNone("validate()", validator.validate(self.__ERROR_MASTERCARD))
        self.assertEqual(
            self.__VALID_MASTERCARD, validator.validate(self.__VALID_MASTERCARD)
        )

        self.assertFalse("Amex", validator.isValid(self.__VALID_AMEX))
        self.assertFalse("Diners", validator.isValid(self.__VALID_DINERS))
        self.assertFalse("Discover", validator.isValid(self.__VALID_DISCOVER))
        self.assertTrue("Mastercard", validator.isValid(self.__VALID_MASTERCARD))
        self.assertFalse("Visa", validator.isValid(self.__VALID_VISA))
        self.assertFalse("Visa Short", validator.isValid(self.__VALID_SHORT_VISA))

    def testMastercardValidator(self) -> None:
        validator: CodeValidator = CreditCardValidator.MASTERCARD_VALIDATOR
        regex: RegexValidator = validator.getRegexValidator()

        self.assertFalse("Length 12", regex.isValid("513456789012"))
        self.assertFalse("Length 13", regex.isValid("5134567890123"))
        self.assertFalse("Length 14", regex.isValid("51345678901234"))
        self.assertFalse("Length 15", regex.isValid("513456789012345"))
        self.assertTrue("Length 16", regex.isValid("5134567890123456"))
        self.assertFalse("Length 17", regex.isValid("51345678901234567"))
        self.assertFalse("Length 18", regex.isValid("513456789012345678"))
        self.assertFalse("Prefix 41", regex.isValid("4134567890123456"))
        self.assertFalse("Prefix 50", regex.isValid("5034567890123456"))
        self.assertTrue("Prefix 51", regex.isValid("5134567890123456"))
        self.assertTrue("Prefix 52", regex.isValid("5234567890123456"))
        self.assertTrue("Prefix 53", regex.isValid("5334567890123456"))
        self.assertTrue("Prefix 54", regex.isValid("5434567890123456"))
        self.assertTrue("Prefix 55", regex.isValid("5534567890123456"))
        self.assertFalse("Prefix 56", regex.isValid("5634567890123456"))
        self.assertFalse("Prefix 61", regex.isValid("6134567890123456"))
        self.assertFalse("Invalid Char", regex.isValid("5134567x90123456"))

        self.assertTrue("Valid regex", regex.isValid(self.__ERROR_MASTERCARD))
        self.assertFalse("Invalid", validator.isValid(self.__ERROR_MASTERCARD))
        self.assertIsNone("validate()", validator.validate(self.__ERROR_MASTERCARD))
        self.assertEqual(
            self.__VALID_MASTERCARD, validator.validate(self.__VALID_MASTERCARD)
        )

        self.assertFalse("Amex", validator.isValid(self.__VALID_AMEX))
        self.assertFalse("Diners", validator.isValid(self.__VALID_DINERS))
        self.assertFalse("Discover", validator.isValid(self.__VALID_DISCOVER))
        self.assertTrue("Mastercard", validator.isValid(self.__VALID_MASTERCARD))
        self.assertFalse("Visa", validator.isValid(self.__VALID_VISA))
        self.assertFalse("Visa Short", validator.isValid(self.__VALID_SHORT_VISA))

        self.assertTrue("Valid-A", validator.isValid("5500000000000004"))
        self.assertTrue("Valid-B", validator.isValid("5424000000000015"))
        self.assertTrue("Valid-C", validator.isValid("5301250070000191"))
        self.assertTrue("Valid-D", validator.isValid("5123456789012346"))
        self.assertTrue("Valid-E", validator.isValid("5555555555554444"))

        rev: RegexValidator = validator.getRegexValidator()
        PAD: str = "0000000000"
        self.assertFalse("222099", rev.isValid("222099" + PAD))
        for i in range(222100, 272099 + 1):
            j: str = str(i) + PAD
            self.assertTrue(j, rev.isValid(j))
        self.assertFalse("272100", rev.isValid("272100" + PAD))

    def testDiscoverOption(self) -> None:
        validator = CreditCardValidator(0, CreditCardValidator.DISCOVER, None, None)
        self.assertFalse("Invalid", validator.isValid(self.__ERROR_DISCOVER))
        self.assertFalse("Invalid65", validator.isValid(self.__ERROR_DISCOVER65))
        self.assertIsNone("validate()", validator.validate(self.__ERROR_DISCOVER))
        self.assertEqual(
            self.__VALID_DISCOVER, validator.validate(self.__VALID_DISCOVER)
        )
        self.assertEqual(
            self.__VALID_DISCOVER65, validator.validate(self.__VALID_DISCOVER65)
        )

        self.assertFalse("Amex", validator.isValid(self.__VALID_AMEX))
        self.assertFalse("Diners", validator.isValid(self.__VALID_DINERS))
        self.assertTrue("Discover", validator.isValid(self.__VALID_DISCOVER))
        self.assertTrue("Discover", validator.isValid(self.__VALID_DISCOVER65))
        self.assertFalse("Mastercard", validator.isValid(self.__VALID_MASTERCARD))
        self.assertFalse("Visa", validator.isValid(self.__VALID_VISA))
        self.assertFalse("Visa Short", validator.isValid(self.__VALID_SHORT_VISA))

    def testDiscoverValidator(self) -> None:
        validator: CodeValidator = CreditCardValidator.DISCOVER_VALIDATOR
        regex: RegexValidator = validator.getRegexValidator()

        self.assertFalse("Length 12-6011", regex.isValid("601156789012"))
        self.assertFalse("Length 12-65", regex.isValid("653456789012"))
        self.assertFalse("Length 13-6011", regex.isValid("6011567890123"))
        self.assertFalse("Length 13-65", regex.isValid("6534567890123"))
        self.assertFalse("Length 14-6011", regex.isValid("60115678901234"))
        self.assertFalse("Length 14-65", regex.isValid("65345678901234"))
        self.assertFalse("Length 15-6011", regex.isValid("601156789012345"))
        self.assertFalse("Length 15-65", regex.isValid("653456789012345"))
        self.assertTrue("Length 16-6011", regex.isValid("6011567890123456"))
        self.assertTrue("Length 16-644", regex.isValid("6444567890123456"))
        self.assertTrue("Length 16-648", regex.isValid("6484567890123456"))
        self.assertTrue("Length 16-65", regex.isValid("6534567890123456"))
        self.assertFalse("Length 17-65", regex.isValid("65345678901234567"))
        self.assertFalse("Length 18-6011", regex.isValid("601156789012345678"))
        self.assertFalse("Length 18-65", regex.isValid("653456789012345678"))

        self.assertFalse("Prefix 640", regex.isValid("6404567890123456"))
        self.assertFalse("Prefix 641", regex.isValid("6414567890123456"))
        self.assertFalse("Prefix 642", regex.isValid("6424567890123456"))
        self.assertFalse("Prefix 643", regex.isValid("6434567890123456"))
        self.assertFalse("Prefix 6010", regex.isValid("6010567890123456"))
        self.assertFalse("Prefix 6012", regex.isValid("6012567890123456"))
        self.assertFalse("Invalid Char", regex.isValid("6011567x90123456"))

        self.assertTrue("Valid regex", regex.isValid(self.__ERROR_DISCOVER))
        self.assertTrue("Valid regex65", regex.isValid(self.__ERROR_DISCOVER65))
        self.assertFalse("Invalid", validator.isValid(self.__ERROR_DISCOVER))
        self.assertFalse("Invalid65", validator.isValid(self.__ERROR_DISCOVER65))
        self.assertIsNone("validate()", validator.validate(self.__ERROR_DISCOVER))
        self.assertEqual(
            self.__VALID_DISCOVER, validator.validate(self.__VALID_DISCOVER)
        )
        self.assertEqual(
            self.__VALID_DISCOVER65, validator.validate(self.__VALID_DISCOVER65)
        )

        self.assertFalse("Amex", validator.isValid(self.__VALID_AMEX))
        self.assertFalse("Diners", validator.isValid(self.__VALID_DINERS))
        self.assertTrue("Discover", validator.isValid(self.__VALID_DISCOVER))
        self.assertTrue("Discover", validator.isValid(self.__VALID_DISCOVER65))
        self.assertFalse("Mastercard", validator.isValid(self.__VALID_MASTERCARD))
        self.assertFalse("Visa", validator.isValid(self.__VALID_VISA))
        self.assertFalse("Visa Short", validator.isValid(self.__VALID_SHORT_VISA))

        self.assertTrue("Valid-A", validator.isValid("6011111111111117"))
        self.assertTrue("Valid-B", validator.isValid("6011000000000004"))
        self.assertTrue("Valid-C", validator.isValid("6011000000000012"))

    def testDinersOption(self) -> None:
        validator = CreditCardValidator(0, CreditCardValidator.DINERS, None, None)
        self.assertFalse("Invalid", validator.isValid(self.__ERROR_DINERS))
        self.assertIsNone("validate()", validator.validate(self.__ERROR_DINERS))
        self.assertEqual(self.__VALID_DINERS, validator.validate(self.__VALID_DINERS))

        self.assertFalse("Amex", validator.isValid(self.__VALID_AMEX))
        self.assertTrue("Diners", validator.isValid(self.__VALID_DINERS))
        self.assertFalse("Discover", validator.isValid(self.__VALID_DISCOVER))
        self.assertFalse("Mastercard", validator.isValid(self.__VALID_MASTERCARD))
        self.assertFalse("Visa", validator.isValid(self.__VALID_VISA))
        self.assertFalse("Visa Short", validator.isValid(self.__VALID_SHORT_VISA))

    def testDinersValidator(self) -> None:
        validator: CodeValidator = CreditCardValidator.DINERS_VALIDATOR
        regex: RegexValidator = validator.getRegexValidator()

        self.assertFalse("Length 12-300", regex.isValid("300456789012"))
        self.assertFalse("Length 12-36", regex.isValid("363456789012"))
        self.assertFalse("Length 13-300", regex.isValid("3004567890123"))
        self.assertFalse("Length 13-36", regex.isValid("3634567890123"))
        self.assertTrue("Length 14-300", regex.isValid("30045678901234"))
        self.assertTrue("Length 14-36", regex.isValid("36345678901234"))
        self.assertFalse("Length 15-300", regex.isValid("300456789012345"))
        self.assertFalse("Length 15-36", regex.isValid("363456789012345"))
        self.assertFalse("Length 16-300", regex.isValid("3004567890123456"))
        self.assertFalse("Length 16-36", regex.isValid("3634567890123456"))
        self.assertFalse("Length 17-300", regex.isValid("30045678901234567"))
        self.assertFalse("Length 17-36", regex.isValid("36345678901234567"))
        self.assertFalse("Length 18-300", regex.isValid("300456789012345678"))
        self.assertFalse("Length 18-36", regex.isValid("363456789012345678"))

        self.assertTrue("Prefix 300", regex.isValid("30045678901234"))
        self.assertTrue("Prefix 301", regex.isValid("30145678901234"))
        self.assertTrue("Prefix 302", regex.isValid("30245678901234"))
        self.assertTrue("Prefix 303", regex.isValid("30345678901234"))
        self.assertTrue("Prefix 304", regex.isValid("30445678901234"))
        self.assertTrue("Prefix 305", regex.isValid("30545678901234"))
        self.assertFalse("Prefix 306", regex.isValid("30645678901234"))
        self.assertFalse("Prefix 3094", regex.isValid("30945678901234"))
        self.assertTrue("Prefix 3095", regex.isValid("30955678901234"))
        self.assertFalse("Prefix 3096", regex.isValid("30965678901234"))
        self.assertFalse("Prefix 35", regex.isValid("35345678901234"))
        self.assertTrue("Prefix 36", regex.isValid("36345678901234"))
        self.assertFalse("Prefix 37", regex.isValid("37345678901234"))
        self.assertTrue("Prefix 38", regex.isValid("38345678901234"))
        self.assertTrue("Prefix 39", regex.isValid("39345678901234"))

        self.assertFalse("Invalid Char-A", regex.isValid("3004567x901234"))
        self.assertFalse("Invalid Char-B", regex.isValid("3634567x901234"))

        self.assertTrue("Valid regex", regex.isValid(self.__ERROR_DINERS))
        self.assertFalse("Invalid", validator.isValid(self.__ERROR_DINERS))
        self.assertIsNone("validate()", validator.validate(self.__ERROR_DINERS))
        self.assertEqual(self.__VALID_DINERS, validator.validate(self.__VALID_DINERS))

        self.assertFalse("Amex", validator.isValid(self.__VALID_AMEX))
        self.assertTrue("Diners", validator.isValid(self.__VALID_DINERS))
        self.assertFalse("Discover", validator.isValid(self.__VALID_DISCOVER))
        self.assertFalse("Mastercard", validator.isValid(self.__VALID_MASTERCARD))
        self.assertFalse("Visa", validator.isValid(self.__VALID_VISA))
        self.assertFalse("Visa Short", validator.isValid(self.__VALID_SHORT_VISA))

        self.assertTrue("Valid-A", validator.isValid("30000000000004"))
        self.assertTrue("Valid-B", validator.isValid("30123456789019"))
        self.assertTrue("Valid-C", validator.isValid("36432685260294"))

    def testAmexOption(self) -> None:
        validator = CreditCardValidator(0, CreditCardValidator.AMEX, None, None)
        self.assertFalse("Invalid", validator.isValid(self.__ERROR_AMEX))
        self.assertIsNone("validate()", validator.validate(self.__ERROR_AMEX))
        self.assertEqual(self.__VALID_AMEX, validator.validate(self.__VALID_AMEX))

        self.assertTrue("Amex", validator.isValid(self.__VALID_AMEX))
        self.assertFalse("Diners", validator.isValid(self.__VALID_DINERS))
        self.assertFalse("Discover", validator.isValid(self.__VALID_DISCOVER))
        self.assertFalse("Mastercard", validator.isValid(self.__VALID_MASTERCARD))
        self.assertFalse("Visa", validator.isValid(self.__VALID_VISA))
        self.assertFalse("Visa Short", validator.isValid(self.__VALID_SHORT_VISA))

    def testAmexValidator(self) -> None:
        validator: CodeValidator = CreditCardValidator.AMEX_VALIDATOR
        regex: RegexValidator = validator.getRegexValidator()

        self.assertFalse("Length 12", regex.isValid("343456789012"))
        self.assertFalse("Length 13", regex.isValid("3434567890123"))
        self.assertFalse("Length 14", regex.isValid("34345678901234"))
        self.assertTrue("Length 15", regex.isValid("343456789012345"))
        self.assertFalse("Length 16", regex.isValid("3434567890123456"))
        self.assertFalse("Length 17", regex.isValid("34345678901234567"))
        self.assertFalse("Length 18", regex.isValid("343456789012345678"))
        self.assertFalse("Prefix 33", regex.isValid("333456789012345"))
        self.assertTrue("Prefix 34", regex.isValid("343456789012345"))
        self.assertFalse("Prefix 35", regex.isValid("353456789012345"))
        self.assertFalse("Prefix 36", regex.isValid("363456789012345"))
        self.assertTrue("Prefix 37", regex.isValid("373456789012345"))
        self.assertFalse("Prefix 38", regex.isValid("383456789012345"))
        self.assertFalse("Prefix 41", regex.isValid("413456789012345"))
        self.assertFalse("Invalid Char", regex.isValid("3434567x9012345"))

        self.assertTrue("Valid regex", regex.isValid(self.__ERROR_AMEX))
        self.assertFalse("Invalid", validator.isValid(self.__ERROR_AMEX))
        self.assertIsNone("validate()", validator.validate(self.__ERROR_AMEX))
        self.assertEqual(self.__VALID_AMEX, validator.validate(self.__VALID_AMEX))

        self.assertTrue("Amex", validator.isValid(self.__VALID_AMEX))
        self.assertFalse("Diners", validator.isValid(self.__VALID_DINERS))
        self.assertFalse("Discover", validator.isValid(self.__VALID_DISCOVER))
        self.assertFalse("Mastercard", validator.isValid(self.__VALID_MASTERCARD))
        self.assertFalse("Visa", validator.isValid(self.__VALID_VISA))
        self.assertFalse("Visa Short", validator.isValid(self.__VALID_SHORT_VISA))

        self.assertTrue("Valid-A", validator.isValid("371449635398431"))
        self.assertTrue("Valid-B", validator.isValid("340000000000009"))
        self.assertTrue("Valid-C", validator.isValid("370000000000002"))
        self.assertTrue("Valid-D", validator.isValid("378734493671000"))

    def testArrayConstructor(self) -> None:
        ccv = CreditCardValidator(
            1,
            0,
            None,
            [CreditCardValidator.VISA_VALIDATOR, CreditCardValidator.AMEX_VALIDATOR],
        )

        self.assertTrue(ccv.isValid(self.__VALID_VISA))
        self.assertTrue(ccv.isValid(self.__VALID_SHORT_VISA))
        self.assertTrue(ccv.isValid(self.__VALID_AMEX))
        self.assertFalse(ccv.isValid(self.__VALID_MASTERCARD))
        self.assertFalse(ccv.isValid(self.__VALID_DISCOVER))

        self.assertFalse(ccv.isValid(self.__ERROR_VISA))
        self.assertFalse(ccv.isValid(self.__ERROR_SHORT_VISA))
        self.assertFalse(ccv.isValid(self.__ERROR_AMEX))
        self.assertFalse(ccv.isValid(self.__ERROR_MASTERCARD))
        self.assertFalse(ccv.isValid(self.__ERROR_DISCOVER))

        try:
            CreditCardValidator(1, 0, None, None)
            self.fail("Expected ValueError")
        except ValueError:
            pass

    def testAddAllowedCardType(self) -> None:
        ccv = CreditCardValidator(0, CreditCardValidator.NONE, None, None)
        self.assertFalse(ccv.isValid(self.__VALID_VISA))
        self.assertFalse(ccv.isValid(self.__VALID_AMEX))
        self.assertFalse(ccv.isValid(self.__VALID_MASTERCARD))
        self.assertFalse(ccv.isValid(self.__VALID_DISCOVER))
        self.assertFalse(ccv.isValid(self.__VALID_DINERS))

    def testIsValid(self) -> None:
        ccv = CreditCardValidator.CreditCardValidator0()

        self.assertIsNone(ccv.validate(None))

        self.assertFalse(ccv.isValid(None))
        self.assertFalse(ccv.isValid(""))
        self.assertFalse(ccv.isValid("123456789012"))  # too short
        self.assertFalse(ccv.isValid("12345678901234567890"))  # too long
        self.assertFalse(ccv.isValid("4417123456789112"))
        self.assertFalse(ccv.isValid("4417q23456w89113"))
        self.assertTrue(ccv.isValid(self.__VALID_VISA))
        self.assertTrue(ccv.isValid(self.__VALID_SHORT_VISA))
        self.assertTrue(ccv.isValid(self.__VALID_AMEX))
        self.assertTrue(ccv.isValid(self.__VALID_MASTERCARD))
        self.assertTrue(ccv.isValid(self.__VALID_DISCOVER))
        self.assertTrue(ccv.isValid(self.__VALID_DISCOVER65))

        self.assertFalse(ccv.isValid(self.__ERROR_VISA))
        self.assertFalse(ccv.isValid(self.__ERROR_SHORT_VISA))
        self.assertFalse(ccv.isValid(self.__ERROR_AMEX))
        self.assertFalse(ccv.isValid(self.__ERROR_MASTERCARD))
        self.assertFalse(ccv.isValid(self.__ERROR_DISCOVER))
        self.assertFalse(ccv.isValid(self.__ERROR_DISCOVER65))

        ccv = CreditCardValidator(0, CreditCardValidator.AMEX, None, None)
        self.assertFalse(ccv.isValid("4417123456789113"))

    def __init__(self, name: str) -> None:
        super().__init__(name)
