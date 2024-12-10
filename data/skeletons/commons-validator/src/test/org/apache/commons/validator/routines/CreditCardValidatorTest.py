from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.validator.routines.checkdigit.LuhnCheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigit import *
from src.main.org.apache.commons.validator.routines.RegexValidator import *
from src.main.org.apache.commons.validator.routines.CreditCardValidator import *
from src.main.org.apache.commons.validator.routines.CodeValidator import *
from src.main.org.apache.commons.validator.CreditCardValidator import *
import unittest
import os
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
    __VALID_CARDS: typing.List[typing.List[str]] = None
    __ERROR_CARDS: typing.List[typing.List[str]] = None
    # Class Fields End

    # Class Methods Begin
    def testDisjointRange_test5_decomposed(self) -> None:
        pass

    def testDisjointRange_test4_decomposed(self) -> None:
        pass

    def testDisjointRange_test3_decomposed(self) -> None:
        pass

    def testDisjointRange_test2_decomposed(self) -> None:
        pass

    def testDisjointRange_test1_decomposed(self) -> None:
        pass

    def testDisjointRange_test0_decomposed(self) -> None:
        pass

    def testValidLength_test12_decomposed(self) -> None:
        pass

    def testValidLength_test11_decomposed(self) -> None:
        pass

    def testValidLength_test10_decomposed(self) -> None:
        pass

    def testValidLength_test9_decomposed(self) -> None:
        pass

    def testValidLength_test8_decomposed(self) -> None:
        pass

    def testValidLength_test7_decomposed(self) -> None:
        pass

    def testValidLength_test6_decomposed(self) -> None:
        pass

    def testValidLength_test5_decomposed(self) -> None:
        pass

    def testValidLength_test4_decomposed(self) -> None:
        pass

    def testValidLength_test3_decomposed(self) -> None:
        pass

    def testValidLength_test2_decomposed(self) -> None:
        pass

    def testValidLength_test1_decomposed(self) -> None:
        pass

    def testValidLength_test0_decomposed(self) -> None:
        pass

    def testRangeGenerator_test1_decomposed(self) -> None:
        pass

    def testRangeGenerator_test0_decomposed(self) -> None:
        pass

    def testRangeGeneratorNoLuhn_test1_decomposed(self) -> None:
        pass

    def testRangeGeneratorNoLuhn_test0_decomposed(self) -> None:
        pass

    def testGeneric_test1_decomposed(self) -> None:
        pass

    def testGeneric_test0_decomposed(self) -> None:
        pass

    def testMastercardUsingSeparators_test4_decomposed(self) -> None:
        pass

    def testMastercardUsingSeparators_test3_decomposed(self) -> None:
        pass

    def testMastercardUsingSeparators_test2_decomposed(self) -> None:
        pass

    def testMastercardUsingSeparators_test1_decomposed(self) -> None:
        pass

    def testMastercardUsingSeparators_test0_decomposed(self) -> None:
        pass

    def testVPayOption_test3_decomposed(self) -> None:
        pass

    def testVPayOption_test2_decomposed(self) -> None:
        pass

    def testVPayOption_test1_decomposed(self) -> None:
        pass

    def testVPayOption_test0_decomposed(self) -> None:
        pass

    def testVisaOption_test3_decomposed(self) -> None:
        pass

    def testVisaOption_test2_decomposed(self) -> None:
        pass

    def testVisaOption_test1_decomposed(self) -> None:
        pass

    def testVisaOption_test0_decomposed(self) -> None:
        pass

    def testVisaValidator_test3_decomposed(self) -> None:
        pass

    def testVisaValidator_test2_decomposed(self) -> None:
        pass

    def testVisaValidator_test1_decomposed(self) -> None:
        pass

    def testVisaValidator_test0_decomposed(self) -> None:
        pass

    def testMastercardOption_test3_decomposed(self) -> None:
        pass

    def testMastercardOption_test2_decomposed(self) -> None:
        pass

    def testMastercardOption_test1_decomposed(self) -> None:
        pass

    def testMastercardOption_test0_decomposed(self) -> None:
        pass

    def testMastercardValidator_test7_decomposed(self) -> None:
        pass

    def testMastercardValidator_test6_decomposed(self) -> None:
        pass

    def testMastercardValidator_test5_decomposed(self) -> None:
        pass

    def testMastercardValidator_test4_decomposed(self) -> None:
        pass

    def testMastercardValidator_test3_decomposed(self) -> None:
        pass

    def testMastercardValidator_test2_decomposed(self) -> None:
        pass

    def testMastercardValidator_test1_decomposed(self) -> None:
        pass

    def testMastercardValidator_test0_decomposed(self) -> None:
        pass

    def testDiscoverOption_test3_decomposed(self) -> None:
        pass

    def testDiscoverOption_test2_decomposed(self) -> None:
        pass

    def testDiscoverOption_test1_decomposed(self) -> None:
        pass

    def testDiscoverOption_test0_decomposed(self) -> None:
        pass

    def testDiscoverValidator_test3_decomposed(self) -> None:
        pass

    def testDiscoverValidator_test2_decomposed(self) -> None:
        pass

    def testDiscoverValidator_test1_decomposed(self) -> None:
        pass

    def testDiscoverValidator_test0_decomposed(self) -> None:
        pass

    def testDinersOption_test3_decomposed(self) -> None:
        pass

    def testDinersOption_test2_decomposed(self) -> None:
        pass

    def testDinersOption_test1_decomposed(self) -> None:
        pass

    def testDinersOption_test0_decomposed(self) -> None:
        pass

    def testDinersValidator_test3_decomposed(self) -> None:
        pass

    def testDinersValidator_test2_decomposed(self) -> None:
        pass

    def testDinersValidator_test1_decomposed(self) -> None:
        pass

    def testDinersValidator_test0_decomposed(self) -> None:
        pass

    def testAmexOption_test3_decomposed(self) -> None:
        pass

    def testAmexOption_test2_decomposed(self) -> None:
        pass

    def testAmexOption_test1_decomposed(self) -> None:
        pass

    def testAmexOption_test0_decomposed(self) -> None:
        pass

    def testAmexValidator_test3_decomposed(self) -> None:
        pass

    def testAmexValidator_test2_decomposed(self) -> None:
        pass

    def testAmexValidator_test1_decomposed(self) -> None:
        pass

    def testAmexValidator_test0_decomposed(self) -> None:
        pass

    def testArrayConstructor_test2_decomposed(self) -> None:
        pass

    def testArrayConstructor_test1_decomposed(self) -> None:
        pass

    def testArrayConstructor_test0_decomposed(self) -> None:
        pass

    def testAddAllowedCardType_test1_decomposed(self) -> None:
        pass

    def testAddAllowedCardType_test0_decomposed(self) -> None:
        pass

    def testIsValid_test4_decomposed(self) -> None:
        pass

    def testIsValid_test3_decomposed(self) -> None:
        pass

    def testIsValid_test2_decomposed(self) -> None:
        pass

    def testIsValid_test1_decomposed(self) -> None:
        pass

    def testIsValid_test0_decomposed(self) -> None:
        pass

    def __init__(self, name: str) -> None:
        pass

    # Class Methods End
