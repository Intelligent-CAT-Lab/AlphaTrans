from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.validator.routines.TimeValidator import *
import zoneinfo
import unittest
import os
import datetime
import typing
from typing import *
import io

# Imports End


class TimeValidatorTest(unittest.TestCase):

    # Class Fields Begin
    __origDefault: typing.Any = None
    __defaultZone: typing.Union[zoneinfo.ZoneInfo, datetime.timezone] = None
    _GMT: typing.Union[zoneinfo.ZoneInfo, datetime.timezone] = None
    _EST: typing.Union[zoneinfo.ZoneInfo, datetime.timezone] = None
    _validator: TimeValidator = None
    _patternValid: typing.List[typing.List[str]] = None
    _patternExpect: typing.List[typing.Union[datetime.date, datetime.datetime]] = None
    _localeValid: typing.List[typing.List[str]] = None
    _localeExpect: typing.List[typing.Union[datetime.date, datetime.datetime]] = None
    _patternInvalid: typing.List[typing.List[str]] = None
    _localeInvalid: typing.List[typing.List[str]] = None
    # Class Fields End

    # Class Methods Begin
    def testCompare_test5_decomposed(self) -> None:
        pass

    def testCompare_test4_decomposed(self) -> None:
        pass

    def testCompare_test3_decomposed(self) -> None:
        pass

    def testCompare_test2_decomposed(self) -> None:
        pass

    def testCompare_test1_decomposed(self) -> None:
        pass

    def testCompare_test0_decomposed(self) -> None:
        pass

    def testFormat_test4_decomposed(self) -> None:
        pass

    def testFormat_test3_decomposed(self) -> None:
        pass

    def testFormat_test2_decomposed(self) -> None:
        pass

    def testFormat_test1_decomposed(self) -> None:
        pass

    def testFormat_test0_decomposed(self) -> None:
        pass

    def testTimeZone_test20_decomposed(self) -> None:
        pass

    def testTimeZone_test19_decomposed(self) -> None:
        pass

    def testTimeZone_test18_decomposed(self) -> None:
        pass

    def testTimeZone_test17_decomposed(self) -> None:
        pass

    def testTimeZone_test16_decomposed(self) -> None:
        pass

    def testTimeZone_test15_decomposed(self) -> None:
        pass

    def testTimeZone_test14_decomposed(self) -> None:
        pass

    def testTimeZone_test13_decomposed(self) -> None:
        pass

    def testTimeZone_test12_decomposed(self) -> None:
        pass

    def testTimeZone_test11_decomposed(self) -> None:
        pass

    def testTimeZone_test10_decomposed(self) -> None:
        pass

    def testTimeZone_test9_decomposed(self) -> None:
        pass

    def testTimeZone_test8_decomposed(self) -> None:
        pass

    def testTimeZone_test7_decomposed(self) -> None:
        pass

    def testTimeZone_test6_decomposed(self) -> None:
        pass

    def testTimeZone_test5_decomposed(self) -> None:
        pass

    def testTimeZone_test4_decomposed(self) -> None:
        pass

    def testTimeZone_test3_decomposed(self) -> None:
        pass

    def testTimeZone_test2_decomposed(self) -> None:
        pass

    def testTimeZone_test1_decomposed(self) -> None:
        pass

    def testTimeZone_test0_decomposed(self) -> None:
        pass

    def testLocaleInvalid_test0_decomposed(self) -> None:
        pass

    def testLocaleValid_test0_decomposed(self) -> None:
        pass

    def testPatternInvalid_test0_decomposed(self) -> None:
        pass

    def testPatternValid_test0_decomposed(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def setUp(self) -> None:
        pass

    @staticmethod
    def _createDate(
        zone: typing.Union[zoneinfo.ZoneInfo, datetime.timezone],
        time: int,
        millisecond: int,
    ) -> typing.Union[datetime.datetime, datetime.date]:
        pass

    @staticmethod
    def _createTime(
        zone: typing.Union[zoneinfo.ZoneInfo, datetime.timezone],
        time: int,
        millisecond: int,
    ) -> typing.Union[
        datetime.datetime,
        datetime.date,
        datetime.time,
        datetime.timedelta,
        datetime.timezone,
    ]:
        pass

    def __init__(self, name: str) -> None:
        pass

    # Class Methods End
