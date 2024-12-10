from __future__ import annotations
import time
import locale
import re
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

        pass  # LLM could not translate this method

    def testLocaleProviders(self) -> None:

        locale_providers = os.getenv("java.locale.providers")
        if locale_providers is not None:  # may be None before Java 9
            self.assertTrue(
                locale_providers.startswith("COMPAT"),
                "java.locale.providers must start with COMPAT",
            )

        txt = "3/20/15 10:59:00 PM"  # This relies on the locale format prior to Java 9 to parse
        dateformat = DateFormat.getDateTimeInstance(3, DateFormat.MEDIUM, Locale.US)
        dateformat.setTimeZone(TimeZone.getTimeZone("GMT"))
        date = dateformat.parse(txt)
        self.assertIsNotNone(date)

    def __init__(self, name: str) -> None:
        super().__init__(name)
