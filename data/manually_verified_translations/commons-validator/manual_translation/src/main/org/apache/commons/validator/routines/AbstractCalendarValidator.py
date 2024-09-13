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

    def _getFormat(self, pattern: str, locale: typing.Any) -> typing.Any:

        formatter = None
        usePattern = pattern is not None and len(pattern) > 0
        if not usePattern:
            formatter = self._getFormat1(locale)
        elif locale is None:
            formatter = datetime.datetime.strptime(pattern, "%Y-%m-%d %H:%M:%S")
        else:
            symbols = datetime.date.strftime(locale, "%c")
            formatter = datetime.datetime.strptime(pattern, symbols)
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
        field: str,
    ) -> int:

        result = 0

        result = self.__calculateCompareResult(value, compare, 'hour')
        if result != 0 or field in ['HOUR', 'HOUR_OF_DAY']:
            return result

        result = self.__calculateCompareResult(value, compare, 'minute')
        if result != 0 or field == 'MINUTE':
            return result

        result = self.__calculateCompareResult(value, compare, 'second')
        if result != 0 or field == 'SECOND':
            return result

        if field == 'MILLISECOND':
            return self.__calculateCompareResult(value, compare, 'microsecond')

        raise ValueError(f"Invalid field: {field}")

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
        field: str,
    ) -> int:

        result = 0

        result = self.__calculateCompareResult(value, compare, 'year')
        if result != 0 or field == 'YEAR':
            return result

        if field == 'WEEK_OF_YEAR':
            return self.__calculateCompareResult(value, compare, 'isocalendar_week')

        if field == 'DAY_OF_YEAR':
            return self.__calculateCompareResult(value, compare, 'day_of_year')

        result = self.__calculateCompareResult(value, compare, 'month')
        if result != 0 or field == 'MONTH':
            return result

        if field == 'WEEK_OF_MONTH':
            return self.__calculateCompareResult(value, compare, 'week_of_month')

        result = self.__calculateCompareResult(value, compare, 'day')
        if result != 0 or field in ['DAY', 'DAY_OF_WEEK', 'DAY_OF_WEEK_IN_MONTH', 'DATE']:
            return result

        return self._compareTime(value, compare, field)

    def _getFormat1(self, locale_: typing.Any) -> typing.Any:

        formatter = None
        if self.__dateStyle >= 0 and self.__timeStyle >= 0:
            if locale_ is None:
                formatter = f"%x %X"
            else:
                locale.setlocale(locale.LC_ALL, locale_)
                formatter = f"%x %X"
        elif self.__timeStyle >= 0:
            if locale is None:
                formatter = "%X"
            else:
                locale.setlocale(locale.LC_ALL, locale_)
                formatter = "%X"
        else:
            if locale is None:
                formatter = "%x"
            else:
                locale.setlocale(locale.LC_ALL, locale_)
                formatter = "%x"
        return formatter

    def _getFormat0(self, pattern: str, locale_: typing.Any) -> typing.Any:

        formatter = None
        usePattern = pattern is not None and len(pattern) > 0
        if not usePattern:
            formatter = self._getFormat1(locale_)
        elif locale is None:
            formatter = pattern + "DATE"
        else:
            locale.setlocale(locale.LC_ALL, locale_)
            formatter = pattern + "DATE"
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
            formatter = [formatter, timeZone]
        return super()._parse(value, formatter)
    
    def _format5(self, value: typing.Any, formatter: typing.Any, locale_: typing.Any) -> str:

        if value is None:
            return None
        elif isinstance(value, datetime.datetime):
            pattern, tz = formatter
            if tz:
                value = value.astimezone(tz)
            if not pattern:
                if locale_ and 'US' in locale_:
                    format_str = "%m/%d/%y"
                else:
                    format_str = "%d/%m/%y"
                return value.strftime(format_str)
            else:
                if locale_:
                    orig = locale.getlocale()
                    locale.setlocale(locale.LC_ALL, locale_)
                    result = value.strftime(self.java_to_python_format(pattern))
                    locale.setlocale(locale.LC_ALL, orig)
                    return result
                else:
                    return value.strftime(self.java_to_python_format(pattern))
        raise ValueError("Expected `datetime.datetime` input for formatting")

    def format4(
        self,
        value: typing.Any,
        pattern: str,
        locale: typing.Any,
        timeZone: typing.Union[zoneinfo.ZoneInfo, datetime.timezone],
    ) -> str:

        formatter = pattern
        if timeZone is not None:
            formatter = [formatter, timeZone]
        elif isinstance(value, datetime.datetime):
            formatter = [formatter, value.tzinfo]
        return self._format5(value, formatter, locale)

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
        field: str,
    ) -> int:

        if field == 'day_of_year':
            difference = value.timetuple().tm_yday - compare.timetuple().tm_yday
        elif field == 'isocalendar_week':
            difference = value.isocalendar()[1] - compare.isocalendar()[1]
        elif field == 'week_of_month':
            difference = self.get_week_of_month(value) - self.get_week_of_month(compare)
        else:
            difference = getattr(value, field) - getattr(compare, field)
        if difference < 0:
            return -1
        elif difference > 0:
            return 1
        else:
            return 0

    def get_week_of_month(self, dt: datetime) -> int:
        first_day_of_month = dt.replace(day=1)
        adjusted_dom = dt.day + first_day_of_month.weekday()
        return (adjusted_dom - 1) // 7 + 1
    
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

    def _processParsedValue(self, value: typing.Any, formatter: typing.Any) -> typing.Any:

        return value
