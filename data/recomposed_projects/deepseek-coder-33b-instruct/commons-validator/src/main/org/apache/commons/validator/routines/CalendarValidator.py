from __future__ import annotations
import io
import typing
from typing import *
import datetime
from src.main.org.apache.commons.validator.routines.AbstractCalendarValidator import *


class CalendarValidator(AbstractCalendarValidator):

    __VALIDATOR: CalendarValidator = CalendarValidator.CalendarValidator1()

    __serialVersionUID: int = 9109652318762134167

    def _processParsedValue(
        self, value: typing.Any, formatter: typing.Union[str, datetime.datetime]
    ) -> typing.Any:

        if isinstance(formatter, str):
            return datetime.datetime.strptime(formatter, "%Y-%m-%d").date()
        elif isinstance(formatter, datetime.datetime):
            return formatter.date()
        else:
            raise TypeError("formatter must be a string or a datetime object")

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

        # Check if the input values are datetime.datetime or datetime.date objects
        if isinstance(value, (datetime.datetime, datetime.date)) and isinstance(
            compare, (datetime.datetime, datetime.date)
        ):
            return self.compare(value, compare, datetime.YEAR)
        else:
            raise TypeError(
                "Both value and compare must be datetime.datetime or datetime.date objects"
            )

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

        return self.compareQuarters(value, compare, monthOfFirstQuarter)

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

        # Check if the input values are datetime objects
        if isinstance(value, datetime.datetime) and isinstance(
            compare, datetime.datetime
        ):
            return self.compare(value, compare, datetime.MONTH)
        else:
            raise TypeError("Both inputs must be datetime objects")

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

        if isinstance(value, datetime.datetime) or isinstance(value, datetime.date):
            value_week = value.isocalendar()[1]
        else:
            raise TypeError("value must be a datetime.datetime or datetime.date object")

        if isinstance(compare, datetime.datetime) or isinstance(compare, datetime.date):
            compare_week = compare.isocalendar()[1]
        else:
            raise TypeError(
                "compare must be a datetime.datetime or datetime.date object"
            )

        return self.compare(value_week, compare_week, Calendar.WEEK_OF_YEAR)

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

        # Assuming that the compare method is a static method in the AbstractCalendarValidator class
        # If it's not, you need to create an instance of AbstractCalendarValidator
        # and call the compare method on that instance
        return AbstractCalendarValidator.compare(value, compare, datetime.DATE)

    @staticmethod
    def adjustToTimeZone(
        value: typing.Union[
            datetime.datetime,
            datetime.date,
            datetime.time,
            datetime.timedelta,
            datetime.timezone,
        ],
        timeZone: datetime.timezone,
    ) -> None:

        if value.tzinfo and value.tzinfo.utcoffset(value) == timeZone.utcoffset(value):
            value = value.replace(tzinfo=timeZone)
        else:
            year = value.year
            month = value.month
            day = value.day
            hour = value.hour
            minute = value.minute
            value = datetime.datetime(year, month, day, hour, minute, tzinfo=timeZone)

    def validate7(
        self, value: str, pattern: str, locale: typing.Any, timeZone: datetime.timezone
    ) -> typing.Union[
        datetime.datetime,
        datetime.date,
        datetime.time,
        datetime.timedelta,
        datetime.timezone,
    ]:

        return self.parse(value, pattern, locale, timeZone)

    def validate6(self, value: str, pattern: str, locale: typing.Any) -> typing.Union[
        datetime.datetime,
        datetime.date,
        datetime.time,
        datetime.timedelta,
        datetime.timezone,
    ]:

        return self.parse(value, pattern, locale, None)

    def validate5(
        self, value: str, locale: typing.Any, timeZone: datetime.timezone
    ) -> typing.Union[
        datetime.datetime,
        datetime.date,
        datetime.time,
        datetime.timedelta,
        datetime.timezone,
    ]:

        return self.parse(value, None, locale, timeZone)

    def validate4(self, value: str, locale: typing.Any) -> typing.Union[
        datetime.datetime,
        datetime.date,
        datetime.time,
        datetime.timedelta,
        datetime.timezone,
    ]:

        return self.parse(value, None, locale, None)

    def validate3(
        self, value: str, pattern: str, timeZone: datetime.timezone
    ) -> typing.Union[
        datetime.datetime,
        datetime.date,
        datetime.time,
        datetime.timedelta,
        datetime.timezone,
    ]:

        return self.parse(value, pattern, None, timeZone)

    def validate2(self, value: str, pattern: str) -> typing.Union[
        datetime.datetime,
        datetime.date,
        datetime.time,
        datetime.timedelta,
        datetime.timezone,
    ]:

        return self.parse(value, pattern, None, None)

    def validate1(self, value: str, timeZone: datetime.timezone) -> typing.Union[
        datetime.datetime,
        datetime.date,
        datetime.time,
        datetime.timedelta,
        datetime.timezone,
    ]:

        return self.parse(value, None, None, timeZone)

    def validate0(self, value: str) -> typing.Union[
        datetime.datetime,
        datetime.date,
        datetime.time,
        datetime.timedelta,
        datetime.timezone,
    ]:

        return self.parse(value, None, None, None)

    @staticmethod
    def CalendarValidator1() -> CalendarValidator:

        # The DateFormat.SHORT constant is not available in Python's datetime module.
        # We can use the equivalent constant from the datetime module.
        # Here, we are assuming that the equivalent constant is datetime.SHORT.
        # If it's not, you need to replace it with the correct constant.

        return CalendarValidator(True, datetime.SHORT)

    def __init__(self, strict: bool, dateStyle: int) -> None:

        # Call the superclass's constructor
        super().__init__(strict, dateStyle, -1)

    @staticmethod
    def getInstance() -> CalendarValidator:

        if not hasattr(CalendarValidator, "__VALIDATOR"):
            CalendarValidator.__VALIDATOR = CalendarValidator()

        return CalendarValidator.__VALIDATOR
