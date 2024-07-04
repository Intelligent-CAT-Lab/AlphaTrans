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


class ByteValidator(AbstractNumberValidator):

    __VALIDATOR: ByteValidator = None
    __serialVersionUID: int = 7001640945881854649

    @staticmethod
    def initialize_fields() -> None:
        ByteValidator.__VALIDATOR: ByteValidator = ByteValidator.ByteValidator1()

    def _processParsedValue(
        self, value: typing.Any, formatter: typing.Union[str, datetime.datetime]
    ) -> typing.Any:

        if isinstance(value, numbers.Integral):
            long_value = int(value)
            if long_value >= -128 and long_value <= 127:
                return long_value.to_bytes(1, "big", signed=True)[0]
        return None

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
        if min is None or max is None:
            raise ValueError("Min and max values must be provided")
        if min > max:
            raise ValueError("Min value must be less than or equal to max value")

        return min <= value <= max

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
    def ByteValidator1() -> ByteValidator:
        return ByteValidator(True, ByteValidator.STANDARD_FORMAT)

    def __init__(self, strict: bool, formatType: int) -> None:
        super().__init__(strict, formatType, False)

    @staticmethod
    def getInstance() -> ByteValidator:
        return ByteValidator.__VALIDATOR


ByteValidator.initialize_fields()
