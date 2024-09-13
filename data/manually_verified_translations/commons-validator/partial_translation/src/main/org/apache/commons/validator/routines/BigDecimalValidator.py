from __future__ import annotations
import locale
import re
import io
import numbers
import typing
from typing import *
import decimal
from src.main.org.apache.commons.validator.routines.AbstractNumberValidator import *


class BigDecimalValidator(AbstractNumberValidator):

    __VALIDATOR: BigDecimalValidator = None
    __serialVersionUID: int = -670320911490506772

    @staticmethod
    def initialize_fields() -> None:
        BigDecimalValidator.__VALIDATOR: BigDecimalValidator = (
            BigDecimalValidator.BigDecimalValidator2()
        )

    def _processParsedValue(self, value: typing.Any, formatter: Format) -> typing.Any:

        decimal_value = None
        if isinstance(value, int):
            decimal_value = decimal.Decimal(value)
        else:
            decimal_value = decimal.Decimal(str(value))

        scale = self._determineScale(formatter)
        if scale >= 0:
            decimal_value = decimal_value.quantize(
                decimal.Decimal(10) ** -scale, decimal.ROUND_DOWN
            )

        return decimal_value

    def maxValue(self, value: decimal.Decimal, max_: float) -> bool:
        return value.compare(decimal.Decimal(max_)) <= 0

    def minValue(self, value: decimal.Decimal, min_: float) -> bool:
        return value.to_eng_string() >= str(min_)

    def isInRange(self, value: decimal.Decimal, min_: float, max_: float) -> bool:
        return min_ <= value.doubleValue() <= max_

    def validate3(
        self, value: str, pattern: str, locale: typing.Any
    ) -> decimal.Decimal:

        value = value.strip() if value is not None else None
        if value is None or len(value) == 0:
            return None
        formatter = self._getFormat0(pattern, locale)
        return self._parse(value, formatter)

    def validate2(self, value: str, locale: typing.Any) -> decimal.Decimal:

        value = value.strip() if value is not None else None
        if value is None or len(value) == 0:
            return None
        formatter = self._getFormat0(None, locale)
        return self._parse(value, formatter)

    def validate1(self, value: str, pattern: str) -> decimal.Decimal:

        value = value.strip() if value is not None else None
        if value is None or len(value) == 0:
            return None
        formatter = self._getFormat0(pattern, None)
        return self._parse(value, formatter)

    def validate0(self, value: str) -> decimal.Decimal:

        value = value.strip() if value is not None else None
        if value is None or len(value) == 0:
            return None
        formatter = self._getFormat0(None, None)
        return self._parse(value, formatter)

    @staticmethod
    def BigDecimalValidator2() -> BigDecimalValidator:
        return BigDecimalValidator.BigDecimalValidator1(True)

    @staticmethod
    def BigDecimalValidator1(strict: bool) -> BigDecimalValidator:
        return BigDecimalValidator(strict, BigDecimalValidator.STANDARD_FORMAT, True)

    def __init__(self, strict: bool, formatType: int, allowFractions: bool) -> None:
        super().__init__(strict, formatType, allowFractions)

    @staticmethod
    def getInstance() -> BigDecimalValidator:
        return BigDecimalValidator.__VALIDATOR


BigDecimalValidator.initialize_fields()
