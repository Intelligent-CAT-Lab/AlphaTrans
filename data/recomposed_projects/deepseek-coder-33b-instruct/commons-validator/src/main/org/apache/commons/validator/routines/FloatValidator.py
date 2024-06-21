from __future__ import annotations
import io
import numbers
import typing
from typing import *
import datetime
from src.main.org.apache.commons.validator.routines.AbstractNumberValidator import *


class FloatValidator(AbstractNumberValidator):

    __VALIDATOR: FloatValidator = FloatValidator.FloatValidator1()

    __serialVersionUID: int = -4513245432806414267

    def _processParsedValue(
        self, value: typing.Any, formatter: typing.Union[str, datetime.datetime]
    ) -> typing.Any:

        doubleValue = float(value)

        if doubleValue > 0:
            if doubleValue < float("-inf"):
                return None
            if doubleValue > float("inf"):
                return None
        elif doubleValue < 0:
            posDouble = doubleValue * -1
            if posDouble < float("-inf"):
                return None
            if posDouble > float("inf"):
                return None

        return float(doubleValue)

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

        # Check if the parsed value is a float
        if isinstance(parsed_value, float):
            return parsed_value
        else:
            raise ValueError("Parsed value is not a float")

    def validate2(self, value: str, locale: typing.Any) -> float:

        # Calling the parse method from AbstractNumberValidator
        parsed_value = self.parse(value, None, locale)

        # Checking if the parsed value is a float
        if isinstance(parsed_value, float):
            return parsed_value
        else:
            raise ValueError("Parsed value is not a float")

    def validate1(self, value: str, pattern: str) -> float:

        # Call the parse method from AbstractNumberValidator
        result = self.parse(value, pattern, None)

        # Check if the result is a float
        if isinstance(result, float):
            return result
        else:
            raise TypeError("The result is not a float")

    def validate0(self, value: str) -> float:

        return float(self.parse(value, None, None))

    @staticmethod
    def FloatValidator1() -> FloatValidator:

        return FloatValidator(True, STANDARD_FORMAT)

    def __init__(self, strict: bool, formatType: int) -> None:

        super().__init__(strict, formatType, True)

    @staticmethod
    def getInstance() -> FloatValidator:

        if not hasattr(FloatValidator, "__VALIDATOR"):
            FloatValidator.__VALIDATOR = FloatValidator()

        return FloatValidator.__VALIDATOR
