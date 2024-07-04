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

        result = self.__calculateCompareResult(value, compare, datetime.datetime.hour)
        if result != 0 or field == datetime.datetime.hour:
            return result

        result = self.__calculateCompareResult(value, compare, datetime.datetime.minute)
        if result != 0 or field == datetime.datetime.minute:
            return result

        result = self.__calculateCompareResult(value, compare, datetime.datetime.second)
        if result != 0 or field == datetime.datetime.second:
            return result

        if field == datetime.datetime.microsecond:
            return self.__calculateCompareResult(
                value, compare, datetime.datetime.microsecond
            )

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

        result = self.__calculateCompareResult(value, compare, datetime.datetime.year)
        if result != 0 or field == datetime.datetime.year:
            return result

        if field == datetime.datetime.week_of_year:
            return self.__calculateCompareResult(
                value, compare, datetime.datetime.week_of_year
            )

        if field == datetime.datetime.day_of_year:
            return self.__calculateCompareResult(
                value, compare, datetime.datetime.day_of_year
            )

        result = self.__calculateCompareResult(value, compare, datetime.datetime.month)
        if result != 0 or field == datetime.datetime.month:
            return result

        if field == datetime.datetime.week_of_month:
            return self.__calculateCompareResult(
                value, compare, datetime.datetime.week_of_month
            )

        result = self.__calculateCompareResult(value, compare, datetime.datetime.date)
        if (
            result != 0
            or field == datetime.datetime.date
            or field == datetime.datetime.day_of_week
            or field == datetime.datetime.day_of_week_in_month
        ):
            return result

        return self._compareTime(value, compare, field)

    def _getFormat1(self, locale: typing.Any) -> typing.Union[str, datetime.datetime]:

        formatter = None
        if self.__dateStyle >= 0 and self.__timeStyle >= 0:
            if locale is None:
                formatter = datetime.datetime.now().strftime(f"%Y-%m-%d %H:%M:%S")
            else:
                formatter = datetime.datetime.now(
                    tz=zoneinfo.ZoneInfo(key=locale)
                ).strftime(f"%Y-%m-%d %H:%M:%S")
        elif self.__timeStyle >= 0:
            if locale is None:
                formatter = datetime.datetime.now().strftime(f"%H:%M:%S")
            else:
                formatter = datetime.datetime.now(
                    tz=zoneinfo.ZoneInfo(key=locale)
                ).strftime(f"%H:%M:%S")
        else:
            useDateStyle = self.__dateStyle if self.__dateStyle >= 0 else datetime.SHORT
            if locale is None:
                formatter = datetime.datetime.now().strftime(f"%Y-%m-%d")
            else:
                formatter = datetime.datetime.now(
                    tz=zoneinfo.ZoneInfo(key=locale)
                ).strftime(f"%Y-%m-%d")
        return formatter

    def _getFormat0(
        self, pattern: str, locale: typing.Any
    ) -> typing.Union[str, datetime.datetime]:

        formatter = None
        usePattern = pattern is not None and len(pattern) > 0
        if not usePattern:
            formatter = self._getFormat1(locale)
        elif locale is None:
            formatter = datetime.datetime.now().strftime(pattern)
        else:
            symbols = datetime.date.locale(locale)
            formatter = datetime.datetime.now(
                tz=zoneinfo.ZoneInfo(key=locale)
            ).strftime(pattern)
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

    def _format5(
        self, value: typing.Any, formatter: typing.Union[str, datetime.datetime]
    ) -> str:

        if value is None:
            return None
        elif isinstance(value, datetime.datetime):
            value = value.replace(tzinfo=zoneinfo.ZoneInfo("UTC"))
        return (
            value.strftime(formatter)
            if isinstance(formatter, str)
            else formatter.format(value)
        )

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
            difference = value - compare
        elif isinstance(value, datetime.time):
            difference = datetime.timedelta(
                hours=value.hour, minutes=value.minute, seconds=value.second
            ) - datetime.timedelta(
                hours=compare.hour, minutes=compare.minute, seconds=compare.second
            )
        elif isinstance(value, datetime.timedelta):
            difference = value - compare
        elif isinstance(value, datetime.timezone):
            difference = value - compare
        else:
            raise TypeError("Unsupported type for value")

        if difference.total_seconds() < 0:
            return -1
        elif difference.total_seconds() > 0:
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

        if isinstance(calendar, datetime.datetime) or isinstance(
            calendar, datetime.date
        ):
            year = calendar.year
            month = calendar.month
        else:
            raise TypeError(
                "calendar must be a datetime.datetime, datetime.date, datetime.time, datetime.timedelta, or datetime.timezone object"
            )

        relativeMonth = (
            (month - monthOfFirstQuarter)
            if (month >= monthOfFirstQuarter)
            else (month + (12 - monthOfFirstQuarter))
        )
        quarter = (relativeMonth // 3) + 1
        if month < monthOfFirstQuarter:
            year -= 1
        return (year * 10) + quarter

    def _processParsedValue(
        self, value: typing.Any, formatter: typing.Union[str, datetime.datetime]
    ) -> typing.Any:

        # Your implementation here
        pass
