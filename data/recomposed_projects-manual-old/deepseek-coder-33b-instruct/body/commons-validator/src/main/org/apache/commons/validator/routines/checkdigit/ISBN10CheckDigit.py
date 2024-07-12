from __future__ import annotations
import re
import io
import os
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigitException import *
from src.main.org.apache.commons.validator.routines.checkdigit.ModulusCheckDigit import *


class ISBN10CheckDigit(ModulusCheckDigit):

    ISBN10_CHECK_DIGIT: CheckDigit = CheckDigit()
    __serialVersionUID: int = 8000855044504864964

    def _toCheckDigit(self, charValue: int) -> str:
        if charValue == 10:
            return "X"
        return super()._toCheckDigit(charValue)

    def _toInt(self, character: str, leftPos: int, rightPos: int) -> int:
        if rightPos == 1 and character == "X":
            return 10
        if character.isdigit():
            return int(character)
        raise CheckDigitException.CheckDigitException1(
            "Invalid Character[" + str(leftPos) + "] = '" + character + "'"
        )

    def _weightedValue(self, charValue: int, leftPos: int, rightPos: int) -> int:
        return charValue * rightPos

    def __init__(self) -> None:
        super().__init__(11)
