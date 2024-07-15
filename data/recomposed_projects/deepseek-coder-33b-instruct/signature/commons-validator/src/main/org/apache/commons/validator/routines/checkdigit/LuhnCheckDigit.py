from __future__ import annotations
import re
import io
import typing
from typing import *
import os
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.ModulusCheckDigit import *


class LuhnCheckDigit(ModulusCheckDigit):

    LUHN_CHECK_DIGIT: CheckDigit = None
    __POSITION_WEIGHT: typing.List[int] = [2, 1]
    __serialVersionUID: int = -2976900113942875999

    @staticmethod
    def initialize_fields() -> None:
        LuhnCheckDigit.LUHN_CHECK_DIGIT: CheckDigit = LuhnCheckDigit()

    def _weightedValue(self, charValue: int, leftPos: int, rightPos: int) -> int:

        weight = self.__POSITION_WEIGHT[rightPos % 2]
        weightedValue = charValue * weight

        return weightedValue - 9 if weightedValue > 9 else weightedValue

    def __init__(self) -> None:
        super().__init__(10)


LuhnCheckDigit.initialize_fields()
