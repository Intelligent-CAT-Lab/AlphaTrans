from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.validator.routines.checkdigit.ModulusCheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigitException import *
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigit import *
import os
import io

# Imports End


class ISBN10CheckDigit(ModulusCheckDigit):

    # Class Fields Begin
    __serialVersionUID: int = None
    ISBN10_CHECK_DIGIT: CheckDigit = None
    # Class Fields End

    # Class Methods Begin
    def _toCheckDigit(self, charValue: int) -> str:
        pass

    def _toInt(self, character: str, leftPos: int, rightPos: int) -> int:
        pass

    def _weightedValue(self, charValue: int, leftPos: int, rightPos: int) -> int:
        pass

    def __init__(self) -> None:
        pass

    # Class Methods End
