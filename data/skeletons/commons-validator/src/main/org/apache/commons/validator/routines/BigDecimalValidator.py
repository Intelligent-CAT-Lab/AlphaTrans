from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.validator.routines.AbstractNumberValidator import *
import decimal
import typing
from typing import *
import numbers
import io

# Imports End


class BigDecimalValidator(AbstractNumberValidator):

    # Class Fields Begin
    __serialVersionUID: int = None
    __VALIDATOR: BigDecimalValidator = None
    # Class Fields End

    # Class Methods Begin
    def _processParsedValue(self, value: typing.Any, formatter: Format) -> typing.Any:
        pass

    def maxValue(self, value: decimal.Decimal, max_: float) -> bool:
        pass

    def minValue(self, value: decimal.Decimal, min_: float) -> bool:
        pass

    def isInRange(self, value: decimal.Decimal, min_: float, max_: float) -> bool:
        pass

    def validate3(
        self, value: str, pattern: str, locale: typing.Any
    ) -> decimal.Decimal:
        pass

    def validate2(self, value: str, locale: typing.Any) -> decimal.Decimal:
        pass

    def validate1(self, value: str, pattern: str) -> decimal.Decimal:
        pass

    def validate0(self, value: str) -> decimal.Decimal:
        pass

    @staticmethod
    def BigDecimalValidator2() -> BigDecimalValidator:
        pass

    @staticmethod
    def BigDecimalValidator1(strict: bool) -> BigDecimalValidator:
        pass

    def __init__(self, strict: bool, formatType: int, allowFractions: bool) -> None:
        pass

    @staticmethod
    def getInstance() -> BigDecimalValidator:
        pass

    # Class Methods End
