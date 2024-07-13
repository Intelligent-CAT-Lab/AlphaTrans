from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.validator.routines.checkdigit.IBANCheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigit import *
from src.test.org.apache.commons.validator.routines.checkdigit.AbstractCheckDigitTest import *
import typing
from typing import *
import io

# Imports End


class IBANCheckDigitTest(AbstractCheckDigitTest):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def _checkDigit(self, code: str) -> str:
        pass

    def _removeCheckDigit(self, code: str) -> str:
        pass

    def _createInvalidCodes(
        self, codes: typing.List[typing.List[str]]
    ) -> typing.List[typing.List[str]]:
        pass

    def testZeroSum(self) -> None:
        pass

    def _setUp(self) -> None:
        pass

    def testOther(self) -> None:
        pass

    def __init__(self, name: str) -> None:
        pass

    # Class Methods End
