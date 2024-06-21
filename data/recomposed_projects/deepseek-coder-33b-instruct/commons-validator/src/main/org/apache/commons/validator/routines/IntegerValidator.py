from __future__ import annotations
import io
import numbers
import typing
from typing import *
import datetime
from src.main.org.apache.commons.validator.routines.AbstractNumberValidator import *


class IntegerValidator(AbstractNumberValidator):

    __VALIDATOR: IntegerValidator = IntegerValidator.IntegerValidator1()

    __serialVersionUID: int = 422081746310306596

    def _processParsedValue(
        self, value: typing.Any, formatter: typing.Union[str, datetime.datetime]
    ) -> typing.Any:

        if isinstance(value, int):
            if value >= -2147483648 and value <= 2147483647:
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

        # Check if the parsed value is an integer
        if isinstance(parsed_value, int):
            return parsed_value
        else:
            raise ValueError("Parsed value is not an integer")

    def validate2(self, value: str, locale: typing.Any) -> int:

        # Calling the parse method from AbstractNumberValidator
        parsed_value = self.parse(value, None, locale)

        # Checking if the parsed value is an integer
        if isinstance(parsed_value, int):
            return parsed_value
        else:
            raise ValueError("Parsed value is not an integer")

    def validate1(self, value: str, pattern: str) -> int:

        # Call the parse method from AbstractNumberValidator
        result = self.parse(value, pattern, None)

        # Check if the result is an integer
        if isinstance(result, int):
            return result
        else:
            raise TypeError("The result is not an integer")

    def validate0(self, value: str) -> int:

        # Calling the parse method from AbstractNumberValidator
        return int(self.parse(value, None, None))

    @staticmethod
    def IntegerValidator1() -> IntegerValidator:

        return IntegerValidator(True, STANDARD_FORMAT)

    def __init__(self, strict: bool, formatType: int) -> None:

        super().__init__(strict, formatType, False)

    @staticmethod
    def getInstance() -> IntegerValidator:

        if not hasattr(IntegerValidator, "__VALIDATOR"):
            IntegerValidator.__VALIDATOR = IntegerValidator()

        return IntegerValidator.__VALIDATOR
