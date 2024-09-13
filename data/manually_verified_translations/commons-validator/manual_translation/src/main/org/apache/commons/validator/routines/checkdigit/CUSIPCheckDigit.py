from __future__ import annotations
import re
import io
import typing
from typing import *
import os
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigitException import *
from src.main.org.apache.commons.validator.routines.checkdigit.ModulusCheckDigit import *


class CUSIPCheckDigit(ModulusCheckDigit):

    CUSIP_CHECK_DIGIT: CheckDigit = None
    __POSITION_WEIGHT: typing.List[int] = [2, 1]
    __serialVersionUID: int = 666941918490152456

    @staticmethod
    def initialize_fields() -> None:
        CUSIPCheckDigit.CUSIP_CHECK_DIGIT: CheckDigit = CUSIPCheckDigit()

    def _weightedValue(self, charValue: int, leftPos: int, rightPos: int) -> int:

        weight = self.__POSITION_WEIGHT[rightPos % 2]
        weightedValue = charValue * weight

        return self.sumDigits(weightedValue)

    def _toInt(self, character: str, leftPos: int, rightPos: int) -> int:

        if character.isdigit():
            charValue = int(character)
        elif character.isalpha():
            charValue = ord(character.lower()) - 87
        else:
            raise CheckDigitException.CheckDigitException1(
                "Invalid Character["
                + str(leftPos)
                + ","
                + str(rightPos)
                + "] = '"
                + str(character)
                + "' is not a digit or a letter"
            )

        charMax = 9 if rightPos == 1 else 35

        if charValue < 0 or charValue > charMax:
            raise CheckDigitException.CheckDigitException1(
                "Invalid Character["
                + str(leftPos)
                + ","
                + str(rightPos)
                + "] = '"
                + str(charValue)
                + "' out of range 0 to "
                + str(charMax)
            )

        return charValue

    def __init__(self) -> None:
        super().__init__(10)


CUSIPCheckDigit.initialize_fields()
