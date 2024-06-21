from __future__ import annotations
import io
import numbers
import typing
from typing import *
import datetime
from src.main.org.apache.commons.validator.routines.AbstractNumberValidator import *


class ShortValidator(AbstractNumberValidator):

    __VALIDATOR: ShortValidator = ShortValidator.ShortValidator1()

    __serialVersionUID: int = -5227510699747787066

    def _processParsedValue(
        self, value: typing.Any, formatter: typing.Union[str, datetime.datetime]
    ) -> typing.Any:

        long_value = int(value)

        if long_value < -32768 or long_value > 32767:
            return None
        return short(long_value)

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
        return int(self.parse(value, None, locale))

    def validate1(self, value: str, pattern: str) -> int:

        # Call the parse method from AbstractNumberValidator
        result = self.parse(value, pattern, None)

        # Check if the result is a Short
        if isinstance(result, numbers.Number):
            return int(result)
        else:
            raise TypeError("The result is not a Short")

    def validate0(self, value: str) -> int:

        # Call the parse method from AbstractNumberValidator
        return self.parse(value, None, None)

    @staticmethod
    def ShortValidator1() -> ShortValidator:

        # Assuming STANDARD_FORMAT is a constant defined somewhere else in the code
        # If it's not, you'll need to replace it with the actual value
        STANDARD_FORMAT = 1

        return ShortValidator(True, STANDARD_FORMAT)

    def __init__(self, strict: bool, formatType: int) -> None:

        super().__init__(strict, formatType, False)

    @staticmethod
    def getInstance() -> ShortValidator:

        if not hasattr(ShortValidator, "__VALIDATOR"):
            ShortValidator.__VALIDATOR = ShortValidator()

        return ShortValidator.__VALIDATOR
