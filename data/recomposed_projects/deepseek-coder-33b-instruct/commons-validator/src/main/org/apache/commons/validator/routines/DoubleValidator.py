from __future__ import annotations
import io
import numbers
import typing
from typing import *
import datetime
from src.main.org.apache.commons.validator.routines.AbstractNumberValidator import *


class DoubleValidator(AbstractNumberValidator):

    __VALIDATOR: DoubleValidator = DoubleValidator.DoubleValidator1()

    __serialVersionUID: int = 5867946581318211330

    def _processParsedValue(
        self, value: typing.Any, formatter: typing.Union[str, datetime.datetime]
    ) -> typing.Any:

        if isinstance(value, float):
            return value
        return float(value)

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

        # Call the parse method from AbstractNumberValidator
        parsed_value = self.parse(value, pattern, locale)

        # Check if the parsed value is a number
        if isinstance(parsed_value, numbers.Number):
            return float(parsed_value)
        else:
            raise ValueError("Parsed value is not a number")

    def validate2(self, value: str, locale: typing.Any) -> float:

        # Calling the parse method from AbstractNumberValidator
        parsed_value = self.parse(value, None, locale)

        # Checking if the parsed value is a number
        if isinstance(parsed_value, numbers.Number):
            return float(parsed_value)
        else:
            raise ValueError("The parsed value is not a number.")

    def validate1(self, value: str, pattern: str) -> float:

        # Call the parse method from AbstractNumberValidator
        result = self.parse(value, pattern, None)

        # Check if the result is a number
        if isinstance(result, numbers.Number):
            return float(result)
        else:
            raise ValueError("The result is not a number")

    def validate0(self, value: str) -> float:

        return self.parse(value, None, None)

    @staticmethod
    def DoubleValidator1() -> DoubleValidator:

        return DoubleValidator(True, STANDARD_FORMAT)

    def __init__(self, strict: bool, formatType: int) -> None:

        super().__init__(strict, formatType, True)

    @staticmethod
    def getInstance() -> DoubleValidator:

        if not hasattr(DoubleValidator, "__VALIDATOR"):
            DoubleValidator.__VALIDATOR = DoubleValidator()

        return DoubleValidator.__VALIDATOR
