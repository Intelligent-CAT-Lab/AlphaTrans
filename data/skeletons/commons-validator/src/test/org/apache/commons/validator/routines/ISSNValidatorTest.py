from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.validator.routines.checkdigit.EAN13CheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigit import *
from src.main.org.apache.commons.validator.routines.ISSNValidator import *
import unittest
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
    def testIsValidExtract(self) -> None:
        pass

    def testValidCheckDigitEan13(self) -> None:
        pass

    def testConversionErrors(self) -> None:
        pass

    def testIsValidISSNConvert(self) -> None:
        pass

    def testIsValidISSNConvertSuffix(self) -> None:
        pass

    def testIsValidISSNConvertNull(self) -> None:
        pass

    def testInvalid(self) -> None:
        pass

    def testNull(self) -> None:
        pass

    def testIsValidISSN(self) -> None:
        pass

    def __init__(self, name: str) -> None:
        pass

    # Class Methods End
