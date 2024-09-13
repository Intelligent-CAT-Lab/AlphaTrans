from __future__ import annotations
import locale
import re
from abc import ABC
import io
import numbers
import typing
from typing import *
from src.main.org.apache.commons.validator.routines.AbstractFormatValidator import *


class AbstractNumberValidator(AbstractFormatValidator, ABC):

    PERCENT_FORMAT: int = 2
    CURRENCY_FORMAT: int = 1
    STANDARD_FORMAT: int = 0
    __formatType: int = 0

    __allowFractions: bool = False

    __serialVersionUID: int = -3088817875906765463

    def _getFormat(self, pattern: str, locale: typing.Any) -> typing.Any:

        return self._getFormat0(pattern, locale)

    def isValid3(self, value: str, pattern: str, locale: typing.Any) -> bool:

        if pattern:
            pattern = pattern.replace("\u00A4","")
        parsedValue = self._parse(value, pattern, locale)
        return parsedValue is not None

    def _getFormat1(self, locale_: typing.Any) -> typing.Any:

        formatter = None
        if self.__formatType == AbstractNumberValidator.CURRENCY_FORMAT:
            if locale is None:
                formatter = locale.localeconv()['currency_symbol']
            else:
                locale.setlocale(locale.LC_ALL, locale_)
                formatter = locale.localeconv()['currency_symbol']
        elif self.__formatType == AbstractNumberValidator.PERCENT_FORMAT:
            if locale is None:
                formatter = "{:.0%}"
            else:
                locale.setlocale(locale.LC_ALL, locale_)
                formatter = "{:.0%}"
        else:
            if locale is None:
                formatter = "{:,}"
            else:
                locale.setlocale(locale.LC_ALL, locale_)
                formatter = "{:,}"
            if not self.isAllowFractions():
                formatter = "{:,.0f}"
        
        return formatter

    def _determineScale(self, format_: typing.Any) -> int:

        if not self.isStrict():
            return -1
        if not self.isAllowFractions() or ".0f" in format_:
            return 0

        minimumFraction = format_.count('f')
        maximumFraction = minimumFraction
        
        if minimumFraction != maximumFraction:
            return -1

        scale = minimumFraction

        if self.__formatType == self.PERCENT_FORMAT:
            scale += 2

        return scale

    def _getFormat0(self, pattern: str, locale_: typing.Any) -> typing.Any:

        formatter = None
        use_pattern = pattern is not None and len(pattern) > 0

        if not use_pattern:
            formatter = self._getFormat1(locale_)
        elif locale_ is None:
            formatter = pattern + "NUMBER"
        else:
            locale.setlocale(locale.LC_ALL, locale_)
            formatter = pattern + "NUMBER"

        if not self.isAllowFractions():
            formatter = "{:,.0f}"

        return formatter

    def _parse(self, value: str, pattern: str, locale_: typing.Any) -> typing.Any:

        value = value.strip() if value is not None else None
        if value is None or len(value) == 0:
            return None
        formatter = self._getFormat0(pattern, locale_)
        if not self.__allowFractions:
            formatter += "DISALLOW FRACTION"
        return super()._parse(value, formatter)

    def maxValue(
        self,
        value: typing.Union[int, float, numbers.Number],
        max_: typing.Union[int, float, numbers.Number],
    ) -> bool:
        if self.isAllowFractions():
            return float(value) <= float(max_)
        return int(value) <= int(max_)

    def minValue(
        self,
        value: typing.Union[int, float, numbers.Number],
        min_: typing.Union[int, float, numbers.Number],
    ) -> bool:
        if self.isAllowFractions():
            return float(value) >= float(min_)
        return int(value) >= int(min_)

    def isInRange(
        self,
        value: typing.Union[int, float, numbers.Number],
        min_: typing.Union[int, float, numbers.Number],
        max_: typing.Union[int, float, numbers.Number],
    ) -> bool:
        return self.minValue(value, min_) and self.maxValue(value, max_)

    def getFormatType(self) -> int:
        return self.__formatType

    def isAllowFractions(self) -> bool:
        return self.__allowFractions

    def __init__(self, strict: bool, formatType: int, allowFractions: bool) -> None:
        super().__init__(strict)
        self.__formatType = formatType
        self.__allowFractions = allowFractions

    def _processParsedValue(self, value: typing.Any, formatter: typing.Any) -> typing.Any:

        pass
