import pytest

import unittest
from abc import ABC
from datetime import datetime
from io import BytesIO
import pickle
from zoneinfo import ZoneInfo

class AbstractCalendarValidatorTest(unittest.TestCase, ABC):

    @classmethod
    def setUpClass(cls):
        if cls == AbstractCalendarValidatorTest:
            "Tests shall only be executed on child classes with concrete implementations."
            raise unittest.SkipTest("Skip tests in the abstract base class.")

    _GMT = ZoneInfo('Etc/GMT')  # 0 offset
    _EST = ZoneInfo('US/Eastern')  # - 5 hours
    _EET = ZoneInfo('EET')  # + 2 hours
    _UTC = ZoneInfo('UTC')  # 0 offset

    
    def __init__(self, methodName='runTest') -> None:
        self.setUpClass()
        super().__init__(methodName)
        self._validator = None
        self._patternValid = [
            "2005-01-01",
            "2005-12-31",
            "2004-02-29",  # valid leap
            "2005-04-30",
            "05-12-31",
            "2005-1-1",
            "05-1-1"
        ]

        self._localeValid = [
            "01/01/2005",
            "12/31/2005",
            "02/29/2004",  # valid leap
            "04/30/2005",
            "12/31/05",
            "1/1/2005",
            "1/1/05"
        ]

        self._patternExpect = [
            datetime.strptime("20050101", "%Y%m%d"),
            datetime.strptime("20051231", "%Y%m%d"),
            datetime.strptime("20040229", "%Y%m%d"),
            datetime.strptime("20050430", "%Y%m%d"),
            datetime.strptime("20051231", "%Y%m%d"),
            datetime.strptime("20050101", "%Y%m%d"),
            datetime.strptime("20050101", "%Y%m%d")
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
            "2005-01-"  # invalid pattern
        ]

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
            "01//2005"  # invalid pattern
        ]

    
    def setUpValidator(self, validator) -> None:
        self._validator = validator

    
    def setUp(self) -> None:
        try:
            super().setUp()
        except Exception as e:
            self.fail(f"An exception occurred when setting up the test: {e}")

    
    def tearDown(self) -> None:
        try:
            super().tearDown()
            self._validator = None
        except Exception as e:
            self.fail(f"An exception occurred when cleaning up the test: {e}")


    @pytest.mark.test
    def testPatternValid(self) -> None:
        for i, pattern in enumerate(self._patternValid):
            text = f"{i} value=[{pattern}] failed "
            date = self._validator.parse(pattern, "yy-MM-dd", None, None)
            self.assertIsNotNone(date, f"validateObj() {text}{date}")
            self.assertTrue(
                self._validator.isValid1(pattern, "yy-MM-dd"),
                f"isValid() {text}"
            )
            if isinstance(date, datetime):
                date = date
            self.assertEqual(date, self._patternExpect[i], f"compare {text}")

    
    @pytest.mark.test
    def testPatternInvalid(self) -> None:
        for i, pattern in enumerate(self._patternInvalid):
            text = f"{i} value=[{pattern}] passed "
            date = self._validator.parse(pattern, "yy-MM-dd", None, None)
            self.assertIsNone(date, f"validateObj() {text}{date}")
            self.assertFalse(
                self._validator.isValid1(pattern, "yy-MM-dd"),
                f"isValid() {text}"
            )

    
    @pytest.mark.test
    def testLocaleValid(self) -> None:
        for i, pattern in enumerate(self._localeValid):
            text = f"{i} value=[{pattern}] failed "
            date = self._validator.parse(pattern, None, 'en_US.UTF-8', None)
            self.assertIsNotNone(date, f"validateObj() {text}{date}")
            self.assertTrue(
                self._validator.isValid2(pattern, 'en_US.UTF-8'),
                f"isValid() {text}"
            )
            if isinstance(date, datetime):
                date = date
            self.assertEqual(date, self._patternExpect[i], f"compare {text}")

    
    @pytest.mark.test
    def testLocaleInvalid(self) -> None:
        for i, pattern in enumerate(self._localeInvalid):
            text = f"{i} value=[{pattern}] passed "
            date = self._validator.parse(pattern, None, 'en_US.UTF-8', None)
            self.assertIsNone(date, f"validateObj() {text}{date}")
            self.assertFalse(
                self._validator.isValid2(pattern, 'en_US.UTF-8'),
                f"isValid() {text}"
            )

    
    @pytest.mark.test
    def testFormat(self) -> None:
        test = self._validator.parse("2005-11-28", "yyyy-MM-dd", None, None)
        self.assertIsNotNone(test, "Test Date")
        self.assertEqual(
            self._validator.format1(test, "dd.MM.yy"),
            "28.11.05",
            "Format pattern"
        )
        self.assertEqual(
            self._validator.format2(test, 'en_US.UTF-8'),
            "11/28/05",
            "Format locale"
        )

    
    @pytest.mark.test
    def testSerialization(self) -> None:
        baos = BytesIO()
        try:
            pickle.dump(self._validator, baos)
        except Exception as e:
            self.fail(f"{self._validator.__class__.__name__} error during serialization: {e}")

        result = None
        try:
            bais = BytesIO(baos.getvalue())
            result = pickle.load(bais)
        except Exception as e:
            self.fail(
                f"{self._validator.__class__.__name__} error during deserialization: {e}"
            )
        
        self.assertIsNotNone(result)

    
    @staticmethod
    def _createCalendar(zone, date, time):
        if zone is None:
            zone = ZoneInfo('UTC')
        year = date // 10000
        mth = (date // 100) % 100
        day = date % 100
        hour = time // 10000
        min = (time // 100) % 100
        sec = time % 100
        return datetime(year, mth, day, hour, min, sec, tzinfo=zone)

    
    @staticmethod
    def _createDate(zone, date, time):
        return AbstractCalendarValidatorTest._createCalendar(zone, date, time)
