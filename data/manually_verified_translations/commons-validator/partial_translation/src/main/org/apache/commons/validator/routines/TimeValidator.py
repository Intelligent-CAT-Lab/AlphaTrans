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


class TimeValidator(AbstractCalendarValidator):

    __VALIDATOR: TimeValidator = None
    __serialVersionUID: int = 3494007492269691581

    @staticmethod
    def initialize_fields() -> None:
        TimeValidator.__VALIDATOR: TimeValidator = TimeValidator.TimeValidator1()

    def _processParsedValue(self, value: typing.Any, formatter: Format) -> typing.Any:
        return formatter.getCalendar()

    def compareHours(
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

        return self._compareTime(value, compare, datetime.timezone.utc)

    def compareMinutes(
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

        return self._compareTime(value, compare, datetime.MINUTE)

    def compareSeconds(
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

        if isinstance(value, datetime.datetime):
            value = value.second
        elif isinstance(value, datetime.time):
            value = value.second
        elif isinstance(value, datetime.timedelta):
            value = value.seconds
        elif isinstance(value, datetime.date):
            value = 0
        elif isinstance(value, datetime.timezone):
            value = 0

        if isinstance(compare, datetime.datetime):
            compare = compare.second
        elif isinstance(compare, datetime.time):
            compare = compare.second
        elif isinstance(compare, datetime.timedelta):
            compare = compare.seconds
        elif isinstance(compare, datetime.date):
            compare = 0
        elif isinstance(compare, datetime.timezone):
            compare = 0

        if value < compare:
            return -1
        elif value == compare:
            return 0
        else:
            return 1

    def compareTime(
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

        return self._compareTime(value, compare, datetime.timezone.utc)

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

        value = None if value is None else value.strip()
        if value is None or len(value) == 0:
            return None
        formatter = self._getFormat0(pattern, locale)
        if timeZone is not None:
            formatter.setTimeZone(timeZone)
        return self._parse(value, formatter)

    def validate6(self, value: str, pattern: str, locale: typing.Any) -> typing.Union[
        datetime.datetime,
        datetime.date,
        datetime.time,
        datetime.timedelta,
        datetime.timezone,
    ]:

        value = None if value is None else value.strip()
        if value is None or len(value) == 0:
            return None
        formatter = self._getFormat0(pattern, locale)
        return self._parse(value, formatter)

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

        value = None if value is None else value.strip()
        if value is None or len(value) == 0:
            return None
        formatter = self._getFormat0(None, locale)
        if timeZone is not None:
            formatter.setTimeZone(timeZone)
        return self._parse(value, formatter)

    def validate4(self, value: str, locale: typing.Any) -> typing.Union[
        datetime.datetime,
        datetime.date,
        datetime.time,
        datetime.timedelta,
        datetime.timezone,
    ]:

        value = None if value is None else value.strip()
        if value is None or len(value) == 0:
            return None
        formatter = self._getFormat0(None, locale)
        return self._parse(value, formatter)

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

        value = None if value is None else value.strip()
        if value is None or len(value) == 0:
            return None
        formatter = self._getFormat0(pattern, None)
        if timeZone is not None:
            formatter.setTimeZone(timeZone)
        return self._parse(value, formatter)

    def validate2(self, value: str, pattern: str) -> typing.Union[
        datetime.datetime,
        datetime.date,
        datetime.time,
        datetime.timedelta,
        datetime.timezone,
    ]:

        value = None if value is None else value.strip()
        if value is None or len(value) == 0:
            return None
        formatter = self._getFormat0(pattern, None)
        return self._parse(value, formatter)

    def validate1(
        self, value: str, timeZone: typing.Union[zoneinfo.ZoneInfo, datetime.timezone]
    ) -> typing.Union[
        datetime.datetime,
        datetime.date,
        datetime.time,
        datetime.timedelta,
        datetime.timezone,
    ]:

        value = None if value is None else value.strip()
        if value is None or len(value) == 0:
            return None
        formatter = self._getFormat0(None, None)
        if timeZone is not None:
            formatter.setTimeZone(timeZone)
        return self._parse(value, formatter)

    def validate0(self, value: str) -> typing.Union[
        datetime.datetime,
        datetime.date,
        datetime.time,
        datetime.timedelta,
        datetime.timezone,
    ]:

        value = None if value is None else value.strip()
        if value is None or len(value) == 0:
            return None
        formatter = self._getFormat0(None, None)
        return self._parse(value, formatter)

    @staticmethod
    def TimeValidator1() -> TimeValidator:
        return TimeValidator(True, 3)

    def __init__(self, strict: bool, timeStyle: int) -> None:
        super().__init__(strict, -1, timeStyle)

    @staticmethod
    def getInstance() -> TimeValidator:
        return TimeValidator.__VALIDATOR


TimeValidator.initialize_fields()
