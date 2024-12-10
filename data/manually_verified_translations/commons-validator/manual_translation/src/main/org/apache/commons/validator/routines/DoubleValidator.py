from __future__ import annotations
import locale
import re
import io
import numbers
import typing
from typing import *
from src.main.org.apache.commons.validator.routines.AbstractNumberValidator import *


class DoubleValidator(AbstractNumberValidator):

    __VALIDATOR: DoubleValidator = None
    __serialVersionUID: int = 5867946581318211330

    @staticmethod
    def initialize_fields() -> None:
        DoubleValidator.__VALIDATOR: DoubleValidator = (
            DoubleValidator.DoubleValidator1()
        )

    def _processParsedValue(self, value: typing.Any, formatter: Format) -> typing.Any:

        if isinstance(value, float):
            return value
        elif isinstance(value, numbers.Number):
            return float(value)
        else:
            raise TypeError("Value must be a number")

    def maxValue1(self, value: float, max_: float) -> bool:
        return self.maxValue0(value, max_)

    def maxValue0(self, value: float, max_: float) -> bool:
        return value <= max_

    def minValue1(self, value: float, min_: float) -> bool:
        return self.minValue0(value, min_)

    def minValue0(self, value: float, min_: float) -> bool:
        return value >= min_

    def isInRange1(self, value: float, min_: float, max_: float) -> bool:
        return self.isInRange0(value, min_, max_)

    def isInRange0(self, value: float, min_: float, max_: float) -> bool:
        return value >= min_ and value <= max_

    def validate3(self, value: str, pattern: str, locale: typing.Any) -> float:

        return self._parse(value, pattern, locale)

    def validate2(self, value: str, locale: typing.Any) -> float:

        return self._parse(value, None, locale)

    def validate1(self, value: str, pattern: str) -> float:

        return self._parse(value, pattern, None)

    def validate0(self, value: str) -> float:

        return self._parse(value, None, None)

    @staticmethod
    def DoubleValidator1() -> DoubleValidator:
        return DoubleValidator(True, DoubleValidator.STANDARD_FORMAT)

    def __init__(self, strict: bool, formatType: int) -> None:
        super().__init__(strict, formatType, True)

    @staticmethod
    def getInstance() -> DoubleValidator:
        return DoubleValidator.__VALIDATOR


DoubleValidator.initialize_fields()
