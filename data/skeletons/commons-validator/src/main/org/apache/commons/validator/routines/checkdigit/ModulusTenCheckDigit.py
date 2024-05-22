from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.validator.routines.checkdigit.ModulusCheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigitException import *
import os
import typing
from typing import *
import io

# Imports End


class ModulusTenCheckDigit(ModulusCheckDigit):

    # Class Fields Begin
    __serialVersionUID: int = None
    __postitionWeight: typing.List[int] = None
    __useRightPos: bool = None
    __sumWeightedDigits: bool = None
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:
        pass

    def _weightedValue(self, charValue: int, leftPos: int, rightPos: int) -> int:
        pass

    def _toInt(self, character: str, leftPos: int, rightPos: int) -> int:
        pass

    def isValid(self, code: str) -> bool:
        pass

    @staticmethod
    def ModulusTenCheckDigit2(
        postitionWeight: typing.List[int],
    ) -> ModulusTenCheckDigit:
        pass

    @staticmethod
    def ModulusTenCheckDigit1(
        postitionWeight: typing.List[int], useRightPos: bool
    ) -> ModulusTenCheckDigit:
        pass

    def __init__(
        self,
        postitionWeight: typing.List[int],
        useRightPos: bool,
        sumWeightedDigits: bool,
    ) -> None:
        pass

    # Class Methods End
