from __future__ import annotations
import time
import locale
import re
import mock
import sys
import os
import datetime
import numbers
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.validator.DateValidator import *

# from src.test.org.apache.commons.validator.DateValidator_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *
from src.main.org.apache.commons.validator.routines.DateValidator import *

# from src.test.org.apache.commons.validator.routines.DateValidator_ESTest_scaffolding import *


class DateValidator_ESTest(unittest.TestCase):

    def test45(self) -> None:

        dateValidator0 = DateValidator(False, 119)
        locale0 = Locale.FRANCE

        try:
            dateValidator0.validate4("[G4%ktnO)ldR", locale0)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            verifyException("java.text.DateFormat", e)

    def test44(self) -> None:

        dateValidator0 = DateValidator.getInstance()
        locale0 = Locale.CHINA
        date0 = dateValidator0.validate6("@1~", "@1~", locale0)
        self.assertEqual("Fri Feb 14 20:21:21 GMT 2014", date0.toString())

    def test43(self) -> None:

        dateValidator0 = DateValidator.DateValidator1()
        simpleTimeZone0 = SimpleTimeZone(2337, "^3")
        dateValidator0.validate3("^3", "^3", simpleTimeZone0)
        self.assertTrue(dateValidator0.isStrict())

    def test42(self) -> None:

        date_validator0 = DateValidator.getInstance()
        mock_date0 = MockDate()
        time_zone0 = TimeZone.getTimeZone("")
        int0 = date_validator0.compareQuarters0(mock_date0, mock_date0, time_zone0)
        self.assertEqual(0, int0)

    def test41(self) -> None:

        dateValidator0 = DateValidator(False, 5)
        # Undeclared exception in Java code
        try:
            dateValidator0.validate0("^Kr@Kls6[")
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            #
            # Illegal date style 5
            #
            self.verifyException("java.text.DateFormat", e)

    def test40(self) -> None:

        date_validator0 = DateValidator.DateValidator1()
        mock_simple_date_format0 = MockSimpleDateFormat()
        time_zone0 = mock_simple_date_format0.getTimeZone()
        locale0 = Locale.PRC
        date_validator0.validate5("+D", locale0, time_zone0)
        self.assertTrue(date_validator0.isStrict())

    def test39(self) -> None:

        date_validator0 = DateValidator.DateValidator1()
        locale0 = Locale.ITALIAN
        zone_offset0 = ZoneOffset.MAX
        time_zone0 = TimeZone.getTimeZone(ZoneId.of(str(zone_offset0)))
        date_validator0.validate7("7", "7", locale0, time_zone0)
        self.assertTrue(date_validator0.isStrict())

    def test38(self) -> None:

        dateValidator0 = DateValidator.DateValidator1()
        # Undeclared exception in Java code
        try:
            dateValidator0.compareYears(None, None, None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            # no message in exception (getMessage() returned null)
            self.verifyException("java.util.Calendar", e)

    def test37(self) -> None:

        dateValidator0 = DateValidator(True, 7)
        timeZone0 = datetime.datetime.now(datetime.timezone.utc).astimezone().tzinfo

        with self.assertRaises(ValueError):
            dateValidator0.validate1("MFi}S>V3s/pbPJ3", timeZone0)
            self.fail("Expecting exception: ValueError")

    def test36(self) -> None:

        dateValidator0 = DateValidator.DateValidator1()
        mockDate0 = MockDate(12, 12, 5, 12, 0, 384)
        mockSimpleDateFormat0 = MockSimpleDateFormat()
        timeZone0 = mockSimpleDateFormat0.getTimeZone()
        dateValidator0.compareDates(mockDate0, mockDate0, timeZone0)
        self.assertTrue(dateValidator0.isStrict())

    def test35(self) -> None:

        date_validator0 = DateValidator.getInstance()

        with pytest.raises(RuntimeError):
            date_validator0.compareMonths(None, None, None)

    def test34(self) -> None:

        date_validator0 = DateValidator.getInstance()

        # Undeclared exception in Java code, but we can use pytest.raises to handle it in Python
        with pytest.raises(ValueError):
            date_validator0.validate2("Invalid field: ", "Invalid field: ")
            # fail("Expecting exception: ValueError")

        # verifyException("java.text.SimpleDateFormat", e)
        # In Python, we don't have a direct equivalent to verifyException.
        # However, if the exception is thrown, it means the test passed.

    def test33(self) -> None:

        dateValidator0 = DateValidator.DateValidator1()
        mockDate0 = MockDate(2, -1906, -1906, -1906, 3, 0)
        simpleTimeZone0 = SimpleTimeZone(0, "_E")
        dateValidator0.compareWeeks(mockDate0, mockDate0, simpleTimeZone0)
        self.assertTrue(dateValidator0.isStrict())

    def test32(self) -> None:

        dateValidator0 = DateValidator.DateValidator1()
        timeZone0 = datetime.datetime.now(datetime.timezone.utc).astimezone().tzinfo

        with pytest.raises(RuntimeError):
            dateValidator0.compareQuarters1(None, None, timeZone0, -738)
            self.fail("Expecting exception: RuntimeError")

    def test31(self) -> None:

        date_validator0 = DateValidator.getInstance()
        time_zone0 = datetime.datetime.now(datetime.timezone.utc).astimezone().tzinfo

        with self.assertRaises(RuntimeError):
            date_validator0.compareDates(None, None, time_zone0)

    def test30(self) -> None:

        date_validator0 = DateValidator.getInstance()
        time_zone0 = datetime.datetime.now(datetime.timezone.utc).astimezone().tzinfo

        with self.assertRaises(RuntimeError):
            date_validator0.compareQuarters0(None, None, time_zone0)

    def test29(self) -> None:

        date_validator0 = DateValidator.getInstance()
        time_zone0 = datetime.datetime.now(datetime.timezone.utc).astimezone().tzinfo

        with pytest.raises(RuntimeError):
            date_validator0.compareWeeks(None, None, time_zone0)
            self.fail("Expecting exception: RuntimeError")

    def test28(self) -> None:

        date_validator0 = DateValidator.getInstance()
        # Undeclared exception in Java code
        try:
            date_validator0.validate3("m2xj2+L4@=JwpFP", "m2xj2+L4@=JwpFP", None)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # Illegal pattern character 'x'
            self.verifyException("java.text.SimpleDateFormat", e)

    def test27(self) -> None:

        dateValidator0 = DateValidator(False, 8)
        locale0 = Locale.CHINESE

        with self.assertRaises(ValueError):
            dateValidator0.validate5("pnIB'V&1\u0001S7.", locale0, None)
            self.fail("Expecting exception: ValueError")

        verifyException("java.text.DateFormat", ValueError)

    def test26(self) -> None:

        dateValidator0 = DateValidator.DateValidator1()
        mockDate0 = MockDate(12, 12, 5, 12, 0, 384)
        mockSimpleDateFormat0 = MockSimpleDateFormat()
        date0 = mockSimpleDateFormat0.get2DigitYearStart()
        timeZone0 = mockSimpleDateFormat0.getTimeZone()
        int0 = dateValidator0.compareDates(mockDate0, date0, timeZone0)
        self.assertEqual((-1), int0)
        self.assertTrue(dateValidator0.isStrict())

    def test25(self) -> None:

        dateValidator0 = DateValidator.DateValidator1()
        mockDate0 = MockDate(12, 3360, 5, 0, 0, 384)
        mockSimpleDateFormat0 = MockSimpleDateFormat()
        date0 = mockSimpleDateFormat0.get2DigitYearStart()
        timeZone0 = mockSimpleDateFormat0.getTimeZone()
        int0 = dateValidator0.compareDates(mockDate0, date0, timeZone0)
        self.assertEqual(1, int0)
        self.assertTrue(dateValidator0.isStrict())

    def test24(self) -> None:

        dateValidator0 = DateValidator.DateValidator1()
        mockGregorianCalendar0 = MockGregorianCalendar()
        date0 = mockGregorianCalendar0.getGregorianChange()
        mockDate0 = MockDate(1)
        simpleTimeZone0 = SimpleTimeZone(
            0, "org.apache.commons.validator.routines.DateValidator"
        )
        int0 = dateValidator0.compareMonths(date0, mockDate0, simpleTimeZone0)
        self.assertEqual((-1), int0)
        self.assertTrue(dateValidator0.isStrict())

    def test23(self) -> None:

        dateValidator0 = DateValidator.DateValidator1()
        mockDate0 = MockDate(309, (-2191), 309, 13, (-2191))
        mockSimpleDateFormat0 = MockSimpleDateFormat()
        date0 = mockSimpleDateFormat0.get2DigitYearStart()
        timeZone0 = mockSimpleDateFormat0.getTimeZone()
        int0 = dateValidator0.compareMonths(mockDate0, date0, timeZone0)
        self.assertTrue(dateValidator0.isStrict())
        self.assertEqual(1, int0)

    def test22(self) -> None:

        dateValidator0 = DateValidator.getInstance()
        mockDate0 = MockDate()
        timeZone0 = TimeZone.getDefault()
        int0 = dateValidator0.compareMonths(mockDate0, mockDate0, timeZone0)
        self.assertEqual(0, int0)

    def test21(self) -> None:

        date_validator0 = DateValidator.getInstance()
        mock_date0 = MockDate()
        mock_date1 = MockDate(2480, -1, 1, 3870, 5, 2)
        time_zone0 = TimeZone.getTimeZone("")
        int0 = date_validator0.compareQuarters0(mock_date0, mock_date1, time_zone0)
        self.assertEqual((-1), int0)

    def test20(self) -> None:

        date_validator0 = DateValidator.DateValidator1()
        zone_offset0 = datetime.timezone(datetime.timedelta(hours=0))
        time_zone0 = timezone(zone_offset0)
        instant0 = datetime.datetime.fromtimestamp(-1)
        date0 = datetime.datetime.fromisoformat(instant0.isoformat())
        mock_date0 = MockDate(0, -3655, 0, -3655, 3)
        int0 = date_validator0.compareQuarters0(date0, mock_date0, time_zone0)
        self.assertEqual(1, int0)
        self.assertTrue(date_validator0.isStrict())

    def test19(self) -> None:

        dateValidator0 = DateValidator.DateValidator1()
        mockGregorianCalendar0 = MockGregorianCalendar(0, 0, 869, 7, (-567))
        date0 = mockGregorianCalendar0.getGregorianChange()
        mockDate0 = MockDate()
        zoneId0 = ZoneId.systemDefault()
        timeZone0 = TimeZone.getTimeZone(zoneId0)
        int0 = dateValidator0.compareQuarters1(date0, mockDate0, timeZone0, 869)
        self.assertEqual((-1), int0)
        self.assertTrue(date0.isStrict())

    def test18(self) -> None:

        dateValidator0 = DateValidator.getInstance()
        mockDate0 = MockDate()
        mockDate1 = MockDate(0, 0, 0, 0, -1635)
        zoneOffset0 = ZoneOffset.UTC
        timeZone0 = TimeZone.getTimeZone(zoneOffset0)
        int0 = dateValidator0.compareQuarters1(mockDate0, mockDate1, timeZone0, -1635)
        self.assertEqual(1, int0)

    def test17(self) -> None:

        dateValidator0 = DateValidator.getInstance()
        locale0 = Locale.UK
        dateFormatSymbols0 = DateFormatSymbols.getInstance(locale0)
        mockSimpleDateFormat0 = MockSimpleDateFormat("", dateFormatSymbols0)
        parsePosition0 = ParsePosition(-2792)
        date0 = mockSimpleDateFormat0.parse("tU`s-FaSAw/@s7o8", parsePosition0)
        timeZone0 = TimeZone.getDefault()
        int0 = dateValidator0.compareQuarters1(date0, date0, timeZone0, 0)
        self.assertEqual(0, int0)

    def test16(self) -> None:

        dateValidator0 = DateValidator.DateValidator1()
        mockDate0 = MockDate(2, -1906, -1906, -1906, 3, 0)
        instant0 = MockInstant.now()
        date0 = datetime.date.fromisoformat(str(instant0))
        simpleTimeZone0 = SimpleTimeZone(0, "_E")
        int0 = dateValidator0.compareWeeks(mockDate0, date0, simpleTimeZone0)
        self.assertEqual((-1), int0)
        self.assertTrue(dateValidator0.isStrict())

    def test15(self) -> None:

        dateValidator0 = DateValidator.DateValidator1()
        zoneOffset0 = datetime.timezone(datetime.timedelta(hours=0))
        timeZone0 = timezone(zoneOffset0)
        mockGregorianCalendar0 = MockGregorianCalendar()
        date0 = mockGregorianCalendar0.getGregorianChange()
        mockDate0 = MockDate(0, 0, -2503, 0, -3665)
        int0 = dateValidator0.compareWeeks(mockDate0, date0, timeZone0)
        self.assertEqual(1, int0)
        self.assertTrue(dateValidator0.isStrict())

    def test14(self) -> None:

        dateValidator0 = DateValidator.DateValidator1()
        mockDate0 = MockDate()
        mockGregorianCalendar0 = MockGregorianCalendar()
        date0 = mockGregorianCalendar0.getGregorianChange()
        simpleTimeZone0 = SimpleTimeZone(
            0, "org.apache.commons.validator.routines.AstractCalendarValidator"
        )
        int0 = dateValidator0.compareYears(date0, mockDate0, simpleTimeZone0)
        self.assertTrue(dateValidator0.isStrict())
        self.assertEqual((-1), int0)

    def test13(self) -> None:

        dateValidator0 = DateValidator.DateValidator1()
        mockDate0 = MockDate()
        mockGregorianCalendar0 = MockGregorianCalendar(0, 0, (-32), 0, 0)
        date0 = mockGregorianCalendar0.getGregorianChange()
        simpleTimeZone0 = SimpleTimeZone(
            (-2153), "org.apache.commons.validator.routines.AstractCalendarValidator"
        )
        int0 = dateValidator0.compareYears(mockDate0, date0, simpleTimeZone0)
        self.assertEqual(1, int0)
        self.assertTrue(date0.isStrict())

    def test12(self) -> None:

        mockDate0 = MockDate()
        dateValidator0 = DateValidator.getInstance()
        int0 = dateValidator0.compareYears(mockDate0, mockDate0, None)
        self.assertEqual(0, int0)

    def test11(self) -> None:
        dateValidator0 = DateValidator.getInstance()
        numberFormat0 = NumberFormat.getNumberInstance()
        object0 = dateValidator0.processParsedValue(dateValidator0, numberFormat0)
        self.assertIs(dateValidator0, object0)

    def test10(self) -> None:

        date_validator0 = DateValidator(False, 1621)
        locale0 = Locale.SIMPLIFIED_CHINESE
        number_format0 = NumberFormat.getNumberInstance(locale0)
        object0 = date_validator0.processParsedValue(None, number_format0)
        self.assertIsNone(object0)

    def test09(self) -> None:

        dateValidator0 = DateValidator.getInstance()
        date0 = dateValidator0.validate0("VI0[1jIl")
        self.assertIsNone(date0)

    def test08(self) -> None:

        dateValidator0 = DateValidator.getInstance()
        timeZone0 = datetime.datetime.now(datetime.timezone.utc).astimezone().tzinfo
        date0 = dateValidator0.validate1("", timeZone0)
        self.assertIsNone(date0)

    def test07(self) -> None:
        dateValidator0 = DateValidator.DateValidator1()
        dateValidator0.validate2("$_2&&|@", "$_2&&|@")
        self.assertTrue(dateValidator0.isStrict())

    def test06(self) -> None:

        dateValidator0 = DateValidator.getInstance()
        date0 = dateValidator0.validate4(None, None)
        self.assertIsNone(date0)

    def test05(self) -> None:

        dateValidator0 = DateValidator.getInstance()
        locale0 = Locale.ITALY
        date0 = dateValidator0.validate6("", "", locale0)
        self.assertIsNone(date0)

    def test04(self) -> None:

        date_validator0 = DateValidator.DateValidator1()
        locale0 = Locale.JAPANESE
        simple_time_zone0 = SimpleTimeZone(12, "")
        date_validator0.validate7("", "", locale0, simple_time_zone0)
        self.assertTrue(date_validator0.isStrict())

    def test03(self) -> None:
        dateValidator0 = DateValidator.DateValidator1()
        dateValidator0.validate2("", ":E|Fr(<BTFD")
        self.assertTrue(dateValidator0.isStrict())

    def test02(self) -> None:

        dateValidator0 = DateValidator.DateValidator1()
        simpleTimeZone0 = SimpleTimeZone(12, "")
        dateValidator0.validate3("M+WGQ*|-[z", "", simpleTimeZone0)
        self.assertTrue(dateValidator0.isStrict())

    def test01(self) -> None:

        date_validator0 = DateValidator.DateValidator1()
        locale0 = Locale.JAPANESE
        # Undeclared exception in Java code
        try:
            date_validator0.validate6(
                "Invalid field: ",
                "org.apache.commons.validator.routines.DateValidator",
                locale0,
            )
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # Illegal pattern character 'o'
            self.verifyException("java.text.SimpleDateFormat", e)

    def test00(self) -> None:

        date_validator0 = DateValidator.getInstance()
        locale0 = Locale.CHINA
        time_zone0 = TimeZone.getDefault()

        with self.assertRaises(ValueError):
            date_validator0.validate7(
                "Invalid field: ", ")NITs-IO", locale0, time_zone0
            )
            self.fail("Expecting exception: ValueError")
