from __future__ import annotations
import re
import io
import typing
from typing import *
import os
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigitException import *
from src.main.org.apache.commons.validator.routines.checkdigit.ModulusCheckDigit import *


def get_numeric_value(c):
    if '0' <= c <= '9':
        return ord(c) - ord('0')
    
    elif 'A' <= c <= 'Z':
        return ord(c) - ord('A') + 10
    
    elif 'a' <= c <= 'z':
        return ord(c) - ord('a') + 10
    
    return -1

class ISINCheckDigit(ModulusCheckDigit):

    ISIN_CHECK_DIGIT: CheckDigit = None
    __POSITION_WEIGHT: typing.List[int] = [2, 1]
    __MAX_ALPHANUMERIC_VALUE: int = get_numeric_value("Z")
    __serialVersionUID: int = -1239211208101323599

    @staticmethod
    def initialize_fields() -> None:
        ISINCheckDigit.ISIN_CHECK_DIGIT: CheckDigit = ISINCheckDigit()

    def _weightedValue(self, charValue: int, leftPos: int, rightPos: int) -> int:

        weight = self.__POSITION_WEIGHT[rightPos % 2]
        weightedValue = charValue * weight

        return self.sumDigits(weightedValue)

    def _calculateModulus(self, code: str, includesCheckDigit: bool) -> int:
        transformed = ""
        if includesCheckDigit:
            checkDigit = code[-1]
            if not checkDigit.isdigit():
                raise CheckDigitException.CheckDigitException1(
                    "Invalid checkdigit[" + checkDigit + "] in " + code
                )
        for i in range(len(code)):
            charValue = get_numeric_value(code[i])
            if charValue < 0 or charValue > self.__MAX_ALPHANUMERIC_VALUE:
                raise CheckDigitException.CheckDigitException1(
                    "Invalid Character[" + str(i + 1) + "] = '" + str(charValue) + "'"
                )
            transformed += str(charValue)
        return super()._calculateModulus(transformed, includesCheckDigit)

    def __init__(self) -> None:
        super().__init__(10)


ISINCheckDigit.initialize_fields()
