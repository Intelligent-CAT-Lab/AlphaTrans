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
        locale.setlocale(locale.LC_ALL, "en_GB.utf8")

        cal20050101 = self._createCalendar(self._GMT, 20051231, 11500)
        self.assertIsNone(self.__calValidator.format0(None))
        self.assertEqual(
            "default", "31/12/05", self.__calValidator.format0(cal20050101)
        )
        self.assertEqual(
            "locale", "12/31/05", self.__calValidator.format2(cal20050101, locale.US)
        )
        self.assertEqual(
            "patternA",
            "2005-12-31 01:15",
            self.__calValidator.format1(cal20050101, "yyyy-MM-dd HH:mm"),
        )
        self.assertEqual(
            "patternB",
            "2005-12-31 GMT",
            self.__calValidator.format1(cal20050101, "yyyy-MM-dd z"),
        )
        self.assertEqual(
            "both",
            "31 Dez 2005",
            self.__calValidator.format3(cal20050101, "dd MMM yyyy", locale.GERMAN),
        )

        self.assertEqual(
            "EST default",
            "30/12/05",
            self.__calValidator.format0(cal20050101, self._EST),
        )
        self.assertEqual(
            "EST locale",
            "12/30/05",
            self.__calValidator.format2(cal20050101, locale.US, self._EST),
        )
        self.assertEqual(
            "EST patternA",
            "2005-12-30 20:15",
            self.__calValidator.format1(cal20050101, "yyyy-MM-dd HH:mm", self._EST),
        )
        self.assertEqual(
            "EST patternB",
            "2005-12-30 EST",
            self.__calValidator.format1(cal20050101, "yyyy-MM-dd z", self._EST),
        )
        self.assertEqual(
            "EST both",
            "30 Dez 2005",
            self.__calValidator.format4(
                cal20050101, "dd MMM yyyy", locale.GERMAN, self._EST
            ),
        )

        locale.setlocale(locale.LC_ALL, origDefault)

    def setUp(self) -> None:
        self._validator = CalendarValidator.CalendarValidator1()
        self.__calValidator = self._validator

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
        self.assertTrue("SAME: UTC = GMT", self._UTC.hasSameRules(self._GMT))
        self.assertEqual("SAME: Check time (A)", calUTC.getTime(), calGMT.getTime())
        self.assertFalse("SAME: Check GMT(A)", self._GMT.equals(calUTC.getTimeZone()))
        self.assertTrue("SAME: Check UTC(A)", self._UTC.equals(calUTC.getTimeZone()))
        CalendarValidator.adjustToTimeZone(calUTC, self._GMT)
        self.assertEqual("SAME: Check time (B)", calUTC.getTime(), calGMT.getTime())
        self.assertTrue("SAME: Check GMT(B)", self._GMT.equals(calUTC.getTimeZone()))
        self.assertFalse("SAME: Check UTC(B)", self._UTC.equals(calUTC.getTimeZone()))

    def testDateTimeStyle(self) -> None:

        origDefault = locale.getdefaultlocale()
        locale.setlocale(locale.LC_ALL, "en_GB.utf8")

        dateTimeValidator = AbstractCalendarValidator(True, locale.SHORT, locale.SHORT)
        self.assertTrue(dateTimeValidator.isValid0("31/12/05 14:23"))
        self.assertTrue(dateTimeValidator.isValid2("12/31/05 2:23 PM", locale.US))

        locale.setlocale(locale.LC_ALL, origDefault)

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
            self.__calValidator.compare(value, diffHour, datetime.HOUR_OF_DAY), 1
        )
        self.assertEqual(
            self.__calValidator.compare(value, diffMin, datetime.HOUR_OF_DAY), 0
        )
        self.assertEqual(
            self.__calValidator.compare(value, diffMin, datetime.MINUTE), 1
        )
        self.assertEqual(
            self.__calValidator.compare(value, diffSec, datetime.MINUTE), 1
        )
        self.assertEqual(
            self.__calValidator.compare(value, diffSec, datetime.SECOND), 1
        )

        self.assertEqual(
            self.__calValidator.compareDates(value, cal20050824), -1
        )  # +1 day
        self.assertEqual(
            self.__calValidator.compareDates(value, diffHour), 0
        )  # same day, diff hour
        self.assertEqual(
            self.__calValidator.compare(value, diffHour, datetime.DAY_OF_YEAR), 0
        )  # same day, diff hour
        self.assertEqual(
            self.__calValidator.compareDates(value, cal20050822), 1
        )  # -1 day

        self.assertEqual(
            self.__calValidator.compareWeeks(value, cal20050830), -1
        )  # +1 week
        self.assertEqual(
            self.__calValidator.compareWeeks(value, cal20050824), 0
        )  # +1 day
        self.assertEqual(
            self.__calValidator.compareWeeks(value, cal20050822), 0
        )  # same week
        self.assertEqual(
            self.__calValidator.compare(value, cal20050822, datetime.WEEK_OF_MONTH), 0
        )  # same week
        self.assertEqual(
            self.__calValidator.compareWeeks(value, cal20050822), 0
        )  # -1 day
        self.assertEqual(
            self.__calValidator.compareWeeks(value, cal20050816), 1
        )  # -1 week

        self.assertEqual(
            self.__calValidator.compareMonths(value, cal20050901), -1
        )  # +1 month
        self.assertEqual(
            self.__calValidator.compareMonths(value, cal20050830), 0
        )  # +1 week
        self.assertEqual(
            self.__calValidator.compareMonths(value, cal20050801), 0
        )  # same month
        self.assertEqual(
            self.__calValidator.compareMonths(value, cal20050816), 0
        )  # -1 week
        self.assertEqual(
            self.__calValidator.compareMonths(value, cal20050731), 1
        )  # -1 month

        self.assertEqual(
            self.__calValidator.compareQuarters0(value, cal20051101), -1
        )  # +1 quarter (Feb)
        self.assertEqual(
            self.__calValidator.compareQuarters0(value, cal20051001), -1
        )  # +1 quarter
        self.assertEqual(
            self.__calValidator.compareQuarters0(value, cal20050901), 0
        )  # +1 month
        self.assertEqual(
            self.__calValidator.compareQuarters0(value, cal20050701), 0
        )  # same quarter
        self.assertEqual(
            self.__calValidator.compareQuarters0(value, cal20050731), 0
        )  # -1 month
        self.assertEqual(
            self.__calValidator.compareQuarters0(value, cal20050630), 1
        )  # -1 quarter

        self.assertEqual(
            self.__calValidator.compareQuarters1(value, cal20051101, 2), -1
        )  # +1 quarter (Feb)
        self.assertEqual(
            self.__calValidator.compareQuarters1(value, cal20051001, 2), 0
        )  # same quarter
        self.assertEqual(
            self.__calValidator.compareQuarters1(value, cal20050901, 2), 0
        )  # +1 month
        self.assertEqual(
            self.__calValidator.compareQuarters1(value, cal20050701, 2), 1
        )  # same quarter
        self.assertEqual(
            self.__calValidator.compareQuarters1(value, cal20050731, 2), 1
        )  # -1 month
        self.assertEqual(
            self.__calValidator.compareQuarters1(value, cal20050630, 2), 1
        )  # -1 quarter

        self.assertEqual(
            self.__calValidator.compareYears(value, cal20060101), -1
        )  # +1 year
        self.assertEqual(
            self.__calValidator.compareYears(value, cal20050101), 0
        )  # same year
        self.assertEqual(
            self.__calValidator.compareYears(value, cal20041231), 1
        )  # -1 year

        with self.assertRaises(ValueError) as context:
            self.__calValidator.compare(value, value, -1)
        self.assertTrue("Invalid field: -1" in str(context.exception))

    def testCalendarValidatorMethods(self) -> None:

        locale.setlocale(locale.LC_ALL, "en_US.UTF-8")
        locale_val = "de_DE"
        pattern = "yyyy-MM-dd"
        pattern_val = "2005-12-31"
        german_val = "31 Dez 2005"
        german_pattern = "dd MMM yyyy"
        locale_val = "31.12.2005"
        default_val = "12/31/05"
        xxxx = "XXXX"
        expected = self._createCalendar(None, 20051231, 0).getTime()

        self.assertEqual(
            "validate(A) default",
            expected,
            CalendarValidator.getInstance().validate0(default_val).getTime(),
        )

        self.assertEqual(
            "validate(A) locale ",
            expected,
            CalendarValidator.getInstance().validate4(locale_val, locale_val).getTime(),
        )

        self.assertEqual(
            "validate(A) pattern",
            expected,
            CalendarValidator.getInstance().validate2(pattern_val, pattern).getTime(),
        )

        self.assertEqual(
            "validate(A) both",
            expected,
            CalendarValidator.getInstance()
            .validate6(german_val, german_pattern, locale_val)
            .getTime(),
        )

        self.assertTrue(
            "isValid(A) default", CalendarValidator.getInstance().isValid0(default_val)
        )
        self.assertTrue(
            "isValid(A) locale ",
            CalendarValidator.getInstance().isValid2(locale_val, locale_val),
        )
        self.assertTrue(
            "isValid(A) pattern",
            CalendarValidator.getInstance().isValid1(pattern_val, pattern),
        )
        self.assertTrue(
            "isValid(A) both",
            CalendarValidator.getInstance().isValid3(
                german_val, german_pattern, locale_val
            ),
        )

        self.assertIsNone(
            "validate(B) default", CalendarValidator.getInstance().validate0(xxxx)
        )
        self.assertIsNone(
            "validate(B) locale ",
            CalendarValidator.getInstance().validate4(xxxx, locale_val),
        )
        self.assertIsNone(
            "validate(B) pattern",
            CalendarValidator.getInstance().validate2(xxxx, pattern),
        )
        self.assertIsNone(
            "validate(B) both",
            CalendarValidator.getInstance().validate6(
                "31 Dec 2005", german_pattern, locale_val
            ),
        )

        self.assertFalse(
            "isValid(B) default", CalendarValidator.getInstance().isValid0(xxxx)
        )
        self.assertFalse(
            "isValid(B) locale ",
            CalendarValidator.getInstance().isValid2(xxxx, locale_val),
        )
        self.assertFalse(
            "isValid(B) pattern",
            CalendarValidator.getInstance().isValid1(xxxx, pattern),
        )
        self.assertFalse(
            "isValid(B) both",
            CalendarValidator.getInstance().isValid3(
                "31 Dec 2005", german_pattern, locale_val
            ),
        )

        zone = time.tzname[time.daylight] if time.daylight else time.tzname[0]
        expected_zone = self._createCalendar(zone, 20051231, 0).getTime()
        self.assertFalse(
            "default/EET same ", expected.getTime() == expected_zone.getTime()
        )

        self.assertEqual(
            "validate(C) default",
            expected_zone,
            CalendarValidator.getInstance().validate1(default_val, zone).getTime(),
        )

        self.assertEqual(
            "validate(C) locale ",
            expected_zone,
            CalendarValidator.getInstance()
            .validate5(locale_val, locale_val, zone)
            .getTime(),
        )

        self.assertEqual(
            "validate(C) pattern",
            expected_zone,
            CalendarValidator.getInstance()
            .validate3(pattern_val, pattern, zone)
            .getTime(),
        )

        self.assertEqual(
            "validate(C) both",
            expected_zone,
            CalendarValidator.getInstance()
            .validate7(german_val, german_pattern, locale_val, zone)
            .getTime(),
        )

    def __init__(self, name: str) -> None:
        super().__init__(name)
