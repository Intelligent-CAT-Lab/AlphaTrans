from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.validator.routines.AbstractCalendarValidator import *
import zoneinfo
import datetime
import typing
from typing import *
import io

# Imports End


class DateValidator(AbstractCalendarValidator):

    # Class Fields Begin
    __serialVersionUID: int = None
    __VALIDATOR: DateValidator = None
    # Class Fields End

    # Class Methods Begin
    def _processParsedValue(self, value: typing.Any, formatter: Format) -> typing.Any:
        pass

    def compareYears(
        self,
        value: typing.Union[datetime.datetime, datetime.date],
        compare: typing.Union[datetime.datetime, datetime.date],
        timeZone: typing.Union[zoneinfo.ZoneInfo, datetime.timezone],
    ) -> int:
        pass

    def compareQuarters1(
        self,
        value: typing.Union[datetime.datetime, datetime.date],
        compare: typing.Union[datetime.datetime, datetime.date],
        timeZone: typing.Union[zoneinfo.ZoneInfo, datetime.timezone],
        monthOfFirstQuarter: int,
    ) -> int:
        pass

    def compareQuarters0(
        self,
        value: typing.Union[datetime.datetime, datetime.date],
        compare: typing.Union[datetime.datetime, datetime.date],
        timeZone: typing.Union[zoneinfo.ZoneInfo, datetime.timezone],
    ) -> int:
        pass

    def compareMonths(
        self,
        value: typing.Union[datetime.datetime, datetime.date],
        compare: typing.Union[datetime.datetime, datetime.date],
        timeZone: typing.Union[zoneinfo.ZoneInfo, datetime.timezone],
    ) -> int:
        pass

    def compareWeeks(
        self,
        value: typing.Union[datetime.datetime, datetime.date],
        compare: typing.Union[datetime.datetime, datetime.date],
        timeZone: typing.Union[zoneinfo.ZoneInfo, datetime.timezone],
    ) -> int:
        pass

    def compareDates(
        self,
        value: typing.Union[datetime.datetime, datetime.date],
        compare: typing.Union[datetime.datetime, datetime.date],
        timeZone: typing.Union[zoneinfo.ZoneInfo, datetime.timezone],
    ) -> int:
        pass

    def validate7(
        self,
        value: str,
        pattern: str,
        locale: typing.Any,
        timeZone: typing.Union[zoneinfo.ZoneInfo, datetime.timezone],
    ) -> typing.Union[datetime.datetime, datetime.date]:
        pass

    def validate6(
        self, value: str, pattern: str, locale: typing.Any
    ) -> typing.Union[datetime.datetime, datetime.date]:
        pass

    def validate5(
        self,
        value: str,
        locale: typing.Any,
        timeZone: typing.Union[zoneinfo.ZoneInfo, datetime.timezone],
    ) -> typing.Union[datetime.datetime, datetime.date]:
        pass

    def validate4(
        self, value: str, locale: typing.Any
    ) -> typing.Union[datetime.datetime, datetime.date]:
        pass

    def validate3(
        self,
        value: str,
        pattern: str,
        timeZone: typing.Union[zoneinfo.ZoneInfo, datetime.timezone],
    ) -> typing.Union[datetime.datetime, datetime.date]:
        pass

    def validate2(
        self, value: str, pattern: str
    ) -> typing.Union[datetime.datetime, datetime.date]:
        pass

    def validate1(
        self, value: str, timeZone: typing.Union[zoneinfo.ZoneInfo, datetime.timezone]
    ) -> typing.Union[datetime.datetime, datetime.date]:
        pass

    def validate0(self, value: str) -> typing.Union[datetime.datetime, datetime.date]:
        pass

    @staticmethod
    def DateValidator1() -> DateValidator:
        pass

    def __init__(self, strict: bool, dateStyle: int) -> None:
        pass

    @staticmethod
    def getInstance() -> DateValidator:
        pass

    def __getCalendar(
        self,
        value: typing.Union[datetime.datetime, datetime.date],
        timeZone: typing.Union[zoneinfo.ZoneInfo, datetime.timezone],
    ) -> typing.Union[
        datetime.datetime,
        datetime.date,
        datetime.time,
        datetime.timedelta,
        datetime.timezone,
    ]:
        pass

    # Class Methods End
