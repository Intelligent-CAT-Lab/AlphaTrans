from __future__ import annotations
import time
import locale
import re
import datetime
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
        locale.setlocale(locale.LC_ALL, "en_GB")
        cal20050101 = self._createCalendar(self._GMT, 20051231, 11500)
        self.assertIsNone("null", self._calValidator.format0(None))
        self.assertEqual("default", "31/12/05", self._calValidator.format0(cal20050101))
        self.assertEqual(
            "locale",
            "12/31/05",
            self._calValidator.format2(cal20050101, locale.LC_TIME),
        )
        self.assertEqual(
            "patternA",
            "2005-12-31 01:15",
            self._calValidator.format1(cal20050101, "yyyy-MM-dd HH:mm"),
        )
        self.assertEqual(
            "patternB",
            "2005-12-31 GMT",
            self._calValidator.format1(cal20050101, "yyyy-MM-dd z"),
        )
        self.assertEqual(
            "both",
            "31 Dez 2005",
            self._calValidator.format3(cal20050101, "dd MMM yyyy", locale.LC_TIME),
        )
        self.assertEqual(
            "EST default",
            "30/12/05",
            self._calValidator.format0(cal20050101, self._EST),
        )
        self.assertEqual(
            "EST locale",
            "12/30/05",
            self._calValidator.format2(cal20050101, locale.LC_TIME, self._EST),
        )
        self.assertEqual(
            "EST patternA",
            "2005-12-30 20:15",
            self._calValidator.format1(cal20050101, "yyyy-MM-dd HH:mm", self._EST),
        )
        self.assertEqual(
            "EST patternB",
            "2005-12-30 EST",
            self._calValidator.format1(cal20050101, "yyyy-MM-dd z", self._EST),
        )
        self.assertEqual(
            "EST both",
            "30 Dez 2005",
            self._calValidator.format4(
                cal20050101, "dd MMM yyyy", locale.LC_TIME, self._EST
            ),
        )
        locale.setlocale(locale.LC_ALL, origDefault)

    def _setUp(self) -> None:
        super()._setUp()
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

        self.assertFalse("Check GMT != CET", dateGMT.getTime() == dateCET.getTime())
        self.assertFalse("Check GMT != EST", dateGMT.getTime() == dateEST.getTime())
        self.assertFalse("Check CET != EST", dateCET.getTime() == dateEST.getTime())

        CalendarValidator.adjustToTimeZone(calEST, self._GMT)
        self.assertEqual("EST to GMT", dateGMT, calEST.getTime())
        self.assertFalse("Check EST = GMT", dateEST == calEST.getTime())
        CalendarValidator.adjustToTimeZone(calEST, self._EST)
        self.assertEqual("back to EST", dateEST, calEST.getTime())
        self.assertFalse("Check EST != GMT", dateGMT == calEST.getTime())

        CalendarValidator.adjustToTimeZone(calCET, self._GMT)
        self.assertEqual("CET to GMT", dateGMT, calCET.getTime())
        self.assertFalse("Check CET = GMT", dateCET == calCET.getTime())
        CalendarValidator.adjustToTimeZone(calCET, self._EET)
        self.assertEqual("back to CET", dateCET, calCET.getTime())
        self.assertFalse("Check CET != GMT", dateGMT == calCET.getTime())

        calUTC = self._createCalendar(
            self._UTC, self.__DATE_2005_11_23, self.__TIME_12_03_45
        )
        self.assertTrue("SAME: UTC = GMT", self._UTC.has_same_rules(self._GMT))
        self.assertEqual("SAME: Check time (A)", calUTC.getTime(), calGMT.getTime())
        self.assertFalse("SAME: Check GMT(A)", self._GMT.equals(calUTC.getTimeZone()))
        self.assertTrue("SAME: Check UTC(A)", self._UTC.equals(calUTC.getTimeZone()))
        CalendarValidator.adjustToTimeZone(calUTC, self._GMT)
        self.assertEqual("SAME: Check time (B)", calUTC.getTime(), calGMT.getTime())
        self.assertTrue("SAME: Check GMT(B)", self._GMT.equals(calUTC.getTimeZone()))
        self.assertFalse("SAME: Check UTC(B)", self._UTC.equals(calUTC.getTimeZone()))

    def testDateTimeStyle(self) -> None:

        pass  # LLM could not translate this method

    def testCompare(self) -> None:
        sameTime = 124522
        testDate = 20050823
        diffHour = self._createCalendar(
            self._GMT, testDate, 115922
        )  # same date, different time
        diffMin = self._createCalendar(
            self._GMT, testDate, 124422
        )  # same date, different time
        diffSec = self._createCalendar(
            self._GMT, testDate, 124521
        )  # same date, different time

        value = self._createCalendar(self._GMT, testDate, sameTime)  # test value
        cal20050824 = self._createCalendar(self._GMT, 20050824, sameTime)  # +1 day
        cal20050822 = self._createCalendar(self._GMT, 20050822, sameTime)  # -1 day

        cal20050830 = self._createCalendar(self._GMT, 20050830, sameTime)  # +1 week
        cal20050816 = self._createCalendar(self._GMT, 20050816, sameTime)  # -1 week

        cal20050901 = self._createCalendar(self._GMT, 20050901, sameTime)  # +1 month
        cal20050801 = self._createCalendar(self._GMT, 20050801, sameTime)  # same month
        cal20050731 = self._createCalendar(self._GMT, 20050731, sameTime)  # -1 month

        cal20051101 = self._createCalendar(
            self._GMT, 20051101, sameTime
        )  # +1 quarter (Feb Start)
        cal20051001 = self._createCalendar(self._GMT, 20051001, sameTime)  # +1 quarter
        cal20050701 = self._createCalendar(
            self._GMT, 20050701, sameTime
        )  # same quarter
        cal20050630 = self._createCalendar(self._GMT, 20050630, sameTime)  # -1 quarter

        cal20060101 = self._createCalendar(self._GMT, 20060101, sameTime)  # +1 year
        cal20050101 = self._createCalendar(self._GMT, 20050101, sameTime)  # same year
        cal20041231 = self._createCalendar(self._GMT, 20041231, sameTime)  # -1 year

        self.assertEqual(
            "hour GT",
            1,
            self.__calValidator.compare(value, diffHour, datetime.date.hour),
        )
        self.assertEqual(
            "hour EQ",
            0,
            self.__calValidator.compare(value, diffMin, datetime.date.hour),
        )
        self.assertEqual(
            "mins GT",
            1,
            self.__calValidator.compare(value, diffMin, datetime.date.minute),
        )
        self.assertEqual(
            "mins EQ",
            0,
            self.__calValidator.compare(value, diffSec, datetime.date.minute),
        )
        self.assertEqual(
            "secs GT",
            1,
            self.__calValidator.compare(value, diffSec, datetime.date.second),
        )

        self.assertEqual(
            "date LT", -1, self.__calValidator.compareDates(value, cal20050824)
        )  # +1 day
        self.assertEqual(
            "date EQ", 0, self.__calValidator.compareDates(value, diffHour)
        )  # same day, diff hour
        self.assertEqual(
            "date(B)",
            0,
            self.__calValidator.compare(value, diffHour, datetime.date.day_of_year),
        )  # same day, diff hour
        self.assertEqual(
            "date GT", 1, self.__calValidator.compareDates(value, cal20050822)
        )  # -1 day

        self.assertEqual(
            "week LT", -1, self.__calValidator.compareWeeks(value, cal20050830)
        )  # +1 week
        self.assertEqual(
            "week =1", 0, self.__calValidator.compareWeeks(value, cal20050824)
        )  # +1 day
        self.assertEqual(
            "week =2", 0, self.__calValidator.compareWeeks(value, cal20050822)
        )  # same week
        self.assertEqual(
            "week =3",
            0,
            self.__calValidator.compare(
                value, cal20050822, datetime.date.week_of_month
            ),
        )  # same week
        self.assertEqual(
            "week =4", 0, self.__calValidator.compareWeeks(value, cal20050822)
        )  # -1 day
        self.assertEqual(
            "week GT", 1, self.__calValidator.compareWeeks(value, cal20050816)
        )  # -1 week

        self.assertEqual(
            "mnth LT", -1, self.__calValidator.compareMonths(value, cal20050901)
        )  # +1 month
        self.assertEqual(
            "mnth =1", 0, self.__calValidator.compareMonths(value, cal20050830)
        )  # +1 week
        self.assertEqual(
            "mnth =2", 0, self.__calValidator.compareMonths(value, cal20050801)
        )  # same month
        self.assertEqual(
            "mnth =3", 0, self.__calValidator.compareMonths(value, cal20050816)
        )  # -1 week
        self.assertEqual(
            "mnth GT", 1, self.__calValidator.compareMonths(value, cal20050731)
        )  # -1 month

        self.assertEqual(
            "qtrA <1", -1, self.__calValidator.compareQuarters0(value, cal20051101)
        )  # +1 quarter (Feb)
        self.assertEqual(
            "qtrA <2", -1, self.__calValidator.compareQuarters0(value, cal20051001)
        )  # +1 quarter
        self.assertEqual(
            "qtrA =1", 0, self.__calValidator.compareQuarters0(value, cal20050901)
        )  # +1 month
        self.assertEqual(
            "qtrA =2", 0, self.__calValidator.compareQuarters0(value, cal20050701)
        )  # same quarter
        self.assertEqual(
            "qtrA =3", 0, self.__calValidator.compareQuarters0(value, cal20050731)
        )  # -1 month
        self.assertEqual(
            "qtrA GT", 1, self.__calValidator.compareQuarters0(value, cal20050630)
        )  # -1 quarter

        self.assertEqual(
            "qtrB LT", -1, self.__calValidator.compareQuarters1(value, cal20051101, 2)
        )  # +1 quarter (Feb)
        self.assertEqual(
            "qtrB =1", 0, self.__calValidator.compareQuarters1(value, cal20051001, 2)
        )  # same quarter
        self.assertEqual(
            "qtrB =2", 0, self.__calValidator.compareQuarters1(value, cal20050901, 2)
        )  # +1 month
        self.assertEqual(
            "qtrB =3", 1, self.__calValidator.compareQuarters1(value, cal20050701, 2)
        )  # same quarter
        self.assertEqual(
            "qtrB =4", 1, self.__calValidator.compareQuarters1(value, cal20050731, 2)
        )  # -1 month
        self.assertEqual(
            "qtrB GT", 1, self.__calValidator.compareQuarters1(value, cal20050630, 2)
        )  # -1 quarter

        self.assertEqual(
            "year LT", -1, self.__calValidator.compareYears(value, cal20060101)
        )  # +1 year
        self.assertEqual(
            "year EQ", 0, self.__calValidator.compareYears(value, cal20050101)
        )  # same year
        self.assertEqual(
            "year GT", 1, self.__calValidator.compareYears(value, cal20041231)
        )  # -1 year

        try:
            self.__calValidator.compare(value, value, -1)
            self.fail("Invalid Compare field - expected ValueError to be thrown")
        except ValueError as e:
            self.assertEqual("check message", "Invalid field: -1", e.getMessage())

    def testCalendarValidatorMethods(self) -> None:

        pass  # LLM could not translate this method

    def __init__(self, name: str) -> None:
        super().__init__(name)
