from __future__ import annotations
import time
import locale
import re
import mock
import os
import datetime
import typing
from typing import *
import numbers
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.validator.routines.CalendarValidator import *

# from src.test.org.apache.commons.validator.routines.CalendarValidator_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class CalendarValidator_ESTest(unittest.TestCase):

    def test50(self) -> None:

        calendar_validator0 = CalendarValidator.getInstance()
        locale0 = Locale.FRENCH
        time_zone0 = TimeZone.getTimeZone("")

        try:
            calendar_validator0.validate7(
                '5W].KF(ZY&=>5fv"",', '5W].KF(ZY&=>5fv"",', locale0, time_zone0
            )
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            verifyException("java.text.SimpleDateFormat", e)

    def test49(self) -> None:

        calendar_validator0 = CalendarValidator(True, 2540)
        time_zone0 = datetime.datetime.now(datetime.timezone.utc).astimezone().tzinfo

        try:
            calendar_validator0.validate1("r", time_zone0)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # Illegal date style 2540
            self.verifyException("java.text.DateFormat", e)

    def test48(self) -> None:

        calendarValidator0 = CalendarValidator.getInstance()
        calendar0 = calendarValidator0.validate3("?", "?", None)
        self.assertFalse(calendar0.isLenient())

    def test47(self) -> None:

        calendar_validator0 = CalendarValidator.getInstance()
        calendar0 = calendar_validator0.validate6("],", "],", None)
        self.assertFalse(calendar0.isLenient())

    def test46(self) -> None:

        calendar_validator0 = CalendarValidator.CalendarValidator1()
        mock_gregorian_calendar0 = MockGregorianCalendar(1292, 10, 1147)
        calendar_validator0.compareQuarters1(
            mock_gregorian_calendar0, mock_gregorian_calendar0, 1
        )
        self.assertTrue(calendar_validator0.isStrict())

    def test45(self) -> None:

        calendar_validator0 = CalendarValidator.CalendarValidator1()
        # Undeclared exception in Java code
        try:
            calendar_validator0.compareMonths(None, None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            # no message in exception (getMessage() returned null)
            self.verifyException(
                "org.apache.commons.validator.routines.AbstractCalendarValidator", e
            )

    def test44(self) -> None:

        calendar_validator0 = CalendarValidator.CalendarValidator1()
        calendar_validator0.validate0("uLBUHe[ wN")
        self.assertTrue(calendar_validator0.isStrict())

    def test43(self) -> None:

        calendar_validator0 = CalendarValidator(False, 13)
        locale0 = Locale.CHINA
        # Undeclared exception in Java code
        try:
            calendar_validator0.validate4("6'+3X-48#?$L", locale0)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            #
            # Illegal date style 13
            #
            self.verifyException("java.text.DateFormat", e)

    def test42(self) -> None:

        calendar_validator0 = CalendarValidator.CalendarValidator1()
        locale0 = Locale.GERMAN
        mock_gregorian_calendar0 = MockGregorianCalendar(locale0)
        calendar_validator0.compareQuarters0(
            mock_gregorian_calendar0, mock_gregorian_calendar0
        )
        self.assertTrue(calendar_validator0.isStrict())

    def test41(self) -> None:

        calendar_validator0 = CalendarValidator.getInstance()
        calendar0 = calendar_validator0.validate2(".96", ".96")
        self.assertFalse(calendar0.isLenient())

    def test40(self) -> None:

        calendar_validator0 = CalendarValidator.CalendarValidator1()
        simple_time_zone0 = SimpleTimeZone(-251, "")
        mock_gregorian_calendar0 = MockGregorianCalendar(simple_time_zone0)
        calendar_validator0.compareDates(
            mock_gregorian_calendar0, mock_gregorian_calendar0
        )
        self.assertTrue(calendar_validator0.isStrict())

    def test39(self) -> None:

        calendar_validator0 = CalendarValidator.getInstance()
        mock_gregorian_calendar0 = MockGregorianCalendar(-2998, -2998, -1163)
        int0 = calendar_validator0.compareYears(
            mock_gregorian_calendar0, mock_gregorian_calendar0
        )
        self.assertEqual(0, int0)

    def test38(self) -> None:

        calendarValidator0 = CalendarValidator(False, 2305)
        locale0 = Locale.ROOT
        timeZone0 = TimeZone.getTimeZone(
            "org.apache.commons.validator.routines.AbstractCalendarValidator"
        )

        try:
            calendarValidator0.validate5(
                "org.apache.commons.validator.routines.AbstractCalendarValidator",
                locale0,
                timeZone0,
            )
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            verifyException("java.text.DateFormat", e)

    def test37(self) -> None:

        calendar_validator0 = CalendarValidator.CalendarValidator1()
        mock_gregorian_calendar0 = MockGregorianCalendar(0, 1, -605)
        calendar_validator0.compareWeeks(
            mock_gregorian_calendar0, mock_gregorian_calendar0
        )
        self.assertTrue(calendar_validator0.isStrict())

    def test36(self) -> None:

        mockGregorianCalendar0 = MockGregorianCalendar()
        timeZone0 = timezone.gettz("2_X9wB")
        CalendarValidator.adjustToTimeZone(mockGregorianCalendar0, timeZone0)
        self.assertEqual(
            'org.evosuite.runtime.mock.java.util.MockGregorianCalendar[time=1392409281320,areFieldsSet=false,areAllFieldsSet=false,lenient=true,zone=sun.util.calendar.ZoneInfo[id="GMT",offset=0,dstSavings=0,useDaylight=false,transitions=0,lastRule=null],firstDayOfWeek=1,minimalDaysInFirstWeek=1,ERA=1,YEAR=2014,MONTH=1,WEEK_OF_YEAR=7,WEEK_OF_MONTH=3,DAY_OF_MONTH=14,DAY_OF_YEAR=45,DAY_OF_WEEK=6,DAY_OF_WEEK_IN_MONTH=2,AM_PM=1,HOUR=8,HOUR_OF_DAY=20,MINUTE=21,SECOND=21,MILLISECOND=320,ZONE_OFFSET=0,DST_OFFSET=0]',
            str(mockGregorianCalendar0),
        )

    def test35(self) -> None:

        mockSimpleDateFormat0 = MockSimpleDateFormat()
        timeZone0 = mockSimpleDateFormat0.getTimeZone()

        with pytest.raises(RuntimeError):
            CalendarValidator.adjustToTimeZone(None, timeZone0)

    def test34(self) -> None:

        calendar_validator0 = CalendarValidator.CalendarValidator1()
        # Undeclared exception in Java code
        try:
            calendar_validator0.compareDates(None, None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            # no message in exception (getMessage() returned null)
            # verifyException("org.apache.commons.validator.routines.AbstractCalendarValidator", e)
            # In Python, we don't have a direct equivalent to verifyException.
            # Instead, we can check the type of the exception and its message.
            self.assertIsInstance(e, TypeError)
            self.assertEqual(
                str(e),
                "compareDates() missing 2 required positional arguments: 'value' and 'compare'",
            )

    def test33(self) -> None:

        calendar_validator0 = CalendarValidator.CalendarValidator1()
        mock_gregorian_calendar0 = MockGregorianCalendar(629, 629, 0, 5, (-2039), 0)
        mock_gregorian_calendar0.set(0, 5)
        # Undeclared exception
        try:
            calendar_validator0.compareMonths(
                mock_gregorian_calendar0, mock_gregorian_calendar0
            )
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # Invalid era
            verifyException("java.util.GregorianCalendar", e)

    def test32(self) -> None:

        calendar_validator0 = CalendarValidator.CalendarValidator1()
        locale0 = Locale.GERMAN
        mock_gregorian_calendar0 = MockGregorianCalendar(locale0)
        CalendarValidator.adjustToTimeZone(mock_gregorian_calendar0, None)

        try:
            calendar_validator0.compareQuarters0(
                mock_gregorian_calendar0, mock_gregorian_calendar0
            )
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("java.util.GregorianCalendar", e)

    def test31(self) -> None:

        calendar_validator0 = CalendarValidator.CalendarValidator1()
        mock_gregorian_calendar0 = MockGregorianCalendar(1292, 10, 1147)
        mock_gregorian_calendar0.set(0, 1292)
        # Undeclared exception in Java code
        try:
            calendar_validator0.compareQuarters1(
                mock_gregorian_calendar0, mock_gregorian_calendar0, 1
            )
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # Invalid era
            self.verifyException("java.util.GregorianCalendar", e)

    def test30(self) -> None:

        calendar_validator0 = CalendarValidator.CalendarValidator1()
        # Undeclared exception in Java code
        try:
            calendar_validator0.compareQuarters1(None, None, -80)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            # no message in exception (getMessage() returned null)
            self.verifyException(
                "org.apache.commons.validator.routines.AbstractCalendarValidator", e
            )

    def test29(self) -> None:

        calendar_validator0 = CalendarValidator.getInstance()

        with self.assertRaises(RuntimeError):
            calendar_validator0.compareWeeks(None, None)

    def test28(self) -> None:

        calendar_validator0 = CalendarValidator.getInstance()

        with pytest.raises(RuntimeError):
            calendar_validator0.compareYears(None, None)

    def test27(self) -> None:

        calendar_validator0 = CalendarValidator.CalendarValidator1()
        number_format0 = NumberFormat.getNumberInstance()

        try:
            calendar_validator0.processParsedValue(None, number_format0)
            self.fail("Expecting exception: TypeError")

        except TypeError as e:
            verifyException(
                "org.apache.commons.validator.routines.CalendarValidator", e
            )

    def test26(self) -> None:

        calendar_validator0 = CalendarValidator.CalendarValidator1()

        with self.assertRaises(RuntimeError):
            calendar_validator0.processParsedValue(calendar_validator0, None)

    def test25(self) -> None:

        calendar_validator0 = CalendarValidator(True, 1074)
        try:
            calendar_validator0.validate0("2l<e<l} 6")
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            #
            # Illegal date style 1074
            #
            self.verifyException("java.text.DateFormat", e)

    def test24(self) -> None:

        calendar_validator0 = CalendarValidator.CalendarValidator1()
        # Undeclared exception in Java code
        try:
            calendar_validator0.validate2("po", "po")
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # Illegal pattern character 'p'
            self.verifyException("java.text.SimpleDateFormat", e)

    def test23(self) -> None:

        calendar_validator0 = CalendarValidator.CalendarValidator1()
        # Undeclared exception in Java code
        try:
            calendar_validator0.validate3("Invalid field: ", "Invalid field: ", None)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # Illegal pattern character 'I'
            self.verifyException("java.text.SimpleDateFormat", e)

    def test22(self) -> None:

        calendar_validator0 = CalendarValidator.getInstance()
        locale0 = Locale.US
        try:
            calendar_validator0.validate6("k", "DMId<wL~9(hzt7V!)", locale0)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            self.verifyException("java.text.SimpleDateFormat", e)

    def test21(self) -> None:

        calendar_validator0 = CalendarValidator.CalendarValidator1()
        simple_time_zone0 = SimpleTimeZone(-251, "")
        mock_gregorian_calendar0 = MockGregorianCalendar(simple_time_zone0)
        mock_gregorian_calendar1 = MockGregorianCalendar(-3558, 1, 1599, 1, 3)
        int0 = calendar_validator0.compareDates(
            mock_gregorian_calendar0, mock_gregorian_calendar1
        )
        self.assertEqual(-1, int0)
        self.assertTrue(calendar_validator0.isStrict())

    def test20(self) -> None:

        calendar_validator0 = CalendarValidator.CalendarValidator1()
        locale0 = Locale.KOREA
        mock_gregorian_calendar0 = MockGregorianCalendar(locale0)
        mock_gregorian_calendar1 = MockGregorianCalendar(1, 2, (-2369), 1, 2851, 747)
        int0 = calendar_validator0.compareDates(
            mock_gregorian_calendar0, mock_gregorian_calendar1
        )
        self.assertEqual(1, int0)
        self.assertTrue(calendar_validator0.isStrict())

    def test19(self) -> None:

        calendar_validator0 = CalendarValidator.CalendarValidator1()
        mock_gregorian_calendar0 = MockGregorianCalendar(
            629, 629, 0, 5, (-2039), (-2615)
        )
        locale0 = Locale.CANADA_FRENCH
        mock_gregorian_calendar1 = MockGregorianCalendar(locale0)
        int0 = calendar_validator0.compareMonths(
            mock_gregorian_calendar0, mock_gregorian_calendar1
        )
        assertTrue(calendar_validator0.isStrict())
        self.assertEqual((-1), int0)

    def test18(self) -> None:

        calendar_validator0 = CalendarValidator.CalendarValidator1()
        mock_gregorian_calendar0 = MockGregorianCalendar(1, -1548, 0, 3, 3, 3)
        locale0 = Locale.JAPAN
        mock_gregorian_calendar1 = MockGregorianCalendar(locale0)
        int0 = calendar_validator0.compareMonths(
            mock_gregorian_calendar1, mock_gregorian_calendar0
        )
        self.assertEqual(1, int0)
        self.assertTrue(calendar_validator0.isStrict())

    def test17(self) -> None:

        calendar_validator0 = CalendarValidator.CalendarValidator1()
        mock_gregorian_calendar0 = MockGregorianCalendar()
        calendar_validator0.compareMonths(
            mock_gregorian_calendar0, mock_gregorian_calendar0
        )
        self.assertTrue(calendar_validator0.isStrict())

    def test16(self) -> None:

        calendar_validator0 = CalendarValidator.CalendarValidator1()
        mock_gregorian_calendar0 = MockGregorianCalendar(-1491, -1491, 5, 5, 5)
        calendar0 = MockCalendar.getInstance()
        int0 = calendar_validator0.compareQuarters0(mock_gregorian_calendar0, calendar0)
        self.assertEqual(-1, int0)
        self.assertTrue(calendar_validator0.isStrict())

    def test15(self) -> None:

        calendar_validator0 = CalendarValidator.getInstance()
        mock_gregorian_calendar0 = MockGregorianCalendar(
            2932, 2932, 2932, 2932, (-1085), 4
        )
        locale0 = Locale.US
        calendar0 = MockCalendar.getInstance(locale0)
        int0 = calendar_validator0.compareQuarters0(mock_gregorian_calendar0, calendar0)
        self.assertEqual(1, int0)

    def test14(self) -> None:

        calendar_validator0 = CalendarValidator.CalendarValidator1()
        mock_gregorian_calendar0 = MockGregorianCalendar()
        mock_gregorian_calendar1 = MockGregorianCalendar(2437, 2465, -1)
        int0 = calendar_validator0.compareQuarters1(
            mock_gregorian_calendar0, mock_gregorian_calendar1, -1
        )
        self.assertTrue(calendar_validator0.isStrict())
        self.assertEqual(-1, int0)

    def test13(self) -> None:

        calendar_validator0 = CalendarValidator.getInstance()
        mock_gregorian_calendar0 = MockGregorianCalendar(2864, 1, 1, 856, 856)
        mock_gregorian_calendar1 = MockGregorianCalendar(1, -56, 0)
        int0 = calendar_validator0.compareQuarters1(
            mock_gregorian_calendar0, mock_gregorian_calendar1, 1
        )
        self.assertEqual(1, int0)

    def test12(self) -> None:

        calendar_validator0 = CalendarValidator.CalendarValidator1()
        mock_gregorian_calendar0 = MockGregorianCalendar(0, 1, -605)
        calendar0 = MockCalendar.getInstance()
        int0 = calendar_validator0.compareWeeks(mock_gregorian_calendar0, calendar0)
        self.assertEqual((-1), int0)
        self.assertTrue(calendar_validator0.isStrict())

    def test11(self) -> None:

        calendar_validator0 = CalendarValidator.getInstance()
        mock_gregorian_calendar0 = MockGregorianCalendar(-1115, -1115, 0)
        mock_gregorian_calendar1 = MockGregorianCalendar(1, 1, 1, 853, -1115, 1)
        int0 = calendar_validator0.compareWeeks(
            mock_gregorian_calendar0, mock_gregorian_calendar1
        )
        self.assertEqual(1, int0)

    def test10(self) -> None:

        calendar_validator0 = CalendarValidator.CalendarValidator1()
        calendar0 = MockCalendar.getInstance()
        mock_gregorian_calendar0 = MockGregorianCalendar(0, 0, 0, 0, 4661, 0)
        int0 = calendar_validator0.compareYears(mock_gregorian_calendar0, calendar0)
        self.assertTrue(calendar_validator0.isStrict())
        self.assertEqual((-1), int0)

    def test09(self) -> None:

        calendar_validator0 = CalendarValidator.getInstance()
        mock_gregorian_calendar0 = MockGregorianCalendar(-2998, -2998, -1163)
        simple_time_zone0 = SimpleTimeZone(-96, "")
        mock_gregorian_calendar1 = MockGregorianCalendar(simple_time_zone0)
        int0 = calendar_validator0.compareYears(
            mock_gregorian_calendar0, mock_gregorian_calendar1
        )
        self.assertEqual(1, int0)

    def test07(self) -> None:

        calendar_validator0 = CalendarValidator.getInstance()
        calendar0 = calendar_validator0.validate1("", None)
        self.assertIsNone(calendar0)

    def test06(self) -> None:

        calendar_validator0 = CalendarValidator(True, 0)
        calendar0 = calendar_validator0.validate2("", "W>Y=2w#|*A@L{C2aq")
        self.assertIsNone(calendar0)

    def test05(self) -> None:

        calendarValidator0 = CalendarValidator.CalendarValidator1()
        timeZone0 = datetime.timezone.utc
        calendarValidator0.validate3(
            "org.apache.commons.validator.routines.AbstractCalendarValidator",
            "",
            timeZone0,
        )
        self.assertTrue(calendarValidator0.isStrict())

    def test04(self) -> None:

        calendar_validator0 = CalendarValidator.CalendarValidator1()
        locale0 = Locale.JAPAN
        calendar_validator0.validate4("Q`", locale0)
        self.assertTrue(calendar_validator0.isStrict())

    def test03(self) -> None:

        calendarValidator0 = CalendarValidator.getInstance()
        calendar0 = calendarValidator0.validate5('i<[*sO{ mQ"-3eN`', None, None)
        self.assertIsNone(calendar0)

    def test02(self) -> None:

        calendar_validator0 = CalendarValidator.CalendarValidator1()
        locale0 = Locale.SIMPLIFIED_CHINESE
        calendar_validator0.validate6("PS9c#WE( zPpK A", "", locale0)
        self.assertTrue(calendar_validator0.isStrict())

    def test01(self) -> None:

        calendarValidator0 = CalendarValidator.getInstance()
        locale0 = Locale.TRADITIONAL_CHINESE
        calendar0 = calendarValidator0.validate7("}", "}", locale0, None)
        self.assertEqual(
            str(calendar0),
            'org.evosuite.runtime.mock.java.util.MockGregorianCalendar[time=?,areFieldsSet=false,areAllFieldsSet=false,lenient=false,zone=sun.util.calendar.ZoneInfo[id="GMT",offset=0,dstSavings=0,useDaylight=false,transitions=0,lastRule=null],firstDayOfWeek=1,minimalDaysInFirstWeek=1,ERA=?,YEAR=?,MONTH=?,WEEK_OF_YEAR=?,WEEK_OF_MONTH=?,DAY_OF_MONTH=?,DAY_OF_YEAR=?,DAY_OF_WEEK=?,DAY_OF_WEEK_IN_MONTH=?,AM_PM=?,HOUR=?,HOUR_OF_DAY=?,MINUTE=?,SECOND=?,MILLISECOND=?,ZONE_OFFSET=?,DST_OFFSET=?]',
        )

    def test00(self) -> None:

        calendar_validator0 = CalendarValidator.CalendarValidator1()
        locale0 = Locale.GERMAN
        date_format_symbols0 = DateFormatSymbols.getInstance(locale0)
        mock_simple_date_format0 = MockSimpleDateFormat("", date_format_symbols0)
        time_zone0 = mock_simple_date_format0.getTimeZone()
        calendar_validator0.validate7("", "|P9xdTEk,+sJA/c6YA", locale0, time_zone0)
        self.assertTrue(calendar_validator0.isStrict())
