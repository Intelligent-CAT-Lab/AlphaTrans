from __future__ import annotations
import time
import locale
import re
import os
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

        super().tearDown()
        self._validator = None
        locale.setlocale(locale.LC_ALL, self.__origDefault)
        datetime.datetime.now(self.__defaultZone)

    def _setUp(self) -> None:

        self.validator = TimeValidator.TimeValidator1()
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
        return calendar.date()

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

        calendar = datetime.datetime.now(zone) if zone else datetime.datetime.now()
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
            "mili LT", -1, self.validator.compareTime(value, milliGreater)
        )  # > milli
        self.assertEqual(
            "mili EQ", 0, self.validator.compareTime(value, value)
        )  # same time
        self.assertEqual(
            "mili GT", 1, self.validator.compareTime(value, milliLess)
        )  # < milli

        self.assertEqual(
            "secs LT", -1, self.validator.compareSeconds(value, secGreater)
        )  # +1 sec
        self.assertEqual(
            "secs =1", 0, self.validator.compareSeconds(value, milliGreater)
        )  # > milli
        self.assertEqual(
            "secs =2", 0, self.validator.compareSeconds(value, value)
        )  # same time
        self.assertEqual(
            "secs =3", 0, self.validator.compareSeconds(value, milliLess)
        )  # < milli
        self.assertEqual(
            "secs GT", 1, self.validator.compareSeconds(value, secLess)
        )  # -1 sec

        self.assertEqual(
            "mins LT", -1, self.validator.compareMinutes(value, minGreater)
        )  # +1 min
        self.assertEqual(
            "mins =1", 0, self.validator.compareMinutes(value, secGreater)
        )  # +1 sec
        self.assertEqual(
            "mins =2", 0, self.validator.compareMinutes(value, value)
        )  # same time
        self.assertEqual(
            "mins =3", 0, self.validator.compareMinutes(value, secLess)
        )  # -1 sec
        self.assertEqual(
            "mins GT", 1, self.validator.compareMinutes(value, minLess)
        )  # -1 min

        self.assertEqual(
            "hour LT", -1, self.validator.compareHours(value, hourGreater)
        )  # +1 hour
        self.assertEqual(
            "hour =1", 0, self.validator.compareHours(value, minGreater)
        )  # +1 min
        self.assertEqual(
            "hour =2", 0, self.validator.compareHours(value, value)
        )  # same time
        self.assertEqual(
            "hour =3", 0, self.validator.compareHours(value, minLess)
        )  # -1 min
        self.assertEqual(
            "hour GT", 1, self.validator.compareHours(value, hourLess)
        )  # -1 hour

    def testFormat(self) -> None:

        locale.setlocale(locale.LC_ALL, "en_GB.utf8")

        test = TimeValidator.getInstance().validate2("16:49:23", "HH:mm:ss")
        self.assertIsNotNone(test, "Test Date ")
        self.assertEqual(
            "Format pattern", "16-49-23", self.validator.format1(test, "HH-mm-ss")
        )
        self.assertEqual(
            "Format locale", "4:49 PM", self.validator.format2(test, locale.US)
        )
        self.assertEqual("Format default", "16:49", self.validator.format0(test))

    def testTimeZone(self) -> None:

        locale.setlocale(locale.LC_ALL, "en_GB.utf8")
        time.tzset()

        result = None

        result = self.validator.validate0("18:01")
        self.assertIsNotNone(result)
        self.assertEqual(time.tzname, ("GMT", "GMT"))
        self.assertEqual(result.hour, 18)
        self.assertEqual(result.minute, 1)
        result = None

        result = self.validator.validate1("16:49", self._EST)
        self.assertIsNotNone(result)
        self.assertEqual(result.tzinfo, self._EST)
        self.assertEqual(result.hour, 16)
        self.assertEqual(result.minute, 49)
        result = None

        result = self.validator.validate3("14-34", "HH-mm", self._EST)
        self.assertIsNotNone(result)
        self.assertEqual(result.tzinfo, self._EST)
        self.assertEqual(result.hour, 14)
        self.assertEqual(result.minute, 34)
        result = None

        result = self.validator.validate5("7:18 PM", locale.US, self._EST)
        self.assertIsNotNone(result)
        self.assertEqual(result.tzinfo, self._EST)
        self.assertEqual(result.hour, 19)
        self.assertEqual(result.minute, 18)
        result = None

        result = self.validator.validate7(
            "31/Dez/05 21-05", "dd/MMM/yy HH-mm", locale.GERMAN, self._EST
        )
        self.assertIsNotNone(result)
        self.assertEqual(result.tzinfo, self._EST)
        self.assertEqual(result.year, 2005)
        self.assertEqual(result.month, 12)
        self.assertEqual(result.day, 31)
        self.assertEqual(result.hour, 21)
        self.assertEqual(result.minute, 5)
        result = None

        result = self.validator.validate6(
            "31/Dez/05 21-05", "dd/MMM/yy HH-mm", locale.GERMAN
        )
        self.assertIsNotNone(result)
        self.assertEqual(time.tzname, ("GMT", "GMT"))
        self.assertEqual(result.year, 2005)
        self.assertEqual(result.month, 12)
        self.assertEqual(result.day, 31)
        self.assertEqual(result.hour, 21)
        self.assertEqual(result.minute, 5)
        result = None

    def testLocaleInvalid(self) -> None:

        for i in range(len(self._localeInvalid)):
            text = str(i) + " value=[" + self._localeInvalid[i] + "] passed "
            date = self._validator.validate4(self._localeInvalid[i], locale.US)
            self.assertIsNone(date, "validate() " + text + str(date))
            self.assertFalse(
                self._validator.isValid2(self._localeInvalid[i], locale.UK),
                "isValid() " + text,
            )

    def testLocaleValid(self) -> None:

        for i in range(len(self._localeValid)):
            text = str(i) + " value=[" + self._localeValid[i] + "] failed "
            calendar = self._validator.validate4(self._localeValid[i], locale.UK)
            self.assertIsNotNone(calendar, "validate() " + text)
            date = calendar.getTime()
            self.assertTrue(
                self._validator.isValid2(self._localeValid[i], locale.UK),
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
            date = calendar.time()
            self.assertTrue(
                self._validator.isValid1(self._patternValid[i], "HH-mm-ss"),
                "isValid() " + text,
            )
            self.assertEqual(self._patternExpect[i], date, "compare " + text)

    def __init__(self, name: str) -> None:

        super().__init__(name)

        self._localeInvalid = [
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
            "10:1:",
        ]

        self._patternInvalid = [
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
        ]

        self._localeExpect = [
            self.createDate(None, 235900, 0),
            self.createDate(None, 0, 0),
            self.createDate(None, 100, 0),
            self.createDate(None, 0, 0),
            self.createDate(None, 11200, 0),
            self.createDate(None, 104900, 0),
            self.createDate(None, 162300, 0),
        ]

        self._localeValid = ["23:59", "00:00", "00:01", "0:0", "1:12", "10:49", "16:23"]

        self._patternExpect = [
            self.createDate(None, 235959, 0),
            self.createDate(None, 0, 0),
            self.createDate(None, 1, 0),
            self.createDate(None, 0, 0),
            self.createDate(None, 11201, 0),
            self.createDate(None, 104918, 0),
            self.createDate(None, 162346, 0),
        ]

        self._patternValid = [
            "23-59-59",
            "00-00-00",
            "00-00-01",
            "0-0-0",
            "1-12-1",
            "10-49-18",
            "16-23-46",
        ]

        self._validator = TimeValidator()

        self._EST = zoneinfo.ZoneInfo("EST")
        self._GMT = zoneinfo.ZoneInfo("GMT")
        self.__defaultZone = None
        self.__origDefault = None


TimeValidatorTest.initialize_fields()
