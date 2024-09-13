from __future__ import annotations
import time
import locale
import re
import os
import enum
from io import BytesIO
import unittest
import pytest
from abc import ABC
import io
import typing
from typing import *
import datetime
import unittest
import zoneinfo
from src.main.org.apache.commons.validator.routines.AbstractCalendarValidator import *


class AbstractCalendarValidatorTest(unittest.TestCase, ABC):

    _localeInvalid: typing.List[str] = [
        "01/00/2005",  # zero month
        "00/01/2005",  # zero day
        "13/01/2005",  # month invalid
        "04/31/2005",  # invalid day
        "03/32/2005",  # invalid day
        "02/29/2005",  # invalid leap
        "01/01/200X",  # invalid char
        "01/0X/2005",  # invalid char
        "0X/01/2005",  # invalid char
        "01-01-2005",  # invalid pattern
        "01/2005",  # invalid pattern
        "01//2005",  # invalid pattern
    ]
    _patternInvalid: typing.List[str] = [
        "2005-00-01",  # zero month
        "2005-01-00",  # zero day
        "2005-13-03",  # month invalid
        "2005-04-31",  # invalid day
        "2005-03-32",  # invalid day
        "2005-02-29",  # invalid leap
        "200X-01-01",  # invalid char
        "2005-0X-01",  # invalid char
        "2005-01-0X",  # invalid char
        "01/01/2005",  # invalid pattern
        "2005-01",  # invalid pattern
        "2005--01",  # invalid pattern
        "2005-01-",  # invalid pattern
    ]
    _patternExpect: typing.List[typing.Union[datetime.date, datetime.datetime]] = None
    _localeValid: List[str] = [
        "01/01/2005",
        "12/31/2005",
        "02/29/2004",  # valid leap
        "04/30/2005",
        "12/31/05",
        "1/1/2005",
        "1/1/05",
    ]
    _patternValid: List[str] = [
        "2005-01-01",
        "2005-12-31",
        "2004-02-29",  # valid leap
        "2005-04-30",
        "05-12-31",
        "2005-1-1",
        "05-1-1",
    ]
    _UTC: typing.Union[zoneinfo.ZoneInfo, datetime.timezone] = zoneinfo.ZoneInfo("UTC")
    _EET: typing.Union[zoneinfo.ZoneInfo, datetime.timezone] = zoneinfo.ZoneInfo("EET")
    _EST: typing.Union[zoneinfo.ZoneInfo, datetime.timezone] = zoneinfo.ZoneInfo(
        "America/New_York"
    )
    _GMT: typing.Union[zoneinfo.ZoneInfo, datetime.timezone] = zoneinfo.ZoneInfo("GMT")
    _validator: AbstractCalendarValidator = None

    @staticmethod
    def initialize_fields() -> None:
        AbstractCalendarValidatorTest._patternExpect: typing.List[
            typing.Union[datetime.date, datetime.datetime]
        ] = [
            AbstractCalendarValidatorTest._createDate(None, 20050101, 0),
            AbstractCalendarValidatorTest._createDate(None, 20051231, 0),
            AbstractCalendarValidatorTest._createDate(None, 20040229, 0),
            AbstractCalendarValidatorTest._createDate(None, 20050430, 0),
            AbstractCalendarValidatorTest._createDate(None, 20051231, 0),
            AbstractCalendarValidatorTest._createDate(None, 20050101, 0),
            AbstractCalendarValidatorTest._createDate(None, 20050101, 0),
        ]

    def tearDown(self) -> None:
        self._validator = None

    def setUp(self) -> None:
        super().setUp()

    @staticmethod
    def _createDate(
        zone: typing.Union[zoneinfo.ZoneInfo, datetime.timezone], date: int, time: int
    ) -> typing.Union[datetime.datetime, datetime.date]:

        calendar = AbstractCalendarValidatorTest._createCalendar(zone, date, time)
        return calendar.getTime()

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

        if zone is None:
            calendar = datetime.datetime.now()
        else:
            calendar = datetime.datetime.now(tz=zone)

        year = (date // 10000) * 10000
        mth = ((date // 100) * 100) - year
        day = date - (year + mth)
        hour = (time // 10000) * 10000
        min = ((time // 100) * 100) - hour
        sec = time - (hour + min)

        calendar = calendar.replace(
            year=(year // 10000),
            month=((mth // 100) - 1),
            day=day,
            hour=(hour // 10000),
            minute=(min // 100),
            second=sec,
            microsecond=0,
        )

        return calendar

    def testSerialization(self) -> None:

        baos = io.BytesIO()
        try:
            oos = typing.cast(object, io.BufferedWriter)
            oos = io.BufferedWriter(baos)
            oos.write(str(self._validator).encode())
            oos.flush()
            oos.close()
        except Exception as e:
            pytest.fail(
                self._validator.__class__.__name__
                + " error during serialization: "
                + str(e)
            )

        result = None
        try:
            bais = io.BytesIO(baos.getvalue())
            ois = typing.cast(object, io.BufferedReader)
            ois = io.BufferedReader(bais)
            result = ois.read()
            bais.close()
        except Exception as e:
            pytest.fail(
                self._validator.__class__.__name__
                + " error during deserialization: "
                + str(e)
            )
        self.assertIsNotNone(result)

    def testFormat(self) -> None:

        test = self._validator.parse("2005-11-28", "yyyy-MM-dd", None, None)
        self.assertIsNotNone(test, "Test Date ")
        self.assertEqual(
            self._validator.format1(test, "dd.MM.yy"), "28.11.05", "Format pattern"
        )
        self.assertEqual(
            self._validator.format2(test, Locale.US), "11/28/05", "Format locale"
        )

    def testLocaleInvalid(self) -> None:

        for i, locale in enumerate(self._localeInvalid):
            text = f"{i} value=[{locale}] passed "
            date = self._validator.parse(locale, None, Locale.US, None)
            self.assertIsNone(date, f"validateObj() {text}{date}")
            self.assertFalse(
                self._validator.isValid2(locale, Locale.US), f"isValid() {text}"
            )

    def testLocaleValid(self) -> None:

        for i in range(len(self._localeValid)):
            text = str(i) + " value=[" + self._localeValid[i] + "] failed "
            date = self._validator.parse(self._localeValid[i], None, Locale.US, None)
            self.assertIsNotNone(date, "validateObj() " + text + str(date))
            self.assertTrue(
                self._validator.isValid2(self._localeValid[i], Locale.US),
                "isValid() " + text,
            )
            if isinstance(date, Calendar):
                date = date.getTime()
            self.assertEqual(self._patternExpect[i], date, "compare " + text)

    def testPatternInvalid(self) -> None:

        for i, pattern in enumerate(self._patternInvalid):
            text = f"{i} value=[{pattern}] passed "
            date = self._validator.parse(pattern, "yy-MM-dd", None, None)
            self.assertIsNone(date, f"validateObj() {text}{date}")
            self.assertFalse(
                self._validator.isValid1(pattern, "yy-MM-dd"), f"isValid() {text}"
            )

    def testPatternValid(self) -> None:

        for i in range(len(self._patternValid)):
            text = str(i) + " value=[" + self._patternValid[i] + "] failed "
            date = self._validator.parse(self._patternValid[i], "yy-MM-dd", None, None)
            self.assertIsNotNone(date, "validateObj() " + text + str(date))
            self.assertTrue(
                self._validator.isValid1(self._patternValid[i], "yy-MM-dd"),
                "isValid() " + text,
            )
            if isinstance(date, datetime.datetime):
                date = date.date()
            self.assertEqual(self._patternExpect[i], date, "compare " + text)

    def __init__(self, name: str) -> None:
        super().__init__(name)


AbstractCalendarValidatorTest.initialize_fields()
