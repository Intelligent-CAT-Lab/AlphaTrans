from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.validator.routines.AbstractCalendarValidator import *
import zoneinfo
import datetime
import typing
from typing import *
import io

# Imports End


class CalendarValidator(AbstractCalendarValidator):

    # Class Fields Begin
    __serialVersionUID: int = None
    __VALIDATOR: CalendarValidator = None
    # Class Fields End

    # Class Methods Begin
    def _processParsedValue(self, value: typing.Any, formatter: Format) -> typing.Any:
        pass

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
        pass

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
        pass

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
        pass

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
        pass

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
        pass

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
        pass

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
    ) -> None:
        pass

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
        pass

    def validate6(self, value: str, pattern: str, locale: typing.Any) -> typing.Union[
        datetime.datetime,
        datetime.date,
        datetime.time,
        datetime.timedelta,
        datetime.timezone,
    ]:
        pass

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
        pass

    def validate4(self, value: str, locale: typing.Any) -> typing.Union[
        datetime.datetime,
        datetime.date,
        datetime.time,
        datetime.timedelta,
        datetime.timezone,
    ]:
        pass

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
        pass

    def validate2(self, value: str, pattern: str) -> typing.Union[
        datetime.datetime,
        datetime.date,
        datetime.time,
        datetime.timedelta,
        datetime.timezone,
    ]:
        pass

    def validate1(
        self, value: str, timeZone: typing.Union[zoneinfo.ZoneInfo, datetime.timezone]
    ) -> typing.Union[
        datetime.datetime,
        datetime.date,
        datetime.time,
        datetime.timedelta,
        datetime.timezone,
    ]:
        pass

    def validate0(self, value: str) -> typing.Union[
        datetime.datetime,
        datetime.date,
        datetime.time,
        datetime.timedelta,
        datetime.timezone,
    ]:
        pass

    @staticmethod
    def CalendarValidator1() -> CalendarValidator:
        pass

    def __init__(self, strict: bool, dateStyle: int) -> None:
        pass

    @staticmethod
    def getInstance() -> CalendarValidator:
        pass

    # Class Methods End
