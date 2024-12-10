from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.validator.routines.checkdigit.EAN13CheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigit import *
from src.main.org.apache.commons.validator.routines.ISSNValidator import *
import unittest
import os
import typing
from typing import *
import io

# Imports End


class ISSNValidatorTest(unittest.TestCase):

    # Class Fields Begin
    __VALIDATOR: ISSNValidator = None
    __validFormat: typing.List[typing.List[str]] = None
    __invalidFormat: typing.List[typing.List[str]] = None
    # Class Fields End

    # Class Methods Begin
    def testIsValidExtract_test0_decomposed(self) -> None:
        pass

    def testValidCheckDigitEan13_test0_decomposed(self) -> None:
        pass

    def testConversionErrors_test1_decomposed(self) -> None:
        pass

    def testConversionErrors_test0_decomposed(self) -> None:
        pass

    def testIsValidISSNConvert_test1_decomposed(self) -> None:
        pass

    def testIsValidISSNConvert_test0_decomposed(self) -> None:
        pass

    def testIsValidISSNConvertSuffix_test0_decomposed(self) -> None:
        pass

    def testIsValidISSNConvertNull_test0_decomposed(self) -> None:
        pass

    def testInvalid_test0_decomposed(self) -> None:
        pass

    def testNull_test0_decomposed(self) -> None:
        pass

    def testIsValidISSN_test0_decomposed(self) -> None:
        pass

    def __init__(self, name: str) -> None:
        pass

    # Class Methods End
