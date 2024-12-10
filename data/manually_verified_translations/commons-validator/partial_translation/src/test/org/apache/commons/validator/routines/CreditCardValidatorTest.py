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

        pass  # LLM could not translate this method

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

        pass  # LLM could not translate this method

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

        pass  # LLM could not translate this method

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

        pass  # LLM could not translate this method

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
