from __future__ import annotations
import locale
import re
import io
import numbers
import typing
from typing import *
from src.main.org.apache.commons.validator.routines.AbstractNumberValidator import *


class ByteValidator(AbstractNumberValidator):

    __VALIDATOR: ByteValidator = None
    __serialVersionUID: int = 7001640945881854649

    @staticmethod
    def initialize_fields() -> None:
        ByteValidator.__VALIDATOR: ByteValidator = ByteValidator.ByteValidator1()

    def _processParsedValue(self, value: typing.Any, formatter: Format) -> typing.Any:

        if isinstance(value, numbers.Number):
            long_value = int(value)
            if long_value >= -128 and long_value <= 127:
                byte_representation = long_value.to_bytes(1, "big", signed=True)
                return int.from_bytes(byte_representation, "big", signed=True)
        return None

    def maxValue1(self, value: int, max_: int) -> bool:
        return self.maxValue0(value, max_)

    def maxValue0(self, value: int, max_: int) -> bool:
        return value <= max_

    def minValue1(self, value: int, min_: int) -> bool:
        return self.minValue0(value, min_)

    def minValue0(self, value: int, min_: int) -> bool:
        return value >= min_

    def isInRange1(self, value: int, min_: int, max_: int) -> bool:
        return self.isInRange0(value, min_, max_)

    def isInRange0(self, value: int, min_: int, max_: int) -> bool:
        return value >= min_ and value <= max_

    def validate3(self, value: str, pattern: str, locale: typing.Any) -> int:
        return self._parse(value, pattern, locale)

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

    def _parse(self, value: str, pattern: str, locale_: typing.Any) -> typing.Any:
        saved_locale = locale.getlocale()
        try:
            locale.setlocale(locale.LC_ALL, locale_)
            conv = locale.localeconv()
            decimalPoint = conv['decimal_point']
        finally:
            locale.setlocale(locale.LC_ALL, saved_locale)
        if value and (decimalPoint in value) and self.isStrict():
            return None
        return super()._parse(value, pattern, locale_)

    @staticmethod
    def getInstance() -> ByteValidator:
        return ByteValidator.__VALIDATOR


ByteValidator.initialize_fields()
