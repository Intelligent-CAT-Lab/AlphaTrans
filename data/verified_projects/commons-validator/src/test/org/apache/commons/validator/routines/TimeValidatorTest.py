import pytest

from src.main.org.apache.commons.validator.routines.TimeValidator import *
import unittest
from datetime import datetime
from zoneinfo import ZoneInfo
from locale import LC_TIME, getlocale, setlocale


def createTime(zone, time, millisecond):
    if zone is None:
        calendar = datetime.utcnow()
    else:
        calendar = datetime.now(zone)
    hour = (time // 10000) * 10000
    min = (time // 100) * 100 - hour
    sec = time - (hour + min)
    calendar = calendar.replace(
        year=1970, month=1, day=1,
        hour=hour // 10000,
        minute=min // 100,
        second=sec,
        microsecond=millisecond * 1000
    )
    return calendar


def createDate(zone, time, millisecond):
    calendar = createTime(zone, time, millisecond)
    return calendar


class TimeValidatorTest(unittest.TestCase):

    _GMT = ZoneInfo('Etc/GMT')  # 0 offset
    _EST = ZoneInfo('US/Eastern')  # - 5 hours

    _validator = None

    _patternValid = [
        "23-59-59", "00-00-00", "00-00-01", "0-0-0", "1-12-1", "10-49-18", "16-23-46"
    ]
    _patternExpect = [
        createDate(None, 235959, 0),
        createDate(None, 0, 0),
        createDate(None, 1, 0),
        createDate(None, 0, 0),
        createDate(None, 11201, 0),
        createDate(None, 104918, 0),
        createDate(None, 162346, 0)
    ]
    _localeValid = ["23:59", "00:00", "00:01", "0:0", "1:12", "10:49", "16:23"]
    _localeExpect = [
        createDate(None, 235900, 0),
        createDate(None, 0, 0),
        createDate(None, 100, 0),
        createDate(None, 0, 0),
        createDate(None, 11200, 0),
        createDate(None, 104900, 0),
        createDate(None, 162300, 0)
    ]
    _patternInvalid = [
        "24-00-00", "24-00-01", "25-02-03", "10-61-31", "10-01-61",
        "05:02-29", "0X-01:01", "05-0X-01", "10-01-0X", "01:01:05",
        "10-10", "10--10", "10-10-"
    ]
    _localeInvalid = [
        "24:00", "24:00", "25:02", "10:61", "05-02", "0X:01", "05:0X",
        "01-01", "10:", "10::1", "10:1:"
    ]

    __origDefault = None
    __defaultZone = None


    
    def setUp(self) -> None:
        try:
            super().setUp()
            self._validator = TimeValidator.TimeValidator1()
            self.__defaultZone = ZoneInfo('UTC')
            self.__origDefault = getlocale(LC_TIME)
        except Exception as e:
            self.fail(f"An exception occurred when setting up the test: {e}")

    
    def tearDown(self) -> None:
        try:
            super().tearDown()
            self._validator = None
            setlocale(LC_TIME, self.__origDefault)
        except Exception as e:
            self.fail(f"An exception occurred when cleaning up the test: {e}")

    
    @pytest.mark.test
    def testPatternValid(self) -> None:
        for i in range(len(self._patternValid)):
            text = f"{i} value=[{self._patternValid[i]}] failed "
            calendar = self._validator.validate2(self._patternValid[i], "HH-mm-ss")
            self.assertIsNotNone(
                calendar,
                "validateObj() " + text
            )
            date = calendar
            self.assertTrue(
                self._validator.isValid1(self._patternValid[i], "HH-mm-ss"),
                "isValid() " + text
            )
            self.assertEqual(
                date,
                self._patternExpect[i],
                "compare " + text
            )

    
    @pytest.mark.test
    def testPatternInvalid(self) -> None:
        for i in range(len(self._patternInvalid)):
            text = f"{i} value=[{self._patternInvalid[i]}] passed "
            date = self._validator.validate2(self._patternInvalid[i], "HH-mm-ss")
            self.assertIsNone(
                date,
                "validate() " + text + str(date)
            )
            self.assertFalse(
                self._validator.isValid1(self._patternInvalid[i], "HH-mm-ss"),
                "isValid() " + text
            )

    
    @pytest.mark.test
    def testLocaleValid(self) -> None:
        for i in range(len(self._localeValid)):
            text = f"{i} value=[{self._localeValid[i]}] failed "
            calendar = self._validator.validate4(self._localeValid[i], 'en_GB.UTF-8')
            self.assertIsNotNone(
                calendar,
                "validate() " + text
            )
            date = calendar
            self.assertTrue(
                self._validator.isValid2(self._localeValid[i], 'en_GB.UTF-8'),
                "isValid() " + text
            )
            self.assertEqual(
                date,
                self._localeExpect[i],
                "compare " + text
            )

    
    @pytest.mark.test
    def testLocaleInvalid(self) -> None:
        for i in range(len(self._localeInvalid)):
            text = f"{i} value=[{self._localeInvalid[i]}] passed "
            date = self._validator.validate4(self._localeInvalid[i], 'en_US.UTF-8')
            self.assertIsNone(
                date,
                "validate() " + text + str(date)
            )
            self.assertFalse(
                self._validator.isValid2(self._localeInvalid[i], 'en_GB.UTF-8'),
                "isValid() " + text
            )

    
    @pytest.mark.test
    def testTimeZone(self) -> None:
        setlocale(LC_TIME, 'en_GB.UTF-8')

        result = None

        result = self._validator.validate0("18:01")
        self.assertIsNotNone(
            result,
            "default result"
        )
        self.assertEqual(
            result.tzinfo,
            TimeValidatorTest._GMT,
            "default zone"
        )
        self.assertEqual(
            result.hour,
            18,
            "default hour"
        )
        self.assertEqual(
            result.minute,
            1,
            "default minute"
        )
        result = None

        result = self._validator.validate1("16:49", TimeValidatorTest._EST)
        self.assertIsNotNone(
            result,
            "zone result"
        )
        self.assertEqual(
            result.tzinfo,
            TimeValidatorTest._EST,
            "zone zone"
        )
        self.assertEqual(
            result.hour,
            16,
            "zone hour"
        )
        self.assertEqual(
            result.minute,
            49,
            "zone minute"
        )
        result = None

        result = self._validator.validate3("14-34", "HH-mm", TimeValidatorTest._EST)
        self.assertIsNotNone(
            result,
            "pattern result"
        )
        self.assertEqual(
            result.tzinfo,
            TimeValidatorTest._EST,
            "pattern zone"
        )
        self.assertEqual(
            result.hour,
            14,
            "pattern hour"
        )
        self.assertEqual(
            result.minute,
            34,
            "pattern minute"
        )
        result = None

        result = self._validator.validate5("7:18 PM", 'en_US.UTF-8', TimeValidatorTest._EST)
        self.assertIsNotNone(
            result,
            "locale result"
        )
        self.assertEqual(
            result.tzinfo,
            TimeValidatorTest._EST,
            "locale zone"
        )
        self.assertEqual(
            result.hour,
            19,
            "locale hour"
        )
        self.assertEqual(
            result.minute,
            18,
            "locale minute"
        )
        result = None

        result = self._validator.validate7(
            "31/Dez/05 21-05", "dd/MMM/yy HH-mm", 'de_DE.UTF-8', TimeValidatorTest._EST
        )
        self.assertIsNotNone(
            result,
            "pattern result"
        )
        self.assertEqual(
            result.tzinfo,
            TimeValidatorTest._EST,
            "pattern zone"
        )
        self.assertEqual(
            result.year,
            2005,
            "pattern day"
        )
        self.assertEqual(
            result.month,
            11,
            "pattern day"
        )
        self.assertEqual(
            result.day,
            31,
            "pattern day"
        )
        self.assertEqual(
            result.hour,
            21,
            "pattern hour"
        )
        self.assertEqual(
            result.minute,
            5,
            "pattern minute"
        )
        result = None

        result = self._validator.validate6(
            "31/Dez/05 21-05", "dd/MMM/yy HH-mm", 'de_DE.UTF-8'
        )
        self.assertIsNotNone(
            result,
            "pattern result"
        )
        self.assertEqual(
            result.tzinfo,
            TimeValidatorTest._GMT,
            "pattern zone"
        )
        self.assertEqual(
            result.year,
            2005,
            "pattern day"
        )
        self.assertEqual(
            result.month,
            11,
            "pattern day"
        )
        self.assertEqual(
            result.day,
            31,
            "pattern day"
        )
        self.assertEqual(
            result.hour,
            21,
            "pattern hour"
        )
        self.assertEqual(
            result.minute,
            5,
            "pattern minute"
        )
        result = None

    @pytest.mark.test
    def testFormat(self) -> None:
        self.__origDefault = 'en_GB.UTF-8'

        test = TimeValidator.getInstance().validate2("16:49:23", "HH:mm:ss")
        self.assertIsNotNone(
            test,
            "Test Date "
        )
        self.assertEqual(
            self._validator.format1(test, "HH-mm-ss"),
            "16-49-23",
            "Format pattern"
        )
        self.assertEqual(
            self._validator.format2(test, 'en_US.UTF-8'),
            "4:49 PM",
            "Format locale"
        )
        self.assertEqual(
            self._validator.format0(test),
            "16:49",
            "Format default"
        )

    @pytest.mark.test
    def testCompare(self) -> None:
        testTime = 154523
        min = 100
        hour = 10000

        milliGreater = TimeValidatorTest.__createTime(
            TimeValidatorTest._GMT,
            testTime,
            500
        )  # > milli sec
        value = TimeValidatorTest.__createTime(
            TimeValidatorTest._GMT,
            testTime,
            400
        )  # test value
        milliLess = TimeValidatorTest.__createTime(
            TimeValidatorTest._GMT,
            testTime,
            300
        )  # < milli sec

        secGreater = TimeValidatorTest.__createTime(
            TimeValidatorTest._GMT,
            testTime + 1,
            100
        )  # +1 sec
        secLess = TimeValidatorTest.__createTime(
            TimeValidatorTest._GMT,
            testTime - 1,
            100
        )  # -1 sec

        minGreater = TimeValidatorTest.__createTime(
            TimeValidatorTest._GMT,
            testTime + min,
            100
        )  # +1 min
        minLess = TimeValidatorTest.__createTime(
            TimeValidatorTest._GMT,
            testTime - min,
            100
        )  # -1 min

        hourGreater = TimeValidatorTest.__createTime(
            TimeValidatorTest._GMT,
            testTime + hour,
            100
        )  # +1 hour
        hourLess = TimeValidatorTest.__createTime(
            TimeValidatorTest._GMT,
            testTime - hour,
            100
        )  # -1 hour

        self.assertEqual(
            self._validator.compareTime(value, milliGreater),
            -1,
            "mili LT"
        )
        self.assertEqual(
            self._validator.compareTime(value, value),
            0,
            "mili EQ"
        )
        self.assertEqual(
            self._validator.compareTime(value, milliLess),
            1,
            "mili GT"
        )

        self.assertEqual(
            self._validator.compareSeconds(value, secGreater),
            -1,
            "secs LT"
        )
        self.assertEqual(
            self._validator.compareSeconds(value, milliGreater),
            0,
            "secs =1"
        )
        self.assertEqual(
            self._validator.compareSeconds(value, value),
            0,
            "secs =2"
        )
        self.assertEqual(
            self._validator.compareSeconds(value, milliLess),
            0,
            "secs =3"
        )
        self.assertEqual(
            self._validator.compareSeconds(value, secLess),
            1,
            "secs GT"
        )

        self.assertEqual(
            self._validator.compareMinutes(value, minGreater),
            -1,
            "mins LT"
        )
        self.assertEqual(
            self._validator.compareMinutes(value, secGreater),
            0,
            "mins =1"
        )
        self.assertEqual(
            self._validator.compareMinutes(value, value),
            0,
            "mins =2"
        )
        self.assertEqual(
            self._validator.compareMinutes(value, secLess),
            0,
            "mins =3"
        )
        self.assertEqual(
            self._validator.compareMinutes(value, minLess),
            1,
            "mins GT"
        )

        self.assertEqual(
            self._validator.compareHours(value, hourGreater),
            -1,
            "hour LT"
        )
        self.assertEqual(
            self._validator.compareHours(value, minGreater),
            0,
            "hour =1"
        )
        self.assertEqual(
            self._validator.compareHours(value, value),
            0,
            "hour =2"
        )
        self.assertEqual(
            self._validator.compareHours(value, minLess),
            0,
            "hour =3"
        )
        self.assertEqual(
            self._validator.compareHours(value, hourLess),
            1,
            "hour GT"
        )

    
    @staticmethod
    def __createTime(zone, time, millisecond):
        if zone is None:
            calendar = datetime.utcnow()
        else:
            calendar = datetime.now(zone)
        hour = (time // 10000) * 10000
        min = (time // 100) * 100 - hour
        sec = time - (hour + min)
        calendar = calendar.replace(
            year=1970, month=1, day=1,
            hour=hour // 10000,
            minute=min // 100,
            second=sec,
            microsecond=millisecond * 1000
        )
        return calendar

    
    @staticmethod
    def __createDate(zone, time, millisecond):
        calendar = TimeValidatorTest.__createTime(zone, time, millisecond)
        return calendar
