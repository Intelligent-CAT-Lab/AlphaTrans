from __future__ import annotations
import re
import os
import io
import typing
from typing import *
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

class VerhoeffCheckDigit(CheckDigit):

    VERHOEFF_CHECK_DIGIT: CheckDigit = None
    __INV_TABLE: typing.List[int] = [0, 4, 3, 2, 1, 5, 6, 7, 8, 9]
    __P_TABLE: typing.List[typing.List[int]] = [
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 5, 7, 6, 2, 8, 3, 0, 9, 4],
        [5, 8, 0, 3, 7, 9, 6, 1, 4, 2],
        [8, 9, 1, 6, 0, 4, 3, 5, 2, 7],
        [9, 4, 5, 3, 1, 2, 6, 8, 7, 0],
        [4, 2, 8, 6, 5, 7, 3, 9, 0, 1],
        [2, 7, 9, 3, 8, 0, 6, 4, 1, 5],
        [7, 0, 4, 6, 9, 1, 3, 2, 5, 8],
    ]
    __D_TABLE: typing.List[typing.List[int]] = [
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 0, 6, 7, 8, 9, 5],
        [2, 3, 4, 0, 1, 7, 8, 9, 5, 6],
        [3, 4, 0, 1, 2, 8, 9, 5, 6, 7],
        [4, 0, 1, 2, 3, 9, 5, 6, 7, 8],
        [5, 9, 8, 7, 6, 0, 4, 3, 2, 1],
        [6, 5, 9, 8, 7, 1, 0, 4, 3, 2],
        [7, 6, 5, 9, 8, 2, 1, 0, 4, 3],
        [8, 7, 6, 5, 9, 3, 2, 1, 0, 4],
        [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],
    ]
    __serialVersionUID: int = 4138993995483695178

    @staticmethod
    def initialize_fields() -> None:
        VerhoeffCheckDigit.VERHOEFF_CHECK_DIGIT: CheckDigit = VerhoeffCheckDigit()

    def calculate(self, code: str) -> str:

        if code is None or len(code) == 0:
            raise CheckDigitException.CheckDigitException1("Code is missing")

        checksum = self.__calculateChecksum(code, False)
        return str(self.__INV_TABLE[checksum])

    def isValid(self, code: str) -> bool:

        if code is None or len(code) == 0:
            return False
        try:
            return self.__calculateChecksum(code, True) == 0
        except CheckDigitException:
            return False

    def __calculateChecksum(self, code: str, includesCheckDigit: bool) -> int:

        checksum = 0
        for i in range(len(code)):
            idx = len(code) - (i + 1)
            num = get_numeric_value(code[idx])
            if num < 0 or num > 9:
                raise CheckDigitException.CheckDigitException1(
                    "Invalid Character[" + str(i) + "] = '" + str(ord(code[idx])) + "'"
                )
            pos = i if includesCheckDigit else i + 1
            checksum = self.__D_TABLE[checksum][self.__P_TABLE[pos % 8][num]]
        return checksum


VerhoeffCheckDigit.initialize_fields()
