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


class BigIntegerValidator(AbstractNumberValidator):

    __VALIDATOR: BigIntegerValidator = None
    __serialVersionUID: int = 6713144356347139988

    @staticmethod
    def initialize_fields() -> None:
        BigIntegerValidator.__VALIDATOR: BigIntegerValidator = (
            BigIntegerValidator.BigIntegerValidator1()
        )

    def _processParsedValue(
        self, value: typing.Any, formatter: typing.Union[str, datetime.datetime]
    ) -> typing.Any:

        pass  # LLM could not translate this method

    def maxValue(self, value: int, max: int) -> bool:
        return value <= max

    def minValue(self, value: int, min: int) -> bool:
        return value >= min

    def isInRange(self, value: int, min: int, max: int) -> bool:
        return value >= min and value <= max

    def validate3(self, value: str, pattern: str, locale: typing.Any) -> int:
        return self._parse(value, pattern, locale)

    def validate2(self, value: str, locale: typing.Any) -> int:
        return self._parse(value, None, locale)

    def validate1(self, value: str, pattern: str) -> int:
        return self._parse(value, pattern, None)

    def validate0(self, value: str) -> int:

        pass  # LLM could not translate this method

    @staticmethod
    def BigIntegerValidator1() -> BigIntegerValidator:
        return BigIntegerValidator(True, STANDARD_FORMAT)

    def __init__(self, strict: bool, formatType: int) -> None:
        super().__init__(strict, formatType, False)

    @staticmethod
    def getInstance() -> BigIntegerValidator:
        return BigIntegerValidator.__VALIDATOR


BigIntegerValidator.initialize_fields()
