from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.validator.routines.checkdigit.ModulusCheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigit import *
import os
import typing
from typing import *
import io

# Imports End


class EAN13CheckDigit(ModulusCheckDigit):

    # Class Fields Begin
    __serialVersionUID: int = None
    EAN13_CHECK_DIGIT: CheckDigit = None
    __POSITION_WEIGHT: typing.List[int] = None
    # Class Fields End

    # Class Methods Begin
    def _weightedValue(self, charValue: int, leftPos: int, rightPos: int) -> int:
        pass

    def __init__(self) -> None:
        pass

    # Class Methods End
