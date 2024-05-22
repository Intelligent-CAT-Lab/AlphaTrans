from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigitException import *
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigit import *
import typing
from typing import *
import io

# Imports End


class VerhoeffCheckDigit(CheckDigit):

    # Class Fields Begin
    __serialVersionUID: int = None
    VERHOEFF_CHECK_DIGIT: CheckDigit = None
    __D_TABLE: typing.List[typing.List[int]] = None
    __P_TABLE: typing.List[typing.List[int]] = None
    __INV_TABLE: typing.List[int] = None
    # Class Fields End

    # Class Methods Begin
    def calculate(self, code: str) -> str:
        pass

    def isValid(self, code: str) -> bool:
        pass

    def __calculateChecksum(self, code: str, includesCheckDigit: bool) -> int:
        pass

    # Class Methods End
