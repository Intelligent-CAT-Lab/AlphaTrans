from __future__ import annotations
import locale
import re
import io
import numbers
import typing
from typing import *
from src.main.org.apache.commons.validator.routines.AbstractNumberValidator import *


class BigIntegerValidator(AbstractNumberValidator):

    __VALIDATOR: BigIntegerValidator = None
    __serialVersionUID: int = 6713144356347139988

    @staticmethod
    def initialize_fields() -> None:
        BigIntegerValidator.__VALIDATOR: BigIntegerValidator = (
            BigIntegerValidator.BigIntegerValidator1()
        )

    def _processParsedValue(self, value: typing.Any, formatter: Format) -> typing.Any:

        if isinstance(value, numbers.Number):
            return int(value)
        else:
            raise TypeError("Value must be a number")

    def maxValue(self, value: int, max_: int) -> bool:
        return value <= max_

    def minValue(self, value: int, min_: int) -> bool:
        return value >= min_

    def isInRange(self, value: int, min_: int, max_: int) -> bool:
        return min_ <= value <= max_

    def validate3(self, value: str, pattern: str, locale: typing.Any) -> int:
        return self._parse(value, pattern, locale)

    def validate2(self, value: str, locale: typing.Any) -> int:
        return self._parse(value, None, locale)

    def validate1(self, value: str, pattern: str) -> int:
        return self._parse(value, pattern, None)

    def validate0(self, value: str) -> int:
        return self._parse(value, None, None)

    @staticmethod
    def BigIntegerValidator1() -> BigIntegerValidator:
        return BigIntegerValidator(True, AbstractNumberValidator.STANDARD_FORMAT)

    def __init__(self, strict: bool, formatType: int) -> None:
        super().__init__(strict, formatType, False)

    @staticmethod
    def getInstance() -> BigIntegerValidator:
        return BigIntegerValidator.__VALIDATOR
    
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


BigIntegerValidator.initialize_fields()
