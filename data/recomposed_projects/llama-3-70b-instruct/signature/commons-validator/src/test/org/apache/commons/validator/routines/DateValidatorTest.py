from __future__ import annotations
import time
import re
import datetime
import unittest
import pytest
import io
from src.main.org.apache.commons.validator.routines.AbstractCalendarValidator import *
from src.test.org.apache.commons.validator.routines.AbstractCalendarValidatorTest import *
from src.main.org.apache.commons.validator.routines.DateValidator import *


class DateValidatorTest(AbstractCalendarValidatorTest):

    __dateValidator: DateValidator = None

    def setUp(self) -> None:
        super().setUp()
        self.__dateValidator = DateValidator.DateValidator1()
        self._validator = self.__dateValidator

    def testCompare(self) -> None:
        sameTime: int = 124522
        testDate: int = 20050823
        diffHour: datetime.datetime = self._createDate(
            self._GMT, testDate, 115922
        )  # same date, different time

        value: datetime.datetime = self._createDate(
            self._GMT, testDate, sameTime
        )  # test value
        date20050824: datetime.datetime = self._createDate(
            self._GMT, 20050824, sameTime
        )  # +1 day
        date20050822: datetime.datetime = self._createDate(
            self._GMT, 20050822, sameTime
        )  # -1 day

        date20050830: datetime.datetime = self._createDate(
            self._GMT, 20050830, sameTime
        )  # +1 week
        date20050816: datetime.datetime = self._createDate(
            self._GMT, 20050816, sameTime
        )  # -1 week

        date20050901: datetime.datetime = self._createDate(
            self._GMT, 20050901, sameTime
        )  # +1 month
        date20050801: datetime.datetime = self._createDate(
            self._GMT, 20050801, sameTime
        )  # same month
        date20050731: datetime.datetime = self._createDate(
            self._GMT, 20050731, sameTime
        )  # -1 month

        date20051101: datetime.datetime = self._createDate(
            self._GMT, 20051101, sameTime
        )  # +1 quarter (Feb Start)
        date20051001: datetime.datetime = self._createDate(
            self._GMT, 20051001, sameTime
        )  # +1 quarter
        date20050701: datetime.datetime = self._createDate(
            self._GMT, 20050701, sameTime
        )  # same quarter
        date20050630: datetime.datetime = self._createDate(
            self._GMT, 20050630, sameTime
        )  # -1 quarter
        date20050110: datetime.datetime = self._createDate(
            self._GMT, 20050110, sameTime
        )  # Previous Year qtr (Fen start)

        date20060101: datetime.datetime = self._createDate(
            self._GMT, 20060101, sameTime
        )  # +1 year
        date20050101: datetime.datetime = self._createDate(
            self._GMT, 20050101, sameTime
        )  # same year
        date20041231: datetime.datetime = self._createDate(
            self._GMT, 20041231, sameTime
        )  # -1 year

        self.assertEqual(
            "date LT",
            -1,
            self.__dateValidator.compareDates(value, date20050824, self._GMT),
        )  # +1 day
        self.assertEqual(
            "date EQ", 0, self.__dateValidator.compareDates(value, diffHour, self._GMT)
        )  # same day, diff hour
        self.assertEqual(
            "date GT",
            1,
            self.__dateValidator.compareDates(value, date20050822, self._GMT),
        )  # -1 day

        self.assertEqual(
            "week LT",
            -1,
            self.__dateValidator.compareWeeks(value, date20050830, self._GMT),
        )  # +1 week
        self.assertEqual(
            "week =1",
            0,
            self.__dateValidator.compareWeeks(value, date20050824, self._GMT),
        )  # +1 day
        self.assertEqual(
            "week =2",
            0,
            self.__dateValidator.compareWeeks(value, date20050822, self._GMT),
        )  # same week
        self.assertEqual(
            "week =3",
            0,
            self.__dateValidator.compareWeeks(value, date20050822, self._GMT),
        )  # -1 day
        self.assertEqual(
            "week GT",
            1,
            self.__dateValidator.compareWeeks(value, date20050816, self._GMT),
        )  # -1 week

        self.assertEqual(
            "mnth LT",
            -1,
            self.__dateValidator.compareMonths(value, date20050901, self._GMT),
        )  # +1 month
        self.assertEqual(
            "mnth =1",
            0,
            self.__dateValidator.compareMonths(value, date20050830, self._GMT),
        )  # +1 week
        self.assertEqual(
            "mnth =2",
            0,
            self.__dateValidator.compareMonths(value, date20050801, self._GMT),
        )  # same month
        self.assertEqual(
            "mnth =3",
            0,
            self.__dateValidator.compareMonths(value, date20050816, self._GMT),
        )  # -1 week
        self.assertEqual(
            "mnth GT",
            1,
            self.__dateValidator.compareMonths(value, date20050731, self._GMT),
        )  # -1 month

        self.assertEqual(
            "qtrA <1",
            -1,
            self.__dateValidator.compareQuarters0(value, date20051101, self._GMT),
        )  # +1 quarter (Feb)
        self.assertEqual(
            "qtrA <2",
            -1,
            self.__dateValidator.compareQuarters0(value, date20051001, self._GMT),
        )  # +1 quarter
        self.assertEqual(
            "qtrA =1",
            0,
            self.__dateValidator.compareQuarters0(value, date20050901, self._GMT),
        )  # +1 month
        self.assertEqual(
            "qtrA =2",
            0,
            self.__dateValidator.compareQuarters0(value, date20050701, self._GMT),
        )  # same quarter
        self.assertEqual(
            "qtrA =3",
            0,
            self.__dateValidator.compareQuarters0(value, date20050731, self._GMT),
        )  # -1 month
        self.assertEqual(
            "qtrA GT",
            1,
            self.__dateValidator.compareQuarters0(value, date20050630, self._GMT),
        )  # -1 quarter

        self.assertEqual(
            "qtrB LT",
            -1,
            self.__dateValidator.compareQuarters1(value, date20051101, self._GMT, 2),
        )  # +1 quarter (Feb)
        self.assertEqual(
            "qtrB =1",
            0,
            self.__dateValidator.compareQuarters1(value, date20051001, self._GMT, 2),
        )  # same quarter
        self.assertEqual(
            "qtrB =2",
            0,
            self.__dateValidator.compareQuarters1(value, date20050901, self._GMT, 2),
        )  # +1 month
        self.assertEqual(
            "qtrB =3",
            1,
            self.__dateValidator.compareQuarters1(value, date20050701, self._GMT, 2),
        )  # same quarter
        self.assertEqual(
            "qtrB =4",
            1,
            self.__dateValidator.compareQuarters1(value, date20050731, self._GMT, 2),
        )  # -1 month
        self.assertEqual(
            "qtrB GT",
            1,
            self.__dateValidator.compareQuarters1(value, date20050630, self._GMT, 2),
        )  # -1 quarter
        self.assertEqual(
            "qtrB prev",
            1,
            self.__dateValidator.compareQuarters1(value, date20050110, self._GMT, 2),
        )  # Jan Prev year qtr

        self.assertEqual(
            "year LT",
            -1,
            self.__dateValidator.compareYears(value, date20060101, self._GMT),
        )  # +1 year
        self.assertEqual(
            "year EQ",
            0,
            self.__dateValidator.compareYears(value, date20050101, self._GMT),
        )  # same year
        self.assertEqual(
            "year GT",
            1,
            self.__dateValidator.compareYears(value, date20041231, self._GMT),
        )  # -1 year

        sameDayTwoAm: datetime.datetime = self._createDate(self._GMT, testDate, 20000)
        self.assertEqual(
            "date LT",
            -1,
            self.__dateValidator.compareDates(value, date20050824, self._EST),
        )  # +1 day
        self.assertEqual(
            "date EQ", 0, self.__dateValidator.compareDates(value, diffHour, self._EST)
        )  # same day, diff hour
        self.assertEqual(
            "date EQ",
            1,
            self.__dateValidator.compareDates(value, sameDayTwoAm, self._EST),
        )  # same day, diff hour
        self.assertEqual(
            "date GT",
            1,
            self.__dateValidator.compareDates(value, date20050822, self._EST),
        )  # -1 day

    def testDateValidatorMethods(self) -> None:

        pass  # LLM could not translate this method

    def testLocaleProviders(self) -> None:

        pass  # LLM could not translate this method

    def __init__(self, name: str) -> None:
        super().__init__(name)
