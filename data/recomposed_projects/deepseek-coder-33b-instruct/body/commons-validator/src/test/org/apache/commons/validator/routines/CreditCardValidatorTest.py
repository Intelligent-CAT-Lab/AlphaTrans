from __future__ import annotations
import re
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
        "4417123456789112",  # ERROR_VISA
        "4222222222229",  # ERROR_SHORT_VISA
        "378282246310001",  # ERROR_AMEX
        "5105105105105105",  # ERROR_MASTERCARD
        "6011000990139421",  # ERROR_DISCOVER
        "6534567890123450",  # ERROR_DISCOVER65
        "30569309025901",  # ERROR_DINERS
        "4370000000000069",  # ERROR_VPAY
        "",
        "12345678901",  # too short (11)
        "12345678901234567890",  # too long (20)
        "4417123456789112",  # invalid check digit
    ]
    __VALID_CARDS: typing.List[str] = [
        "4417123456789113",  # VALID_VISA
        "4222222222222",  # VALID_SHORT_VISA
        "378282246310005",  # VALID_AMEX
        "5105105105105100",  # VALID_MASTERCARD
        "6011000990139424",  # VALID_DISCOVER
        "6534567890123458",  # VALID_DISCOVER65
        "30569309025904",  # VALID_DINERS
        "4370000000000012",  # VALID_VPAY
        "4370000000000061",  # VALID_VPAY2
        "60115564485789458",  # VALIDATOR-403
    ]
    __ERROR_VPAY: str = "4370000000000069"
    __VALID_VPAY2: str = "4370000000000012"
    __VALID_VPAY: str = "4370000000000061"
    __ERROR_DINERS: str = "30569309025901"
    __VALID_DINERS: str = "30569309025904"  # 14
    __ERROR_DISCOVER65: str = (
        "6534567890123450"  # FIXME need verified test data for Discover with "65" prefix
    )
    __VALID_DISCOVER65: str = (
        "6534567890123458"  # FIXME need verified test data for Discover with "65" prefix
    )
    __ERROR_DISCOVER: str = "6011000990139421"
    __VALID_DISCOVER: str = "6011000990139424"
    __ERROR_MASTERCARD: str = "5105105105105105"
    __VALID_MASTERCARD: str = "5105105105105100"
    __ERROR_AMEX: str = "378282246310001"
    __VALID_AMEX: str = "378282246310005"  # 15
    __ERROR_SHORT_VISA: str = "4222222222229"
    __VALID_SHORT_VISA: str = "4222222222222"  # 13
    __ERROR_VISA: str = "4417123456789112"
    __VALID_VISA: str = "4417123456789113"  # 16

    def testDisjointRange(self) -> None:

        ccv = CreditCardValidator(
            2, 0, [CreditCardRange(1, "305", "4", 0, 0, [13, 16])], None
        )
        self.assertEqual(len(self.__VALID_SHORT_VISA), 13)
        self.assertEqual(len(self.__VALID_VISA), 16)
        self.assertEqual(len(self.__VALID_DINERS), 14)
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

        pass  # LLM could not translate this method

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

        pass  # LLM could not translate this method

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

        pass  # LLM could not translate this method

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
