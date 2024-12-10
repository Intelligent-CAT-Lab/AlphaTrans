from __future__ import annotations
import time
import locale
import re
import os
import enum
import unittest
import pytest
import io
import typing
from typing import *
import datetime
import unittest
import zoneinfo
from src.main.org.apache.commons.validator.routines.TimeValidator import *


class TimeValidatorTest(unittest.TestCase):

    _localeInvalid: List[str] = [
        "24:00",  # midnight
        "24:00",  # past midnight
        "25:02",  # invalid hour
        "10:61",  # invalid minute
        "05-02",  # invalid sep
        "0X:01",  # invalid sep
        "05:0X",  # invalid char
        "01-01",  # invalid pattern
        "10:",  # invalid pattern
        "10::1",  # invalid pattern
        "10:1:",  # invalid pattern
    ]
    _patternInvalid: typing.List[typing.List[str]] = [
        ["24-00-00"],  # midnight
        ["24-00-01"],  # past midnight
        ["25-02-03"],  # invalid hour
        ["10-61-31"],  # invalid minute
        ["10-01-61"],  # invalid second
        ["05:02-29"],  # invalid sep
        ["0X-01:01"],  # invalid sep
        ["05-0X-01"],  # invalid char
        ["10-01-0X"],  # invalid char
        ["01:01:05"],  # invalid pattern
        ["10-10"],  # invalid pattern
        ["10--10"],  # invalid pattern
        ["10-10-"],  # invalid pattern
    ]
    _localeExpect: typing.List[typing.Union[datetime.date, datetime.datetime]] = None
    _localeValid: List[str] = [
        "23:59",
        "00:00",
        "00:01",
        "0:0",
        "1:12",
        "10:49",
        "16:23",
    ]
    _patternExpect: typing.List[typing.Union[datetime.date, datetime.datetime]] = None
    _patternValid: List[str] = [
        "23-59-59",
        "00-00-00",
        "00-00-01",
        "0-0-0",
        "1-12-1",
        "10-49-18",
        "16-23-46",
    ]
    _validator: TimeValidator = None

    _EST: typing.Union[zoneinfo.ZoneInfo, datetime.timezone] = zoneinfo.ZoneInfo(
        "America/New_York"
    )
    _GMT: typing.Union[zoneinfo.ZoneInfo, datetime.timezone] = zoneinfo.ZoneInfo("GMT")
    __defaultZone: typing.Union[zoneinfo.ZoneInfo, datetime.timezone] = None

    __origDefault: typing.Any = None

    @staticmethod
    def initialize_fields() -> None:
        _localeExpect: typing.List[typing.Union[datetime.date, datetime.datetime]] = [
            TimeValidatorTest._createDate(None, 235900, 0),
            TimeValidatorTest._createDate(None, 0, 0),
            TimeValidatorTest._createDate(None, 100, 0),
            TimeValidatorTest._createDate(None, 0, 0),
            TimeValidatorTest._createDate(None, 11200, 0),
            TimeValidatorTest._createDate(None, 104900, 0),
            TimeValidatorTest._createDate(None, 162300, 0),
        ]

        TimeValidatorTest._patternExpect: typing.List[
            typing.Union[datetime.date, datetime.datetime]
        ] = [
            TimeValidatorTest._createDate(None, 235959, 0),
            TimeValidatorTest._createDate(None, 0, 0),
            TimeValidatorTest._createDate(None, 1, 0),
            TimeValidatorTest._createDate(None, 0, 0),
            TimeValidatorTest._createDate(None, 11201, 0),
            TimeValidatorTest._createDate(None, 104918, 0),
            TimeValidatorTest._createDate(None, 162346, 0),
        ]

    def tearDown(self) -> None:

        super().tearDown()
        self._validator = None
        locale.setlocale(locale.LC_ALL, self.__origDefault)
        time.tzset(self.__defaultZone)

    def setUp(self) -> None:
        super().setUp()
        self._validator = TimeValidator.TimeValidator1()
        self.__defaultZone = (
            datetime.datetime.now(datetime.timezone.utc).astimezone().tzinfo
        )
        self.__origDefault = locale.getdefaultlocale()

    @staticmethod
    def _createDate(
        zone: typing.Union[zoneinfo.ZoneInfo, datetime.timezone],
        time: int,
        millisecond: int,
    ) -> typing.Union[datetime.datetime, datetime.date]:

        # Create a datetime object from the time and millisecond
        dt = datetime.datetime.fromtimestamp(time / 1000)

        # Add the timezone offset to the datetime object
        dt = dt.replace(tzinfo=zone)

        return dt.date()

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

        if zone is None:
            calendar = datetime.datetime.now()
        else:
            calendar = datetime.datetime.now(tz=zone)

        hour = (time // 10000) * 10000
        min = ((time // 100) * 100) - hour
        sec = time - (hour + min)

        calendar = calendar.replace(
            year=1970,
            month=1,
            day=1,
            hour=(hour // 10000),
            minute=(min // 100),
            second=sec,
            microsecond=millisecond * 1000,
        )

        return calendar

    def testCompare(self) -> None:

        testTime = 154523
        min = 100
        hour = 10000

        milliGreater = self._createTime(self._GMT, testTime, 500)  # > milli sec
        value = self._createTime(self._GMT, testTime, 400)  # test value
        milliLess = self._createTime(self._GMT, testTime, 300)  # < milli sec

        secGreater = self._createTime(self._GMT, testTime + 1, 100)  # +1 sec
        secLess = self._createTime(self._GMT, testTime - 1, 100)  # -1 sec

        minGreater = self._createTime(self._GMT, testTime + min, 100)  # +1 min
        minLess = self._createTime(self._GMT, testTime - min, 100)  # -1 min

        hourGreater = self._createTime(self._GMT, testTime + hour, 100)  # +1 hour
        hourLess = self._createTime(self._GMT, testTime - hour, 100)  # -1 hour

        self.assertEqual(
            "mili LT", -1, self._validator.compareTime(value, milliGreater)
        )  # > milli
        self.assertEqual(
            "mili EQ", 0, self._validator.compareTime(value, value)
        )  # same time
        self.assertEqual(
            "mili GT", 1, self._validator.compareTime(value, milliLess)
        )  # < milli

        self.assertEqual(
            "secs LT", -1, self._validator.compareSeconds(value, secGreater)
        )  # +1 sec
        self.assertEqual(
            "secs =1", 0, self._validator.compareSeconds(value, milliGreater)
        )  # > milli
        self.assertEqual(
            "secs =2", 0, self._validator.compareSeconds(value, value)
        )  # same time
        self.assertEqual(
            "secs =3", 0, self._validator.compareSeconds(value, milliLess)
        )  # < milli
        self.assertEqual(
            "secs GT", 1, self._validator.compareSeconds(value, secLess)
        )  # -1 sec

        self.assertEqual(
            "mins LT", -1, self._validator.compareMinutes(value, minGreater)
        )  # +1 min
        self.assertEqual(
            "mins =1", 0, self._validator.compareMinutes(value, secGreater)
        )  # +1 sec
        self.assertEqual(
            "mins =2", 0, self._validator.compareMinutes(value, value)
        )  # same time
        self.assertEqual(
            "mins =3", 0, self._validator.compareMinutes(value, secLess)
        )  # -1 sec
        self.assertEqual(
            "mins GT", 1, self._validator.compareMinutes(value, minLess)
        )  # -1 min

        self.assertEqual(
            "hour LT", -1, self._validator.compareHours(value, hourGreater)
        )  # +1 hour
        self.assertEqual(
            "hour =1", 0, self._validator.compareHours(value, minGreater)
        )  # +1 min
        self.assertEqual(
            "hour =2", 0, self._validator.compareHours(value, value)
        )  # same time
        self.assertEqual(
            "hour =3", 0, self._validator.compareHours(value, minLess)
        )  # -1 min
        self.assertEqual(
            "hour GT", 1, self._validator.compareHours(value, hourLess)
        )  # -1 hour

    def testFormat(self) -> None:

        # Set the default locale to UK
        locale.setlocale(locale.LC_ALL, "en_GB.utf8")

        # Test the validate2 method
        test = TimeValidator.getInstance().validate2("16:49:23", "HH:mm:ss")
        self.assertIsNotNone(test, "Test Date ")

        # Test the format1 method
        self.assertEqual(
            self._validator.format1(test, "HH-mm-ss"), "16-49-23", "Format pattern"
        )

        # Test the format2 method
        self.assertEqual(
            self._validator.format2(test, locale.US), "4:49 PM", "Format locale"
        )

        # Test the format0 method
        self.assertEqual(self._validator.format0(test), "16:49", "Format default")

    def testTimeZone(self) -> None:

        locale.setlocale(locale.LC_ALL, "en_GB.UTF-8")
        time.tzset()

        result = None

        result = self._validator.validate0("18:01")
        self.assertIsNotNone(result, "default result")
        self.assertEqual(self._GMT, result.tzinfo, "default zone")
        self.assertEqual(18, result.hour, "default hour")
        self.assertEqual(1, result.minute, "default minute")
        result = None

        result = self._validator.validate1("16:49", self._EST)
        self.assertIsNotNone(result, "zone result")
        self.assertEqual(self._EST, result.tzinfo, "zone zone")
        self.assertEqual(16, result.hour, "zone hour")
        self.assertEqual(49, result.minute, "zone minute")
        result = None

        result = self._validator.validate3("14-34", "HH-mm", self._EST)
        self.assertIsNotNone(result, "pattern result")
        self.assertEqual(self._EST, result.tzinfo, "pattern zone")
        self.assertEqual(14, result.hour, "pattern hour")
        self.assertEqual(34, result.minute, "pattern minute")
        result = None

        result = self._validator.validate5("7:18 PM", locale.US, self._EST)
        self.assertIsNotNone(result, "locale result")
        self.assertEqual(self._EST, result.tzinfo, "locale zone")
        self.assertEqual(19, result.hour, "locale hour")
        self.assertEqual(18, result.minute, "locale minute")
        result = None

        result = self._validator.validate7(
            "31/Dez/05 21-05", "dd/MMM/yy HH-mm", locale.GERMAN, self._EST
        )
        self.assertIsNotNone(result, "pattern result")
        self.assertEqual(self._EST, result.tzinfo, "pattern zone")
        self.assertEqual(2005, result.year, "pattern year")
        self.assertEqual(11, result.month - 1, "pattern month")  # months are 0-11
        self.assertEqual(31, result.day, "pattern day")
        self.assertEqual(21, result.hour, "pattern hour")
        self.assertEqual(5, result.minute, "pattern minute")
        result = None

        result = self._validator.validate6(
            "31/Dez/05 21-05", "dd/MMM/yy HH-mm", locale.GERMAN
        )
        self.assertIsNotNone(result, "pattern result")
        self.assertEqual(self._GMT, result.tzinfo, "pattern zone")
        self.assertEqual(2005, result.year, "pattern year")
        self.assertEqual(11, result.month - 1, "pattern month")  # months are 0-11
        self.assertEqual(31, result.day, "pattern day")
        self.assertEqual(21, result.hour, "pattern hour")
        self.assertEqual(5, result.minute, "pattern minute")
        result = None

    def testLocaleInvalid(self) -> None:

        for i, value in enumerate(self._localeInvalid):
            text = f"{i} value=[{value}] passed "
            date = self._validator.validate4(value, zoneinfo.ZoneInfo("US/Pacific"))
            self.assertIsNone(date, f"validate() {text}{date}")
            self.assertFalse(
                self._validator.isValid2(value, zoneinfo.ZoneInfo("US/Pacific")),
                f"isValid() {text}",
            )

    def testLocaleValid(self) -> None:

        for i in range(len(self._localeValid)):
            text = str(i) + " value=[" + self._localeValid[i] + "] failed "
            calendar = self._validator.validate4(
                self._localeValid[i], zoneinfo.ZoneInfo("Europe/London")
            )
            self.assertIsNotNone(calendar, "validate() " + text)
            date = calendar.getTime()
            self.assertTrue(
                self._validator.isValid2(
                    self._localeValid[i], zoneinfo.ZoneInfo("Europe/London")
                ),
                "isValid() " + text,
            )
            self.assertEqual(self._localeExpect[i], date, "compare " + text)

    def testPatternInvalid(self) -> None:

        for i, pattern in enumerate(self._patternInvalid):
            text = f"{i} value=[{pattern[0]}] passed "
            date = self._validator.validate2(pattern[0], "HH-mm-ss")
            self.assertIsNone(date, f"validate() {text}{date}")
            self.assertFalse(
                self._validator.isValid1(pattern[0], "HH-mm-ss"), f"isValid() {text}"
            )

    def testPatternValid(self) -> None:

        for i in range(len(self._patternValid)):
            text = str(i) + " value=[" + self._patternValid[i] + "] failed "
            calendar = self._validator.validate2(self._patternValid[i], "HH-mm-ss")
            self.assertIsNotNone(calendar, "validateObj() " + text)
            date = calendar.getTime()
            self.assertTrue(
                self._validator.isValid1(self._patternValid[i], "HH-mm-ss"),
                "isValid() " + text,
            )
            self.assertEqual(self._patternExpect[i], date, "compare " + text)

    def __init__(self, name: str) -> None:
        super().__init__(name)


TimeValidatorTest.initialize_fields()
