from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.validator.routines.AbstractCalendarValidator import *
import zoneinfo
import unittest
import datetime
import typing
from typing import *
import io
from abc import ABC

# Imports End


class AbstractCalendarValidatorTest(unittest.TestCase, ABC):

    # Class Fields Begin
    _localeInvalid: typing.List[typing.List[str]] = None
    _validator: AbstractCalendarValidator = None
    _GMT: typing.Union[zoneinfo.ZoneInfo, datetime.timezone] = None
    _EST: typing.Union[zoneinfo.ZoneInfo, datetime.timezone] = None
    _EET: typing.Union[zoneinfo.ZoneInfo, datetime.timezone] = None
    _UTC: typing.Union[zoneinfo.ZoneInfo, datetime.timezone] = None
    _patternValid: typing.List[typing.List[str]] = None
    _localeValid: typing.List[typing.List[str]] = None
    _patternExpect: typing.List[typing.Union[datetime.date, datetime.datetime]] = None
    _patternInvalid: typing.List[typing.List[str]] = None
    # Class Fields End

    # Class Methods Begin
    def tearDown(self) -> None:
        pass

    def setUp(self) -> None:
        pass

    @staticmethod
    def _createDate(
        zone: typing.Union[zoneinfo.ZoneInfo, datetime.timezone], date: int, time: int
    ) -> typing.Union[datetime.datetime, datetime.date]:
        pass

    @staticmethod
    def _createCalendar(
        zone: typing.Union[zoneinfo.ZoneInfo, datetime.timezone], date: int, time: int
    ) -> typing.Union[
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
