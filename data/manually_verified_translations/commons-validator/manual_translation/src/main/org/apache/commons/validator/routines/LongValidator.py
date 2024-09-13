from __future__ import annotations
import locale
import re
import io
import numbers
import typing
from typing import *
from src.main.org.apache.commons.validator.routines.AbstractNumberValidator import *


class LongValidator(AbstractNumberValidator):

    __VALIDATOR: LongValidator = None
    __serialVersionUID: int = -5117231731027866098

    @staticmethod
    def initialize_fields() -> None:
        LongValidator.__VALIDATOR: LongValidator = LongValidator.LongValidator1()

    def _processParsedValue(self, value: typing.Any, formatter: typing.Any) -> typing.Any:

        if value > -9223372036854775809 and value < 9223372036854775808:
            if value != int(value):
                if self.isStrict():
                    return None
                else:
                    return int(value)
            return value
        else:
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
    def LongValidator1() -> LongValidator:
        return LongValidator(True, LongValidator.STANDARD_FORMAT)

    def __init__(self, strict: bool, formatType: int) -> None:
        super().__init__(strict, formatType, False)

    @staticmethod
    def getInstance() -> LongValidator:
        return LongValidator.__VALIDATOR


LongValidator.initialize_fields()
