from __future__ import annotations
import re
import io
import numbers
import typing
from typing import *
import os
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.ModulusCheckDigit import *


class ABANumberCheckDigit(ModulusCheckDigit):

    ABAN_CHECK_DIGIT: CheckDigit = None
    __POSITION_WEIGHT: typing.List[int] = [3, 1, 7]
    __serialVersionUID: int = -8255937433810380145

    @staticmethod
    def initialize_fields() -> None:
        ABANumberCheckDigit.ABAN_CHECK_DIGIT: CheckDigit = ABANumberCheckDigit()

    def _weightedValue(self, charValue: int, leftPos: int, rightPos: int) -> int:
        weight = self.__POSITION_WEIGHT[rightPos % 3]
        return charValue * weight

    def __init__(self) -> None:
        super().__init__(10)


ABANumberCheckDigit.initialize_fields()
