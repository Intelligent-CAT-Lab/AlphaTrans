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

    def _processParsedValue(
        self, value: typing.Any, formatter: typing.Union[str, datetime.datetime]
    ) -> typing.Any:

        if isinstance(formatter, str):
            formatter = datetime.datetime.strptime(formatter, "%Y-%m-%d")

        return formatter.date()

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

        # Assuming that the Calendar.YEAR field is equivalent to datetime.date.year
        # If it's not, you'll need to adjust this line
        return self._compare(value.year, compare.year, datetime.date.year)

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

        # The super()._compareQuarters() method is not defined in the provided partial Python translation.
        # If it's defined in another class, you need to import that class and use super() to call it.
        # If it's a static method, you can call it directly.
        # Here, I'm assuming it's a static method and calling it directly.
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

        # The Calendar.MONTH constant is not available in Python's datetime module.
        # Instead, we can use the month attribute of the datetime object.
        # If the input is a datetime object, we can directly access the month attribute.
        # If the input is a date object, we can convert it to a datetime object and then access the month attribute.
        # If the input is a time object, we can convert it to a datetime object and then access the month attribute.
        # If the input is a timedelta object, we can convert it to a datetime object and then access the month attribute.
        # If the input is a timezone object, we can convert it to a datetime object and then access the month attribute.

        if isinstance(value, datetime.datetime):
            value_month = value.month
        elif isinstance(value, datetime.date):
            value_month = value.month
        elif isinstance(value, datetime.time):
            value_month = value.month
        elif isinstance(value, datetime.timedelta):
            value_month = value.month
        elif isinstance(value, datetime.timezone):
            value_month = value.month

        if isinstance(compare, datetime.datetime):
            compare_month = compare.month
        elif isinstance(compare, datetime.date):
            compare_month = compare.month
        elif isinstance(compare, datetime.time):
            compare_month = compare.month
        elif isinstance(compare, datetime.timedelta):
            compare_month = compare.month
        elif isinstance(compare, datetime.timezone):
            compare_month = compare.month

        if value_month > compare_month:
            return 1
        elif value_month < compare_month:
            return -1
        else:
            return 0

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
        return self._compare(value, compare, datetime.WEEK_OF_YEAR)

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

        # Convert the input to datetime.date if they are not already
        if isinstance(value, datetime.datetime):
            value = value.date()
        if isinstance(compare, datetime.datetime):
            compare = compare.date()

        # Compare the dates
        if value < compare:
            return -1
        elif value == compare:
            return 0
        else:
            return 1

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

        if value.tzinfo and value.tzinfo.key == timeZone.key:
            value = value.replace(tzinfo=timeZone)
        else:
            year = value.year
            month = value.month
            day = value.day
            hour = value.hour
            minute = value.minute
            value = datetime.datetime(year, month, day, hour, minute, tzinfo=timeZone)

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
