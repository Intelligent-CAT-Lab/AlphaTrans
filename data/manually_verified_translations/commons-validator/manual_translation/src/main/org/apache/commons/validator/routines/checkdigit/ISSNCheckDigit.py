from __future__ import annotations
import re
import io
import os
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigitException import *
from src.main.org.apache.commons.validator.routines.checkdigit.ModulusCheckDigit import *


class ISSNCheckDigit(ModulusCheckDigit):

    ISSN_CHECK_DIGIT: CheckDigit = None
    __serialVersionUID: int = 1

    @staticmethod
    def initialize_fields() -> None:
        ISSNCheckDigit.ISSN_CHECK_DIGIT: CheckDigit = ISSNCheckDigit()

    def _toInt(self, character: str, leftPos: int, rightPos: int) -> int:
        if rightPos == 1 and character == "X":
            return 10
        if character.isdigit():
            return int(character)
        raise CheckDigitException.CheckDigitException1(
            "Invalid Character[" + str(leftPos) + "] = '" + character + "'"
        )

    def _toCheckDigit(self, charValue: int) -> str:
        if charValue == 10:
            return "X"
        elif 0 <= charValue <= 9:
            return str(charValue)
        raise CheckDigitException.CheckDigitException1(
            "Invalid Check Digit Value =" + str(charValue)
        )

    def _weightedValue(self, charValue: int, leftPos: int, rightPos: int) -> int:
        return charValue * (9 - leftPos)

    def __init__(self) -> None:
        super().__init__(11)


ISSNCheckDigit.initialize_fields()
