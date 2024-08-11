from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.validator.routines.checkdigit.IBANCheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigit import *
from src.main.org.apache.commons.validator.routines.IBANValidator import *
import unittest
import os
import typing
from typing import *
import io

# Imports End


class IBANValidatorTest(unittest.TestCase):

    # Class Fields Begin
    __invalidIBANFormat: typing.List[typing.List[str]] = None
    __VALIDATOR: IBANValidator = None
    __IBAN_PART: str = None
    __IBAN_PAT: re.Pattern = None
    __validIBANFormat: typing.List[typing.List[str]] = None
    # Class Fields End

    # Class Methods Begin
    def testSorted_test2_decomposed(self) -> None:
        pass

    def testSorted_test1_decomposed(self) -> None:
        pass

    def testSorted_test0_decomposed(self) -> None:
        pass

    def testSetValidatorLen_1_test1_decomposed(self) -> None:
        pass

    def testSetValidatorLen_1_test0_decomposed(self) -> None:
        pass

    def testSetValidatorLen35_test1_decomposed(self) -> None:
        pass

    def testSetValidatorLen35_test0_decomposed(self) -> None:
        pass

    def testSetValidatorLen7_test1_decomposed(self) -> None:
        pass

    def testSetValidatorLen7_test0_decomposed(self) -> None:
        pass

    def testSetValidatorLC_test1_decomposed(self) -> None:
        pass

    def testSetValidatorLC_test0_decomposed(self) -> None:
        pass

    def testSetDefaultValidator2_test0_decomposed(self) -> None:
        pass

    def testSetDefaultValidator1_test0_decomposed(self) -> None:
        pass

    def testGetValidator_test0_decomposed(self) -> None:
        pass

    def testHasValidator_test0_decomposed(self) -> None:
        pass

    def testNull_test0_decomposed(self) -> None:
        pass

    def testInValid_test0_decomposed(self) -> None:
        pass

    def testValid_test0_decomposed(self) -> None:
        pass

    @staticmethod
    def __fmtRE(iban_pat: str, iban_len: int) -> str:
        pass

    @staticmethod
    def __formatToRE(type_: str, len_: int) -> str:
        pass

    @staticmethod
    def __printEntry(ccode: str, length: str, ib: str, country: str) -> None:
        pass

    # Class Methods End
