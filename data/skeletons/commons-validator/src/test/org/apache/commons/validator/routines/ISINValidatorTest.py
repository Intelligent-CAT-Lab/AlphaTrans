from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.validator.routines.ISINValidator import *
import unittest
import typing
from typing import *
import io

# Imports End


class ISINValidatorTest(unittest.TestCase):

    # Class Fields Begin
    __VALIDATOR_TRUE: ISINValidator = None
    __VALIDATOR_FALSE: ISINValidator = None
    __validFormat: typing.List[str] = None
    __invalidFormat: typing.List[str] = None
    __invalidFormatTrue: typing.List[str] = None
    # Class Fields End

    # Class Methods Begin
    def testInvalidFalse(self) -> None:
        pass

    def testIsValidFalse(self) -> None:
        pass

    def testInvalidTrue(self) -> None:
        pass

    def testIsValidTrue(self) -> None:
        pass

    def __init__(self, name: str) -> None:
        pass

    # Class Methods End
