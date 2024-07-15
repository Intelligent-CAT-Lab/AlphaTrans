from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.validator.routines.AbstractNumberValidator import *
import typing
from typing import *
import numbers
import io

# Imports End


class BigIntegerValidator(AbstractNumberValidator):

    # Class Fields Begin
    __serialVersionUID: int = None
    __VALIDATOR: BigIntegerValidator = None
    # Class Fields End

    # Class Methods Begin
    def _processParsedValue(self, value: typing.Any, formatter: Format) -> typing.Any:
        pass

    def maxValue(self, value: int, max_: int) -> bool:
        pass

    def minValue(self, value: int, min_: int) -> bool:
        pass

    def isInRange(self, value: int, min_: int, max_: int) -> bool:
        pass

    def validate3(self, value: str, pattern: str, locale: typing.Any) -> int:
        pass

    def validate2(self, value: str, locale: typing.Any) -> int:
        pass

    def validate1(self, value: str, pattern: str) -> int:
        pass

    def validate0(self, value: str) -> int:
        pass

    @staticmethod
    def BigIntegerValidator1() -> BigIntegerValidator:
        pass

    def __init__(self, strict: bool, formatType: int) -> None:
        pass

    @staticmethod
    def getInstance() -> BigIntegerValidator:
        pass

    # Class Methods End
