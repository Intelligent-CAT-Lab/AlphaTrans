from __future__ import annotations
import io
import typing
from typing import *
import datetime
from src.main.org.apache.commons.validator.routines.AbstractCalendarValidator import *


class TimeValidator(AbstractCalendarValidator):

    __VALIDATOR: TimeValidator = TimeValidator.TimeValidator1()

    __serialVersionUID: int = 3494007492269691581

    def _processParsedValue(
        self, value: typing.Any, formatter: typing.Union[str, datetime.datetime]
    ) -> typing.Any:

        if isinstance(formatter, str):
            formatter = datetime.datetime.strptime(formatter, "%Y-%m-%d %H:%M:%S")

        return formatter.date()

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

        return self.compareTime(value, compare, datetime.datetime.HOUR)

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

        # Convert datetime objects to minutes
        def to_minutes(time):
            if isinstance(time, datetime.datetime) or isinstance(time, datetime.date):
                return time.hour * 60 + time.minute
            elif isinstance(time, datetime.time):
                return time.hour * 60 + time.minute
            elif isinstance(time, datetime.timedelta):
                return time.seconds // 60
            elif isinstance(time, datetime.timezone):
                return 0
            else:
                raise TypeError("Unsupported type")

        # Compare minutes
        value_minutes = to_minutes(value)
        compare_minutes = to_minutes(compare)

        if value_minutes < compare_minutes:
            return -1
        elif value_minutes == compare_minutes:
            return 0
        else:
            return 1

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

        return self.compareTime(value, compare, datetime.SECOND)

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

        if isinstance(value, (datetime.datetime, datetime.date)) and isinstance(
            compare, (datetime.datetime, datetime.date)
        ):
            return (value - compare).total_seconds()
        elif isinstance(value, datetime.time) and isinstance(compare, datetime.time):
            return (
                datetime.datetime.combine(datetime.date.today(), value)
                - datetime.datetime.combine(datetime.date.today(), compare)
            ).total_seconds()
        elif isinstance(value, datetime.timedelta) and isinstance(
            compare, datetime.timedelta
        ):
            return (value - compare).total_seconds()
        elif isinstance(value, datetime.timezone) and isinstance(
            compare, datetime.timezone
        ):
            return (value.utcoffset(None) - compare.utcoffset(None)).total_seconds()
        else:
            raise TypeError("Incompatible types for comparison")

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
    def TimeValidator1() -> TimeValidator:

        return TimeValidator(True, 0)

    def __init__(self, strict: bool, timeStyle: int) -> None:

        super().__init__(strict, -1, timeStyle)

    @staticmethod
    def getInstance() -> TimeValidator:

        if not hasattr(TimeValidator, "__VALIDATOR"):
            TimeValidator.__VALIDATOR = TimeValidator()

        return TimeValidator.__VALIDATOR
