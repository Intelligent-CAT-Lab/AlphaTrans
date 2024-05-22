from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.validator.routines.TimeValidator import *
import unittest
import datetime
import typing
from typing import *
import io

# Imports End


class TimeValidatorTest(unittest.TestCase):

    # Class Fields Begin
    __origDefault: typing.Any = None
    __defaultZone: datetime.timezone = None
    _GMT: datetime.timezone = None
    _EST: datetime.timezone = None
    _validator: TimeValidator = None
    _patternValid: typing.List[str] = None
    _patternExpect: typing.List[typing.Union[datetime.date, datetime.datetime]] = None
    _localeValid: typing.List[str] = None
    _localeExpect: typing.List[typing.Union[datetime.date, datetime.datetime]] = None
    _patternInvalid: typing.List[str] = None
    _localeInvalid: typing.List[str] = None
    # Class Fields End

    # Class Methods Begin
    def _tearDown(self) -> None:
        pass

    def _setUp(self) -> None:
        pass

    @staticmethod
    def _createDate(
        zone: datetime.timezone, time: int, millisecond: int
    ) -> typing.Union[datetime.date, datetime.datetime]:
        pass

    @staticmethod
    def _createTime(
        zone: datetime.timezone, time: int, millisecond: int
    ) -> typing.Union[
        datetime.datetime,
        datetime.date,
        datetime.time,
        datetime.timedelta,
        datetime.timezone,
    ]:
        pass

    def testCompare(self) -> None:
        pass

    def testFormat(self) -> None:
        pass

    def testTimeZone(self) -> None:
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
