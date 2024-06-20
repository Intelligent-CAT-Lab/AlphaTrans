from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.validator.routines.checkdigit.IBANCheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigit import *
from src.main.org.apache.commons.validator.routines.IBANValidator import *
import unittest
import typing
from typing import *
import io

# Imports End


class IBANValidatorTest(unittest.TestCase):

    # Class Fields Begin
    __invalidIBANFormat: typing.List[str] = None
    __VALIDATOR: IBANValidator = None
    __IBAN_PART: str = None
    __IBAN_PAT: re.Pattern = None
    __validIBANFormat: typing.List[str] = None
    # Class Fields End

    # Class Methods Begin
    def testSorted(self) -> None:
        pass

    def testSetValidatorLen_1(self) -> None:
        pass

    def testSetValidatorLen35(self) -> None:
        pass

    def testSetValidatorLen7(self) -> None:
        pass

    def testSetValidatorLC(self) -> None:
        pass

    def testSetDefaultValidator2(self) -> None:
        pass

    def testSetDefaultValidator1(self) -> None:
        pass

    def testGetValidator(self) -> None:
        pass

    def testHasValidator(self) -> None:
        pass

    def testNull(self) -> None:
        pass

    def testInValid(self) -> None:
        pass

    def testValid(self) -> None:
        pass

    @staticmethod
    def __fmtRE(iban_pat: str, iban_len: int) -> str:
        pass

    @staticmethod
    def __formatToRE(type: str, len: int) -> str:
        pass

    @staticmethod
    def __printEntry(ccode: str, length: str, ib: str, country: str) -> None:
        pass

    # Class Methods End
