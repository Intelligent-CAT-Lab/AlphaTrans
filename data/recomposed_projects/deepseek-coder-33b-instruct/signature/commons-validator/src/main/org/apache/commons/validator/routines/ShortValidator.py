from __future__ import annotations
import time
import locale
import re
import io
import numbers
import typing
from typing import *
import datetime
from src.main.org.apache.commons.validator.routines.AbstractNumberValidator import *


class ShortValidator(AbstractNumberValidator):

    __VALIDATOR: ShortValidator = None
    __serialVersionUID: int = -5227510699747787066

    @staticmethod
    def initialize_fields() -> None:
        ShortValidator.__VALIDATOR: ShortValidator = ShortValidator.ShortValidator1()

    def _processParsedValue(
        self, value: typing.Any, formatter: typing.Union[str, datetime.datetime]
    ) -> typing.Any:

        long_value = value.value

        if long_value < -32768 or long_value > 32767:
            return None
        return short(long_value)

    def maxValue1(self, value: int, max: int) -> bool:
        return self.maxValue0(value, max)

    def maxValue0(self, value: int, max: int) -> bool:
        return value <= max

    def minValue1(self, value: int, min: int) -> bool:
        return self.minValue0(value, min)

    def minValue0(self, value: int, min: int) -> bool:
        return value >= min

    def isInRange1(self, value: int, min: int, max: int) -> bool:

        if value is None:
            return False
        if value < min or value > max:
            return False
        return True

    def isInRange0(self, value: int, min: int, max: int) -> bool:
        return value >= min and value <= max

    def validate3(self, value: str, pattern: str, locale: typing.Any) -> int:
        return int(self._parse(value, pattern, locale))

    def validate2(self, value: str, locale: typing.Any) -> int:
        return self._parse(value, None, locale)

    def validate1(self, value: str, pattern: str) -> int:
        return self._parse(value, pattern, None)

    def validate0(self, value: str) -> int:
        return self._parse(value, None, None)

    @staticmethod
    def ShortValidator1() -> ShortValidator:
        return ShortValidator(True, ShortValidator.STANDARD_FORMAT)

    def __init__(self, strict: bool, formatType: int) -> None:
        super().__init__(strict, formatType, False)

    @staticmethod
    def getInstance() -> ShortValidator:
        return ShortValidator.__VALIDATOR


ShortValidator.initialize_fields()
