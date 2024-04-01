# Imports Begin
from src.main.org.apache.commons.validator.routines.TimeValidator import *
import unittest
import os
import datetime
import typing
from typing import *

# Imports End


class TimeValidatorTest(unittest.TestCase, TestCase):

    # Class Fields Begin
    __origDefault: typing.Any = None
    __defaultZone: datetime.timezone = None
    _GMT: datetime.timezone = ""  # LLM could not translate field
    _EST: datetime.timezone = ""  # LLM could not translate field
    _validator: TimeValidator = None
    _patternValid: List[str] = [
        "23-59-59",
        "00-00-00",
        "00-00-01",
        "0-0-0",
        "1-12-1",
        "10-49-18",
        "16-23-46",
    ]
    _patternExpect: List[datetime.date] = [
        datetime.date(235959, 0, 0),
        datetime.date(0, 0, 0),
        datetime.date(1, 0, 0),
        datetime.date(0, 0, 0),
        datetime.date(11201, 0, 0),
        datetime.date(104918, 0, 0),
        datetime.date(162346, 0, 0),
    ]
    _localeValid: List[str] = [
        "23:59",
        "00:00",
        "00:01",
        "0:0",
        "1:12",
        "10:49",
        "16:23",
    ]
    _localeExpect: List[datetime.date] = [
        datetime.date(year=1970, month=1, day=1, hour=23, minute=59, second=0),
        datetime.date(year=1970, month=1, day=1, hour=0, minute=0, second=0),
        datetime.date(year=1970, month=1, day=1, hour=10, minute=0, second=0),
        datetime.date(year=1970, month=1, day=1, hour=0, minute=0, second=0),
        datetime.date(year=1970, month=1, day=1, hour=11, minute=20, second=0),
        datetime.date(year=1970, month=1, day=1, hour=10, minute=49, second=0),
        datetime.date(year=1970, month=1, day=1, hour=16, minute=23, second=0),
    ]
    _patternInvalid: List[str] = [
        "24-00-00",
        "24-00-01",
        "25-02-03",
        "10-61-31",
        "10-01-61",
        "05:02-29",
        "0X-01:01",
        "05-0X-01",
        "10-01-0X",
        "01:01:05",
        "10-10",
        "10--10",
        "10-10-",
    ]
    _localeInvalid: typing.List[str] = ""  # LLM could not translate field
    # Class Fields End

    # Class Methods Begin
    def _tearDown(self) -> None:

        pass  # LLM could not translate method body

    def _setUp(self) -> None:

        pass  # LLM could not translate method body

    @staticmethod
    def _createDate(
        zone: datetime.timezone, time: int, millisecond: int
    ) -> typing.Union[datetime.date, datetime.datetime]:

        pass  # LLM could not translate method body

    @staticmethod
    def _createTime(
        zone: datetime.timezone, time: int, millisecond: int
    ) -> typing.Union[
        datetime.datetime,
        datetime.date,
        datetime.time,
        datetime.timedelta,
        datetime.timezone,
    ]:

        calendar = (
            zone.localize(datetime.datetime.now())
            if zone is None
            else datetime.datetime.now(zone)
        )
        hour = (time // 10000) * 10000
        min = (time // 100) * 100 - hour
        sec = time - (hour + min)
        calendar.replace(
            year=1970,
            month=1,
            day=1,
            hour=hour // 10000,
            minute=min // 100,
            second=sec,
            microsecond=millisecond * 1000,
        )
        return calendar

    def testCompare(self) -> None:

        pass  # LLM could not translate method body

    def testFormat(self) -> None:

        Locale.setDefault(Locale.UK)
        test = TimeValidator.getInstance().validate2("16:49:23", "HH:mm:ss")
        assertNotNull("Test Date ", test)
        self.assertEqual(
            "Format pattern", "16-49-23", self.validator.format1(test, "HH-mm-ss")
        )
        self.assertEqual(
            "Format locale", "4:49 PM", self.validator.format2(test, Locale.US)
        )
        self.assertEqual("Format default", "16:49", self.validator.format0(test))

    def testTimeZone(self) -> None:

        pass  # LLM could not translate method body

    def testLocaleInvalid(self) -> None:

        for i in range(len(self._localeInvalid)):
            text = f"{i} value=[" + self._localeInvalid[i] + "] passed "
            date = self._validator.validate4(self._localeInvalid[i], Locale.US)
            assert date is None, f"validate() {text} {date}"
            assert not self._validator.isValid2(
                self._localeInvalid[i], Locale.UK
            ), f"isValid() {text}"

    def testLocaleValid(self) -> None:

        for i in range(len(self._localeValid)):
            text = f"{i} value=['{self._localeValid[i]}'] failed "
            calendar = self._validator.validate4(self._localeValid[i], Locale.UK)
            assert calendar is not None, f"validate() {text}"
            date = calendar.getTime()
            assert self._validator.isValid2(
                self._localeValid[i], Locale.UK
            ), f"isValid() {text}"
            assert date == self._localeExpect[i], f"compare {text}"

    def testPatternInvalid(self) -> None:

        for i in range(len(self._patternInvalid)):
            text = str(i) + " value=[" + self._patternInvalid[i] + "] passed "
            date = self._validator.validate2(self._patternInvalid[i], "HH-mm-ss")
            assert date is None, "validate() " + text + str(date)
            assert not self._validator.isValid1(self._patternInvalid[i], "HH-mm-ss"), (
                "isValid() " + text
            )

    def testPatternValid(self) -> None:

        for i in range(len(self._patternValid)):
            text = f"{i} value=[{self._patternValid[i]}] failed "
            calendar = self._validator.validate2(self._patternValid[i], "HH-mm-ss")
            assert calendar is not None, f"validateObj() {text}"
            date = calendar.getTime()
            assert self._validator.isValid1(
                self._patternValid[i], "HH-mm-ss"
            ), f"isValid() {text}"
            assert date == self._patternExpect[i], f"compare {text}"

    def __init__(self, name: str) -> None:

        super().__init__(name)

    # Class Methods End
