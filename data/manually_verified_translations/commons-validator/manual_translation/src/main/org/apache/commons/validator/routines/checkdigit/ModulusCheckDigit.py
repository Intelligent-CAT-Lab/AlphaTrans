from __future__ import annotations
import re
from abc import ABC
import io
import os
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigitException import *


def get_numeric_value(c):
    if '0' <= c <= '9':
        return ord(c) - ord('0')
    
    elif 'A' <= c <= 'Z':
        return ord(c) - ord('A') + 10
    
    elif 'a' <= c <= 'z':
        return ord(c) - ord('a') + 10
    
    return -1

class ModulusCheckDigit(CheckDigit, ABC):

    __modulus: int = 0

    __serialVersionUID: int = 2948962251251528941

    def calculate(self, code: str) -> str:
        if code is None or len(code) == 0:
            raise CheckDigitException.CheckDigitException1("Code is missing")
        modulusResult = self._calculateModulus(code, False)
        charValue = (self.__modulus - modulusResult) % self.__modulus
        return self._toCheckDigit(charValue)

    def isValid(self, code: str) -> bool:
        if code is None or len(code) == 0:
            return False
        try:
            modulusResult = self._calculateModulus(code, True)
            return modulusResult == 0
        except CheckDigitException:
            return False

    @staticmethod
    def sumDigits(number: int) -> int:

        total = 0
        todo = number

        while todo > 0:
            total += todo % 10
            todo = todo // 10

        return total

    def _toCheckDigit(self, charValue: int) -> str:
        if 0 <= charValue <= 9:
            return str(charValue)
        raise CheckDigitException.CheckDigitException1(
            "Invalid Check Digit Value =" + str(charValue)
        )

    def _toInt(self, character: str, leftPos: int, rightPos: int) -> int:
        if character.isdigit():
            return get_numeric_value(character)
        raise CheckDigitException.CheckDigitException1(
            "Invalid Character[" + str(leftPos) + "] = '" + character + "'"
        )

    def _calculateModulus(self, code: str, includesCheckDigit: bool) -> int:
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

    def getModulus(self) -> int:
        return self.__modulus

    def __init__(self, modulus: int) -> None:
        self.__modulus = modulus

    def _weightedValue(self, charValue: int, leftPos: int, rightPos: int) -> int:
        raise NotImplementedError("Subclass must implement abstract method")
