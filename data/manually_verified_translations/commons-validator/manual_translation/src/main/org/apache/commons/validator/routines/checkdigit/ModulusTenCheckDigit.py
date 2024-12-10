from __future__ import annotations
import copy
import re
import io
import typing
from typing import *
import os
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

class ModulusTenCheckDigit(ModulusCheckDigit):

    __sumWeightedDigits: bool = False

    __useRightPos: bool = False

    __postitionWeight: typing.List[int] = None

    __serialVersionUID: int = -3752929983453368497

    def toString(self) -> str:
        return (
            self.__class__.__name__
            + "[postitionWeight="
            + str(self.__postitionWeight)
            + ", useRightPos="
            + str(self.__useRightPos)
            + ", sumWeightedDigits="
            + str(self.__sumWeightedDigits)
            + "]"
        )

    def _weightedValue(self, charValue: int, leftPos: int, rightPos: int) -> int:

        pos = rightPos if self.__useRightPos else leftPos
        weight = self.__postitionWeight[(pos - 1) % len(self.__postitionWeight)]
        weightedValue = charValue * weight

        if self.__sumWeightedDigits:
            weightedValue = ModulusCheckDigit.sumDigits(weightedValue)

        return weightedValue

    def _toInt(self, character: str, leftPos: int, rightPos: int) -> int:

        num = get_numeric_value(character)
        if num < 0:
            raise CheckDigitException.CheckDigitException1(
                "Invalid Character[" + str(leftPos) + "] = '" + character + "'"
            )

        return num

    def isValid(self, code: str) -> bool:
        if code is None or len(code) == 0:
            return False
        if not code[-1].isdigit():
            return False

        try:
            modulusResult = self._calculateModulus(code, True)
            return modulusResult == 0
        except CheckDigitException:
            return False

    @staticmethod
    def ModulusTenCheckDigit2(
        postitionWeight: typing.List[int],
    ) -> ModulusTenCheckDigit:
        return ModulusTenCheckDigit(postitionWeight, False, False)

    @staticmethod
    def ModulusTenCheckDigit1(
        postitionWeight: typing.List[int], useRightPos: bool
    ) -> ModulusTenCheckDigit:
        return ModulusTenCheckDigit(postitionWeight, useRightPos, False)

    def __init__(
        self,
        postitionWeight: typing.List[int],
        useRightPos: bool,
        sumWeightedDigits: bool,
    ) -> None:
        super().__init__(10)
        self.__postitionWeight = postitionWeight.copy()
        self.__useRightPos = useRightPos
        self.__sumWeightedDigits = sumWeightedDigits
