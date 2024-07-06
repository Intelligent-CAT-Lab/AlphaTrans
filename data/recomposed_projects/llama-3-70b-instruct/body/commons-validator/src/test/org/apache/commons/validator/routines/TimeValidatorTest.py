from __future__ import annotations
import time
import locale
import re
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

    _localeInvalid: typing.List[str] = [
        "24:00",
        "24:00",
        "25:02",
        "10:61",
        "05-02",
        "0X:01",
        "05:0X",
        "01-01",
        "10:",
        "10::1",
        "10:1:",
    ]
    _patternInvalid: typing.List[str] = [
        "24-00-00",  # midnight
        "24-00-01",  # past midnight
        "25-02-03",  # invalid hour
        "10-61-31",  # invalid minute
        "10-01-61",  # invalid second
        "05:02-29",  # invalid sep
        "0X-01:01",  # invalid sep
        "05-0X-01",  # invalid char
        "10-01-0X",  # invalid char
        "01:01:05",  # invalid pattern
        "10-10",  # invalid pattern
        "10--10",  # invalid pattern
        "10-10-",
    ]  # invalid pattern
    _localeExpect: typing.List[typing.Union[datetime.date, datetime.datetime]] = None
    _localeValid: typing.List[str] = [
        "23:59",
        "00:00",
        "00:01",
        "0:0",
        "1:12",
        "10:49",
        "16:23",
    ]
    _patternExpect: typing.List[typing.Union[datetime.date, datetime.datetime]] = None
    _patternValid: typing.List[str] = [
        "23-59-59",
        "00-00-00",
        "00-00-01",
        "0-0-0",
        "1-12-1",
        "10-49-18",
        "16-23-46",
    ]
    _validator: TimeValidator = None

    _EST: typing.Union[zoneinfo.ZoneInfo, datetime.timezone] = zoneinfo.ZoneInfo("EST")
    _GMT: typing.Union[zoneinfo.ZoneInfo, datetime.timezone] = zoneinfo.ZoneInfo("GMT")
    __defaultZone: typing.Union[zoneinfo.ZoneInfo, datetime.timezone] = None

    __origDefault: typing.Any = None

    @staticmethod
    def initialize_fields() -> None:
        TimeValidatorTest._localeExpect: typing.List[
            typing.Union[datetime.date, datetime.datetime]
        ] = [
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

    def _tearDown(self) -> None:
        super()._tearDown()
        self._validator = None
        locale.setlocale(locale.LC_ALL, self.__origDefault)
        timezone.set_default_timezone(self.__defaultZone)

    def _setUp(self) -> None:
        super()._setUp()
        self._validator = TimeValidator.TimeValidator1()
        self.__defaultZone = zoneinfo.ZoneInfo(
            datetime.datetime.now().astimezone().tzname()
        )
        self.__origDefault = locale.getdefaultlocale()

    @staticmethod
    def _createDate(
        zone: typing.Union[zoneinfo.ZoneInfo, datetime.timezone],
        time: int,
        millisecond: int,
    ) -> typing.Union[datetime.datetime, datetime.date]:
        calendar = TimeValidatorTest._createTime(zone, time, millisecond)
        return calendar

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

        pass  # LLM could not translate this method

    def testCompare(self) -> None:
        testTime: int = 154523
        min: int = 100
        hour: int = 10000

        milliGreater: typing.Union[
            datetime.datetime,
            datetime.date,
            datetime.time,
            datetime.timedelta,
            datetime.timezone,
        ] = self._createTime(
            self._GMT, testTime, 500
        )  # > milli sec
        value: typing.Union[
            datetime.datetime,
            datetime.date,
            datetime.time,
            datetime.timedelta,
            datetime.timezone,
        ] = self._createTime(
            self._GMT, testTime, 400
        )  # test value
        milliLess: typing.Union[
            datetime.datetime,
            datetime.date,
            datetime.time,
            datetime.timedelta,
            datetime.timezone,
        ] = self._createTime(
            self._GMT, testTime, 300
        )  # < milli sec

        secGreater: typing.Union[
            datetime.datetime,
            datetime.date,
            datetime.time,
            datetime.timedelta,
            datetime.timezone,
        ] = self._createTime(
            self._GMT, testTime + 1, 100
        )  # +1 sec
        secLess: typing.Union[
            datetime.datetime,
            datetime.date,
            datetime.time,
            datetime.timedelta,
            datetime.timezone,
        ] = self._createTime(
            self._GMT, testTime - 1, 100
        )  # -1 sec

        minGreater: typing.Union[
            datetime.datetime,
            datetime.date,
            datetime.time,
            datetime.timedelta,
            datetime.timezone,
        ] = self._createTime(
            self._GMT, testTime + min, 100
        )  # +1 min
        minLess: typing.Union[
            datetime.datetime,
            datetime.date,
            datetime.time,
            datetime.timedelta,
            datetime.timezone,
        ] = self._createTime(
            self._GMT, testTime - min, 100
        )  # -1 min

        hourGreater: typing.Union[
            datetime.datetime,
            datetime.date,
            datetime.time,
            datetime.timedelta,
            datetime.timezone,
        ] = self._createTime(
            self._GMT, testTime + hour, 100
        )  # +1 hour
        hourLess: typing.Union[
            datetime.datetime,
            datetime.date,
            datetime.time,
            datetime.timedelta,
            datetime.timezone,
        ] = self._createTime(
            self._GMT, testTime - hour, 100
        )  # -1 hour

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
        TimeValidatorTest._validator = TimeValidator.getInstance()
        TimeValidatorTest._validator.validate2("16:49:23", "HH:mm:ss")
        assert (
            TimeValidatorTest._validator.validate2("16:49:23", "HH:mm:ss") is not None
        )
        assert (
            TimeValidatorTest._validator.format1(
                TimeValidatorTest._validator.validate2("16:49:23", "HH:mm:ss"),
                "HH-mm-ss",
            )
            == "16-49-23"
        )
        assert (
            TimeValidatorTest._validator.format2(
                TimeValidatorTest._validator.validate2("16:49:23", "HH:mm:ss"),
                Locale.US,
            )
            == "4:49 PM"
        )
        assert (
            TimeValidatorTest._validator.format0(
                TimeValidatorTest._validator.validate2("16:49:23", "HH:mm:ss")
            )
            == "16:49"
        )

    def testTimeZone(self) -> None:

        pass  # LLM could not translate this method

    def testLocaleInvalid(self) -> None:
        for i in range(len(self._localeInvalid)):
            text = str(i) + " value=[" + self._localeInvalid[i] + "] passed "
            date = self._validator.validate4(self._localeInvalid[i], Locale.US)
            self.assertIsNone("validate() " + text + date, date)
            self.assertFalse(
                "isValid() " + text,
                self._validator.isValid2(self._localeInvalid[i], Locale.UK),
            )

    def testLocaleValid(self) -> None:
        for i in range(len(self._localeValid)):
            text = str(i) + " value=[" + self._localeValid[i] + "] failed "
            calendar = self._validator.validate4(self._localeValid[i], Locale.UK)
            self.assertIsNotNone(calendar, "validate() " + text)
            date = calendar.getTime()
            self.assertTrue(
                self._validator.isValid2(self._localeValid[i], Locale.UK),
                "isValid() " + text,
            )
            self.assertEqual(self._localeExpect[i], date, "compare " + text)

    def testPatternInvalid(self) -> None:
        for i in range(len(self._patternInvalid)):
            text: str = str(i) + " value=[" + self._patternInvalid[i] + "] passed "
            date: typing.Union[
                datetime.datetime,
                datetime.date,
                datetime.time,
                datetime.timedelta,
                datetime.timezone,
            ] = self._validator.validate2(self._patternInvalid[i], "HH-mm-ss")
            self.assertIsNone("validate() " + text + str(date), date)
            self.assertFalse(
                "isValid() " + text,
                self._validator.isValid1(self._patternInvalid[i], "HH-mm-ss"),
            )

    def testPatternValid(self) -> None:
        for i in range(len(self._patternValid)):
            text: str = str(i) + " value=[" + self._patternValid[i] + "] failed "
            calendar: typing.Union[
                datetime.datetime,
                datetime.date,
                datetime.time,
                datetime.timedelta,
                datetime.timezone,
            ] = self._validator.validate2(self._patternValid[i], "HH-mm-ss")
            self.assertIsNotNone(calendar, "validateObj() " + text)
            date: typing.Union[datetime.date, datetime.datetime] = calendar
            self.assertTrue(
                self._validator.isValid1(self._patternValid[i], "HH-mm-ss"),
                "isValid() " + text,
            )
            self.assertEqual(self._patternExpect[i], date, "compare " + text)

    def __init__(self, name: str) -> None:
        super().__init__(name)


TimeValidatorTest.initialize_fields()
