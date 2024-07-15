from __future__ import annotations
import time
import locale
import re
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

        cal20050101 = self._createCalendar(self._GMT, 20051231, 11500)
        self.assertIsNone(self._calValidator.format0(None), "null")
        self.assertEqual(self._calValidator.format0(cal20050101), "31/12/05", "default")
        self.assertEqual(
            self._calValidator.format2(cal20050101, locale.US), "12/31/05", "locale"
        )
        self.assertEqual(
            self._calValidator.format1(cal20050101, "yyyy-MM-dd HH:mm"),
            "2005-12-31 01:15",
            "patternA",
        )
        self.assertEqual(
            self._calValidator.format1(cal20050101, "yyyy-MM-dd z"),
            "2005-12-31 GMT",
            "patternB",
        )
        self.assertEqual(
            self._calValidator.format3(cal20050101, "dd MMM yyyy", locale.GERMAN),
            "31 Dez 2005",
            "both",
        )

        self.assertEqual(
            self._calValidator.format0(cal20050101, self._EST),
            "30/12/05",
            "EST default",
        )
        self.assertEqual(
            self._calValidator.format2(cal20050101, locale.US, self._EST),
            "12/30/05",
            "EST locale",
        )
        self.assertEqual(
            self._calValidator.format1(cal20050101, "yyyy-MM-dd HH:mm", self._EST),
            "2005-12-30 20:15",
            "EST patternA",
        )
        self.assertEqual(
            self._calValidator.format1(cal20050101, "yyyy-MM-dd z", self._EST),
            "2005-12-30 EST",
            "EST patternB",
        )
        self.assertEqual(
            self._calValidator.format4(
                cal20050101, "dd MMM yyyy", locale.GERMAN, self._EST
            ),
            "30 Dez 2005",
            "EST both",
        )

        locale.setlocale(locale.LC_ALL, origDefault)

    def setUp(self) -> None:
        self.__calValidator = CalendarValidator.CalendarValidator1()
        self._validator = self.__calValidator

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

        assert dateGMT.getTime() != dateCET.getTime(), "Check GMT != CET"
        assert dateGMT.getTime() != dateEST.getTime(), "Check GMT != EST"
        assert dateCET.getTime() != dateEST.getTime(), "Check CET != EST"

        CalendarValidator.adjustToTimeZone(calEST, self._GMT)
        assert dateGMT == calEST.getTime(), "EST to GMT"
        assert dateEST != calEST.getTime(), "Check EST = GMT"
        CalendarValidator.adjustToTimeZone(calEST, self._EST)
        assert dateEST == calEST.getTime(), "back to EST"
        assert dateGMT != calEST.getTime(), "Check EST != GMT"

        CalendarValidator.adjustToTimeZone(calCET, self._GMT)
        assert dateGMT == calCET.getTime(), "CET to GMT"
        assert dateCET != calCET.getTime(), "Check CET = GMT"
        CalendarValidator.adjustToTimeZone(calCET, self._EET)
        assert dateCET == calCET.getTime(), "back to CET"
        assert dateGMT != calCET.getTime(), "Check CET != GMT"

        calUTC = self._createCalendar(
            self._UTC, self.__DATE_2005_11_23, self.__TIME_12_03_45
        )
        assert self._UTC.hasSameRules(self._GMT), "SAME: UTC = GMT"
        assert calUTC.getTime() == calGMT.getTime(), "SAME: Check time (A)"
        assert self._GMT != calUTC.getTimeZone(), "SAME: Check GMT(A)"
        assert self._UTC == calUTC.getTimeZone(), "SAME: Check UTC(A)"
        CalendarValidator.adjustToTimeZone(calUTC, self._GMT)
        assert calUTC.getTime() == calGMT.getTime(), "SAME: Check time (B)"
        assert self._GMT == calUTC.getTimeZone(), "SAME: Check GMT(B)"
        assert self._UTC != calUTC.getTimeZone(), "SAME: Check UTC(B)"

    def testDateTimeStyle(self) -> None:

        origDefault = locale.getdefaultlocale()
        locale.setlocale(locale.LC_ALL, "en_GB.utf8")

        dateTimeValidator = AbstractCalendarValidator(True, locale.SHORT, locale.SHORT)
        dateTimeValidator.processParsedValue = lambda value, formatter: value
        self.assertTrue(
            "validate(A) default", dateTimeValidator.isValid0("31/12/05 14:23")
        )
        self.assertTrue(
            "validate(A) locale ",
            dateTimeValidator.isValid2("12/31/05 2:23 PM", locale.US),
        )

        locale.setlocale(locale.LC_ALL, origDefault)

    def testCompare(self) -> None:

        pass  # LLM could not translate this method

    def testCalendarValidatorMethods(self) -> None:

        pass  # LLM could not translate this method

    def __init__(self, name: str) -> None:
        super().__init__(name)
