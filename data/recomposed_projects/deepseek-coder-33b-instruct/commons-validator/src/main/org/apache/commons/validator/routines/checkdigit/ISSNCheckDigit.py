from __future__ import annotations
import io
import os
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigitException import *
from src.main.org.apache.commons.validator.routines.checkdigit.ModulusCheckDigit import *


class ISSNCheckDigit(ModulusCheckDigit):

    ISSN_CHECK_DIGIT: CheckDigit = ISSNCheckDigit()

    __serialVersionUID: int = 1

    def _toInt(self, character: str, leftPos: int, rightPos: int) -> int:

        if rightPos == 1 and character == "X":
            return 10
        else:
            return super()._toInt(character, leftPos, rightPos)

    def _toCheckDigit(self, charValue: int) -> str:

        if charValue == 10:
            return "X"
        else:
            return super()._toCheckDigit(charValue)

    def _weightedValue(self, charValue: int, leftPos: int, rightPos: int) -> int:

        return charValue * (9 - leftPos)

    def __init__(self) -> None:

        # Call the superclass constructor with the appropriate weighting factor
        super().__init__(11)
