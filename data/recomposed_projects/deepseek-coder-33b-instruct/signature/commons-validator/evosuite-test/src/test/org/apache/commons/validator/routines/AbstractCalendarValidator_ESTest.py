from __future__ import annotations
import time
import locale
import re
import mock
import sys
import os
import datetime
import unittest
import pytest
import io
import unittest

# from src.test.org.apache.commons.validator.routines.AbstractCalendarValidator_ESTest_scaffolding import *
from src.main.org.apache.commons.validator.routines.CalendarValidator import *
from src.main.org.apache.commons.validator.routines.DateValidator import *
from src.main.org.apache.commons.validator.routines.TimeValidator import *

# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class AbstractCalendarValidator_ESTest(unittest.TestCase):

    def test61(self) -> None:

        calendarValidator0 = CalendarValidator.getInstance()
        timeValidator0 = TimeValidator.getInstance()

        with pytest.raises(ValueError):
            timeValidator0.format1(calendarValidator0, None, None)
            pytest.fail("Expecting exception: ValueError")

    def test60(self) -> None:

        calendar_validator0 = CalendarValidator.getInstance()
        locale0 = Locale.US
        time_zone0 = TimeZone.getDefault()

        with pytest.raises(ValueError):
            calendar_validator0.format2(locale0, locale0, time_zone0)
            verifyException("java.text.DateFormat", ValueError)

    def test58(self) -> None:

        calendar_validator0 = CalendarValidator.CalendarValidator1()
        object0 = object()
        time_zone0 = datetime.datetime.now(datetime.timezone.utc).astimezone().tzinfo

        with pytest.raises(ValueError):
            calendar_validator0.format0(object0, time_zone0)
            self.fail("Expecting exception: ValueError")

    def test57(self) -> None:

        calendar_validator0 = CalendarValidator.getInstance()
        locale0 = Locale.CHINESE
        boolean0 = calendar_validator0.isValid3("2", "2", locale0)
        self.assertTrue(boolean0)

    def test56(self) -> None:

        locale0 = Locale.CHINESE
        calendarValidator0 = CalendarValidator.getInstance()
        boolean0 = calendarValidator0.isValid3("", "", locale0)
        self.assertFalse(boolean0)

    def test55(self) -> None:

        calendar_validator0 = CalendarValidator.getInstance()
        locale0 = Locale.ENGLISH
        string0 = calendar_validator0.format2(None, locale0, None)
        self.assertIsNone(string0)

    def test54(self) -> None:

        date_validator0 = DateValidator(False, -498)
        locale0 = Locale.ENGLISH
        date0 = date_validator0.validate6(None, None, locale0)
        self.assertIsNone(date0)

    def test53(self) -> None:

        calendar_validator0 = CalendarValidator.getInstance()
        # Undeclared exception in Java code
        try:
            calendar_validator0.isValid3("##FbpU9j", "##FbpU9j", None)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # Illegal pattern character 'b'
            self.verifyException("java.text.SimpleDateFormat", e)

    def test52(self) -> None:
        dateValidator0 = DateValidator(False, -498)
        boolean0 = dateValidator0.isValid0('c"u@s|RFy#w0Hc tgK')
        self.assertFalse(boolean0)

    def test51(self) -> None:

        mockGregorianCalendar0 = MockGregorianCalendar()
        timeValidator0 = TimeValidator.getInstance()
        mockGregorianCalendar1 = MockGregorianCalendar(-376, -376, -376, -376, -376)
        int0 = timeValidator0.compare(
            mockGregorianCalendar1, mockGregorianCalendar0, -376
        )
        self.assertEqual(-1, int0)

    def test50(self) -> None:

        mockGregorianCalendar0 = MockGregorianCalendar()
        timeValidator0 = TimeValidator.TimeValidator1()
        int0 = timeValidator0.compare(mockGregorianCalendar0, mockGregorianCalendar0, 1)
        self.assertEqual(0, int0)

    def test49(self) -> None:

        calendar_validator0 = CalendarValidator.CalendarValidator1()
        mock_gregorian_calendar0 = MockGregorianCalendar()
        int0 = calendar_validator0.compareMonths(
            mock_gregorian_calendar0, mock_gregorian_calendar0
        )
        self.assertEqual(0, int0)

    def test48(self) -> None:

        mockGregorianCalendar0 = MockGregorianCalendar()
        timeValidator0 = TimeValidator.getInstance()
        int0 = timeValidator0.compare(mockGregorianCalendar0, mockGregorianCalendar0, 7)
        self.assertEqual(0, int0)

    def test47(self) -> None:

        mockGregorianCalendar0 = MockGregorianCalendar()
        timeValidator0 = TimeValidator.TimeValidator1()
        int0 = timeValidator0.compare(mockGregorianCalendar0, mockGregorianCalendar0, 8)
        self.assertEqual(0, int0)

    def test46(self) -> None:

        mockGregorianCalendar0 = MockGregorianCalendar()
        timeValidator0 = TimeValidator.getInstance()
        mockGregorianCalendar1 = MockGregorianCalendar(-1616, -1616, -1616)
        int0 = timeValidator0.compareTime(
            mockGregorianCalendar0, mockGregorianCalendar1
        )
        self.assertEqual(1, int0)

    def test45(self) -> None:

        mockGregorianCalendar0 = MockGregorianCalendar()
        timeValidator0 = TimeValidator.getInstance()
        int0 = timeValidator0.compare(
            mockGregorianCalendar0, mockGregorianCalendar0, 11
        )
        self.assertEqual(0, int0)

    def test44(self) -> None:

        mockGregorianCalendar0 = MockGregorianCalendar()
        timeValidator0 = TimeValidator.TimeValidator1()
        int0 = timeValidator0.compare(
            mockGregorianCalendar0, mockGregorianCalendar0, 12
        )
        self.assertEqual(0, int0)

    def test43(self) -> None:

        mockGregorianCalendar0 = MockGregorianCalendar()
        timeValidator0 = TimeValidator.getInstance()
        simpleTimeZone0 = SimpleTimeZone(
            1044, "org.apache.commons.validator.routines.AbstractCalendarValidator"
        )
        mockGregorianCalendar1 = MockGregorianCalendar(simpleTimeZone0)
        int0 = timeValidator0.compareSeconds(
            mockGregorianCalendar0, mockGregorianCalendar1
        )
        self.assertEqual((-1), int0)

    def test42(self) -> None:

        mockGregorianCalendar0 = MockGregorianCalendar()
        timeValidator0 = TimeValidator.TimeValidator1()
        int0 = timeValidator0.compare(
            mockGregorianCalendar0, mockGregorianCalendar0, 13
        )
        self.assertEqual(0, int0)

    def test41(self) -> None:

        mockGregorianCalendar0 = MockGregorianCalendar()
        timeValidator0 = TimeValidator.TimeValidator1()
        int0 = timeValidator0.compareQuarters(
            mockGregorianCalendar0, mockGregorianCalendar0, 4
        )
        self.assertEqual(0, int0)

    def test40(self) -> None:

        calendar_validator0 = CalendarValidator.CalendarValidator1()
        calendar0 = MockCalendar.getInstance()
        mock_gregorian_calendar0 = MockGregorianCalendar(4, 20, -64)
        int0 = calendar_validator0.compareQuarters(
            calendar0, mock_gregorian_calendar0, -832
        )
        self.assertEqual(1, int0)

    def test39(self) -> None:

        locale0 = Locale.CHINESE
        calendarValidator0 = CalendarValidator.getInstance()

        with self.assertRaises(ValueError):
            calendarValidator0.format4(locale0, "", locale0, None)

        verifyException("java.text.DateFormat", ValueError)

    def test37(self) -> None:

        mockGregorianCalendar0 = MockGregorianCalendar()
        mockGregorianCalendar0.set(1013, 1013, 0, 0, 0, 153)
        timeValidator0 = TimeValidator.getInstance()
        mockGregorianCalendar0.setLenient(False)

        try:
            timeValidator0.compare(mockGregorianCalendar0, mockGregorianCalendar0, 11)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            self.verifyException("java.util.GregorianCalendar", e)

    def test36(self) -> None:

        time_validator0 = TimeValidator.getInstance()

        try:
            time_validator0.compare(None, None, -14)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.verifyException(
                "org.apache.commons.validator.routines.AbstractCalendarValidator", e
            )

    def test35(self) -> None:

        calendar_validator0 = CalendarValidator.CalendarValidator1()
        # Undeclared exception
        try:
            calendar_validator0.compareQuarters(None, None, -2445)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            # no message in exception (getMessage() returned null)
            self.verifyException(
                "org.apache.commons.validator.routines.AbstractCalendarValidator", e
            )

    def test34(self) -> None:

        time_validator0 = TimeValidator.getInstance()

        try:
            time_validator0.compareTime(None, None, 981)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.verifyException(
                "org.apache.commons.validator.routines.AbstractCalendarValidator", e
            )

    def test33(self) -> None:

        calendar_validator0 = CalendarValidator.CalendarValidator1()
        locale0 = Locale.US

        with pytest.raises(ValueError):
            calendar_validator0.format3(locale0, "", locale0)
            self.fail("Expecting exception: ValueError")

        verifyException("java.text.DateFormat", ValueError)

    def test32(self) -> None:

        calendar_validator0 = CalendarValidator.getInstance()
        object0 = object()
        message_format0 = MessageFormat("")

        try:
            calendar_validator0.format5(object0, message_format0)
            self.fail("Expecting exception: TypeError")
        except TypeError as e:
            self.verifyException("java.text.MessageFormat", e)

    def test31(self) -> None:

        calendar_validator0 = CalendarValidator.getInstance()
        locale0 = "US"
        format0 = calendar_validator0._getFormat1(locale0)

        try:
            calendar_validator0._format5(format0, format0)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            self.verifyException("java.text.DateFormat", e)

    def test30(self) -> None:

        calendar_validator0 = CalendarValidator.CalendarValidator1()
        locale0 = Locale.TAIWAN
        # Undeclared exception in Java code
        try:
            calendar_validator0.format5(locale0, None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            # no message in exception (getMessage() returned null)
            self.verifyException(
                "org.apache.commons.validator.routines.AbstractCalendarValidator", e
            )

    def test29(self) -> None:

        time_validator = TimeValidator.getInstance()
        locale = Locale.CANADA_FRENCH

        with self.assertRaises(ValueError):
            time_validator.getFormat("f%,1iAt", locale)

        verifyException("java.text.SimpleDateFormat", ValueError)

    def test28(self) -> None:

        calendar_validator0 = CalendarValidator.getInstance()
        locale0 = "TAIWAN"
        try:
            calendar_validator0.getFormat0(
                "org.apache.commons.validator.routines.AbstractCalendarValidator",
                locale0,
            )
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            self.verifyException("java.text.SimpleDateFormat", e)

    def test27(self) -> None:

        locale0 = "zh"
        calendarValidator0 = CalendarValidator(True, 948)

        try:
            calendarValidator0._getFormat1(locale0)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            self.verifyException("java.text.DateFormat", e)

    def test26(self) -> None:

        calendar_validator0 = CalendarValidator.getInstance()
        locale0 = Locale.US
        # Undeclared exception in Java code
        try:
            calendar_validator0.parse("1Z_Q", "1Z_Q", locale0, None)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            #
            # Illegal pattern character 'Q'
            #
            self.verifyException("java.text.SimpleDateFormat", e)

    def test25(self) -> None:

        mockGregorianCalendar0 = MockGregorianCalendar()
        timeValidator0 = TimeValidator.getInstance()
        mockGregorianCalendar1 = MockGregorianCalendar(11, 11, 11)
        int0 = timeValidator0.compare(
            mockGregorianCalendar0, mockGregorianCalendar1, 1779
        )
        self.assertEqual(1, int0)

    def test24(self) -> None:

        date_validator0 = DateValidator.getInstance()
        mock_gregorian_calendar0 = MockGregorianCalendar(2, 1, 5135, 3449, 3449)
        zone_id0 = ZoneId.systemDefault()
        time_zone0 = TimeZone.getTimeZone(zone_id0)
        mock_gregorian_calendar1 = MockGregorianCalendar(time_zone0)
        int0 = date_validator0.compareQuarters(
            mock_gregorian_calendar0, mock_gregorian_calendar1, 2
        )
        self.assertEqual((-1), int0)

    def test23(self) -> None:

        mockGregorianCalendar0 = MockGregorianCalendar()
        timeValidator0 = TimeValidator.getInstance()
        int0 = timeValidator0.compareTime(
            mockGregorianCalendar0, mockGregorianCalendar0, 10
        )
        self.assertEqual(0, int0)

    def test22(self) -> None:

        mockGregorianCalendar0 = MockGregorianCalendar(981, 3, 3, 3, 1256, 1256)
        timeZone0 = datetime.timezone.utc
        dateValidator0 = DateValidator(True, 3)
        string0 = dateValidator0.format0(mockGregorianCalendar0, timeZone0)
        self.assertEqual("1/1/70", string0)

    def test21(self) -> None:
        time_validator0 = TimeValidator.getInstance()
        mock_simple_date_format0 = MockSimpleDateFormat()
        time_zone0 = mock_simple_date_format0.getTimeZone()
        string0 = time_validator0.format0(None, time_zone0)
        self.assertIsNone(string0)

    def test20(self) -> None:

        calendar_validator0 = CalendarValidator.getInstance()
        mock_simple_date_format0 = MockSimpleDateFormat()
        calendar0 = mock_simple_date_format0.getCalendar()
        simple_time_zone0 = SimpleTimeZone(3847, "")
        string0 = calendar_validator0.format1(calendar0, "", simple_time_zone0)
        self.assertEqual("2/14/14", string0)

    def test19(self) -> None:
        time_validator0 = TimeValidator.TimeValidator1()
        string0 = time_validator0.format1(None, None, None)
        self.assertIsNone(string0)

    def test17(self) -> None:

        calendar_validator0 = CalendarValidator(False, -2569)
        locale0 = Locale.ITALY
        date_format0 = DateFormat.getDateTimeInstance()
        object0 = calendar_validator0.processParsedValue(locale0, date_format0)
        string0 = calendar_validator0.format3(object0, "", locale0)

        # Unstable assertion: self.assertEqual("java.util.GregorianCalendar[time=-805541510593,areFieldsSet=true,areAllFieldsSet=true,lenient=true,zone=sun.util.calendar.ZoneInfo[id=\"GMT\",offset=0,dstSavings=0,useDaylight=false,transitions=0,lastRule=null],firstDayOfWeek=1,minimalDaysInFirstWeek=1,ERA=1,YEAR=1944,MONTH=5,WEEK_OF_YEAR=26,WEEK_OF_MONTH=4,DAY_OF_MONTH=22,DAY_OF_YEAR=174,DAY_OF_WEEK=5,DAY_OF_WEEK_IN_MONTH=4,AM_PM=1,HOUR=2,HOUR_OF_DAY=14,MINUTE=28,SECOND=9,MILLISECOND=407,ZONE_OFFSET=0,DST_OFFSET=0]", object0.toString())
        # Unstable assertion: self.assertEqual("22/06/44", string0)

    def test16(self) -> None:
        date_validator0 = DateValidator.DateValidator1()
        locale0 = Locale.PRC
        string0 = date_validator0.format3(None, "", locale0)
        self.assertIsNone(string0)

    def test15(self) -> None:

        mockSimpleDateFormat0 = MockSimpleDateFormat()
        dateValidator0 = DateValidator.getInstance()
        locale0 = Locale.UK
        timeZone0 = mockSimpleDateFormat0.getTimeZone()
        string0 = dateValidator0.format4(None, "", locale0, timeZone0)
        self.assertIsNone(string0)

    def test14(self) -> None:

        date_validator0 = DateValidator.getInstance()
        mock_gregorian_calendar0 = MockGregorianCalendar(2, 1, 5135, 3449, 3449)
        date_format0 = DateFormat.getTimeInstance()
        string0 = date_validator0.format5(mock_gregorian_calendar0, date_format0)
        self.assertEqual("12:00:00 AM", string0)

    def test13(self) -> None:

        calendar_validator0 = CalendarValidator(False, 1)
        date_format_symbols0 = DateFormatSymbols()
        mock_simple_date_format0 = MockSimpleDateFormat("", date_format_symbols0)
        string0 = calendar_validator0.format5(None, mock_simple_date_format0)
        self.assertIsNone(string0)

    def test11(self) -> None:

        timeZone0 = datetime.datetime.now(datetime.timezone.utc).astimezone().tzinfo
        timeValidator0 = TimeValidator.getInstance()
        locale0 = Locale.KOREAN
        mockGregorianCalendar0 = timeValidator0.parse(
            "오후 12:00", "", locale0, timeZone0
        )
        assert mockGregorianCalendar0 is not None
        assert not mockGregorianCalendar0.isLenient()

    def test10(self) -> None:

        dateValidator0 = DateValidator(False, 0)
        locale0 = Locale.JAPANESE
        simpleTimeZone0 = SimpleTimeZone(0, "")
        object0 = dateValidator0._parse("", "", locale0, simpleTimeZone0)
        self.assertIsNone(object0)

    def test08(self) -> None:

        dateValidator0 = DateValidator.getInstance()
        mockGregorianCalendar0 = MockGregorianCalendar(2, 1, 5135, 3449, 3449)
        date0 = mockGregorianCalendar0.getGregorianChange()
        timeZone0 = datetime.datetime.now(datetime.timezone.utc).astimezone().tzinfo
        int0 = dateValidator0.compareWeeks(date0, date0, timeZone0)
        self.assertEqual(0, int0)

    def test07(self) -> None:

        mockGregorianCalendar0 = MockGregorianCalendar()
        timeValidator0 = TimeValidator.TimeValidator1()
        calendar0 = MockCalendar.getInstance()
        int0 = timeValidator0.compare(calendar0, mockGregorianCalendar0, 6)
        self.assertEqual(0, int0)

    def test06(self) -> None:

        dateValidator0 = DateValidator.getInstance()
        mockGregorianCalendar0 = MockGregorianCalendar(2, 1, 5135, 3449, 3449)
        date0 = mockGregorianCalendar0.getGregorianChange()
        timeZone0 = datetime.datetime.now(datetime.timezone.utc).astimezone().tzinfo
        int0 = dateValidator0.compareDates(date0, date0, timeZone0)
        self.assertEqual(0, int0)

    def test05(self) -> None:

        mockGregorianCalendar0 = MockGregorianCalendar()
        timeValidator0 = TimeValidator.getInstance()
        simpleTimeZone0 = SimpleTimeZone(4, "UKGLEv")
        calendar0 = MockCalendar.getInstance(simpleTimeZone0)
        int0 = timeValidator0.compare(mockGregorianCalendar0, calendar0, 4)
        self.assertEqual(0, int0)

    def test04(self) -> None:

        time_validator0 = TimeValidator.TimeValidator1()
        mock_simple_date_format0 = MockSimpleDateFormat()
        time_zone0 = mock_simple_date_format0.getTimeZone()
        locale0 = Locale.PRC
        mock_gregorian_calendar0 = MockGregorianCalendar(time_zone0, locale0)
        calendar0 = MockCalendar.getInstance()

        with pytest.raises(ValueError):
            time_validator0.compare(calendar0, mock_gregorian_calendar0, (-3250))
            pytest.fail("Expecting exception: ValueError")

        verifyException(
            "org.apache.commons.validator.routines.AbstractCalendarValidator",
            ValueError,
        )

    def test03(self) -> None:

        mockGregorianCalendar0 = MockGregorianCalendar(981, 3, 3, 3, 1256, 1256)
        timeValidator0 = TimeValidator.TimeValidator1()
        mockSimpleDateFormat0 = MockSimpleDateFormat("")
        timeZone0 = mockSimpleDateFormat0.getTimeZone()
        locale0 = Locale.ROOT
        mockGregorianCalendar1 = MockGregorianCalendar(timeZone0, locale0)
        int0 = timeValidator0.compareTime(
            mockGregorianCalendar0, mockGregorianCalendar1
        )
        self.assertEqual((-1), int0)

    def test02(self) -> None:

        mockSimpleDateFormat0 = MockSimpleDateFormat()
        calendar0 = mockSimpleDateFormat0.getCalendar()
        timeValidator0 = TimeValidator.getInstance()
        simpleTimeZone0 = SimpleTimeZone(-1437, "F>@")
        mockGregorianCalendar0 = MockGregorianCalendar(simpleTimeZone0)
        int0 = timeValidator0.compareTime(calendar0, mockGregorianCalendar0)
        self.assertEqual(1, int0)

    def test01(self) -> None:

        calendar_validator0 = CalendarValidator.getInstance()
        locale0 = Locale.SIMPLIFIED_CHINESE
        calendar0 = MockCalendar.getInstance(locale0)

        with pytest.raises(ValueError):
            calendar_validator0.compareTime(calendar0, calendar0, 51)

    def test00(self) -> None:

        time_validator0 = TimeValidator.TimeValidator1()
        mock_gregorian_calendar0 = MockGregorianCalendar(0, 0, 0)
        zoned_date_time0 = mock_gregorian_calendar0.toZonedDateTime()
        gregorian_calendar0 = MockGregorianCalendar.from_(zoned_date_time0)
        time_validator0.compareTime(gregorian_calendar0, mock_gregorian_calendar0)
