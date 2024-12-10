from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigitException import *
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigit import *

# from src.main.org.apache.commons.logging.LogFactory import *
# from src.main.org.apache.commons.logging.Log import *
import logging
import unittest
import typing
from typing import *
import io
from abc import ABC

# Imports End


class AbstractCheckDigitTest(unittest.TestCase, ABC):

    # Class Fields Begin
    __POSSIBLE_CHECK_DIGITS: str = None
    _log: logging.Logger = None
    _checkDigitLth: int = None
    _routine: CheckDigit = None
    _valid: typing.List[typing.List[str]] = None
    _invalid: typing.List[typing.List[str]] = None
    _zeroSum: str = None
    _missingMessage: str = None
    # Class Fields End

    # Class Methods Begin
    def tearDown(self) -> None:
        pass

    def _checkDigit(self, code: str) -> str:
        pass

    def _removeCheckDigit(self, code: str) -> str:
        pass

    def _createInvalidCodes(
        self, codes: typing.List[typing.List[str]]
    ) -> typing.List[typing.List[str]]:
        pass

    def testSerialization(self) -> None:
        pass

    def testZeroSum(self) -> None:
        pass

    def testMissingCode(self) -> None:
        pass

    def testCalculateInvalid(self) -> None:
        pass

    def testCalculateValid(self) -> None:
        pass

    def testIsValidFalse(self) -> None:
        pass

    def testIsValidTrue(self) -> None:
        pass

    def __init__(self, name: str) -> None:
        pass

    # Class Methods End
