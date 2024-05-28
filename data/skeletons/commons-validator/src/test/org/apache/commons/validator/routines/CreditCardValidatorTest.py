from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.validator.routines.checkdigit.LuhnCheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigit import *
from src.main.org.apache.commons.validator.routines.RegexValidator import *
from src.main.org.apache.commons.validator.routines.CreditCardValidator import *
from src.main.org.apache.commons.validator.routines.CodeValidator import *
from src.main.org.apache.commons.validator.CreditCardValidator import *
import unittest
import typing
from typing import *
import io

# Imports End


class CreditCardValidatorTest(unittest.TestCase):

    # Class Fields Begin
    __VALID_VISA: str = None
    __ERROR_VISA: str = None
    __VALID_SHORT_VISA: str = None
    __ERROR_SHORT_VISA: str = None
    __VALID_AMEX: str = None
    __ERROR_AMEX: str = None
    __VALID_MASTERCARD: str = None
    __ERROR_MASTERCARD: str = None
    __VALID_DISCOVER: str = None
    __ERROR_DISCOVER: str = None
    __VALID_DISCOVER65: str = None
    __ERROR_DISCOVER65: str = None
    __VALID_DINERS: str = None
    __ERROR_DINERS: str = None
    __VALID_VPAY: str = None
    __VALID_VPAY2: str = None
    __ERROR_VPAY: str = None
    __VALID_CARDS: typing.List[str] = None
    __ERROR_CARDS: typing.List[str] = None
    # Class Fields End

    # Class Methods Begin
    def testDisjointRange(self) -> None:
        pass

    def testValidLength(self) -> None:
        pass

    def testRangeGenerator(self) -> None:
        pass

    def testRangeGeneratorNoLuhn(self) -> None:
        pass

    def testGeneric(self) -> None:
        pass

    def testMastercardUsingSeparators(self) -> None:
        pass

    def testVPayOption(self) -> None:
        pass

    def testVisaOption(self) -> None:
        pass

    def testVisaValidator(self) -> None:
        pass

    def testMastercardOption(self) -> None:
        pass

    def testMastercardValidator(self) -> None:
        pass

    def testDiscoverOption(self) -> None:
        pass

    def testDiscoverValidator(self) -> None:
        pass

    def testDinersOption(self) -> None:
        pass

    def testDinersValidator(self) -> None:
        pass

    def testAmexOption(self) -> None:
        pass

    def testAmexValidator(self) -> None:
        pass

    def testArrayConstructor(self) -> None:
        pass

    def testAddAllowedCardType(self) -> None:
        pass

    def testIsValid(self) -> None:
        pass

    def __init__(self, name: str) -> None:
        pass

    # Class Methods End
