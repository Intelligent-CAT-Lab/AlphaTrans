from __future__ import annotations
import io
import typing
from typing import *
import datetime
from src.main.org.apache.commons.validator.routines.AbstractCalendarValidator import *


class DateValidator(AbstractCalendarValidator):

    __VALIDATOR: DateValidator = DateValidator.DateValidator1()

    __serialVersionUID: int = -3966328400469953190

    def _processParsedValue(
        self, value: typing.Any, formatter: typing.Union[str, datetime.datetime]
    ) -> typing.Any:

        return value

    def compareYears(
        self,
        value: typing.Union[datetime.date, datetime.datetime],
        compare: typing.Union[datetime.date, datetime.datetime],
        timeZone: datetime.timezone,
    ) -> int:

        calendarValue = self.__getCalendar(value, timeZone)
        calendarCompare = self.__getCalendar(compare, timeZone)

        return self.compare(
            calendarValue, calendarCompare, datetime.datetime.now().year
        )

    def compareQuarters1(
        self,
        value: typing.Union[datetime.date, datetime.datetime],
        compare: typing.Union[datetime.date, datetime.datetime],
        timeZone: datetime.timezone,
        monthOfFirstQuarter: int,
    ) -> int:

        calendarValue = self.__getCalendar(value, timeZone)
        calendarCompare = self.__getCalendar(compare, timeZone)
        return self.compareQuarters(calendarValue, calendarCompare, monthOfFirstQuarter)

    def compareQuarters0(
        self,
        value: typing.Union[datetime.date, datetime.datetime],
        compare: typing.Union[datetime.date, datetime.datetime],
        timeZone: datetime.timezone,
    ) -> int:

        return self.compareQuarters1(value, compare, timeZone, 1)

    def compareMonths(
        self,
        value: typing.Union[datetime.date, datetime.datetime],
        compare: typing.Union[datetime.date, datetime.datetime],
        timeZone: datetime.timezone,
    ) -> int:

        calendarValue = self.__getCalendar(value, timeZone)
        calendarCompare = self.__getCalendar(compare, timeZone)

        return self.compare(calendarValue, calendarCompare, Calendar.MONTH)

    def compareWeeks(
        self,
        value: typing.Union[datetime.date, datetime.datetime],
        compare: typing.Union[datetime.date, datetime.datetime],
        timeZone: datetime.timezone,
    ) -> int:

        calendarValue = self.__getCalendar(value, timeZone)
        calendarCompare = self.__getCalendar(compare, timeZone)
        return self.compare(
            calendarValue, calendarCompare, datetime.datetime.WEEK_OF_YEAR
        )

    def compareDates(
        self,
        value: typing.Union[datetime.date, datetime.datetime],
        compare: typing.Union[datetime.date, datetime.datetime],
        timeZone: datetime.timezone,
    ) -> int:

        calendarValue = self.__getCalendar(value, timeZone)
        calendarCompare = self.__getCalendar(compare, timeZone)

        return self.compare(calendarValue, calendarCompare, datetime.date.today().day)

    def validate7(
        self, value: str, pattern: str, locale: typing.Any, timeZone: datetime.timezone
    ) -> typing.Union[datetime.date, datetime.datetime]:

        return self.parse(value, pattern, locale, timeZone)

    def validate6(
        self, value: str, pattern: str, locale: typing.Any
    ) -> typing.Union[datetime.date, datetime.datetime]:

        return self.parse(value, pattern, locale, None)

    def validate5(
        self, value: str, locale: typing.Any, timeZone: datetime.timezone
    ) -> typing.Union[datetime.date, datetime.datetime]:

        return self.parse(value, None, locale, timeZone)

    def validate4(
        self, value: str, locale: typing.Any
    ) -> typing.Union[datetime.date, datetime.datetime]:

        return self.parse(value, None, locale, None)

    def validate3(
        self, value: str, pattern: str, timeZone: datetime.timezone
    ) -> typing.Union[datetime.date, datetime.datetime]:

        return self.parse(value, pattern, None, timeZone)

    def validate2(
        self, value: str, pattern: str
    ) -> typing.Union[datetime.date, datetime.datetime]:

        return self.parse(value, pattern, None, None)

    def validate1(
        self, value: str, timeZone: datetime.timezone
    ) -> typing.Union[datetime.date, datetime.datetime]:

        return self.parse(value, None, None, timeZone)

    def validate0(self, value: str) -> typing.Union[datetime.date, datetime.datetime]:

        return self.parse(value, None, None, None)

    @staticmethod
    def DateValidator1() -> DateValidator:

        # The DateFormat.SHORT in Java is equivalent to datetime.SHORT in Python
        return DateValidator(True, datetime.SHORT)

    def __init__(self, strict: bool, dateStyle: int) -> None:

        super().__init__(strict, dateStyle, -1)

    @staticmethod
    def getInstance() -> DateValidator:

        if not hasattr(DateValidator, "__VALIDATOR"):
            DateValidator.__VALIDATOR = DateValidator()

        return DateValidator.__VALIDATOR

    def __getCalendar(
        self,
        value: typing.Union[datetime.date, datetime.datetime],
        timeZone: datetime.timezone,
    ) -> typing.Union[
        datetime.datetime,
        datetime.date,
        datetime.time,
        datetime.timedelta,
        datetime.timezone,
    ]:

        calendar = None
        if timeZone is not None:
            calendar = datetime.datetime.now(timeZone)
        else:
            calendar = datetime.datetime.now()
        calendar = calendar.replace(
            hour=value.hour, minute=value.minute, second=value.second
        )
        return calendar
