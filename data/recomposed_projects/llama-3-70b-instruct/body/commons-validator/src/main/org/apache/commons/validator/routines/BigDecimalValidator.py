from __future__ import annotations
import time
import locale
import re
import io
import numbers
import typing
from typing import *
import decimal
import datetime
from src.main.org.apache.commons.validator.routines.AbstractNumberValidator import *


class BigDecimalValidator(AbstractNumberValidator):

    __VALIDATOR: BigDecimalValidator = None
    __serialVersionUID: int = -670320911490506772

    @staticmethod
    def initialize_fields() -> None:
        BigDecimalValidator.__VALIDATOR: BigDecimalValidator = (
            BigDecimalValidator.BigDecimalValidator2()
        )

    def _processParsedValue(
        self, value: typing.Any, formatter: typing.Union[str, datetime.datetime]
    ) -> typing.Any:
        decimal = None
        if isinstance(value, int):
            decimal = decimal.Decimal(value)
        else:
            decimal = decimal.Decimal(value.toString())

        scale = self._determineScale(formatter)
        if scale >= 0:
            decimal = decimal.setScale(scale, decimal.ROUND_DOWN)

        return decimal

    def maxValue(self, value: decimal.Decimal, max: float) -> bool:
        return value <= max

    def minValue(self, value: decimal.Decimal, min: float) -> bool:
        return value >= min

    def isInRange(self, value: decimal.Decimal, min: float, max: float) -> bool:
        return value >= min and value <= max

    def validate3(
        self, value: str, pattern: str, locale: typing.Any
    ) -> decimal.Decimal:
        return decimal.Decimal(self._parse(value, pattern, locale))

    def validate2(self, value: str, locale: typing.Any) -> decimal.Decimal:

        pass  # LLM could not translate this method

    def validate1(self, value: str, pattern: str) -> decimal.Decimal:
        return self._parse(value, pattern, None)

    def validate0(self, value: str) -> decimal.Decimal:

        pass  # LLM could not translate this method

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
