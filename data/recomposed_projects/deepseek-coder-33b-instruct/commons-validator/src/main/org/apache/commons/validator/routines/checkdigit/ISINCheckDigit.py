from __future__ import annotations
import io
import typing
from typing import *
import os
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigitException import *
from src.main.org.apache.commons.validator.routines.checkdigit.ModulusCheckDigit import *


class ISINCheckDigit(ModulusCheckDigit):

    ISIN_CHECK_DIGIT: CheckDigit = ISINCheckDigit()

    __POSITION_WEIGHT: typing.List[int] = [2, 1]

    __MAX_ALPHANUMERIC_VALUE: int = ord("Z")

    __serialVersionUID: int = -1239211208101323599

    def _weightedValue(self, charValue: int, leftPos: int, rightPos: int) -> int:

        weight = self._POSITION_WEIGHT[rightPos % 2]
        weightedValue = charValue * weight
        return self.sumDigits(weightedValue)

    def _calculateModulus(self, code: str, includesCheckDigit: bool) -> int:

        transformed = io.StringIO()
        if includesCheckDigit:
            checkDigit = code[-1]  # fetch the last character
            if not checkDigit.isdigit():
                raise CheckDigitException.CheckDigitException1(
                    "Invalid checkdigit[" + checkDigit + "] in " + code
                )

        for i in range(len(code)):
            charValue = ord(code[i])
            if charValue < 0 or charValue > self.__MAX_ALPHANUMERIC_VALUE:
                raise CheckDigitException.CheckDigitException1(
                    "Invalid Character[" + str(i + 1) + "] = '" + str(charValue) + "'"
                )
            transformed.write(str(charValue))

        return super()._calculateModulus(transformed.getvalue(), includesCheckDigit)

    def __init__(self) -> None:

        # Call the superclass constructor with the base number 10
        super(ModulusCheckDigit, self).__init__(10)
