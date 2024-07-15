from __future__ import annotations
import locale
import re
import zoneinfo
import os
import unittest
import pytest
import io
from src.main.org.apache.commons.validator.routines.AbstractCalendarValidator import *
from src.test.org.apache.commons.validator.routines.AbstractCalendarValidatorTest import *
from src.main.org.apache.commons.validator.routines.DateValidator import *


class DateValidatorTest(AbstractCalendarValidatorTest):

    __dateValidator: DateValidator = None

    def setUp(self) -> None:

        self._localeInvalid = [
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

        self._patternInvalid = [
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

        self._patternExpect = [
            self.createDate(None, 20050101, 0),
            self.createDate(None, 20051231, 0),
            self.createDate(None, 20040229, 0),
            self.createDate(None, 20050430, 0),
            self.createDate(None, 20051231, 0),
            self.createDate(None, 20050101, 0),
            self.createDate(None, 20050101, 0),
        ]

        self._localeValid = [
            "01/01/2005",
            "12/31/2005",
            "02/29/2004",  # valid leap
            "04/30/2005",
            "12/31/05",
            "1/1/2005",
            "1/1/05",
        ]

        self._patternValid = [
            "2005-01-01",
            "2005-12-31",
            "2004-02-29",  # valid leap
            "2005-04-30",
            "05-12-31",
            "2005-1-1",
            "05-1-1",
        ]

        self._UTC = zoneinfo.ZoneInfo("UTC")  # + 2 hours
        self._EET = zoneinfo.ZoneInfo("EET")  # + 2 hours
        self._EST = zoneinfo.ZoneInfo("EST")  # - 5 hours
        self._GMT = zoneinfo.ZoneInfo("GMT")  # 0 offset
        self._validator = DateValidator.DateValidator1()

    def testCompare(self) -> None:

        pass  # LLM could not translate this method

    def testDateValidatorMethods(self) -> None:

        pass  # LLM could not translate this method

    def testLocaleProviders(self) -> None:

        localeProviders = os.getenv("java.locale.providers")
        if localeProviders is not None:  # may be None before Java 9
            self.assertTrue(
                "java.locale.providers must start with COMPAT",
                localeProviders.startswith("COMPAT"),
            )

        txt = "3/20/15 10:59:00 PM"  # This relies on the locale format prior to Java 9 to parse
        dateformat = DateFormat.getDateTimeInstance(3, DateFormat.MEDIUM, Locale.US)
        dateformat.setTimeZone(TimeZone.getTimeZone("GMT"))
        date = dateformat.parse(txt)
        self.assertIsNotNone(date)

    # def __init__(self, name: str) -> None:
    #
    #     pass  # LLM could not translate this method
