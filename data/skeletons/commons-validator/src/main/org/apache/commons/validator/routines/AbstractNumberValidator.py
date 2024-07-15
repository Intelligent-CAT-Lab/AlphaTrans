from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.validator.routines.AbstractFormatValidator import *
import typing
from typing import *
import numbers
import io
from abc import ABC

# Imports End


class AbstractNumberValidator(AbstractFormatValidator, ABC):

    # Class Fields Begin
    __serialVersionUID: int = None
    STANDARD_FORMAT: int = None
    CURRENCY_FORMAT: int = None
    PERCENT_FORMAT: int = None
    __allowFractions: bool = None
    __formatType: int = None
    # Class Fields End

    # Class Methods Begin
    def _getFormat(self, pattern: str, locale: typing.Any) -> Format:
        pass

    def isValid3(self, value: str, pattern: str, locale: typing.Any) -> bool:
        pass

    def _getFormat1(self, locale: typing.Any) -> Format:
        pass

    def _determineScale(self, format_: typing.Any) -> int:
        pass

    def _getFormat0(self, pattern: str, locale: typing.Any) -> Format:
        pass

    def _parse(self, value: str, pattern: str, locale: typing.Any) -> typing.Any:
        pass

    def maxValue(
        self,
        value: typing.Union[int, float, numbers.Number],
        max_: typing.Union[int, float, numbers.Number],
    ) -> bool:
        pass

    def minValue(
        self,
        value: typing.Union[int, float, numbers.Number],
        min_: typing.Union[int, float, numbers.Number],
    ) -> bool:
        pass

    def isInRange(
        self,
        value: typing.Union[int, float, numbers.Number],
        min_: typing.Union[int, float, numbers.Number],
        max_: typing.Union[int, float, numbers.Number],
    ) -> bool:
        pass

    def getFormatType(self) -> int:
        pass

    def isAllowFractions(self) -> bool:
        pass

    def __init__(self, strict: bool, formatType: int, allowFractions: bool) -> None:
        pass

    def _processParsedValue(self, value: typing.Any, formatter: Format) -> typing.Any:
        pass

    # Class Methods End
