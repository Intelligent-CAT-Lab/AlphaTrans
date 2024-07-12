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


class DoubleValidator(AbstractNumberValidator):

    __VALIDATOR: DoubleValidator = None
    __serialVersionUID: int = 5867946581318211330

    @staticmethod
    def initialize_fields() -> None:
        DoubleValidator.__VALIDATOR: DoubleValidator = (
            DoubleValidator.DoubleValidator1()
        )

    def _processParsedValue(
        self, value: typing.Any, formatter: typing.Union[str, datetime.datetime]
    ) -> typing.Any:

        if isinstance(value, float):
            return value
        return float(value.value)

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

        value = None if value is None else value.strip()
        if value is None or len(value) == 0:
            return None
        formatter = self._getFormat0(pattern, locale)
        return self._parse(value, formatter)

    def validate2(self, value: str, locale: typing.Any) -> float:

        value = None if value is None else value.strip()
        if value is None or len(value) == 0:
            return None
        formatter = self._getFormat0(None, locale)
        return self._parse(value, formatter)

    def validate1(self, value: str, pattern: str) -> float:

        formatter = self._getFormat0(pattern, None)
        return self._parse(value, formatter)

    def validate0(self, value: str) -> float:

        return self._parse(value, None, None)

    @staticmethod
    def DoubleValidator1() -> DoubleValidator:
        return DoubleValidator(True, DoubleValidator.STANDARD_FORMAT)

    def __init__(self, strict: bool, formatType: int) -> None:
        super().__init__(strict, formatType, True)

    @staticmethod
    def getInstance() -> DoubleValidator:
        return DoubleValidator.__VALIDATOR


DoubleValidator.initialize_fields()
