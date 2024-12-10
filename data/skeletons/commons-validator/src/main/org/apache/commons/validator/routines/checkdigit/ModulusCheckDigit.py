from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigitException import *
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigit import *
import os
import io
from abc import ABC

# Imports End


class ModulusCheckDigit(CheckDigit, ABC):

    # Class Fields Begin
    __serialVersionUID: int = None
    __modulus: int = None
    # Class Fields End

    # Class Methods Begin
    def calculate(self, code: str) -> str:
        pass

    def isValid(self, code: str) -> bool:
        pass

    @staticmethod
    def sumDigits(number: int) -> int:
        pass

    def _toCheckDigit(self, charValue: int) -> str:
        pass

    def _toInt(self, character: str, leftPos: int, rightPos: int) -> int:
        pass

    def _calculateModulus(self, code: str, includesCheckDigit: bool) -> int:
        pass

    def getModulus(self) -> int:
        pass

    def __init__(self, modulus: int) -> None:
        pass

    def _weightedValue(self, charValue: int, leftPos: int, rightPos: int) -> int:
        pass

    # Class Methods End
