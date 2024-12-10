from __future__ import annotations
import re
import io
import os
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigitException import *
from src.main.org.apache.commons.validator.routines.checkdigit.ModulusCheckDigit import *


class ISBN10CheckDigit(ModulusCheckDigit):

    ISBN10_CHECK_DIGIT: CheckDigit = None
    __serialVersionUID: int = 8000855044504864964

    @staticmethod
    def initialize_fields() -> None:
        ISBN10CheckDigit.ISBN10_CHECK_DIGIT: CheckDigit = ISBN10CheckDigit()

    def _toCheckDigit(self, charValue: int) -> str:
        if charValue == 10:
            return "X"
        return super()._toCheckDigit(charValue)

    def _toInt(self, character: str, leftPos: int, rightPos: int) -> int:
        if rightPos == 1 and character == "X":
            return 10
        return super()._toInt(character, leftPos, rightPos)

    def _weightedValue(self, charValue: int, leftPos: int, rightPos: int) -> int:
        return charValue * rightPos

    def __init__(self) -> None:
        super().__init__(11)


ISBN10CheckDigit.initialize_fields()
