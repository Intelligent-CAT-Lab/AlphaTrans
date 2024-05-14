# Imports Begin
from src.main.org.apache.commons.validator.routines.AbstractCalendarValidator import *
import datetime
import typing
from abc import ABC

# Imports End


class AbstractCalendarValidatorTest(TestCase, ABC):

    # Class Fields Begin
    _localeInvalid: typing.List[str] = None
    _validator: AbstractCalendarValidator = None
    _GMT: datetime.timezone = None
    _EST: datetime.timezone = None
    _EET: datetime.timezone = None
    _UTC: datetime.timezone = None
    _patternValid: typing.List[str] = None
    _localeValid: typing.List[str] = None
    _patternExpect: typing.List[typing.Union[datetime.date, datetime.datetime]] = None
    _patternInvalid: typing.List[str] = None
    # Class Fields End

    # Class Methods Begin
    def _tearDown(self) -> None:
        pass

    def _setUp(self) -> None:
        pass

    @staticmethod
    def _createDate(
        zone: datetime.timezone, date: int, time: int
    ) -> typing.Union[datetime.date, datetime.datetime]:
        pass

    @staticmethod
    def _createCalendar(zone: datetime.timezone, date: int, time: int) -> typing.Union[
        datetime.datetime,
        datetime.date,
        datetime.time,
        datetime.timedelta,
        datetime.timezone,
    ]:
        pass

    def testSerialization(self) -> None:
        pass

    def testFormat(self) -> None:
        pass

    def testLocaleInvalid(self) -> None:
        pass

    def testLocaleValid(self) -> None:
        pass

    def testPatternInvalid(self) -> None:
        pass

    def testPatternValid(self) -> None:
        pass

    def __init__(self, name: str) -> None:
        pass

    # Class Methods End
