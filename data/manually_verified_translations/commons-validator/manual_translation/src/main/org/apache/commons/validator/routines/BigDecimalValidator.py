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

    def _processParsedValue(self, value: typing.Any, formatter: typing.Any) -> typing.Any:

        if formatter == "{:,}" or "#" in formatter:
            return value  # Handled manually when parsing
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
        return value <= decimal.Decimal(max_)

    def minValue(self, value: decimal.Decimal, min_: float) -> bool:
        return float(value) >= min_

    def isInRange(self, value: decimal.Decimal, min_: float, max_: float) -> bool:
        return min_ <= float(value) <= max_

    def validate3(
        self, value: str, pattern: str, locale: typing.Any
    ) -> decimal.Decimal:
        return self._parse(value, pattern, locale)

    def validate2(self, value: str, locale: typing.Any) -> decimal.Decimal:
        return self._parse(value, None, locale)

    def validate1(self, value: str, pattern: str) -> decimal.Decimal:
        return self._parse(value, pattern, None)

    def validate0(self, value: str) -> decimal.Decimal:
        return self._parse(value, None, None)

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
