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

    __serialVersionUID: int = -8255937433810380145
    __POSITION_WEIGHT: List[int] = [3, 1, 7]

    def _weightedValue(self, charValue: int, leftPos: int, rightPos: int) -> int:

        weight = self.__POSITION_WEIGHT[rightPos % 3]
        return charValue * weight

    def __init__(self) -> None:

        super().__init__(10)
        self.__serialVersionUID = -8255937433810380145
