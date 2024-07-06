from __future__ import annotations
import time
import locale
import re
from abc import ABC
import io
import numbers
import typing
from typing import *
import datetime
from src.main.org.apache.commons.validator.routines.AbstractFormatValidator import *


class AbstractNumberValidator(AbstractFormatValidator, ABC):

    PERCENT_FORMAT: int = 2
    CURRENCY_FORMAT: int = 1
    STANDARD_FORMAT: int = 0
    __formatType: int = 0

    __allowFractions: bool = False

    __serialVersionUID: int = -3088817875906765463

    def _getFormat(
        self, pattern: str, locale: typing.Any
    ) -> typing.Union[str, datetime.datetime]:
        return self._getFormat0(pattern, locale)

    def isValid3(self, value: str, pattern: str, locale: typing.Any) -> bool:

        pass  # LLM could not translate this method

    def _getFormat1(self, locale: typing.Any) -> typing.Union[str, datetime.datetime]:
        formatter = None
        if self.__formatType == self.CURRENCY_FORMAT:
            if locale is None:
                formatter = NumberFormat.getCurrencyInstance()
            else:
                formatter = NumberFormat.getCurrencyInstance(locale)
        elif self.__formatType == self.PERCENT_FORMAT:
            if locale is None:
                formatter = NumberFormat.getPercentInstance()
            else:
                formatter = NumberFormat.getPercentInstance(locale)
        else:
            if locale is None:
                formatter = NumberFormat.getInstance()
            else:
                formatter = NumberFormat.getInstance(locale)
            if not self.isAllowFractions():
                formatter.setParseIntegerOnly(True)
        return formatter

    def _determineScale(self, format: typing.Any) -> int:
        if not self.isStrict():
            return -1
        if not self.isAllowFractions() or format.isParseIntegerOnly():
            return 0
        minimumFraction = format.getMinimumFractionDigits()
        maximumFraction = format.getMaximumFractionDigits()
        if minimumFraction != maximumFraction:
            return -1
        scale = minimumFraction
        if isinstance(format, DecimalFormat):
            multiplier = format.getMultiplier()
            if multiplier == 100:
                scale += 2
            elif multiplier == 1000:
                scale += 3
        elif self.__formatType == AbstractNumberValidator.PERCENT_FORMAT:
            scale += 2
        return scale

    def _getFormat0(
        self, pattern: str, locale: typing.Any
    ) -> typing.Union[str, datetime.datetime]:
        formatter: typing.Union[str, datetime.datetime] = None
        usePattern: bool = pattern != None and len(pattern) > 0
        if not usePattern:
            formatter = self._getFormat1(locale)
        elif locale == None:
            formatter = DecimalFormat(pattern)
        else:
            symbols: typing.Union[str, datetime.datetime] = DecimalFormatSymbols(locale)
            formatter = DecimalFormat(pattern, symbols)

        if not self.isAllowFractions():
            formatter.setParseIntegerOnly(True)
        return formatter

    def _parse(self, value: str, pattern: str, locale: typing.Any) -> typing.Any:
        value = value if value is not None else None
        if value is None or len(value) == 0:
            return None
        formatter = self._getFormat0(pattern, locale)
        return self._parse(value, formatter)

    def maxValue(
        self,
        value: typing.Union[int, float, numbers.Number],
        max: typing.Union[int, float, numbers.Number],
    ) -> bool:
        if self.isAllowFractions():
            return value <= max
        return value <= max

    def minValue(
        self,
        value: typing.Union[int, float, numbers.Number],
        min: typing.Union[int, float, numbers.Number],
    ) -> bool:
        if self.isAllowFractions():
            return value >= min
        return value >= min

    def isInRange(
        self,
        value: typing.Union[int, float, numbers.Number],
        min: typing.Union[int, float, numbers.Number],
        max: typing.Union[int, float, numbers.Number],
    ) -> bool:
        return self.minValue(value, min) and self.maxValue(value, max)

    def getFormatType(self) -> int:
        return self.__formatType

    def isAllowFractions(self) -> bool:
        return self.__allowFractions

    def __init__(self, strict: bool, formatType: int, allowFractions: bool) -> None:
        super().__init__(strict)
        self.__allowFractions = allowFractions
        self.__formatType = formatType

    def _processParsedValue(
        self, value: typing.Any, formatter: typing.Union[str, datetime.datetime]
    ) -> typing.Any:
        return value
