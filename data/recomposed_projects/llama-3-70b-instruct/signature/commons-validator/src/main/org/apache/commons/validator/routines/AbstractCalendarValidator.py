from __future__ import annotations
import time
import locale
import re
import os
from abc import ABC
import io
import typing
from typing import *
import datetime
import zoneinfo
from src.main.org.apache.commons.validator.routines.AbstractFormatValidator import *


class AbstractCalendarValidator(AbstractFormatValidator, ABC):

    __timeStyle: int = 0

    __dateStyle: int = 0

    __serialVersionUID: int = -1410008585975827379

    def _getFormat(
        self, pattern: str, locale: typing.Any
    ) -> typing.Union[str, datetime.datetime]:
        return self._getFormat0(pattern, locale)

    def isValid3(self, value: str, pattern: str, locale: typing.Any) -> bool:
        parsedValue = self._parse(value, pattern, locale, None)
        return parsedValue is not None

    def _compareQuarters(
        self,
        value: typing.Union[
            datetime.datetime,
            datetime.date,
            datetime.time,
            datetime.timedelta,
            datetime.timezone,
        ],
        compare: typing.Union[
            datetime.datetime,
            datetime.date,
            datetime.time,
            datetime.timedelta,
            datetime.timezone,
        ],
        monthOfFirstQuarter: int,
    ) -> int:
        valueQuarter = self.__calculateQuarter(value, monthOfFirstQuarter)
        compareQuarter = self.__calculateQuarter(compare, monthOfFirstQuarter)
        if valueQuarter < compareQuarter:
            return -1
        elif valueQuarter > compareQuarter:
            return 1
        else:
            return 0

    def _compareTime(
        self,
        value: typing.Union[
            datetime.datetime,
            datetime.date,
            datetime.time,
            datetime.timedelta,
            datetime.timezone,
        ],
        compare: typing.Union[
            datetime.datetime,
            datetime.date,
            datetime.time,
            datetime.timedelta,
            datetime.timezone,
        ],
        field: int,
    ) -> int:
        result: int = 0

        result = self.__calculateCompareResult(value, compare, datetime.time.hour)
        if result != 0 or (field == datetime.time.hour or field == datetime.time.hour):
            return result

        result = self.__calculateCompareResult(value, compare, datetime.time.minute)
        if result != 0 or field == datetime.time.minute:
            return result

        result = self.__calculateCompareResult(value, compare, datetime.time.second)
        if result != 0 or field == datetime.time.second:
            return result

        if field == datetime.time.microsecond:
            return self.__calculateCompareResult(
                value, compare, datetime.time.microsecond
            )

        raise ValueError("Invalid field: " + field)

    def _compare(
        self,
        value: typing.Union[
            datetime.datetime,
            datetime.date,
            datetime.time,
            datetime.timedelta,
            datetime.timezone,
        ],
        compare: typing.Union[
            datetime.datetime,
            datetime.date,
            datetime.time,
            datetime.timedelta,
            datetime.timezone,
        ],
        field: int,
    ) -> int:
        result: int = 0
        result = self.__calculateCompareResult(value, compare, Calendar.YEAR)
        if result != 0 or field == Calendar.YEAR:
            return result
        if field == Calendar.WEEK_OF_YEAR:
            return self.__calculateCompareResult(value, compare, Calendar.WEEK_OF_YEAR)
        if field == Calendar.DAY_OF_YEAR:
            return self.__calculateCompareResult(value, compare, Calendar.DAY_OF_YEAR)
        result = self.__calculateCompareResult(value, compare, Calendar.MONTH)
        if result != 0 or field == Calendar.MONTH:
            return result
        if field == Calendar.WEEK_OF_MONTH:
            return self.__calculateCompareResult(value, compare, Calendar.WEEK_OF_MONTH)
        result = self.__calculateCompareResult(value, compare, Calendar.DATE)
        if result != 0 or (
            field == Calendar.DATE
            or field == Calendar.DAY_OF_WEEK
            or field == Calendar.DAY_OF_WEEK_IN_MONTH
        ):
            return result
        return self._compareTime(value, compare, field)

    def _getFormat1(self, locale: typing.Any) -> typing.Union[str, datetime.datetime]:
        formatter = None
        if self.__dateStyle >= 0 and self.__timeStyle >= 0:
            if locale is None:
                formatter = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            else:
                formatter = datetime.datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S", locale
                )
        elif self.__timeStyle >= 0:
            if locale is None:
                formatter = datetime.datetime.now().strftime("%H:%M:%S")
            else:
                formatter = datetime.datetime.now().strftime("%H:%M:%S", locale)
        else:
            useDateStyle = (
                self.__dateStyle >= 0
                and self.__dateStyle
                or datetime.datetime.now().strftime("%Y-%m-%d")
            )
            if locale is None:
                formatter = datetime.datetime.now().strftime("%Y-%m-%d")
            else:
                formatter = datetime.datetime.now().strftime("%Y-%m-%d", locale)
        formatter.setLenient(False)
        return formatter

    def _getFormat0(
        self, pattern: str, locale: typing.Any
    ) -> typing.Union[str, datetime.datetime]:
        formatter: typing.Union[str, datetime.datetime] = None
        usePattern: bool = pattern != None and len(pattern) > 0
        if not usePattern:
            formatter = self._getFormat1(locale)
        elif locale == None:
            formatter = datetime.datetime.strptime(pattern, "%Y-%m-%d %H:%M:%S")
        else:
            formatter = datetime.datetime.strptime(pattern, "%Y-%m-%d %H:%M:%S", locale)
        formatter.setLenient(False)
        return formatter

    def _parse(
        self,
        value: str,
        pattern: str,
        locale: typing.Any,
        timeZone: typing.Union[zoneinfo.ZoneInfo, datetime.timezone],
    ) -> typing.Any:
        value = value if value is None else value.strip()
        if value is None or len(value) == 0:
            return None
        formatter = self._getFormat0(pattern, locale)
        if timeZone is not None:
            formatter.setTimeZone(timeZone)
        return self._parse(value, formatter)

    def _format5(
        self, value: typing.Any, formatter: typing.Union[str, datetime.datetime]
    ) -> str:
        if value is None:
            return None
        elif isinstance(value, datetime.datetime):
            value = value.time()
        return formatter.format(value)

    def format4(
        self,
        value: typing.Any,
        pattern: str,
        locale: typing.Any,
        timeZone: typing.Union[zoneinfo.ZoneInfo, datetime.timezone],
    ) -> str:
        formatter: typing.Union[str, datetime.datetime] = self._getFormat0(
            pattern, locale
        )
        if timeZone is not None:
            formatter.setTimeZone(timeZone)
        elif isinstance(value, Calendar):
            formatter.setTimeZone(value.getTimeZone())
        return self._format5(value, formatter)

    def format3(self, value: typing.Any, pattern: str, locale: typing.Any) -> str:
        return self.format4(value, pattern, locale, None)

    def format2(
        self,
        value: typing.Any,
        locale: typing.Any,
        timeZone: typing.Union[zoneinfo.ZoneInfo, datetime.timezone],
    ) -> str:
        return self.format4(value, None, locale, timeZone)

    def format1(
        self,
        value: typing.Any,
        pattern: str,
        timeZone: typing.Union[zoneinfo.ZoneInfo, datetime.timezone],
    ) -> str:
        return self.format4(value, pattern, None, timeZone)

    def format0(
        self,
        value: typing.Any,
        timeZone: typing.Union[zoneinfo.ZoneInfo, datetime.timezone],
    ) -> str:
        return self.format4(value, None, None, timeZone)

    def __init__(self, strict: bool, dateStyle: int, timeStyle: int) -> None:
        super().__init__(strict)
        self.__dateStyle = dateStyle
        self.__timeStyle = timeStyle

    def __calculateCompareResult(
        self,
        value: typing.Union[
            datetime.datetime,
            datetime.date,
            datetime.time,
            datetime.timedelta,
            datetime.timezone,
        ],
        compare: typing.Union[
            datetime.datetime,
            datetime.date,
            datetime.time,
            datetime.timedelta,
            datetime.timezone,
        ],
        field: int,
    ) -> int:
        difference = value.get(field) - compare.get(field)
        if difference < 0:
            return -1
        elif difference > 0:
            return 1
        else:
            return 0

    def __calculateQuarter(
        self,
        calendar: typing.Union[
            datetime.datetime,
            datetime.date,
            datetime.time,
            datetime.timedelta,
            datetime.timezone,
        ],
        monthOfFirstQuarter: int,
    ) -> int:
        year = calendar.year

        month = calendar.month + 1
        relativeMonth = (
            (month - monthOfFirstQuarter)
            if (month >= monthOfFirstQuarter)
            else (month + (12 - monthOfFirstQuarter))
        )
        quarter = (relativeMonth / 3) + 1
        if month < monthOfFirstQuarter:
            year -= 1
        return (year * 10) + quarter

    def _processParsedValue(
        self, value: typing.Any, formatter: typing.Union[str, datetime.datetime]
    ) -> typing.Any:
        return value
