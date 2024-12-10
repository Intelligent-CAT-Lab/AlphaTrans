from __future__ import annotations
import time
import locale
import re
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

    def _getFormat(self, pattern: str, locale: typing.Any) -> Format:

        formatter = None
        usePattern = pattern is not None and len(pattern) > 0
        if not usePattern:
            formatter = self._getFormat1(locale)
        elif locale is None:
            formatter = datetime.datetime.strptime(pattern, "%Y-%m-%d %H:%M:%S")
        else:
            symbols = datetime.date.strftime(locale, "%c")
            formatter = datetime.datetime.strptime(pattern, symbols)
        formatter.setLenient(False)
        return formatter

    def isValid3(self, value: str, pattern: str, locale: typing.Any) -> bool:

        parsedValue = self._parse(value, pattern, locale, None)
        return False if parsedValue is None else True

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

        result = 0

        result = self.__calculateCompareResult(value, compare, datetime.timezone.utc)
        if result != 0 or (field == datetime.timezone.utc):
            return result

        result = self.__calculateCompareResult(value, compare, datetime.timezone.utc)
        if result != 0 or field == datetime.timezone.utc:
            return result

        result = self.__calculateCompareResult(value, compare, datetime.timezone.utc)
        if result != 0 or field == datetime.timezone.utc:
            return result

        if field == datetime.timezone.utc:
            return self.__calculateCompareResult(value, compare, datetime.timezone.utc)

        raise ValueError("Invalid field: " + str(field))

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

        result = 0

        result = self.__calculateCompareResult(value, compare, datetime.timezone.utc)
        if result != 0 or (field == datetime.timezone.utc):
            return result

        result = self.__calculateCompareResult(value, compare, datetime.timezone.utc)
        if result != 0 or field == datetime.timezone.utc:
            return result

        result = self.__calculateCompareResult(value, compare, datetime.timezone.utc)
        if result != 0 or field == datetime.timezone.utc:
            return result

        if field == datetime.timezone.utc:
            return self.__calculateCompareResult(value, compare, datetime.timezone.utc)

        raise ValueError("Invalid field: " + str(field))

    def _getFormat1(self, locale: typing.Any) -> Format:

        formatter = None
        if self.__dateStyle >= 0 and self.__timeStyle >= 0:
            if locale is None:
                formatter = datetime.datetime.now().strftime("%c")
            else:
                formatter = datetime.datetime.now(
                    tz=zoneinfo.ZoneInfo(key=locale)
                ).strftime("%c")
        elif self.__timeStyle >= 0:
            if locale is None:
                formatter = datetime.datetime.now().strftime("%X")
            else:
                formatter = datetime.datetime.now(
                    tz=zoneinfo.ZoneInfo(key=locale)
                ).strftime("%X")
        else:
            useDateStyle = (
                self.__dateStyle if self.__dateStyle >= 0 else datetime.DATE_SHORT
            )
            if locale is None:
                formatter = datetime.datetime.now().strftime("%x")
            else:
                formatter = datetime.datetime.now(
                    tz=zoneinfo.ZoneInfo(key=locale)
                ).strftime("%x")
        return formatter

    def _getFormat0(self, pattern: str, locale: typing.Any) -> Format:

        formatter = None
        usePattern = pattern is not None and len(pattern) > 0
        if not usePattern:
            formatter = self._getFormat1(locale)
        elif locale is None:
            formatter = datetime.datetime.strptime(pattern, "%Y-%m-%d %H:%M:%S")
        else:
            symbols = datetime.date.strftime(locale, "%c")
            formatter = datetime.datetime.strptime(pattern, symbols)
        formatter.setLenient(False)
        return formatter

    def _parse(
        self,
        value: str,
        pattern: str,
        locale: typing.Any,
        timeZone: typing.Union[zoneinfo.ZoneInfo, datetime.timezone],
    ) -> typing.Any:

        value = None if value is None else value.strip()
        if value is None or len(value) == 0:
            return None
        formatter = self._getFormat0(pattern, locale)
        if timeZone is not None:
            formatter.setTimeZone(timeZone)
        return self._parse(value, formatter)

    def _format5(self, value: typing.Any, formatter: Format) -> str:

        if value is None:
            return None
        elif isinstance(value, datetime.datetime):
            value = value.replace(tzinfo=zoneinfo.ZoneInfo("UTC"))
        return formatter.format(value)

    def format4(
        self,
        value: typing.Any,
        pattern: str,
        locale: typing.Any,
        timeZone: typing.Union[zoneinfo.ZoneInfo, datetime.timezone],
    ) -> str:

        formatter = self._getFormat0(pattern, locale)
        if timeZone is not None:
            formatter.setTimeZone(timeZone)
        elif isinstance(value, datetime.datetime):
            formatter.setTimeZone(value.tzinfo)
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

        if isinstance(value, datetime.datetime):
            difference = value.replace(tzinfo=None) - compare.replace(tzinfo=None)
        elif isinstance(value, datetime.date):
            difference = (value - compare).days
        elif isinstance(value, datetime.time):
            difference = (
                datetime.datetime.combine(datetime.date.min, value)
                - datetime.datetime.combine(datetime.date.min, compare)
            ).seconds
        elif isinstance(value, datetime.timedelta):
            difference = value - compare
        elif isinstance(value, datetime.timezone):
            difference = (value.utcoffset(None) - compare.utcoffset(None)).seconds
        else:
            raise TypeError("Unsupported type")

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

        month = calendar.month
        relativeMonth = (
            (month - monthOfFirstQuarter)
            if month >= monthOfFirstQuarter
            else (month + (12 - monthOfFirstQuarter))
        )
        quarter = (relativeMonth // 3) + 1
        if month < monthOfFirstQuarter:
            year -= 1
        return (year * 10) + quarter

    def _processParsedValue(self, value: typing.Any, formatter: Format) -> typing.Any:

        # Your implementation here
        pass
