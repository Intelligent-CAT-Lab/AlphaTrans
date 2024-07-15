from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.validator.routines.AbstractFormatValidator import *
import zoneinfo
import datetime
import typing
from typing import *
import io
from abc import ABC

# Imports End


class AbstractCalendarValidator(AbstractFormatValidator, ABC):

    # Class Fields Begin
    __serialVersionUID: int = None
    __dateStyle: int = None
    __timeStyle: int = None
    # Class Fields End

    # Class Methods Begin
    def _getFormat(self, pattern: str, locale: typing.Any) -> Format:
        pass

    def isValid3(self, value: str, pattern: str, locale: typing.Any) -> bool:
        pass

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
        pass

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
        pass

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
        pass

    def _getFormat1(self, locale: typing.Any) -> Format:
        pass

    def _getFormat0(self, pattern: str, locale: typing.Any) -> Format:
        pass

    def _parse(
        self,
        value: str,
        pattern: str,
        locale: typing.Any,
        timeZone: typing.Union[zoneinfo.ZoneInfo, datetime.timezone],
    ) -> typing.Any:
        pass

    def _format5(self, value: typing.Any, formatter: Format) -> str:
        pass

    def format4(
        self,
        value: typing.Any,
        pattern: str,
        locale: typing.Any,
        timeZone: typing.Union[zoneinfo.ZoneInfo, datetime.timezone],
    ) -> str:
        pass

    def format3(self, value: typing.Any, pattern: str, locale: typing.Any) -> str:
        pass

    def format2(
        self,
        value: typing.Any,
        locale: typing.Any,
        timeZone: typing.Union[zoneinfo.ZoneInfo, datetime.timezone],
    ) -> str:
        pass

    def format1(
        self,
        value: typing.Any,
        pattern: str,
        timeZone: typing.Union[zoneinfo.ZoneInfo, datetime.timezone],
    ) -> str:
        pass

    def format0(
        self,
        value: typing.Any,
        timeZone: typing.Union[zoneinfo.ZoneInfo, datetime.timezone],
    ) -> str:
        pass

    def __init__(self, strict: bool, dateStyle: int, timeStyle: int) -> None:
        pass

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
        pass

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
        pass

    def _processParsedValue(self, value: typing.Any, formatter: Format) -> typing.Any:
        pass

    # Class Methods End
