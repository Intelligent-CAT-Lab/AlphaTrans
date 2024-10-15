from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.validator.routines.ISINValidator import *
import unittest
import os
import typing
from typing import *
import io

# Imports End


class ISINValidatorTest(unittest.TestCase):

    # Class Fields Begin
    __VALIDATOR_TRUE: ISINValidator = None
    __VALIDATOR_FALSE: ISINValidator = None
    __validFormat: typing.List[typing.List[str]] = None
    __invalidFormat: typing.List[typing.List[str]] = None
    __invalidFormatTrue: typing.List[typing.List[str]] = None
    # Class Fields End

    # Class Methods Begin
    def testInvalidFalse_test0_decomposed(self) -> None:
        pass

    def testIsValidFalse_test0_decomposed(self) -> None:
        pass

    def testInvalidTrue_test0_decomposed(self) -> None:
        pass

    def testIsValidTrue_test0_decomposed(self) -> None:
        pass

    def __init__(self, name: str) -> None:
        pass

    # Class Methods End
