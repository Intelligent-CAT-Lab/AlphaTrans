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
    __ERROR_CARDS: List[str] = [
        __ERROR_VISA,
        __ERROR_SHORT_VISA,
        __ERROR_AMEX,
        __ERROR_MASTERCARD,
        __ERROR_DISCOVER,
        __ERROR_DISCOVER65,
        __ERROR_DINERS,
        __ERROR_VPAY,
        "",
        "12345678901",  # too short (11)
        "12345678901234567890",  # too long (20)
        "4417123456789112",  # invalid check digit
    ]
    __VALID_CARDS: List[str] = [
        __VALID_VISA,
        __VALID_SHORT_VISA,
        __VALID_AMEX,
        __VALID_MASTERCARD,
        __VALID_DISCOVER,
        __VALID_DISCOVER65,
        __VALID_DINERS,
        __VALID_VPAY,
        __VALID_VPAY2,
        "60115564485789458",  # VALIDATOR-403
    ]

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

        self.assertTrue(
            CreditCardValidator.validLength(
                14, CreditCardRange(0, "", "", 14, 14, None)
            )
        )
        self.assertFalse(
            CreditCardValidator.validLength(
                15, CreditCardRange(0, "", "", 14, 14, None)
            )
        )
        self.assertFalse(
            CreditCardValidator.validLength(
                13, CreditCardRange(0, "", "", 14, 14, None)
            )
        )

        self.assertFalse(
            CreditCardValidator.validLength(
                14, CreditCardRange(0, "", "", 15, 17, None)
            )
        )
        self.assertTrue(
            CreditCardValidator.validLength(
                15, CreditCardRange(0, "", "", 15, 17, None)
            )
        )
        self.assertTrue(
            CreditCardValidator.validLength(
                16, CreditCardRange(0, "", "", 15, 17, None)
            )
        )
        self.assertTrue(
            CreditCardValidator.validLength(
                17, CreditCardRange(0, "", "", 15, 17, None)
            )
        )
        self.assertFalse(
            CreditCardValidator.validLength(
                18, CreditCardRange(0, "", "", 15, 17, None)
            )
        )

        self.assertFalse(
            CreditCardValidator.validLength(
                14, CreditCardRange(1, "", "", 0, 0, [15, 17])
            )
        )
        self.assertTrue(
            CreditCardValidator.validLength(
                15, CreditCardRange(1, "", "", 0, 0, [15, 17])
            )
        )
        self.assertFalse(
            CreditCardValidator.validLength(
                16, CreditCardRange(1, "", "", 0, 0, [15, 17])
            )
        )
        self.assertTrue(
            CreditCardValidator.validLength(
                17, CreditCardRange(1, "", "", 0, 0, [15, 17])
            )
        )
        self.assertFalse(
            CreditCardValidator.validLength(
                18, CreditCardRange(1, "", "", 0, 0, [15, 17])
            )
        )

    def testRangeGenerator(self) -> None:

        ccv = CreditCardValidator(
            3,
            0,
            [
                CreditCardRange(0, "300", "305", 14, 14, None),  # Diners
                CreditCardRange(0, "3095", None, 14, 14, None),  # Diners
                CreditCardRange(0, "36", None, 14, 14, None),  # Diners
                CreditCardRange(0, "38", "39", 14, 14, None),  # Diners
            ],
            [
                CreditCardValidator.AMEX_VALIDATOR,
                CreditCardValidator.VISA_VALIDATOR,
                CreditCardValidator.MASTERCARD_VALIDATOR,
                CreditCardValidator.DISCOVER_VALIDATOR,
            ],
        )

        for s in self.__VALID_CARDS:
            self.assertTrue(ccv.isValid(s))

        for s in self.__ERROR_CARDS:
            self.assertFalse(ccv.isValid(s))

    def testRangeGeneratorNoLuhn(self) -> None:

        cv = CreditCardValidator.createRangeValidator(
            [
                CreditCardRange(0, "1", None, 6, 7, None),
                CreditCardRange(0, "644", "65", 8, 8, None)
            ],
            None
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

        ccv = CreditCardValidator.genericCreditCardValidator2()
        for s in self.__VALID_CARDS:
            self.assertTrue(ccv.isValid(s))
        for s in self.__ERROR_CARDS:
            self.assertFalse(ccv.isValid(s))

    def testMastercardUsingSeparators(self) -> None:

        MASTERCARD_REGEX_SEP = (
            "^(5[1-5]\\d{2})(?:[- ])?(\\d{4})(?:[- ])?(\\d{4})(?:[- ])?(\\d{4})$"
        )
        validator = CodeValidator.CodeValidator5(
            MASTERCARD_REGEX_SEP, LuhnCheckDigit.LUHN_CHECK_DIGIT
        )
        regex = validator.getRegexValidator()

        self.assertEqual(
            "5134567890123456", regex.validate("5134567890123456"), "Number"
        )
        self.assertEqual(
            "5134567890123456", regex.validate("5134-5678-9012-3456"), "Hyphen"
        )
        self.assertEqual(
            "5134567890123456", regex.validate("5134 5678 9012 3456"), "Space"
        )
        self.assertEqual(
            "5134567890123456", regex.validate("5134-5678 9012-3456"), "MixedA"
        )
        self.assertEqual(
            "5134567890123456", regex.validate("5134 5678-9012 3456"), "MixedB"
        )

        self.assertFalse(regex.isValid("5134.5678.9012.3456"), "Invalid Separator A")
        self.assertFalse(regex.isValid("5134_5678_9012_3456"), "Invalid Separator B")
        self.assertFalse(regex.isValid("513-45678-9012-3456"), "Invalid Grouping A")
        self.assertFalse(regex.isValid("5134-567-89012-3456"), "Invalid Grouping B")
        self.assertFalse(regex.isValid("5134-5678-901-23456"), "Invalid Grouping C")

        self.assertEqual(
            "5500000000000004", validator.validate("5500-0000-0000-0004"), "Valid-A"
        )
        self.assertEqual(
            "5424000000000015", validator.validate("5424 0000 0000 0015"), "Valid-B"
        )
        self.assertEqual(
            "5301250070000191", validator.validate("5301-250070000191"), "Valid-C"
        )
        self.assertEqual(
            "5123456789012346", validator.validate("5123456789012346"), "Valid-D"
        )

    def testVPayOption(self) -> None:

        validator = CreditCardValidator(0, CreditCardValidator.VPAY, None, None)

        self.assertTrue(validator.isValid(self.__VALID_VPAY))
        self.assertTrue(validator.isValid(self.__VALID_VPAY2))
        self.assertFalse(validator.isValid(self.__ERROR_VPAY))
        self.assertEqual(self.__VALID_VPAY, validator.validate(self.__VALID_VPAY))
        self.assertEqual(self.__VALID_VPAY2, validator.validate(self.__VALID_VPAY2))

        self.assertFalse(validator.isValid(self.__VALID_AMEX))
        self.assertFalse(validator.isValid(self.__VALID_DINERS))
        self.assertFalse(validator.isValid(self.__VALID_DISCOVER))
        self.assertFalse(validator.isValid(self.__VALID_MASTERCARD))
        self.assertTrue(validator.isValid(self.__VALID_VISA))
        self.assertTrue(validator.isValid(self.__VALID_SHORT_VISA))

    def testVisaOption(self) -> None:

        validator = CreditCardValidator(0, CreditCardValidator.VISA, None, None)

        self.assertFalse(validator.isValid(self.__ERROR_VISA))
        self.assertFalse(validator.isValid(self.__ERROR_SHORT_VISA))
        self.assertIsNone(validator.validate(self.__ERROR_VISA))
        self.assertEqual(self.__VALID_VISA, validator.validate(self.__VALID_VISA))
        self.assertEqual(
            self.__VALID_SHORT_VISA, validator.validate(self.__VALID_SHORT_VISA)
        )

        self.assertFalse(validator.isValid(self.__VALID_AMEX))
        self.assertFalse(validator.isValid(self.__VALID_DINERS))
        self.assertFalse(validator.isValid(self.__VALID_DISCOVER))
        self.assertFalse(validator.isValid(self.__VALID_MASTERCARD))
        self.assertTrue(validator.isValid(self.__VALID_VISA))
        self.assertTrue(validator.isValid(self.__VALID_SHORT_VISA))

    def testVisaValidator(self) -> None:

        validator = CreditCardValidator.VISA_VALIDATOR
        regex = validator.getRegexValidator()

        self.assertFalse(regex.isValid("423456789012"), "Length 12")
        self.assertTrue(regex.isValid("4234567890123"), "Length 13")
        self.assertFalse(regex.isValid("42345678901234"), "Length 14")
        self.assertFalse(regex.isValid("423456789012345"), "Length 15")
        self.assertTrue(regex.isValid("4234567890123456"), "Length 16")
        self.assertFalse(regex.isValid("42345678901234567"), "Length 17")
        self.assertFalse(regex.isValid("423456789012345678"), "Length 18")
        self.assertFalse(regex.isValid("3234567890123"), "Invalid Pref-A")
        self.assertFalse(regex.isValid("3234567890123456"), "Invalid Pref-B")
        self.assertFalse(regex.isValid("4234567x90123"), "Invalid Char-A")
        self.assertFalse(regex.isValid("4234567x90123456"), "Invalid Char-B")

        self.assertTrue(regex.isValid(CreditCardValidatorTest.__ERROR_VISA), "Valid regex")
        self.assertTrue(
            regex.isValid(CreditCardValidatorTest.__ERROR_SHORT_VISA),
            "Valid regex-S"
        )
        self.assertFalse(validator.isValid(CreditCardValidatorTest.__ERROR_VISA), "Invalid")
        self.assertFalse(
            validator.isValid(CreditCardValidatorTest.__ERROR_SHORT_VISA),
            "Invalid-S"
        )
        self.assertIsNone(
            validator.validate(CreditCardValidatorTest.__ERROR_VISA),
            "validate()"
        )
        self.assertEqual(
            validator.validate(CreditCardValidatorTest.__VALID_VISA),
            CreditCardValidatorTest.__VALID_VISA
        )
        self.assertEqual(
            validator.validate(CreditCardValidatorTest.__VALID_SHORT_VISA),
            CreditCardValidatorTest.__VALID_SHORT_VISA
        )

        self.assertFalse(validator.isValid(CreditCardValidatorTest.__VALID_AMEX), "Amex")
        self.assertFalse(validator.isValid(CreditCardValidatorTest.__VALID_DINERS), "Diners")
        self.assertFalse(
            validator.isValid(CreditCardValidatorTest.__VALID_DISCOVER),
            "Discover"
        )
        self.assertFalse(
            validator.isValid(CreditCardValidatorTest.__VALID_MASTERCARD),
            "Mastercard"
        )
        self.assertTrue(validator.isValid(CreditCardValidatorTest.__VALID_VISA), "Visa")
        self.assertTrue(
            validator.isValid(CreditCardValidatorTest.__VALID_SHORT_VISA),
            "Visa Short"
        )

        self.assertTrue(validator.isValid("4111111111111111"), "Valid-A")
        self.assertTrue(validator.isValid("4543059999999982"), "Valid-C")
        self.assertTrue(validator.isValid("4462000000000003"), "Valid-B")
        self.assertTrue(validator.isValid("4508750000000009"), "Valid-D")  # Electron
        self.assertTrue(validator.isValid("4012888888881881"), "Valid-E")

    def testMastercardOption(self) -> None:

        validator = CreditCardValidator(0, CreditCardValidator.MASTERCARD, None, None)
        self.assertFalse(validator.isValid(self.__ERROR_MASTERCARD))
        self.assertIsNone(validator.validate(self.__ERROR_MASTERCARD))
        self.assertEqual(
            self.__VALID_MASTERCARD, validator.validate(self.__VALID_MASTERCARD)
        )

        self.assertFalse(validator.isValid(self.__VALID_AMEX))
        self.assertFalse(validator.isValid(self.__VALID_DINERS))
        self.assertFalse(validator.isValid(self.__VALID_DISCOVER))
        self.assertTrue(validator.isValid(self.__VALID_MASTERCARD))
        self.assertFalse(validator.isValid(self.__VALID_VISA))
        self.assertFalse(validator.isValid(self.__VALID_SHORT_VISA))

    def testMastercardValidator(self) -> None:

        validator = CreditCardValidator.MASTERCARD_VALIDATOR
        regex = validator.getRegexValidator()

        self.assertFalse(regex.isValid("513456789012"))
        self.assertFalse(regex.isValid("5134567890123"))
        self.assertFalse(regex.isValid("51345678901234"))
        self.assertFalse(regex.isValid("513456789012345"))
        self.assertTrue(regex.isValid("5134567890123456"))
        self.assertFalse(regex.isValid("51345678901234567"))
        self.assertFalse(regex.isValid("513456789012345678"))
        self.assertFalse(regex.isValid("4134567890123456"))
        self.assertFalse(regex.isValid("5034567890123456"))
        self.assertTrue(regex.isValid("5134567890123456"))
        self.assertTrue(regex.isValid("5234567890123456"))
        self.assertTrue(regex.isValid("5334567890123456"))
        self.assertTrue(regex.isValid("5434567890123456"))
        self.assertTrue(regex.isValid("5534567890123456"))
        self.assertFalse(regex.isValid("5634567890123456"))
        self.assertFalse(regex.isValid("6134567890123456"))
        self.assertFalse(regex.isValid("5134567x90123456"))

        self.assertTrue(regex.isValid(self.__ERROR_MASTERCARD))
        self.assertFalse(validator.isValid(self.__ERROR_MASTERCARD))
        self.assertIsNone(validator.validate(self.__ERROR_MASTERCARD))
        self.assertEqual(
            self.__VALID_MASTERCARD, validator.validate(self.__VALID_MASTERCARD)
        )

        self.assertFalse(validator.isValid(self.__VALID_AMEX))
        self.assertFalse(validator.isValid(self.__VALID_DINERS))
        self.assertFalse(validator.isValid(self.__VALID_DISCOVER))
        self.assertTrue(validator.isValid(self.__VALID_MASTERCARD))
        self.assertFalse(validator.isValid(self.__VALID_VISA))
        self.assertFalse(validator.isValid(self.__VALID_SHORT_VISA))

        self.assertTrue(validator.isValid("5500000000000004"))
        self.assertTrue(validator.isValid("5424000000000015"))
        self.assertTrue(validator.isValid("5301250070000191"))
        self.assertTrue(validator.isValid("5123456789012346"))
        self.assertTrue(validator.isValid("5555555555554444"))

        rev = validator.getRegexValidator()
        PAD = "0000000000"
        self.assertFalse(rev.isValid("222099" + PAD))
        for i in range(222100, 272100):
            j = str(i) + PAD
            self.assertTrue(rev.isValid(j))
        self.assertFalse(rev.isValid("272100" + PAD))

    def testDiscoverOption(self) -> None:

        validator = CreditCardValidator(0, CreditCardValidator.DISCOVER, None, None)

        self.assertFalse(validator.isValid(self.__ERROR_DISCOVER))
        self.assertFalse(validator.isValid(self.__ERROR_DISCOVER65))
        self.assertIsNone(validator.validate(self.__ERROR_DISCOVER))
        self.assertEqual(
            self.__VALID_DISCOVER, validator.validate(self.__VALID_DISCOVER)
        )
        self.assertEqual(
            self.__VALID_DISCOVER65, validator.validate(self.__VALID_DISCOVER65)
        )

        self.assertFalse(validator.isValid(self.__VALID_AMEX))
        self.assertFalse(validator.isValid(self.__VALID_DINERS))
        self.assertTrue(validator.isValid(self.__VALID_DISCOVER))
        self.assertTrue(validator.isValid(self.__VALID_DISCOVER65))
        self.assertFalse(validator.isValid(self.__VALID_MASTERCARD))
        self.assertFalse(validator.isValid(self.__VALID_VISA))
        self.assertFalse(validator.isValid(self.__VALID_SHORT_VISA))

    def testDiscoverValidator(self) -> None:

        validator = CreditCardValidator.DISCOVER_VALIDATOR
        regex = validator.getRegexValidator()

        self.assertFalse(regex.isValid("601156789012"), "Length 12-6011")
        self.assertFalse(regex.isValid("653456789012"), "Length 12-65")
        self.assertFalse(regex.isValid("6011567890123"), "Length 13-6011")
        self.assertFalse(regex.isValid("6534567890123"), "Length 13-65")
        self.assertFalse(regex.isValid("60115678901234"), "Length 14-6011")
        self.assertFalse(regex.isValid("65345678901234"), "Length 14-65")
        self.assertFalse(regex.isValid("601156789012345"), "Length 15-6011")
        self.assertFalse(regex.isValid("653456789012345"), "Length 15-65")
        self.assertTrue(regex.isValid("6011567890123456"), "Length 16-6011")
        self.assertTrue(regex.isValid("6444567890123456"), "Length 16-644")
        self.assertTrue(regex.isValid("6484567890123456"), "Length 16-648")
        self.assertTrue(regex.isValid("6534567890123456"), "Length 16-65")
        self.assertFalse(regex.isValid("65345678901234567"), "Length 17-65")
        self.assertFalse(regex.isValid("601156789012345678"), "Length 18-6011")
        self.assertFalse(regex.isValid("653456789012345678"), "Length 18-65")

        self.assertFalse(regex.isValid("6404567890123456"), "Prefix 640")
        self.assertFalse(regex.isValid("6414567890123456"), "Prefix 641")
        self.assertFalse(regex.isValid("6424567890123456"), "Prefix 642")
        self.assertFalse(regex.isValid("6434567890123456"), "Prefix 643")
        self.assertFalse(regex.isValid("6010567890123456"), "Prefix 6010")
        self.assertFalse(regex.isValid("6012567890123456"), "Prefix 6012")
        self.assertFalse(regex.isValid("6011567x90123456"), "Invalid Char")

        self.assertTrue(regex.isValid(CreditCardValidatorTest.__ERROR_DISCOVER), "Valid regex")
        self.assertTrue(
            regex.isValid(CreditCardValidatorTest.__ERROR_DISCOVER65),
            "Valid regex65"
        )
        self.assertFalse(validator.isValid(CreditCardValidatorTest.__ERROR_DISCOVER), "Invalid")
        self.assertFalse(
            validator.isValid(CreditCardValidatorTest.__ERROR_DISCOVER65),
            "Invalid65"
        )
        self.assertIsNone(
            validator.validate(CreditCardValidatorTest.__ERROR_DISCOVER),
            "validate()"
        )
        self.assertEqual(
            validator.validate(CreditCardValidatorTest.__VALID_DISCOVER),
            CreditCardValidatorTest.__VALID_DISCOVER
        )
        self.assertEqual(
            validator.validate(CreditCardValidatorTest.__VALID_DISCOVER65),
            CreditCardValidatorTest.__VALID_DISCOVER65
        )

        self.assertFalse(validator.isValid(CreditCardValidatorTest.__VALID_AMEX), "Amex")
        self.assertFalse(validator.isValid(CreditCardValidatorTest.__VALID_DINERS), "Diners")
        self.assertTrue(validator.isValid(CreditCardValidatorTest.__VALID_DISCOVER), "Discover")
        self.assertTrue(
            validator.isValid(CreditCardValidatorTest.__VALID_DISCOVER65),
            "Discover"
        )
        self.assertFalse(
            validator.isValid(CreditCardValidatorTest.__VALID_MASTERCARD),
            "Mastercard"
        )
        self.assertFalse(validator.isValid(CreditCardValidatorTest.__VALID_VISA), "Visa")
        self.assertFalse(
            validator.isValid(CreditCardValidatorTest.__VALID_SHORT_VISA),
            "Visa Short"
        )

        self.assertTrue(validator.isValid("6011111111111117"), "Valid-A")
        self.assertTrue(validator.isValid("6011000000000004"), "Valid-B")
        self.assertTrue(validator.isValid("6011000000000012"), "Valid-C")

    def testDinersOption(self) -> None:

        validator = CreditCardValidator(0, CreditCardValidator.DINERS, None, None)

        self.assertFalse(validator.isValid(self.__ERROR_DINERS))
        self.assertIsNone(validator.validate(self.__ERROR_DINERS))
        self.assertEqual(self.__VALID_DINERS, validator.validate(self.__VALID_DINERS))

        self.assertFalse(validator.isValid(self.__VALID_AMEX))
        self.assertTrue(validator.isValid(self.__VALID_DINERS))
        self.assertFalse(validator.isValid(self.__VALID_DISCOVER))
        self.assertFalse(validator.isValid(self.__VALID_MASTERCARD))
        self.assertFalse(validator.isValid(self.__VALID_VISA))
        self.assertFalse(validator.isValid(self.__VALID_SHORT_VISA))

    def testDinersValidator(self) -> None:

        validator = CreditCardValidator.DINERS_VALIDATOR
        regex = validator.getRegexValidator()

        self.assertFalse(regex.isValid("300456789012"), "Length 12-300")
        self.assertFalse(regex.isValid("363456789012"), "Length 12-36")
        self.assertFalse(regex.isValid("3004567890123"), "Length 13-300")
        self.assertFalse(regex.isValid("3634567890123"), "Length 13-36")
        self.assertTrue(regex.isValid("30045678901234"), "Length 14-300")
        self.assertTrue(regex.isValid("36345678901234"), "Length 14-36")
        self.assertFalse(regex.isValid("300456789012345"), "Length 15-300")
        self.assertFalse(regex.isValid("363456789012345"), "Length 15-36")
        self.assertFalse(regex.isValid("3004567890123456"), "Length 16-300")
        self.assertFalse(regex.isValid("3634567890123456"), "Length 16-36")
        self.assertFalse(regex.isValid("30045678901234567"), "Length 17-300")
        self.assertFalse(regex.isValid("36345678901234567"), "Length 17-36")
        self.assertFalse(regex.isValid("300456789012345678"), "Length 18-300")
        self.assertFalse(regex.isValid("363456789012345678"), "Length 18-36")

        self.assertTrue(regex.isValid("30045678901234"), "Prefix 300")
        self.assertTrue(regex.isValid("30145678901234"), "Prefix 301")
        self.assertTrue(regex.isValid("30245678901234"), "Prefix 302")
        self.assertTrue(regex.isValid("30345678901234"), "Prefix 303")
        self.assertTrue(regex.isValid("30445678901234"), "Prefix 304")
        self.assertTrue(regex.isValid("30545678901234"), "Prefix 305")
        self.assertFalse(regex.isValid("30645678901234"), "Prefix 306")
        self.assertFalse(regex.isValid("30945678901234"), "Prefix 3094")
        self.assertTrue(regex.isValid("30955678901234"), "Prefix 3095")
        self.assertFalse(regex.isValid("30965678901234"), "Prefix 3096")
        self.assertFalse(regex.isValid("35345678901234"), "Prefix 35")
        self.assertTrue(regex.isValid("36345678901234"), "Prefix 36")
        self.assertFalse(regex.isValid("37345678901234"), "Prefix 37")
        self.assertTrue(regex.isValid("38345678901234"), "Prefix 38")
        self.assertTrue(regex.isValid("39345678901234"), "Prefix 39")

        self.assertFalse(regex.isValid("3004567x901234"), "Invalid Char-A")
        self.assertFalse(regex.isValid("3634567x901234"), "Invalid Char-B")

        self.assertTrue(regex.isValid(CreditCardValidatorTest.__ERROR_DINERS), "Valid regex")
        self.assertFalse(validator.isValid(CreditCardValidatorTest.__ERROR_DINERS), "Invalid")
        self.assertIsNone(
            validator.validate(CreditCardValidatorTest.__ERROR_DINERS),
            "validate()"
        )
        self.assertEqual(
            validator.validate(CreditCardValidatorTest.__VALID_DINERS),
            CreditCardValidatorTest.__VALID_DINERS
        )

        self.assertFalse(validator.isValid(CreditCardValidatorTest.__VALID_AMEX), "Amex")
        self.assertTrue(validator.isValid(CreditCardValidatorTest.__VALID_DINERS), "Diners")
        self.assertFalse(
            validator.isValid(CreditCardValidatorTest.__VALID_DISCOVER),
            "Discover"
        )
        self.assertFalse(
            validator.isValid(CreditCardValidatorTest.__VALID_MASTERCARD),
            "Mastercard"
        )
        self.assertFalse(validator.isValid(CreditCardValidatorTest.__VALID_VISA), "Visa")
        self.assertFalse(
            validator.isValid(CreditCardValidatorTest.__VALID_SHORT_VISA),
            "Visa Short"
        )

        self.assertTrue(validator.isValid("30000000000004"), "Valid-A")
        self.assertTrue(validator.isValid("30123456789019"), "Valid-B")
        self.assertTrue(validator.isValid("36432685260294"), "Valid-C")

    def testAmexOption(self) -> None:

        validator = CreditCardValidator(0, CreditCardValidator.AMEX, None, None)

        self.assertFalse(validator.isValid(self.__ERROR_AMEX))
        self.assertIsNone(validator.validate(self.__ERROR_AMEX))
        self.assertEqual(self.__VALID_AMEX, validator.validate(self.__VALID_AMEX))

        self.assertTrue(validator.isValid(self.__VALID_AMEX))
        self.assertFalse(validator.isValid(self.__VALID_DINERS))
        self.assertFalse(validator.isValid(self.__VALID_DISCOVER))
        self.assertFalse(validator.isValid(self.__VALID_MASTERCARD))
        self.assertFalse(validator.isValid(self.__VALID_VISA))
        self.assertFalse(validator.isValid(self.__VALID_SHORT_VISA))

    def testAmexValidator(self) -> None:

        validator = CreditCardValidator.AMEX_VALIDATOR
        regex = validator.getRegexValidator()

        self.assertFalse(regex.isValid("343456789012"))
        self.assertFalse(regex.isValid("3434567890123"))
        self.assertFalse(regex.isValid("34345678901234"))
        self.assertTrue(regex.isValid("343456789012345"))
        self.assertFalse(regex.isValid("3434567890123456"))
        self.assertFalse(regex.isValid("34345678901234567"))
        self.assertFalse(regex.isValid("343456789012345678"))
        self.assertFalse(regex.isValid("333456789012345"))
        self.assertTrue(regex.isValid("343456789012345"))
        self.assertFalse(regex.isValid("353456789012345"))
        self.assertFalse(regex.isValid("363456789012345"))
        self.assertTrue(regex.isValid("373456789012345"))
        self.assertFalse(regex.isValid("383456789012345"))
        self.assertFalse(regex.isValid("413456789012345"))
        self.assertFalse(regex.isValid("3434567x9012345"))

        self.assertTrue(regex.isValid(self.__ERROR_AMEX))
        self.assertFalse(validator.isValid(self.__ERROR_AMEX))
        self.assertIsNone(validator.validate(self.__ERROR_AMEX))
        self.assertEqual(self.__VALID_AMEX, validator.validate(self.__VALID_AMEX))

        self.assertTrue(validator.isValid(self.__VALID_AMEX))
        self.assertFalse(validator.isValid(self.__VALID_DINERS))
        self.assertFalse(validator.isValid(self.__VALID_DISCOVER))
        self.assertFalse(validator.isValid(self.__VALID_MASTERCARD))
        self.assertFalse(validator.isValid(self.__VALID_VISA))
        self.assertFalse(validator.isValid(self.__VALID_SHORT_VISA))

        self.assertTrue(validator.isValid("371449635398431"))
        self.assertTrue(validator.isValid("340000000000009"))
        self.assertTrue(validator.isValid("370000000000002"))
        self.assertTrue(validator.isValid("378734493671000"))

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

        with self.assertRaises(ValueError):
            CreditCardValidator(1, 0, None, None)

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
        self.assertFalse(ccv.isValid("123456789012"))
        self.assertFalse(ccv.isValid("12345678901234567890"))
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
