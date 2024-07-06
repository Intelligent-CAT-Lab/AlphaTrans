from __future__ import annotations
import time
import locale
import re
import os
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
        "01//2005",
    ]  # invalid pattern
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
        "2005-01-",
    ]  # invalid pattern
    _patternExpect: typing.List[typing.Union[datetime.date, datetime.datetime]] = None
    _localeValid: typing.List[str] = [
        "01/01/2005",
        "12/31/2005",
        "02/29/2004",
        "04/30/2005",
        "12/31/05",
        "1/1/2005",
        "1/1/05",
    ]
    _patternValid: typing.List[str] = [
        "2005-01-01",
        "2005-12-31",
        "2004-02-29",
        "2005-04-30",
        "05-12-31",
        "2005-1-1",
        "05-1-1",
    ]
    _UTC: typing.Union[zoneinfo.ZoneInfo, datetime.timezone] = zoneinfo.ZoneInfo("UTC")
    _EET: typing.Union[zoneinfo.ZoneInfo, datetime.timezone] = zoneinfo.ZoneInfo("EET")
    _EST: typing.Union[zoneinfo.ZoneInfo, datetime.timezone] = zoneinfo.ZoneInfo("EST")
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

    def _tearDown(self) -> None:
        super()._tearDown()
        self._validator = None

    def _setUp(self) -> None:
        super()._setUp()

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

        pass  # LLM could not translate this method

    def testSerialization(self) -> None:
        baos = io.BytesIO()
        try:
            oos = io.ObjectOutputStream(baos)
            oos.writeObject(self._validator)
            oos.flush()
            oos.close()
        except Exception as e:
            self.fail(
                self._validator.getClass().getName()
                + " error during serialization: "
                + e
            )

        result = None
        try:
            bais = io.ByteArrayInputStream(baos.toByteArray())
            ois = io.ObjectInputStream(bais)
            result = ois.readObject()
            bais.close()
        except Exception as e:
            self.fail(
                self._validator.getClass().getName()
                + " error during deserialization: "
                + e
            )
        self.assertNotNull(result)

    def testFormat(self) -> None:
        test = self._validator._parse("2005-11-28", "yyyy-MM-dd", None, None)
        self.assertIsNotNone("Test Date ", test)
        self.assertEqual(
            "Format pattern", "28.11.05", self._validator.format1(test, "dd.MM.yy")
        )
        self.assertEqual(
            "Format locale", "11/28/05", self._validator.format2(test, Locale.US)
        )

    def testLocaleInvalid(self) -> None:
        for i in range(len(self._localeInvalid)):
            text = str(i) + " value=[" + self._localeInvalid[i] + "] passed "
            date = self._validator._parse(self._localeInvalid[i], None, Locale.US, None)
            self.assertIsNone("validateObj() " + text + date, date)
            self.assertFalse(
                "isValid() " + text,
                self._validator.isValid2(self._localeInvalid[i], Locale.US),
            )

    def testLocaleValid(self) -> None:
        for i in range(len(self._localeValid)):
            text = str(i) + " value=[" + self._localeValid[i] + "] failed "
            date = self._validator.parse(self._localeValid[i], None, Locale.US, None)
            self.assertIsNotNone("validateObj() " + text + date, date)
            self.assertTrue(
                "isValid() " + text,
                self._validator.isValid2(self._localeValid[i], Locale.US),
            )
            if isinstance(date, Calendar):
                date = date.getTime()
            self.assertEqual("compare " + text, self._patternExpect[i], date)

    def testPatternInvalid(self) -> None:
        for i in range(len(self._patternInvalid)):
            text = str(i) + " value=[" + self._patternInvalid[i] + "] passed "
            date = self._validator._parse(
                self._patternInvalid[i], "yy-MM-dd", None, None
            )
            self.assertIsNone("validateObj() " + text + date, date)
            self.assertFalse(
                "isValid() " + text,
                self._validator.isValid1(self._patternInvalid[i], "yy-MM-dd"),
            )

    def testPatternValid(self) -> None:
        for i in range(len(self._patternValid)):
            text = str(i) + " value=[" + self._patternValid[i] + "] failed "
            date = self._validator._parse(self._patternValid[i], "yy-MM-dd", None, None)
            self.assertIsNotNone("validateObj() " + text + date, date)
            self.assertTrue(
                "isValid() " + text,
                self._validator.isValid1(self._patternValid[i], "yy-MM-dd"),
            )
            if isinstance(date, Calendar):
                date = date.getTime()
            self.assertEqual("compare " + text, self._patternExpect[i], date)

    def __init__(self, name: str) -> None:
        super().__init__(name)


AbstractCalendarValidatorTest.initialize_fields()
