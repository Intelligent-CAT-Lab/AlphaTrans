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
        "10-10-",  # invalid pattern
    ]
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

        _patternExpect: typing.List[typing.Union[datetime.date, datetime.datetime]] = [
            TimeValidatorTest._createDate(None, 235959, 0),
            TimeValidatorTest._createDate(None, 0, 0),
            TimeValidatorTest._createDate(None, 1, 0),
            TimeValidatorTest._createDate(None, 0, 0),
            TimeValidatorTest._createDate(None, 11201, 0),
            TimeValidatorTest._createDate(None, 104918, 0),
            TimeValidatorTest._createDate(None, 162346, 0),
        ]

    def _tearDown(self) -> None:
        super().tearDown()
        self._validator = None
        locale.setlocale(locale.LC_ALL, self.__origDefault)
        time.tzset(self.__defaultZone)

    def _setUp(self) -> None:

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

        calendar = TimeValidatorTest._createTime(zone, time, millisecond)
        return calendar.getTime()

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
            tz = datetime.timezone.utc
        else:
            tz = zone

        hour = (time // 10000) * 10000
        min = ((time // 100) * 100) - hour
        sec = time - (hour + min)

        dt = datetime.datetime(
            1970, 1, 1, hour // 10000, min // 100, sec, millisecond, tzinfo=tz
        )

        return dt

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

        # Validate the time string
        test = TimeValidator.getInstance().validate2("16:49:23", "HH:mm:ss")

        # Assert that the test is not null
        self.assertIsNotNone(test, "Test Date ")

        # Assert that the formatted time matches the expected output
        self.assertEqual(
            self._validator.format1(test, "HH-mm-ss"), "16-49-23", "Format pattern"
        )

        # Assert that the formatted time matches the expected output for the US locale
        self.assertEqual(
            self._validator.format2(test, locale.US), "4:49 PM", "Format locale"
        )

        # Assert that the formatted time matches the expected output for the default locale
        self.assertEqual(self._validator.format0(test), "16:49", "Format default")

    def testTimeZone(self) -> None:

        locale.setlocale(locale.LC_ALL, "en_GB.UTF-8")
        time.tzset()

        result = None

        result = self._validator.validate0("18:01")
        self.assertIsNotNone(result)
        self.assertEqual(result.tzinfo, self._GMT)
        self.assertEqual(result.hour, 18)
        self.assertEqual(result.minute, 1)
        result = None

        result = self._validator.validate1("16:49", self._EST)
        self.assertIsNotNone(result)
        self.assertEqual(result.tzinfo, self._EST)
        self.assertEqual(result.hour, 16)
        self.assertEqual(result.minute, 49)
        result = None

        result = self._validator.validate3("14-34", "HH-mm", self._EST)
        self.assertIsNotNone(result)
        self.assertEqual(result.tzinfo, self._EST)
        self.assertEqual(result.hour, 14)
        self.assertEqual(result.minute, 34)
        result = None

        result = self._validator.validate5("7:18 PM", locale.US, self._EST)
        self.assertIsNotNone(result)
        self.assertEqual(result.tzinfo, self._EST)
        self.assertEqual(result.hour, 19)
        self.assertEqual(result.minute, 18)
        result = None

        result = self._validator.validate7(
            "31/Dez/05 21-05", "dd/MMM/yy HH-mm", locale.GERMAN, self._EST
        )
        self.assertIsNotNone(result)
        self.assertEqual(result.tzinfo, self._EST)
        self.assertEqual(result.year, 2005)
        self.assertEqual(result.month, 11)  # months are 0-11
        self.assertEqual(result.day, 31)
        self.assertEqual(result.hour, 21)
        self.assertEqual(result.minute, 5)
        result = None

        result = self._validator.validate6(
            "31/Dez/05 21-05", "dd/MMM/yy HH-mm", locale.GERMAN
        )
        self.assertIsNotNone(result)
        self.assertEqual(result.tzinfo, self._GMT)
        self.assertEqual(result.year, 2005)
        self.assertEqual(result.month, 11)  # months are 0-11
        self.assertEqual(result.day, 31)
        self.assertEqual(result.hour, 21)
        self.assertEqual(result.minute, 5)
        result = None

    def testLocaleInvalid(self) -> None:

        for i in range(len(self._localeInvalid)):
            text = str(i) + " value=[" + self._localeInvalid[i] + "] passed "
            date = self._validator.validate4(
                self._localeInvalid[i], zoneinfo.ZoneInfo("US/Pacific")
            )
            self.assertIsNone(date, "validate() " + text + str(date))
            self.assertFalse(
                self._validator.isValid2(
                    self._localeInvalid[i], zoneinfo.ZoneInfo("Europe/London")
                ),
                "isValid() " + text,
            )

    def testLocaleValid(self) -> None:

        for i in range(len(self._localeValid)):
            text = str(i) + " value=[" + self._localeValid[i] + "] failed "
            calendar = self._validator.validate4(
                self._localeValid[i], zoneinfo.ZoneInfo("Europe/London")
            )
            self.assertIsNotNone(calendar, "validate() " + text)
            date = calendar.time()
            self.assertTrue(
                self._validator.isValid2(
                    self._localeValid[i], zoneinfo.ZoneInfo("Europe/London")
                ),
                "isValid() " + text,
            )
            self.assertEqual(self._localeExpect[i], date, "compare " + text)

    def testPatternInvalid(self) -> None:

        for i in range(len(self._patternInvalid)):
            text = str(i) + " value=[" + self._patternInvalid[i] + "] passed "
            date = self._validator.validate2(self._patternInvalid[i], "HH-mm-ss")
            self.assertIsNone(date, "validate() " + text + str(date))
            self.assertFalse(
                self._validator.isValid1(self._patternInvalid[i], "HH-mm-ss"),
                "isValid() " + text,
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
