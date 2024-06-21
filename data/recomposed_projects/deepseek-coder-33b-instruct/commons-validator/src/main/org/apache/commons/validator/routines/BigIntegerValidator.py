from __future__ import annotations
import io
import numbers
import typing
from typing import *
import datetime
from src.main.org.apache.commons.validator.routines.AbstractNumberValidator import *


class BigIntegerValidator(AbstractNumberValidator):

    __VALIDATOR: BigIntegerValidator = BigIntegerValidator.BigIntegerValidator1()

    __serialVersionUID: int = 6713144356347139988

    def _processParsedValue(
        self, value: typing.Any, formatter: typing.Union[str, datetime.datetime]
    ) -> typing.Any:

        if isinstance(value, numbers.Number):
            return int(value)
        else:
            raise TypeError("Value must be a number")

    def maxValue(self, value: int, max: int) -> bool:

        return value <= max

    def minValue(self, value: int, min: int) -> bool:

        return value >= min

    def isInRange(self, value: int, min: int, max: int) -> bool:

        return value >= min and value <= max

    def validate3(self, value: str, pattern: str, locale: typing.Any) -> int:

        # Call the parse method from AbstractNumberValidator
        result = self.parse(value, pattern, locale)

        # Convert the result to int
        result = int(result)

        return result

    def validate2(self, value: str, locale: typing.Any) -> int:

        # Calling the parse method from AbstractNumberValidator
        result = self.parse(value, None, locale)

        # Checking if the result is a BigInteger
        if isinstance(result, numbers.Number):
            return int(result)
        else:
            raise ValueError("The result is not a BigInteger")

    def validate1(self, value: str, pattern: str) -> int:

        # Calling the parse method from AbstractNumberValidator
        result = self.parse(value, pattern, None)

        # Assuming parse method returns a BigInteger, we convert it to int
        return int(result)

    def validate0(self, value: str) -> int:

        # Calling the parse method from AbstractNumberValidator
        # Assuming parse method returns a BigInteger
        # We are converting it to int
        return int(self.parse(value, None, None))

    @staticmethod
    def BigIntegerValidator1() -> BigIntegerValidator:

        # Assuming STANDARD_FORMAT is a constant defined somewhere in the code
        STANDARD_FORMAT = 1

        return BigIntegerValidator(True, STANDARD_FORMAT)

    def __init__(self, strict: bool, formatType: int) -> None:

        super().__init__(strict, formatType, False)

    @staticmethod
    def getInstance() -> BigIntegerValidator:

        if not hasattr(BigIntegerValidator, "__VALIDATOR"):
            BigIntegerValidator.__VALIDATOR = BigIntegerValidator()

        return BigIntegerValidator.__VALIDATOR
