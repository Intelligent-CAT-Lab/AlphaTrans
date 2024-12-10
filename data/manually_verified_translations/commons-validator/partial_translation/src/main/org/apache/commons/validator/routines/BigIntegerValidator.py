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

        value = value.strip() if value is not None else None
        if value is None or len(value) == 0:
            return None
        formatter = self._getFormat0(pattern, locale)
        return self._parse(value, formatter)

    def validate2(self, value: str, locale: typing.Any) -> int:

        value = value.strip() if value is not None else None
        if value is None or len(value) == 0:
            return None
        formatter = self._getFormat0(None, locale)
        return self._parse(value, formatter)

    def validate1(self, value: str, pattern: str) -> int:

        value = value.strip() if value is not None else None
        if value is None or len(value) == 0:
            return None
        formatter = self._getFormat0(pattern, None)
        return self._parse(value, formatter)

    def validate0(self, value: str) -> int:

        value = value.strip() if value is not None else None
        if value is None or len(value) == 0:
            return None
        formatter = self._getFormat0(None, None)
        return self._parse(value, formatter)

    @staticmethod
    def BigIntegerValidator1() -> BigIntegerValidator:
        return BigIntegerValidator(True, AbstractNumberValidator.STANDARD_FORMAT)

    def __init__(self, strict: bool, formatType: int) -> None:
        super().__init__(strict, formatType, False)

    @staticmethod
    def getInstance() -> BigIntegerValidator:
        return BigIntegerValidator.__VALIDATOR


BigIntegerValidator.initialize_fields()
