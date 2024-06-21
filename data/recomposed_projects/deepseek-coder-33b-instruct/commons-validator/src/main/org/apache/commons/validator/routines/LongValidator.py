from __future__ import annotations
import io
import numbers
import typing
from typing import *
import datetime
from src.main.org.apache.commons.validator.routines.AbstractNumberValidator import *


class LongValidator(AbstractNumberValidator):

    __VALIDATOR: LongValidator = LongValidator.LongValidator1()

    __serialVersionUID: int = -5117231731027866098

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

        # Call the parse method from AbstractNumberValidator
        parsed_value = self.parse(value, pattern, locale)

        # Check if the parsed value is a number
        if isinstance(parsed_value, numbers.Number):
            return int(parsed_value)
        else:
            raise ValueError("Parsed value is not a number")

    def validate2(self, value: str, locale: typing.Any) -> int:

        # Calling the parse method from AbstractNumberValidator
        parsed_value = self.parse(value, None, locale)

        # Checking if the parsed value is a Long
        if isinstance(parsed_value, numbers.Number):
            return int(parsed_value)
        else:
            raise ValueError("Parsed value is not a Long")

    def validate1(self, value: str, pattern: str) -> int:

        # Call the parse method from AbstractNumberValidator
        result = self.parse(value, pattern, None)

        # Check if the result is a Long
        if isinstance(result, numbers.Number):
            return int(result)
        else:
            raise TypeError("The result is not a Long")

    def validate0(self, value: str) -> int:

        # Calling the parse method from AbstractNumberValidator
        return self.parse(value, None, None)

    @staticmethod
    def LongValidator1() -> LongValidator:

        return LongValidator(True, STANDARD_FORMAT)

    def __init__(self, strict: bool, formatType: int) -> None:

        super().__init__(strict, formatType, False)

    @staticmethod
    def getInstance() -> LongValidator:

        if not hasattr(LongValidator, "__VALIDATOR"):
            LongValidator.__VALIDATOR = LongValidator()

        return LongValidator.__VALIDATOR
