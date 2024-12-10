from __future__ import annotations
import locale
import re
import os
import io
import numbers
import typing
from typing import *
from src.main.org.apache.commons.validator.routines.AbstractNumberValidator import *


class FloatValidator(AbstractNumberValidator):

    __VALIDATOR: FloatValidator = None
    __serialVersionUID: int = -4513245432806414267

    @staticmethod
    def initialize_fields() -> None:
        FloatValidator.__VALIDATOR: FloatValidator = FloatValidator.FloatValidator1()

    def _processParsedValue(self, value: typing.Any, formatter: Format) -> typing.Any:

        doubleValue = float(value)

        if doubleValue > 0:
            if doubleValue < float("-inf"):
                return None
            if doubleValue > float("inf"):
                return None
        elif doubleValue < 0:
            posDouble = doubleValue * -1
            if posDouble < float("-inf"):
                return None
            if posDouble > float("inf"):
                return None

        return float(doubleValue)

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

        value = value.strip() if value is not None else None
        if value is None or len(value) == 0:
            return None
        formatter = self._getFormat0(pattern, locale)
        return float(self._parse(value, formatter))

    def validate2(self, value: str, locale: typing.Any) -> float:

        value = value.strip() if value is not None else None
        if value is None or len(value) == 0:
            return None
        formatter = self._getFormat0(None, locale)
        return self._parse(value, formatter)

    def validate1(self, value: str, pattern: str) -> float:

        value = value.strip() if value is not None else None
        if value is None or len(value) == 0:
            return None
        formatter = self._getFormat0(pattern, None)
        return self._parse(value, formatter)

    def validate0(self, value: str) -> float:

        value = value.strip() if value is not None else None
        if value is None or len(value) == 0:
            return None
        formatter = self._getFormat0(None, None)
        return self._parse(value, formatter)

    @staticmethod
    def FloatValidator1() -> FloatValidator:
        return FloatValidator(True, FloatValidator.STANDARD_FORMAT)

    def __init__(self, strict: bool, formatType: int) -> None:
        super().__init__(strict, formatType, True)

    @staticmethod
    def getInstance() -> FloatValidator:
        return FloatValidator.__VALIDATOR


FloatValidator.initialize_fields()
