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


class DateValidator(AbstractCalendarValidator):

    __VALIDATOR: DateValidator = None
    __serialVersionUID: int = -3966328400469953190

    @staticmethod
    def initialize_fields() -> None:
        DateValidator.__VALIDATOR: DateValidator = DateValidator.DateValidator1()

    def _processParsedValue(self, value: typing.Any, formatter: Format) -> typing.Any:
        return value

    def compareYears(
        self,
        value: typing.Union[datetime.datetime, datetime.date],
        compare: typing.Union[datetime.datetime, datetime.date],
        timeZone: typing.Union[zoneinfo.ZoneInfo, datetime.timezone],
    ) -> int:

        calendarValue = self.__getCalendar(value, timeZone)
        calendarCompare = self.__getCalendar(compare, timeZone)
        return self._compare(calendarValue, calendarCompare, datetime.timezone.utc)

    def compareQuarters1(
        self,
        value: typing.Union[datetime.datetime, datetime.date],
        compare: typing.Union[datetime.datetime, datetime.date],
        timeZone: typing.Union[zoneinfo.ZoneInfo, datetime.timezone],
        monthOfFirstQuarter: int,
    ) -> int:

        calendarValue = self.__getCalendar(value, timeZone)
        calendarCompare = self.__getCalendar(compare, timeZone)
        return self._compareQuarters(
            calendarValue, calendarCompare, monthOfFirstQuarter
        )

    def compareQuarters0(
        self,
        value: typing.Union[datetime.datetime, datetime.date],
        compare: typing.Union[datetime.datetime, datetime.date],
        timeZone: typing.Union[zoneinfo.ZoneInfo, datetime.timezone],
    ) -> int:

        return self.compareQuarters1(value, compare, timeZone, 1)

    def compareMonths(
        self,
        value: typing.Union[datetime.datetime, datetime.date],
        compare: typing.Union[datetime.datetime, datetime.date],
        timeZone: typing.Union[zoneinfo.ZoneInfo, datetime.timezone],
    ) -> int:

        calendarValue = self.__getCalendar(value, timeZone)
        calendarCompare = self.__getCalendar(compare, timeZone)
        return self._compare(calendarValue, calendarCompare, datetime.timezone.utc)

    def compareWeeks(
        self,
        value: typing.Union[datetime.datetime, datetime.date],
        compare: typing.Union[datetime.datetime, datetime.date],
        timeZone: typing.Union[zoneinfo.ZoneInfo, datetime.timezone],
    ) -> int:

        calendarValue = self.__getCalendar(value, timeZone)
        calendarCompare = self.__getCalendar(compare, timeZone)
        return self._compare(calendarValue, calendarCompare, datetime.WEEK_OF_YEAR)

    def compareDates(
        self,
        value: typing.Union[datetime.datetime, datetime.date],
        compare: typing.Union[datetime.datetime, datetime.date],
        timeZone: typing.Union[zoneinfo.ZoneInfo, datetime.timezone],
    ) -> int:

        calendarValue = self.__getCalendar(value, timeZone)
        calendarCompare = self.__getCalendar(compare, timeZone)

        return self._compare(calendarValue, calendarCompare, datetime.timezone.utc)

    def validate7(
        self,
        value: str,
        pattern: str,
        locale: typing.Any,
        timeZone: typing.Union[zoneinfo.ZoneInfo, datetime.timezone],
    ) -> typing.Union[datetime.datetime, datetime.date]:

        value = None if value is None else value.strip()
        if value is None or len(value) == 0:
            return None
        formatter = self._getFormat0(pattern, locale)
        if timeZone is not None:
            formatter.setTimeZone(timeZone)
        return self._parse(value, formatter)

    def validate6(
        self, value: str, pattern: str, locale: typing.Any
    ) -> typing.Union[datetime.datetime, datetime.date]:

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
    ) -> typing.Union[datetime.datetime, datetime.date]:

        value = None if value is None else value.strip()
        if value is None or len(value) == 0:
            return None
        formatter = self._getFormat0(None, locale)
        if timeZone is not None:
            formatter.setTimeZone(timeZone)
        return self._parse(value, formatter)

    def validate4(
        self, value: str, locale: typing.Any
    ) -> typing.Union[datetime.datetime, datetime.date]:

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
    ) -> typing.Union[datetime.datetime, datetime.date]:

        value = None if value is None else value.strip()
        if value is None or len(value) == 0:
            return None
        formatter = self._getFormat0(pattern, None)
        if timeZone is not None:
            formatter.setTimeZone(timeZone)
        return self._parse(value, formatter)

    def validate2(
        self, value: str, pattern: str
    ) -> typing.Union[datetime.datetime, datetime.date]:

        value = None if value is None else value.strip()
        if value is None or len(value) == 0:
            return None
        formatter = self._getFormat0(pattern, None)
        return self._parse(value, formatter)

    def validate1(
        self, value: str, timeZone: typing.Union[zoneinfo.ZoneInfo, datetime.timezone]
    ) -> typing.Union[datetime.datetime, datetime.date]:

        value = None if value is None else value.strip()
        if value is None or len(value) == 0:
            return None
        formatter = self._getFormat0(None, None)
        if timeZone is not None:
            formatter.setTimeZone(timeZone)
        return self._parse(value, formatter)

    def validate0(self, value: str) -> typing.Union[datetime.datetime, datetime.date]:

        value = None if value is None else value.strip()
        if value is None or len(value) == 0:
            return None
        formatter = self._getFormat0(None, None)
        return self._parse(value, formatter)

    @staticmethod
    def DateValidator1() -> DateValidator:
        return DateValidator(True, 3)

    def __init__(self, strict: bool, dateStyle: int) -> None:
        super().__init__(strict, dateStyle, -1)

    @staticmethod
    def getInstance() -> DateValidator:
        return DateValidator.__VALIDATOR

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

        if timeZone is not None:
            calendar = value.replace(tzinfo=timeZone)
        else:
            calendar = value
        return calendar


DateValidator.initialize_fields()
