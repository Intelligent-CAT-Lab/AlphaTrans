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


class IntegerValidator(AbstractNumberValidator):

    __VALIDATOR: IntegerValidator = None
    __serialVersionUID: int = 422081746310306596

    @staticmethod
    def initialize_fields() -> None:
        IntegerValidator.__VALIDATOR: IntegerValidator = (
            IntegerValidator.IntegerValidator1()
        )

    def _processParsedValue(
        self, value: typing.Any, formatter: typing.Union[str, datetime.datetime]
    ) -> typing.Any:
        if isinstance(value, numbers.Integral):
            longValue = value
            if longValue >= -2147483648 and longValue <= 2147483647:
                return int(longValue)
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

        pass  # LLM could not translate this method

    def validate2(self, value: str, locale: typing.Any) -> int:
        return self._parse(value, None, locale)

    def validate1(self, value: str, pattern: str) -> int:
        return self._parse(value, pattern, None)

    def validate0(self, value: str) -> int:
        return self._parse(value, None, None)

    @staticmethod
    def IntegerValidator1() -> IntegerValidator:
        return IntegerValidator(True, AbstractNumberValidator.STANDARD_FORMAT)

    def __init__(self, strict: bool, formatType: int) -> None:
        super().__init__(strict, formatType, False)

    @staticmethod
    def getInstance() -> IntegerValidator:
        return IntegerValidator.__VALIDATOR


IntegerValidator.initialize_fields()
