from __future__ import annotations
from abc import ABC
import io
import typing
from typing import *
import datetime
from src.main.org.apache.commons.validator.routines.AbstractFormatValidator import *


class AbstractCalendarValidator(AbstractFormatValidator, ABC):

    __timeStyle: int = None
    __dateStyle: int = None

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

        result = 0

        result = self.__calculateCompareResult(value, compare, datetime.datetime.hour)
        if result != 0 or (
            field == datetime.datetime.hour or field == datetime.datetime.hour
        ):
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

        result = self.__calculateCompareResult(value, compare, datetime.datetime.YEAR)
        if result != 0 or field == datetime.datetime.YEAR:
            return result

        if field == datetime.datetime.WEEK_OF_YEAR:
            return self.__calculateCompareResult(
                value, compare, datetime.datetime.WEEK_OF_YEAR
            )

        if field == datetime.datetime.DAY_OF_YEAR:
            return self.__calculateCompareResult(
                value, compare, datetime.datetime.DAY_OF_YEAR
            )

        result = self.__calculateCompareResult(value, compare, datetime.datetime.MONTH)
        if result != 0 or field == datetime.datetime.MONTH:
            return result

        if field == datetime.datetime.WEEK_OF_MONTH:
            return self.__calculateCompareResult(
                value, compare, datetime.datetime.WEEK_OF_MONTH
            )

        result = self.__calculateCompareResult(value, compare, datetime.datetime.DATE)
        if result != 0 or (
            field == datetime.datetime.DATE
            or field == datetime.datetime.DAY_OF_WEEK
            or field == datetime.datetime.DAY_OF_WEEK_IN_MONTH
        ):
            return result

        return self._compareTime(value, compare, field)

    def _getFormat1(self, locale: typing.Any) -> typing.Union[str, datetime.datetime]:

        formatter = None
        if self._dateStyle >= 0 and self._timeStyle >= 0:
            if locale is None:
                formatter = datetime.datetime.now().strftime("%c")
            else:
                formatter = datetime.datetime.now(locale).strftime("%c")
        elif self._timeStyle >= 0:
            if locale is None:
                formatter = datetime.datetime.now().strftime("%X")
            else:
                formatter = datetime.datetime.now(locale).strftime("%X")
        else:
            useDateStyle = self._dateStyle if self._dateStyle >= 0 else datetime.SHORT
            if locale is None:
                formatter = datetime.datetime.now().strftime("%x")
            else:
                formatter = datetime.datetime.now(locale).strftime("%x")

        return formatter

    def _getFormat0(
        self, pattern: str, locale: typing.Any
    ) -> typing.Union[str, datetime.datetime]:

        formatter = None
        use_pattern = pattern is not None and len(pattern) > 0
        if not use_pattern:
            formatter = self._getFormat1(locale)
        elif locale is None:
            formatter = datetime.datetime.strptime(pattern, "%Y-%m-%d")
        else:
            formatter = datetime.datetime.strptime(pattern, "%Y-%m-%d")
            formatter.locale = locale
        formatter.setLenient(False)
        return formatter

    def _parse(
        self, value: str, pattern: str, locale: typing.Any, timeZone: datetime.timezone
    ) -> typing.Any:

        value = None if value is None else value.strip()
        if value is None or len(value) == 0:
            return None
        formatter = self._getFormat0(pattern, locale)
        if timeZone is not None:
            formatter.setTimeZone(timeZone)
        return self.parse(value, formatter)

    def _format5(
        self, value: typing.Any, formatter: typing.Union[str, datetime.datetime]
    ) -> str:

        if value is None:
            return None
        elif isinstance(value, datetime.datetime):
            value = value.date()
        return formatter.format(value)

    def format4(
        self,
        value: typing.Any,
        pattern: str,
        locale: typing.Any,
        timeZone: datetime.timezone,
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
        self, value: typing.Any, locale: typing.Any, timeZone: datetime.timezone
    ) -> str:

        return self.format4(value, None, locale, timeZone)

    def format1(
        self, value: typing.Any, pattern: str, timeZone: datetime.timezone
    ) -> str:

        return self.format4(value, pattern, None, timeZone)

    def format0(self, value: typing.Any, timeZone: datetime.timezone) -> str:

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

        if difference.days < 0:
            return -1
        elif difference.days > 0:
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
            month - monthOfFirstQuarter
            if month >= monthOfFirstQuarter
            else month + (12 - monthOfFirstQuarter)
        )
        quarter = (relativeMonth // 3) + 1
        if month < monthOfFirstQuarter:
            year -= 1
        return (year * 10) + quarter

    def _processParsedValue(
        self, value: typing.Any, formatter: typing.Union[str, datetime.datetime]
    ) -> typing.Any:

        pass
