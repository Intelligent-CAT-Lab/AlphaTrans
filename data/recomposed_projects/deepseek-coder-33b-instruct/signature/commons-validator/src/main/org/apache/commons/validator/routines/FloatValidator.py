from __future__ import annotations
import time
import locale
import re
import os
import io
import numbers
import typing
from typing import *
import datetime
from src.main.org.apache.commons.validator.routines.AbstractNumberValidator import *


class FloatValidator(AbstractNumberValidator):

    __VALIDATOR: FloatValidator = None
    __serialVersionUID: int = -4513245432806414267

    @staticmethod
    def initialize_fields() -> None:
        FloatValidator.__VALIDATOR: FloatValidator = FloatValidator.FloatValidator1()

    def _processParsedValue(
        self, value: typing.Any, formatter: typing.Union[str, datetime.datetime]
    ) -> typing.Any:

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

    def maxValue1(self, value: float, max: float) -> bool:
        return self.maxValue0(value, max)

    def maxValue0(self, value: float, max: float) -> bool:
        return value <= max

    def minValue1(self, value: float, min: float) -> bool:
        return self.minValue0(value, min)

    def minValue0(self, value: float, min: float) -> bool:
        return value >= min

    def isInRange1(self, value: float, min: float, max: float) -> bool:
        return self.isInRange0(value, min, max)

    def isInRange0(self, value: float, min: float, max: float) -> bool:
        return value >= min and value <= max

    def validate3(self, value: str, pattern: str, locale: typing.Any) -> float:
        return float(self._parse(value, pattern, locale))

    def validate2(self, value: str, locale: typing.Any) -> float:
        return float(self._parse(value, None, locale))

    def validate1(self, value: str, pattern: str) -> float:
        return self._parse(value, pattern, None)

    def validate0(self, value: str) -> float:
        return self._parse(value, None, None)

    @staticmethod
    def FloatValidator1() -> FloatValidator:
        return FloatValidator(True, FloatValidator.STANDARD_FORMAT)

    def __init__(self, strict: bool, formatType: int) -> None:
        super().__init__(strict, formatType, True)

    @staticmethod
    def getInstance() -> FloatValidator:
        return FloatValidator.__VALIDATOR


FloatValidator.initialize_fields()
