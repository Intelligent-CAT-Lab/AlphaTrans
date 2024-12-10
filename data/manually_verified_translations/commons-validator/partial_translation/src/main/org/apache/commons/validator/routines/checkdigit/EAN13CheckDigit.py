from __future__ import annotations
import re
import io
import typing
from typing import *
import os
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.ModulusCheckDigit import *


class EAN13CheckDigit(ModulusCheckDigit):

    EAN13_CHECK_DIGIT: CheckDigit = None
    __POSITION_WEIGHT: typing.List[int] = [3, 1]
    __serialVersionUID: int = 1726347093230424107

    @staticmethod
    def initialize_fields() -> None:
        EAN13CheckDigit.EAN13_CHECK_DIGIT: CheckDigit = EAN13CheckDigit()

    def _weightedValue(self, charValue: int, leftPos: int, rightPos: int) -> int:
        weight = self.__POSITION_WEIGHT[rightPos % 2]
        return charValue * weight

    def __init__(self) -> None:
        super().__init__(10)


EAN13CheckDigit.initialize_fields()
