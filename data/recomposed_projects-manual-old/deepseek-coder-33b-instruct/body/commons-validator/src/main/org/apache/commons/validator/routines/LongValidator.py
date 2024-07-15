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


class LongValidator(AbstractNumberValidator):

    __VALIDATOR: LongValidator = None
    __serialVersionUID: int = -5117231731027866098

    @staticmethod
    def initialize_fields() -> None:
        LongValidator.__VALIDATOR: LongValidator = LongValidator.LongValidator1()

    def _processParsedValue(
        self, value: typing.Any, formatter: typing.Union[str, datetime.datetime]
    ) -> typing.Any:

        if isinstance(value, int):
            return value
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
        return self.isInRange0(value, min, max)

    def isInRange0(self, value: int, min: int, max: int) -> bool:
        return value >= min and value <= max

    def validate3(self, value: str, pattern: str, locale: typing.Any) -> int:

        value = None if value is None else value.strip()
        if value is None or len(value) == 0:
            return None
        formatter = self._getFormat0(pattern, locale)
        return self._parse(value, formatter)

    def validate2(self, value: str, locale: typing.Any) -> int:

        formatter = self._getFormat0(None, locale)
        return self._parse(value, formatter)

    def validate1(self, value: str, pattern: str) -> int:

        formatter = self._getFormat0(pattern, None)
        parsed_value = self._parse(value, formatter)
        return parsed_value

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
