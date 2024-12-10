from __future__ import annotations
import re
import io
import typing
from typing import *
import os
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigitException import *
from src.main.org.apache.commons.validator.routines.checkdigit.ModulusCheckDigit import *


class SedolCheckDigit(ModulusCheckDigit):

    SEDOL_CHECK_DIGIT: CheckDigit = None
    __POSITION_WEIGHT: typing.List[int] = [1, 3, 1, 7, 3, 9, 1]
    __MAX_ALPHANUMERIC_VALUE: int = ord("Z")
    __serialVersionUID: int = -8976881621148878443

    @staticmethod
    def initialize_fields() -> None:
        SedolCheckDigit.SEDOL_CHECK_DIGIT: CheckDigit = SedolCheckDigit()

    def _toInt(self, character: str, leftPos: int, rightPos: int) -> int:

        charValue = ord(character)
        charMax = self.__MAX_ALPHANUMERIC_VALUE if rightPos == 1 else 9

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

    def _weightedValue(self, charValue: int, leftPos: int, rightPos: int) -> int:
        return charValue * self.__POSITION_WEIGHT[leftPos - 1]

    def _calculateModulus(self, code: str, includesCheckDigit: bool) -> int:
        if len(code) > len(self.__POSITION_WEIGHT):
            raise CheckDigitException.CheckDigitException1(
                "Invalid Code Length = " + str(len(code))
            )
        total = 0
        for i in range(len(code)):
            lth = len(code) + (0 if includesCheckDigit else 1)
            leftPos = i + 1
            rightPos = lth - i
            charValue = self._toInt(code[i], leftPos, rightPos)
            total += self._weightedValue(charValue, leftPos, rightPos)
        if total == 0:
            raise CheckDigitException.CheckDigitException1("Invalid code, sum is zero")
        return total % self.__modulus

    def __init__(self) -> None:
        super().__init__(10)


SedolCheckDigit.initialize_fields()
