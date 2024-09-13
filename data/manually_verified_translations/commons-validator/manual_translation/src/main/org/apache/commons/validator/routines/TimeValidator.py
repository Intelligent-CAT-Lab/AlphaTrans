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

    def _format5(self, value: typing.Any, formatter: typing.Any, locale_: typing.Any) -> str:
        if value is None:
            return None
        elif isinstance(value, datetime.datetime):
            pattern, tz = formatter
            if tz:
                value = value.astimezone(tz)
            if not pattern:
                if locale_:
                    format_str = "%I:%M %p"
                    orig = locale.getlocale()
                    locale.setlocale(locale.LC_ALL, locale_)
                    result = value.strftime(format_str).lstrip("0")
                    locale.setlocale(locale.LC_ALL, orig) 
                else:
                    format_str = "%H:%M"
                    result = value.strftime(format_str)
                return result
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
    
    def _processParsedValue(self, value: typing.Any, formatter: typing.Any) -> typing.Any:
        return value

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

        return self._compareTime(value, compare, "HOUR_OF_DAY")

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

        return self._compareTime(value, compare, "MINUTE")

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

        return self._compareTime(value, compare, "SECOND")

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

        return self._compareTime(value, compare, "MILLISECOND")

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

        return self._parse(value, pattern, locale, zoneinfo.ZoneInfo("GMT"))

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

        return self._parse(value, None, None, zoneinfo.ZoneInfo("GMT"))

    @staticmethod
    def TimeValidator1() -> TimeValidator:
        return TimeValidator(True, 3)

    def __init__(self, strict: bool, timeStyle: int) -> None:
        super().__init__(strict, -1, timeStyle)

    @staticmethod
    def getInstance() -> TimeValidator:
        return TimeValidator.__VALIDATOR


TimeValidator.initialize_fields()
