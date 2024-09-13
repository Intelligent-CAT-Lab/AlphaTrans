from __future__ import annotations
import time
import locale
import re
import os
import unittest
import pytest
import io
from zoneinfo import ZoneInfo
import platform
from src.main.org.apache.commons.validator.routines.AbstractCalendarValidator import *
from src.test.org.apache.commons.validator.routines.AbstractCalendarValidatorTest import *
from src.main.org.apache.commons.validator.routines.DateValidator import *


class DateValidatorTest(AbstractCalendarValidatorTest):

    __dateValidator: DateValidator = None

    def setUp(self) -> None:
        self.__dateValidator = DateValidator.DateValidator1()
        self._validator = self.__dateValidator

    def testCompare(self) -> None:

        sameTime = 124522
        testDate = 20050823
        diffHour = self._createDate(
            self._GMT, testDate, 115922
        )  # same date, different time

        value = self._createDate(self._GMT, testDate, sameTime)  # test value
        date20050824 = self._createDate(self._GMT, 20050824, sameTime)  # +1 day
        date20050822 = self._createDate(self._GMT, 20050822, sameTime)  # -1 day

        date20050830 = self._createDate(self._GMT, 20050830, sameTime)  # +1 week
        date20050816 = self._createDate(self._GMT, 20050816, sameTime)  # -1 week

        date20050901 = self._createDate(self._GMT, 20050901, sameTime)  # +1 month
        date20050801 = self._createDate(self._GMT, 20050801, sameTime)  # same month
        date20050731 = self._createDate(self._GMT, 20050731, sameTime)  # -1 month

        date20051101 = self._createDate(
            self._GMT, 20051101, sameTime
        )  # +1 quarter (Feb Start)
        date20051001 = self._createDate(self._GMT, 20051001, sameTime)  # +1 quarter
        date20050701 = self._createDate(self._GMT, 20050701, sameTime)  # same quarter
        date20050630 = self._createDate(self._GMT, 20050630, sameTime)  # -1 quarter
        date20050110 = self._createDate(
            self._GMT, 20050110, sameTime
        )  # Previous Year qtr (Jan Start)

        date20060101 = self._createDate(self._GMT, 20060101, sameTime)  # +1 year
        date20050101 = self._createDate(self._GMT, 20050101, sameTime)  # same year
        date20041231 = self._createDate(self._GMT, 20041231, sameTime)  # -1 year

        self.assertEqual(
            -1, self.__dateValidator.compareDates(value, date20050824, self._GMT)
        )  # +1 day
        self.assertEqual(
            0, self.__dateValidator.compareDates(value, diffHour, self._GMT)
        )  # same day, diff hour
        self.assertEqual(
            1, self.__dateValidator.compareDates(value, date20050822, self._GMT)
        )  # -1 day

        self.assertEqual(
            -1, self.__dateValidator.compareWeeks(value, date20050830, self._GMT)
        )  # +1 week
        self.assertEqual(
            0, self.__dateValidator.compareWeeks(value, date20050824, self._GMT)
        )  # +1 day
        self.assertEqual(
            0, self.__dateValidator.compareWeeks(value, date20050822, self._GMT)
        )  # same week
        self.assertEqual(
            0, self.__dateValidator.compareWeeks(value, date20050822, self._GMT)
        )  # -1 day
        self.assertEqual(
            1, self.__dateValidator.compareWeeks(value, date20050816, self._GMT)
        )  # -1 week

        self.assertEqual(
            -1, self.__dateValidator.compareMonths(value, date20050901, self._GMT)
        )  # +1 month
        self.assertEqual(
            0, self.__dateValidator.compareMonths(value, date20050830, self._GMT)
        )  # +1 week
        self.assertEqual(
            0, self.__dateValidator.compareMonths(value, date20050801, self._GMT)
        )  # same month
        self.assertEqual(
            0, self.__dateValidator.compareMonths(value, date20050816, self._GMT)
        )  # -1 week
        self.assertEqual(
            1, self.__dateValidator.compareMonths(value, date20050731, self._GMT)
        )  # -1 month

        self.assertEqual(
            -1, self.__dateValidator.compareQuarters0(value, date20051101, self._GMT)
        )  # +1 quarter (Feb)
        self.assertEqual(
            -1, self.__dateValidator.compareQuarters0(value, date20051001, self._GMT)
        )  # +1 quarter
        self.assertEqual(
            0, self.__dateValidator.compareQuarters0(value, date20050901, self._GMT)
        )  # +1 month
        self.assertEqual(
            0, self.__dateValidator.compareQuarters0(value, date20050701, self._GMT)
        )  # same quarter
        self.assertEqual(
            0, self.__dateValidator.compareQuarters0(value, date20050731, self._GMT)
        )  # -1 month
        self.assertEqual(
            1, self.__dateValidator.compareQuarters0(value, date20050630, self._GMT)
        )  # -1 quarter

        self.assertEqual(
            -1, self.__dateValidator.compareQuarters1(value, date20051101, self._GMT, 2)
        )  # +1 quarter (Feb)
        self.assertEqual(
            0, self.__dateValidator.compareQuarters1(value, date20051001, self._GMT, 2)
        )  # same quarter
        self.assertEqual(
            0, self.__dateValidator.compareQuarters1(value, date20050901, self._GMT, 2)
        )  # +1 month
        self.assertEqual(
            1, self.__dateValidator.compareQuarters1(value, date20050701, self._GMT, 2)
        )  # same quarter
        self.assertEqual(
            1, self.__dateValidator.compareQuarters1(value, date20050731, self._GMT, 2)
        )  # -1 month
        self.assertEqual(
            1, self.__dateValidator.compareQuarters1(value, date20050630, self._GMT, 2)
        )  # -1 quarter
        self.assertEqual(
            1, self.__dateValidator.compareQuarters1(value, date20050110, self._GMT, 2)
        )  # Jan Prev year qtr

        self.assertEqual(
            -1, self.__dateValidator.compareYears(value, date20060101, self._GMT)
        )  # +1 year
        self.assertEqual(
            0, self.__dateValidator.compareYears(value, date20050101, self._GMT)
        )  # same year
        self.assertEqual(
            1, self.__dateValidator.compareYears(value, date20041231, self._GMT)
        )  # -1 year

        sameDayTwoAm = self._createDate(self._GMT, testDate, 20000)
        self.assertEqual(
            -1, self.__dateValidator.compareDates(value, date20050824, self._EST)
        )  # +1 day
        self.assertEqual(
            0, self.__dateValidator.compareDates(value, diffHour, self._EST)
        )  # same day, diff hour
        self.assertEqual(
            1, self.__dateValidator.compareDates(value, sameDayTwoAm, self._EST)
        )  # same day, diff hour
        self.assertEqual(
            1, self.__dateValidator.compareDates(value, date20050822, self._EST)
        )  # -1 day

    def testDateValidatorMethods(self) -> None:

        locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
        locale_ = 'de_DE.UTF-8'
        pattern = "yyyy-MM-dd"
        patternVal = "2005-12-31"
        germanVal = "31 Dez 2005"
        germanPattern = "dd MMM yyyy"
        localeVal = "31.12.2005"
        defaultVal = "12/31/05"
        XXXX = "XXXX"
        expected = self._createCalendar(None, 20051231, 0)

        self.assertEqual(
            DateValidator.getInstance().validate0(defaultVal),
            expected,
            "validate(A) default"
        )
        self.assertEqual(
            DateValidator.getInstance().validate4(localeVal, locale_),
            expected,
            "validate(A) locale"
        )
        self.assertEqual(
            DateValidator.getInstance().validate2(patternVal, pattern),
            expected,
            "validate(A) pattern"
        )
        self.assertEqual(
            DateValidator.getInstance().validate6(germanVal, germanPattern, locale_),
            expected,
            "validate(A) both"
        )

        self.assertTrue(
            DateValidator.getInstance().isValid0(defaultVal), 
            "isValid(A) default"
        )
        self.assertTrue(
            DateValidator.getInstance().isValid2(localeVal, locale_),
            "isValid(A) locale"
        )
        self.assertTrue(
            DateValidator.getInstance().isValid1(patternVal, pattern),
            "isValid(A) pattern"
        )
        self.assertTrue(
            DateValidator.getInstance().isValid3(germanVal, germanPattern, locale_),
            "isValid(A) both"
        )

        self.assertIsNone(
            DateValidator.getInstance().validate0(XXXX),
            "validate(B) default"
        )
        self.assertIsNone(
            DateValidator.getInstance().validate4(XXXX, locale_),
            "validate(B) locale"
        )
        self.assertIsNone(
            DateValidator.getInstance().validate2(XXXX, pattern),
            "validate(B) pattern"
        )
        self.assertIsNone(
            DateValidator.getInstance().validate6('31 Dec 2005', germanPattern, locale_),
            "validate(B) both"
        )

        self.assertFalse(
            DateValidator.getInstance().isValid0(XXXX),
            "isValid(B) default"
        )
        self.assertFalse(
            DateValidator.getInstance().isValid2(XXXX, locale_),
            "isValid(B) locale"
        )
        self.assertFalse(
            DateValidator.getInstance().isValid1(XXXX, pattern),
            "isValid(B) pattern"
        )
        self.assertFalse(
            DateValidator.getInstance().isValid3('31 Dec 2005', germanPattern, locale_),
            "isValid(B) both"
        )

        now = datetime.datetime.now()
        if now.astimezone(AbstractCalendarValidatorTest\
            ._EET).utcoffset() == now\
            .astimezone().utcoffset():
            zone = AbstractCalendarValidatorTest._EST
        else:
            zone = AbstractCalendarValidatorTest._EET
        expectedZone = self._createCalendar(zone, 20051231, 0)
        self.assertNotEqual(
            expected,
            expectedZone,
            "default/zone same " + str(zone)
        )

        self.assertEqual(
            DateValidator.getInstance().validate1(defaultVal, zone),
            expectedZone,
            "validate(C) default"
        )
        self.assertEqual(
            DateValidator.getInstance().validate5(localeVal, locale_, zone),
            expectedZone,
            "validate(C) locale"
        )
        self.assertEqual(
            DateValidator.getInstance().validate3(patternVal, pattern, zone),
            expectedZone,
            "validate(C) pattern"
        )
        self.assertEqual(
            DateValidator.getInstance().validate7(germanVal, germanPattern, locale_, zone),
            expectedZone,
            "validate(C) both"
        )

    def testLocaleProviders(self) -> None:

        localeProviders = os.getenv('java.locale.providers')
        if localeProviders is not None:
            self.assertTrue(
                localeProviders.startswith('COMPAT'),
                "java.locale.providers must start with COMPAT"
            )
        txt = "3/20/15 10:59:00 PM"
        if platform.system() == 'Linux':
            dateformat = datetime.datetime\
                .strptime(txt,"%m/%d/%y %I:%M:%S %p")\
                .replace(tzinfo=ZoneInfo('GMT'))
            date = dateformat
            self.assertIsNotNone(
                date,
                "Date should not be None"
            )

    def __init__(self, name: str) -> None:
        super().__init__(name)
