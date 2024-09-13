from __future__ import annotations
import time
import locale
import re
import io
import typing
from typing import *
import datetime
import zoneinfo
from src.main.org.apache.commons.validator.routines.AbstractCalendarValidator import *


class CalendarValidator(AbstractCalendarValidator):

    __VALIDATOR: CalendarValidator = None
    __serialVersionUID: int = 9109652318762134167

    @staticmethod
    def initialize_fields() -> None:
        CalendarValidator.__VALIDATOR: CalendarValidator = (
            CalendarValidator.CalendarValidator1()
        )

    def _processParsedValue(self, value: typing.Any, formatter: typing.Any) -> typing.Any:
        return value

    def compareYears(
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
    ) -> int:

        return self._compare(value, compare, "YEAR")

    def compareQuarters1(
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

        return self._compareQuarters(value, compare, monthOfFirstQuarter)

    def compareQuarters0(
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
    ) -> int:

        return self.compareQuarters1(value, compare, 1)

    def compareMonths(
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
    ) -> int:

        return self._compare(value, compare, "MONTH")

    def compareWeeks(
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
    ) -> int:

        return self._compare(value, compare, "WEEK_OF_YEAR")

    def compareDates(
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
    ) -> int:

        return self._compare(value, compare, "DATE")

    @staticmethod
    def adjustToTimeZone(
        value: typing.Union[
            datetime.datetime,
            datetime.date,
            datetime.time,
            datetime.timedelta,
            datetime.timezone,
        ],
        timeZone: typing.Union[zoneinfo.ZoneInfo, datetime.timezone],
    ) -> datetime.datetime:
        
        if not isinstance(value, datetime.datetime):
            raise TypeError("Adjusting time zone only works for `datetime.datetime` objects")

        now = datetime.datetime.now()
        if value.tzinfo and\
            now.astimezone(value.tzinfo).utcoffset() == now.astimezone(timeZone).utcoffset():
            value = value.replace(tzinfo=timeZone)
        else:
            year = value.year
            month = value.month
            day = value.day
            hour = value.hour
            minute = value.minute
            second = value.second
            microsecond = value.microsecond
            value = datetime.datetime(
                year, month, day, hour, minute, second, microsecond, tzinfo=timeZone
            )
        return value

    def validate7(
        self,
        value: str,
        pattern: str,
        locale: typing.Any,
        timeZone: typing.Union[zoneinfo.ZoneInfo, datetime.timezone],
    ) -> typing.Union[
        datetime.datetime,
        datetime.date,
        datetime.time,
        datetime.timedelta,
        datetime.timezone,
    ]:
        return self._parse(value, pattern, locale, timeZone)

    def validate6(self, value: str, pattern: str, locale: typing.Any) -> typing.Union[
        datetime.datetime,
        datetime.date,
        datetime.time,
        datetime.timedelta,
        datetime.timezone,
    ]:
        return self._parse(value, pattern, locale, None)

    def validate5(
        self,
        value: str,
        locale: typing.Any,
        timeZone: typing.Union[zoneinfo.ZoneInfo, datetime.timezone],
    ) -> typing.Union[
        datetime.datetime,
        datetime.date,
        datetime.time,
        datetime.timedelta,
        datetime.timezone,
    ]:
        return self._parse(value, None, locale, timeZone)

    def validate4(self, value: str, locale: typing.Any) -> typing.Union[
        datetime.datetime,
        datetime.date,
        datetime.time,
        datetime.timedelta,
        datetime.timezone,
    ]:
        return self._parse(value, None, locale, None)

    def validate3(
        self,
        value: str,
        pattern: str,
        timeZone: typing.Union[zoneinfo.ZoneInfo, datetime.timezone],
    ) -> typing.Union[
        datetime.datetime,
        datetime.date,
        datetime.time,
        datetime.timedelta,
        datetime.timezone,
    ]:
        return self._parse(value, pattern, None, timeZone)

    def validate2(self, value: str, pattern: str) -> typing.Union[
        datetime.datetime,
        datetime.date,
        datetime.time,
        datetime.timedelta,
        datetime.timezone,
    ]:
        return self._parse(value, pattern, None, None)

    def validate1(
        self, value: str, timeZone: typing.Union[zoneinfo.ZoneInfo, datetime.timezone]
    ) -> typing.Union[
        datetime.datetime,
        datetime.date,
        datetime.time,
        datetime.timedelta,
        datetime.timezone,
    ]:
        return self._parse(value, None, None, timeZone)

    def validate0(self, value: str) -> typing.Union[
        datetime.datetime,
        datetime.date,
        datetime.time,
        datetime.timedelta,
        datetime.timezone,
    ]:
        return self._parse(value, None, None, None)

    @staticmethod
    def CalendarValidator1() -> CalendarValidator:
        return CalendarValidator(True, 3)

    def __init__(self, strict: bool, dateStyle: int) -> None:
        super().__init__(strict, dateStyle, -1)

    @staticmethod
    def getInstance() -> CalendarValidator:
        return CalendarValidator.__VALIDATOR


CalendarValidator.initialize_fields()
