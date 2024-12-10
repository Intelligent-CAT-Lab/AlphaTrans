from __future__ import annotations
import time
import locale
import re
import datetime
from zoneinfo import ZoneInfo
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

        origDefault = locale.getlocale()
        locale.setlocale(locale.LC_ALL, "en_GB.UTF-8")

        cal20050101 = self._createCalendar(self._GMT, 20051231, 11500)
        self.assertIsNone(self.__calValidator._format0(None))
        self.assertEqual(
            "31/12/05",
            self.__calValidator._format0(cal20050101),
            "default"
        )
        self.assertEqual(
            "12/31/05",
            self.__calValidator._format2(cal20050101, "en_US.UTF-8"),
            "locale"
        )
        self.assertEqual(
            "2005-12-31 01:15",
            self.__calValidator._format1(cal20050101, "yyyy-MM-dd HH:mm"),
            "patternA"
        )
        self.assertEqual(
            "2005-12-31 +0000",
            self.__calValidator._format1(cal20050101, "yyyy-MM-dd z"),
            "patternB"
        )
        self.assertEqual(
            "31 Dez 2005",
            self.__calValidator.format3(cal20050101, "dd MMM yyyy", "de_DE.UTF-8"),
            "both"
        )

        self.assertEqual(
            "30/12/05",
            self.__calValidator.format0(cal20050101, self._EST),
            "EST default"
        )
        self.assertEqual(
            "12/30/05",
            self.__calValidator.format2(cal20050101, "en_US.UTF-8", self._EST),
            "EST locale"
        )
        self.assertEqual(
            "2005-12-30 20:15",
            self.__calValidator.format1(cal20050101, "yyyy-MM-dd HH:mm", self._EST),
            "EST patternA"
        )
        self.assertEqual(
            "2005-12-30 -0500",
            self.__calValidator.format1(cal20050101, "yyyy-MM-dd z", self._EST),
            "EST patternB"
        )
        self.assertEqual(
            "30 Dez 2005",
            self.__calValidator.format4(
                cal20050101, "dd MMM yyyy", "de_DE.UTF-8", self._EST
            ),
            "EST both"
        )

        locale.setlocale(locale.LC_ALL, origDefault)

    def setUp(self) -> None:
        self._validator = CalendarValidator.CalendarValidator1()
        self.__calValidator = self._validator

    def testAdjustToTimeZone(self) -> None:

        calEST = self._createCalendar(
            self._EST, self.__DATE_2005_11_23, self.__TIME_12_03_45
        )
        dateEST = calEST

        calGMT = self._createCalendar(
            self._GMT, self.__DATE_2005_11_23, self.__TIME_12_03_45
        )
        dateGMT = calGMT

        calCET = self._createCalendar(
            self._EET, self.__DATE_2005_11_23, self.__TIME_12_03_45
        )
        dateCET = calCET

        self.assertFalse(dateGMT is dateCET, "Check GMT is not CET")
        self.assertFalse(dateGMT is dateEST, "Check GMT is not EST")
        self.assertFalse(dateCET is dateEST, "Check CET is not EST")

        calEST = CalendarValidator.adjustToTimeZone(calEST, self._GMT)
        self.assertEqual(dateGMT, calEST, "EST to GMT")
        self.assertFalse(dateEST is calEST, "Check EST is not GMT")
        calEST = CalendarValidator.adjustToTimeZone(calEST, self._EST)
        self.assertEqual(dateEST, calEST, "back to EST")
        self.assertFalse(dateGMT is calEST, "Check EST is not GMT")

        calCET = CalendarValidator.adjustToTimeZone(calCET, self._GMT)
        self.assertEqual(dateGMT, calCET, "CET to GMT")
        self.assertFalse(dateCET is calCET, "Check CET is not GMT")
        calCET = CalendarValidator.adjustToTimeZone(calCET, self._EET)
        self.assertEqual(dateCET, calCET, "back to CET")
        self.assertFalse(dateGMT is calCET, "Check CET is not GMT")

        calUTC = self._createCalendar(
            self._UTC, self.__DATE_2005_11_23, self.__TIME_12_03_45
        )
        now = datetime.datetime.now()
        self.assertTrue(
            now.astimezone(self._UTC).utcoffset() == now.astimezone(self._GMT).utcoffset(), 
            "SAME: UTC = GMT"
        )
        self.assertEqual(calUTC, calGMT, "SAME: Check time (A)")
        self.assertFalse(self._GMT == calUTC.tzinfo, "SAME: Check GMT(A)")
        self.assertTrue(self._UTC == calUTC.tzinfo, "SAME: Check UTC(A)")
        calUTC = CalendarValidator.adjustToTimeZone(calUTC, self._GMT)
        self.assertEqual(calUTC, calGMT, "SAME: Check time (B)")
        self.assertTrue(self._GMT == calUTC.tzinfo, "SAME: Check GMT(B)")
        self.assertFalse(self._UTC == calUTC.tzinfo, "SAME: Check UTC(B)")

    def testDateTimeStyle(self) -> None:

        origDefault = locale.getlocale()
        locale.setlocale(locale.LC_ALL, "en_GB.UTF-8")

        dateTimeValidator = AbstractCalendarValidator(True, 3, 3)
        self.assertTrue(dateTimeValidator.isValid0("31/12/05 14:23"))
        self.assertTrue(dateTimeValidator.isValid2("12/31/05 2:23 PM", "en_US.UTF-8"))

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
            self.__calValidator._compare(value, diffHour, "HOUR_OF_DAY"), 1
        )
        self.assertEqual(
            self.__calValidator._compare(value, diffMin, "HOUR_OF_DAY"), 0
        )
        self.assertEqual(
            self.__calValidator._compare(value, diffMin, "MINUTE"), 1
        )
        self.assertEqual(
            self.__calValidator._compare(value, diffSec, "MINUTE"), 0
        )
        self.assertEqual(
            self.__calValidator._compare(value, diffSec, "SECOND"), 1
        )

        self.assertEqual(
            self.__calValidator.compareDates(value, cal20050824), -1
        )  # +1 day
        self.assertEqual(
            self.__calValidator.compareDates(value, diffHour), 0
        )  # same day, diff hour
        self.assertEqual(
            self.__calValidator._compare(value, diffHour, "DAY_OF_YEAR"), 0
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
            self.__calValidator._compare(value, cal20050822, "WEEK_OF_MONTH"), 0
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
            self.__calValidator._compare(value, value, -1)
        self.assertTrue("Invalid field: -1" in str(context.exception))

    def testCalendarValidatorMethods(self) -> None:

        locale.setlocale(locale.LC_ALL, "en_US.UTF-8")
        locale_ = "de_DE.UTF-8"
        pattern = "yyyy-MM-dd"
        pattern_val = "2005-12-31"
        german_val = "31 Dez 2005"
        german_pattern = "dd MMM yyyy"
        locale_val = "31.12.2005"
        default_val = "12/31/05"
        xxxx = "XXXX"
        expected = self._createCalendar(None, 20051231, 0)

        self.assertEqual(
            expected,
            CalendarValidator.getInstance().validate0(default_val),
            "validate(A) default"
        )

        self.assertEqual(
            expected,
            CalendarValidator.getInstance().validate4(locale_val, locale_),
            "validate(A) locale "
        )

        self.assertEqual(
            expected,
            CalendarValidator.getInstance().validate2(pattern_val, pattern),
            "validate(A) pattern"
        )

        self.assertEqual(
            expected,
            CalendarValidator.getInstance()\
                .validate6(german_val, german_pattern, "de_DE.UTF-8"),
            "validate(A) both"
        )

        self.assertTrue(
            CalendarValidator.getInstance().isValid0(default_val), "isValid(A) default"
        )
        self.assertTrue(
            CalendarValidator.getInstance().isValid2(locale_val, locale_),
            "isValid(A) locale "
        )
        self.assertTrue(
            CalendarValidator.getInstance().isValid1(pattern_val, pattern),
            "isValid(A) pattern"
        )
        self.assertTrue(
            CalendarValidator.getInstance().isValid3(
                german_val, german_pattern, "de_DE.UTF-8"
            ),
            "isValid(A) both"
        )

        self.assertIsNone(
            CalendarValidator.getInstance().validate0(xxxx),
            "validate(B) default"
        )
        self.assertIsNone(
            CalendarValidator.getInstance().validate4(xxxx, locale_),
            "validate(B) locale "
        )
        self.assertIsNone(
            CalendarValidator.getInstance().validate2(xxxx, pattern),
            "validate(B) pattern"
        )
        self.assertIsNone(
            CalendarValidator.getInstance().validate6(
                "31 Dec 2005", german_pattern, "de_DE.UTF-8"
            ),
            "validate(B) both"
        )

        self.assertFalse(
            CalendarValidator.getInstance().isValid0(xxxx),
            "isValid(B) default"
        )
        self.assertFalse(
            CalendarValidator.getInstance().isValid2(xxxx, locale_),
            "isValid(B) locale "
        )
        self.assertFalse(
            CalendarValidator.getInstance().isValid1(xxxx, pattern),
            "isValid(B) pattern"
        )
        self.assertFalse(
            CalendarValidator.getInstance().isValid3(
                "31 Dec 2005", german_pattern, locale_
            ),
            "isValid(B) both"
        )

        defaultZone = ZoneInfo("UTC")
        defaultOffset = datetime.datetime.now(defaultZone).utcoffset().total_seconds()
        eetOffset = datetime.datetime.now(self._EET)\
            .utcoffset().total_seconds()

        if defaultOffset == eetOffset:
            zone = self._EST
        else:
            zone = self._EET
        
        expected_zone = self._createCalendar(zone, 20051231, 0)

        self.assertFalse(
            expected is expected_zone, "default/EET same "
        )

        self.assertEqual(
            expected_zone,
            CalendarValidator.getInstance().validate1(default_val, zone),
            "validate(C) default"
        )

        self.assertEqual(
            expected_zone,
            CalendarValidator.getInstance().validate5(locale_val, locale_, zone),
            "validate(C) locale "
        )

        self.assertEqual(
            expected_zone,
            CalendarValidator.getInstance().validate3(pattern_val, pattern, zone),
            "validate(C) pattern"
        )

        self.assertEqual(
            expected_zone,
            CalendarValidator.getInstance()\
                .validate7(german_val, german_pattern, "de_DE.UTF-8", zone),
            "validate(C) both"
        )

    def __init__(self, name: str) -> None:
        super().__init__(name)
