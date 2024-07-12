from __future__ import annotations
import locale
import re
import zoneinfo
import unittest
import pytest
import io
from src.main.org.apache.commons.validator.routines.AbstractCalendarValidator import *
from src.test.org.apache.commons.validator.routines.AbstractCalendarValidatorTest import *
from src.main.org.apache.commons.validator.routines.CalendarValidator import *


class CalendarValidatorTest(AbstractCalendarValidatorTest):

    __calValidator: CalendarValidator = None

    __TIME_12_03_45: int = 120345
    __DATE_2005_11_23: int = 20051123

    def testFormat(self) -> None:

        origDefault = locale.getdefaultlocale()
        locale.setlocale(locale.LC_ALL, "en_GB.utf8")

        cal20050101 = self._createCalendar(
            self._GMT, self.__DATE_2005_11_23, self.__TIME_12_03_45
        )
        self.assertIsNone(self.__calValidator.format0(None), "null")
        self.assertEqual(
            self.__calValidator.format0(cal20050101), "31/12/05", "default"
        )
        self.assertEqual(
            self.__calValidator.format2(cal20050101, locale.US), "12/31/05", "locale"
        )
        self.assertEqual(
            self.__calValidator.format1(cal20050101, "yyyy-MM-dd HH:mm"),
            "2005-12-31 01:15",
            "patternA",
        )
        self.assertEqual(
            self.__calValidator.format1(cal20050101, "yyyy-MM-dd z"),
            "2005-12-31 GMT",
            "patternB",
        )
        self.assertEqual(
            self.__calValidator.format3(cal20050101, "dd MMM yyyy", locale.GERMAN),
            "31 Dez 2005",
            "both",
        )

        self.assertEqual(
            self.__calValidator.format0(cal20050101, self._EST),
            "30/12/05",
            "EST default",
        )
        self.assertEqual(
            self.__calValidator.format2(cal20050101, locale.US, self._EST),
            "12/30/05",
            "EST locale",
        )
        self.assertEqual(
            self.__calValidator.format1(cal20050101, "yyyy-MM-dd HH:mm", self._EST),
            "2005-12-30 20:15",
            "EST patternA",
        )
        self.assertEqual(
            self.__calValidator.format1(cal20050101, "yyyy-MM-dd z", self._EST),
            "2005-12-30 EST",
            "EST patternB",
        )
        self.assertEqual(
            self.__calValidator.format4(
                cal20050101, "dd MMM yyyy", locale.GERMAN, self._EST
            ),
            "30 Dez 2005",
            "EST both",
        )

        locale.setlocale(locale.LC_ALL, origDefault)

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
        self._validator = AbstractCalendarValidator()

    def testAdjustToTimeZone(self) -> None:

        calEST = self._createCalendar(
            self._EST, self.__DATE_2005_11_23, self.__TIME_12_03_45
        )
        dateEST = calEST.getTime()

        calGMT = self._createCalendar(
            self._GMT, self.__DATE_2005_11_23, self.__TIME_12_03_45
        )
        dateGMT = calGMT.getTime()

        calCET = self._createCalendar(
            self._EET, self.__DATE_2005_11_23, self.__TIME_12_03_45
        )
        dateCET = calCET.getTime()

        assert dateGMT.getTime() != dateCET.getTime()
        assert dateGMT.getTime() != dateEST.getTime()
        assert dateCET.getTime() != dateEST.getTime()

        CalendarValidator.adjustToTimeZone(calEST, self._GMT)
        assert dateGMT == calEST.getTime()
        assert dateEST != calEST.getTime()
        CalendarValidator.adjustToTimeZone(calEST, self._EST)
        assert dateEST == calEST.getTime()
        assert dateGMT != calEST.getTime()

        CalendarValidator.adjustToTimeZone(calCET, self._GMT)
        assert dateGMT == calCET.getTime()
        assert dateCET != calCET.getTime()
        CalendarValidator.adjustToTimeZone(calCET, self._EET)
        assert dateCET == calCET.getTime()
        assert dateGMT != calCET.getTime()

        calUTC = self._createCalendar(
            self._UTC, self.__DATE_2005_11_23, self.__TIME_12_03_45
        )
        assert self._UTC.hasSameRules(self._GMT)
        assert calUTC.getTime() == calGMT.getTime()
        assert self._GMT != calUTC.getTimeZone()
        assert self._UTC == calUTC.getTimeZone()
        CalendarValidator.adjustToTimeZone(calUTC, self._GMT)
        assert calUTC.getTime() == calGMT.getTime()
        assert self._GMT == calUTC.getTimeZone()
        assert self._UTC != calUTC.getTimeZone()

    def testDateTimeStyle(self) -> None:

        origDefault = locale.getdefaultlocale()
        locale.setlocale(locale.LC_ALL, "en_GB.utf8")

        dateTimeValidator = AbstractCalendarValidator(True, 3, 3)
        assert dateTimeValidator.isValid0("31/12/05 14:23")
        assert dateTimeValidator.isValid2("12/31/05 2:23 PM", locale.US)

        locale.setlocale(locale.LC_ALL, origDefault[0])

    def testCompare(self) -> None:

        pass  # LLM could not translate this method

    def testCalendarValidatorMethods(self) -> None:

        pass  # LLM could not translate this method

    def __init__(self, name: str) -> None:

        super().__init__(name)
