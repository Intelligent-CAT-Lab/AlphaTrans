from __future__ import annotations
import io
import numbers
import typing
from typing import *
import decimal
import datetime
from src.main.org.apache.commons.validator.routines.AbstractNumberValidator import *


class BigDecimalValidator(AbstractNumberValidator):

    __VALIDATOR: BigDecimalValidator = BigDecimalValidator.BigDecimalValidator2()

    __serialVersionUID: int = -670320911490506772

    def _processParsedValue(
        self, value: typing.Any, formatter: typing.Union[str, datetime.datetime]
    ) -> typing.Any:

        decimal_value = None
        if isinstance(value, int):
            decimal_value = decimal.Decimal(value)
        else:
            decimal_value = decimal.Decimal(str(value))

        scale = self.determineScale(formatter)
        if scale >= 0:
            decimal_value = decimal_value.quantize(
                decimal.Decimal(10) ** -scale, rounding=decimal.ROUND_DOWN
            )

        return decimal_value

    def maxValue(self, value: decimal.Decimal, max: float) -> bool:

        return value.compare(decimal.Decimal(max)) <= 0

    def minValue(self, value: decimal.Decimal, min: float) -> bool:

        return value.to_eng_string() >= str(min)

    def isInRange(self, value: decimal.Decimal, min: float, max: float) -> bool:

        return value.to_eng_string() >= str(min) and value.to_eng_string() <= str(max)

    def validate3(
        self, value: str, pattern: str, locale: typing.Any
    ) -> decimal.Decimal:

        # Call the parse method from AbstractNumberValidator
        parsed_value = self.parse(value, pattern, locale)

        # Check if the parsed value is a number
        if isinstance(parsed_value, numbers.Number):
            return decimal.Decimal(parsed_value)
        else:
            raise ValueError("Parsed value is not a number")

    def validate2(self, value: str, locale: typing.Any) -> decimal.Decimal:

        return decimal.Decimal(self.parse(value, None, locale))

    def validate1(self, value: str, pattern: str) -> decimal.Decimal:

        # Calling the parse method from AbstractNumberValidator
        return self.parse(value, pattern, None)

    def validate0(self, value: str) -> decimal.Decimal:

        return self.parse(value, None, None)

    @staticmethod
    def BigDecimalValidator2() -> BigDecimalValidator:

        return BigDecimalValidator.BigDecimalValidator1(True)

    @staticmethod
    def BigDecimalValidator1(strict: bool) -> BigDecimalValidator:

        return BigDecimalValidator(strict, STANDARD_FORMAT, True)

    def __init__(self, strict: bool, formatType: int, allowFractions: bool) -> None:

        super().__init__(strict, formatType, allowFractions)

    @staticmethod
    def getInstance() -> BigDecimalValidator:

        if not hasattr(BigDecimalValidator, "__VALIDATOR"):
            BigDecimalValidator.__VALIDATOR = BigDecimalValidator()

        return BigDecimalValidator.__VALIDATOR
