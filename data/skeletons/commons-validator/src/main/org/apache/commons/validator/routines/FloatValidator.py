# Imports Begin
from src.main.org.apache.commons.validator.routines.AbstractNumberValidator import *
import datetime
import typing
import numbers

# Imports End


class FloatValidator(AbstractNumberValidator):

    # Class Fields Begin
    __serialVersionUID: int = None
    __VALIDATOR: FloatValidator = None
    # Class Fields End

    # Class Methods Begin
    def _processParsedValue(
        self, value: typing.Any, formatter: typing.Union[str, datetime.datetime]
    ) -> typing.Any:
        pass

    def maxValue1(self, value: float, max: float) -> bool:
        pass

    def maxValue0(self, value: float, max: float) -> bool:
        pass

    def minValue1(self, value: float, min: float) -> bool:
        pass

    def minValue0(self, value: float, min: float) -> bool:
        pass

    def isInRange1(self, value: float, min: float, max: float) -> bool:
        pass

    def isInRange0(self, value: float, min: float, max: float) -> bool:
        pass

    def validate3(self, value: str, pattern: str, locale: typing.Any) -> float:
        pass

    def validate2(self, value: str, locale: typing.Any) -> float:
        pass

    def validate1(self, value: str, pattern: str) -> float:
        pass

    def validate0(self, value: str) -> float:
        pass

    @staticmethod
    def FloatValidator1() -> "FloatValidator":
        pass

    def __init__(self, strict: bool, formatType: int) -> None:
        pass

    @staticmethod
    def getInstance() -> "FloatValidator":
        pass

    # Class Methods End
