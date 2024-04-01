# Imports Begin
from src.main.org.apache.commons.validator.routines.AbstractCalendarValidator import *
import unittest
import pickle
import os
import datetime
import typing
from typing import *
import io
from abc import ABC

# Imports End


class AbstractCalendarValidatorTest(unittest.TestCase, TestCase, ABC):

    # Class Fields Begin
    _localeInvalid: typing.List[str] = ""  # LLM could not translate field
    _validator: AbstractCalendarValidator = None
    _GMT: datetime.timezone = ""  # LLM could not translate field
    _EST: datetime.timezone = ""  # LLM could not translate field
    _EET: datetime.timezone = ""  # LLM could not translate field
    _UTC: datetime.timezone = ""  # LLM could not translate field
    _patternValid: List[str] = [
        "2005-01-01",
        "2005-12-31",
        "2004-02-29",
        "2005-04-30",
        "05-12-31",
        "2005-1-1",
        "05-1-1",
    ]
    _localeValid: List[str] = [
        "01/01/2005",
        "12/31/2005",
        "02/29/2004",
        "04/30/2005",
        "12/31/05",
        "1/1/2005",
        "1/1/05",
    ]
    _patternExpect: List[datetime.date] = [
        datetime.date(2005, 1, 1),
        datetime.date(2005, 12, 31),
        datetime.date(2004, 2, 29),
        datetime.date(2005, 4, 30),
        datetime.date(2005, 12, 31),
        datetime.date(2005, 1, 1),
        datetime.date(2005, 1, 1),
    ]
    _patternInvalid: List[str] = [
        "2005-00-01",
        "2005-01-00",
        "2005-13-03",
        "2005-04-31",
        "2005-03-32",
        "2005-02-29",
        "200X-01-01",
        "2005-0X-01",
        "2005-01-0X",
        "01/01/2005",
        "2005-01",
        "2005--01",
        "2005-01-",
    ]
    # Class Fields End

    # Class Methods Begin
    def _tearDown(self) -> None:

        pass  # LLM could not translate method body

    def _setUp(self) -> None:

        pass  # LLM could not translate method body

    @staticmethod
    def _createDate(
        zone: datetime.timezone, date: int, time: int
    ) -> typing.Union[datetime.date, datetime.datetime]:

        pass  # LLM could not translate method body

    @staticmethod
    def _createCalendar(zone: datetime.timezone, date: int, time: int) -> typing.Union[
        datetime.datetime,
        datetime.date,
        datetime.time,
        datetime.timedelta,
        datetime.timezone,
    ]:

        pass  # LLM could not translate method body

    def testSerialization(self) -> None:

        baos = io.BytesIO()
        try:
            oos = pickle.Pickler(baos)
            oos.dump(self._validator)
            oos.flush()
            oos.close()
        except Exception as e:
            self.fail(
                f"{type(self._validator).__name__} error during serialization: {e}"
            )
        result = None
        try:
            bais = io.BytesIO(baos.getvalue())
            ois = pickle.Unpickler(bais)
            result = ois.load()
            bais.close()
        except Exception as e:
            self.fail(
                f"{type(self._validator).__name__} error during deserialization: {e}"
            )
        self.assertIsNotNone(result)

    def testFormat(self) -> None:

        test = self._parse("2005-11-28", "yyyy-MM-dd", None, None)
        assert test is not None
        assert self.format1(test, "dd.MM.yy") == "28.11.05"
        assert self.format2(test, Locale.US) == "11/28/05"

    def testLocaleInvalid(self) -> None:

        for i in range(len(self.localeInvalid)):
            text = f"{i} value=[" + self.localeInvalid[i] + "] passed "
            date = self._parse(self.localeInvalid[i], None, Locale.US, None)
            assert date is None, f"validateObj() {text} {date}"
            assert not self.isValid2(
                self.localeInvalid[i], Locale.US
            ), f"isValid() {text}"

    def testLocaleValid(self) -> None:

        for i in range(len(self._localeValid)):
            text = f"{i} value=['{self._localeValid[i]}'] failed "
            date = self._validator._parse(self._localeValid[i], None, Locale.US, None)
            assert date is not None, f"validateObj() {text} {date}"
            assert self._validator.isValid2(
                self._localeValid[i], Locale.US
            ), f"isValid() {text}"
            if isinstance(date, Calendar):
                date = date.getTime()
            assert date == self._patternExpect[i], f"compare {text}"

    def testPatternInvalid(self) -> None:

        for i in range(len(self._patternInvalid)):
            text = f"{i} value=['{self._patternInvalid[i]}'] passed "
            date = self._validator._parse(
                self._patternInvalid[i], "yy-MM-dd", None, None
            )
            assert date is None, f"validateObj() {text} {date}"
            assert not self._validator.isValid1(
                self._patternInvalid[i], "yy-MM-dd"
            ), f"isValid() {text}"

    def testPatternValid(self) -> None:

        for i in range(len(self._patternValid)):
            text = f"{i} value=[{self._patternValid[i]}] failed "
            date = self._validator._parse(self._patternValid[i], "yy-MM-dd", None, None)
            assert date is not None, f"validateObj() {text} {date}"
            assert self._validator.isValid1(
                self._patternValid[i], "yy-MM-dd"
            ), f"isValid() {text}"
            if isinstance(date, datetime.datetime):
                date = date.date()
            assert self._patternExpect[i] == date, f"compare {text}"

    def __init__(self, name: str) -> None:

        super().__init__(name)

    # Class Methods End
