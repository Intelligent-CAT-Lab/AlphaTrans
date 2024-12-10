from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.validator.routines.AbstractNumberValidator import *
import typing
from typing import *
import numbers
import io

# Imports End


class DoubleValidator(AbstractNumberValidator):

    # Class Fields Begin
    __serialVersionUID: int = None
    __VALIDATOR: DoubleValidator = None
    # Class Fields End

    # Class Methods Begin
    def _processParsedValue(self, value: typing.Any, formatter: Format) -> typing.Any:
        pass

    def maxValue1(self, value: float, max_: float) -> bool:
        pass

    def maxValue0(self, value: float, max_: float) -> bool:
        pass

    def minValue1(self, value: float, min_: float) -> bool:
        pass

    def minValue0(self, value: float, min_: float) -> bool:
        pass

    def isInRange1(self, value: float, min_: float, max_: float) -> bool:
        pass

    def isInRange0(self, value: float, min_: float, max_: float) -> bool:
        pass

    def validate3(self, value: str, pattern: str, locale: typing.Any) -> float:
        pass

    def validate2(self, value: str, locale: typing.Any) -> float:
        pass

    def validate1(self, value: str, pattern: str) -> float:
        pass

    def validate0(self, value: str) -> float:
        pass

    @staticmethod
    def DoubleValidator1() -> DoubleValidator:
        pass

    def __init__(self, strict: bool, formatType: int) -> None:
        pass

    @staticmethod
    def getInstance() -> DoubleValidator:
        pass

    # Class Methods End
