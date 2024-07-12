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
from src.main.org.apache.commons.validator.routines.TimeValidator import *

# from src.test.org.apache.commons.validator.routines.TimeValidator_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class TimeValidator_ESTest(unittest.TestCase):

    def test40(self) -> None:

        time_validator0 = TimeValidator(True, 12)
        # Undeclared exception in Java code
        try:
            time_validator0.validate0(
                "org.apache.commons.validator.routines.TimeValidator"
            )
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            #
            # Illegal time style 12
            #
            self.verifyException("java.text.DateFormat", e)

    def test39(self) -> None:

        time_validator0 = TimeValidator.getInstance()

        with pytest.raises(RuntimeError):
            time_validator0.compareHours(None, None)

    def test38(self) -> None:

        time_validator0 = TimeValidator(False, 13)
        locale0 = Locale.ROOT
        time_zone0 = TimeZone.getDefault()

        try:
            time_validator0.validate5("b5M0i3m.Qw=?", locale0, time_zone0)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # Illegal time style 13
            self.verifyException("java.text.DateFormat", e)

    def test37(self) -> None:

        time_validator0 = TimeValidator.getInstance()
        mock_gregorian_calendar0 = MockGregorianCalendar(-961, -961, -961, -961, 3)
        int0 = time_validator0.compareSeconds(
            mock_gregorian_calendar0, mock_gregorian_calendar0
        )
        self.assertEqual(0, int0)

    def test36(self) -> None:

        time_validator0 = TimeValidator.getInstance()
        locale0 = Locale.US
        # Undeclared exception in Java code
        try:
            time_validator0.validate6(
                "8KqEg)~CrZf2w0$A+#", "8KqEg)~CrZf2w0$A+#", locale0
            )
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # Illegal pattern character 'q'
            self.verifyException("java.text.SimpleDateFormat", e)

    def test35(self) -> None:

        time_validator0 = TimeValidator.getInstance()
        mock_gregorian_calendar0 = MockGregorianCalendar(-2722, -227, -485, 0, -485)
        int0 = time_validator0.compareTime(
            mock_gregorian_calendar0, mock_gregorian_calendar0
        )
        self.assertEqual(0, int0)

    def test34(self) -> None:

        time_validator0 = TimeValidator(True, 1353)
        # Undeclared exception in Java code
        try:
            time_validator0.validate4("~uMJ1S_ElQL.%IS", None)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            #
            # Illegal time style 1353
            #
            self.verifyException("java.text.DateFormat", e)

    def test33(self) -> None:

        time_validator0 = TimeValidator.getInstance()
        calendar0 = time_validator0.validate2("/", "/")
        self.assertEqual(1, calendar0.getMinimalDaysInFirstWeek())

    def test32(self) -> None:

        time_validator0 = TimeValidator.getInstance()
        locale0 = Locale.JAPANESE
        calendar0 = MockCalendar.getInstance(locale0)
        int0 = time_validator0.compareMinutes(calendar0, calendar0)
        self.assertEqual(0, int0)

    def test31(self) -> None:

        timeValidator0 = TimeValidator(False, 818)
        # Undeclared exception in Java code
        try:
            timeValidator0.validate1(
                "org.apache.commons.validator.routines.AbstractFormatValidator", None
            )
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            #
            # Illegal time style 818
            #
            self.verifyException("java.text.DateFormat", e)

    def test30(self) -> None:

        time_validator0 = TimeValidator.TimeValidator1()
        # Undeclared exception in Java code
        try:
            time_validator0.compareSeconds(None, None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            # no message in exception (getMessage() returned null)
            self.verifyException(
                "org.apache.commons.validator.routines.AbstractCalendarValidator", e
            )

    def test29(self) -> None:

        time_validator0 = TimeValidator.getInstance()
        # Undeclared exception in Java code
        try:
            time_validator0.validate3("}w84U'QoOKwh", "}w84U'QoOKwh", None)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # Illegal pattern character 'U'
            self.verifyException("java.text.SimpleDateFormat", e)

    def test28(self) -> None:

        time_validator0 = TimeValidator.getInstance()
        mock_gregorian_calendar0 = MockGregorianCalendar(-347, 0, 0, -347, 0)
        mock_gregorian_calendar0.set(0, -347)
        # Undeclared exception
        try:
            time_validator0.compareMinutes(
                mock_gregorian_calendar0, mock_gregorian_calendar0
            )
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # Invalid era
            self.verifyException("java.util.GregorianCalendar", e)

    def test27(self) -> None:

        time_validator0 = TimeValidator.getInstance()

        with pytest.raises(RuntimeError):
            time_validator0.compareMinutes(None, None)

    def test26(self) -> None:

        time_validator0 = TimeValidator.getInstance()
        mock_gregorian_calendar0 = MockGregorianCalendar(-961, -961, -961, -961, 3)
        mock_gregorian_calendar0.setLenient(False)

        with pytest.raises(ValueError):
            time_validator0.compareSeconds(
                mock_gregorian_calendar0, mock_gregorian_calendar0
            )

        # YEAR
        #
        self.verifyException("java.util.GregorianCalendar", ValueError)

    def test25(self) -> None:

        time_validator0 = TimeValidator.TimeValidator1()
        # Undeclared exception in Java code
        try:
            time_validator0.compareTime(None, None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            # no message in exception (getMessage() returned null)
            # verifyException("org.apache.commons.validator.routines.AbstractCalendarValidator", e)
            self.assertIsInstance(e, TypeError)

    def test24(self) -> None:

        time_validator0 = TimeValidator.getInstance()
        locale0 = Locale.SIMPLIFIED_CHINESE
        number_format0 = NumberFormat.getCurrencyInstance()

        with self.assertRaises(TypeError):
            time_validator0.processParsedValue(locale0, number_format0)

        self.verifyException(
            "org.apache.commons.validator.routines.TimeValidator", TypeError
        )

    def test23(self) -> None:

        time_validator0 = TimeValidator.getInstance()
        locale0 = Locale.ITALIAN

        with self.assertRaises(RuntimeError):
            time_validator0.processParsedValue(locale0, None)

    def test22(self) -> None:

        time_validator0 = TimeValidator.TimeValidator1()
        # Undeclared exception
        try:
            time_validator0.validate2(
                "org.apache.commons.validator.routines.AbstractCalendarValidator",
                "org.apache.commons.validator.routines.AbstractCalendarValidator",
            )
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # Illegal pattern character 'o'
            self.verifyException("java.text.SimpleDateFormat", e)

    def test21(self) -> None:

        time_validator0 = TimeValidator.getInstance()
        locale0 = Locale.CHINESE
        time_zone0 = TimeZone.getTimeZone("{GP;ve")

        try:
            time_validator0.validate7("{GP;ve", "{GP;ve", locale0, time_zone0)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            verifyException("java.text.SimpleDateFormat", e)

    def test20(self) -> None:

        time_validator0 = TimeValidator.getInstance()
        calendar0 = MockCalendar.getInstance()
        mock_gregorian_calendar0 = MockGregorianCalendar(0, -533, 2104, -1597, 14, 13)
        int0 = time_validator0.compareHours(mock_gregorian_calendar0, calendar0)
        self.assertEqual(-1, int0)

    def test19(self) -> None:

        time_validator0 = TimeValidator.TimeValidator1()
        mock_gregorian_calendar0 = MockGregorianCalendar(-358, 0, 2104, 0, -1597, 12)
        mock_gregorian_calendar1 = MockGregorianCalendar()
        int0 = time_validator0.compareHours(
            mock_gregorian_calendar0, mock_gregorian_calendar1
        )
        assert time_validator0.isStrict()
        self.assertEqual(1, int0)

    def test18(self) -> None:

        time_validator0 = TimeValidator.TimeValidator1()
        mock_gregorian_calendar0 = MockGregorianCalendar(2104, -1594, 3, 0, 1, 1)
        time_validator0.compareHours(mock_gregorian_calendar0, mock_gregorian_calendar0)
        self.assertTrue(time_validator0.isStrict())

    def test17(self) -> None:

        time_validator0 = TimeValidator.getInstance()
        mock_gregorian_calendar0 = MockGregorianCalendar(0, 0, 0, 0, 0)
        time_zone0 = TimeZone.getTimeZone("")
        locale0 = Locale.GERMANY
        calendar0 = MockCalendar.getInstance(time_zone0, locale0)
        int0 = time_validator0.compareMinutes(mock_gregorian_calendar0, calendar0)
        self.assertEqual((-1), int0)

    def test16(self) -> None:

        time_validator0 = TimeValidator.getInstance()
        locale0 = Locale.JAPANESE
        calendar0 = MockCalendar.getInstance(locale0)
        mock_gregorian_calendar0 = MockGregorianCalendar((-92), (-92), (-92))
        int0 = time_validator0.compareMinutes(calendar0, mock_gregorian_calendar0)
        self.assertEqual(1, int0)

    def test15(self) -> None:

        time_validator0 = TimeValidator.getInstance()
        mock_gregorian_calendar0 = MockGregorianCalendar(13, 13, 13, -2851, 360)
        calendar0 = MockCalendar.getInstance()
        int0 = time_validator0.compareSeconds(mock_gregorian_calendar0, calendar0)
        self.assertEqual(-1, int0)

    def test14(self) -> None:

        time_validator0 = TimeValidator.getInstance()
        mock_gregorian_calendar0 = MockGregorianCalendar(838, 0, 0, 838, 0, 0)
        mock_gregorian_calendar1 = MockGregorianCalendar(0, 2, 2, 2, 2)
        int0 = time_validator0.compareSeconds(
            mock_gregorian_calendar0, mock_gregorian_calendar1
        )
        self.assertEqual(1, int0)

    def test13(self) -> None:

        time_validator0 = TimeValidator.getInstance()
        mock_gregorian_calendar0 = MockGregorianCalendar(-2722, -227, -485, 0, -485)
        time_zone0 = TimeZone.getTimeZone("KSN2O]")
        calendar0 = MockCalendar.getInstance(time_zone0)
        int0 = time_validator0.compareTime(mock_gregorian_calendar0, calendar0)
        self.assertEqual(-1, int0)

    def test12(self) -> None:

        time_validator0 = TimeValidator.TimeValidator1()
        mock_simple_date_format0 = MockSimpleDateFormat()
        calendar0 = mock_simple_date_format0.get_calendar()
        mock_gregorian_calendar0 = MockGregorianCalendar(0, -5932, 0, 13, 13, 0)
        int0 = time_validator0.compare_time(calendar0, mock_gregorian_calendar0)
        self.assertEqual(1, int0)
        self.assertTrue(time_validator0.is_strict())

    def test11(self) -> None:

        time_validator0 = TimeValidator.getInstance()
        mock_simple_date_format0 = MockSimpleDateFormat()
        mock_gregorian_calendar0 = time_validator0.processParsedValue(
            None, mock_simple_date_format0
        )
        self.assertTrue(mock_gregorian_calendar0.isLenient())

    def test10(self) -> None:

        time_validator0 = TimeValidator.TimeValidator1()
        time_validator0.validate0(
            "org.apache.commons.validator.routines.AbstractCalendarValidator"
        )
        self.assertTrue(time_validator0.isStrict())

    def test09(self) -> None:

        time_validator0 = TimeValidator.TimeValidator1()
        time_zone0 = dt.timezone.utc
        time_validator0.validate1(
            "org.apache.commons.validator.routines.TimeValidator", time_zone0
        )
        self.assertTrue(time_validator0.isStrict())

    def test08(self) -> None:

        time_validator0 = TimeValidator.getInstance()
        calendar0 = time_validator0.validate2("", "My")
        self.assertIsNone(calendar0)

    def test07(self) -> None:

        time_validator0 = TimeValidator.TimeValidator1()
        time_validator0.validate3("~", "~", None)
        self.assertTrue(time_validator0.isStrict())

    def test06(self) -> None:

        time_validator0 = TimeValidator.TimeValidator1()
        time_zone0 = datetime.datetime.now(datetime.timezone.utc).astimezone().tzinfo
        time_validator0.validate3("", "", time_zone0)
        self.assertTrue(time_validator0.isStrict())

    def test05(self) -> None:

        time_validator0 = TimeValidator.getInstance()
        locale0 = Locale.TAIWAN
        calendar0 = time_validator0.validate4("", locale0)
        self.assertIsNone(calendar0)

    def test04(self) -> None:

        time_validator0 = TimeValidator.getInstance()
        locale0 = Locale.UK
        time_zone0 = TimeZone.getTimeZone("A#&m)")
        calendar0 = time_validator0.validate5("A#&m)", locale0, time_zone0)
        self.assertIsNone(calendar0)

    def test03(self) -> None:

        time_validator0 = TimeValidator.TimeValidator1()
        locale0 = Locale.TRADITIONAL_CHINESE
        time_validator0.validate6("1", "1", locale0)
        self.assertTrue(time_validator0.isStrict())

    def test02(self) -> None:

        time_validator0 = TimeValidator.TimeValidator1()
        locale0 = Locale("315mz9-fwWa")
        time_validator0.validate6(
            None,
            "org.apache.commons.validator.routines.AbstractFormatValidator",
            locale0,
        )
        self.assertTrue(time_validator0.isStrict())

    def test01(self) -> None:

        time_validator0 = TimeValidator.TimeValidator1()
        locale0 = Locale.US
        time_validator0.validate7("^", "^", locale0, None)
        self.assertTrue(time_validator0.isStrict())

    def test00(self) -> None:

        time_validator0 = TimeValidator.TimeValidator1()
        time_zone0 = TimeZone.getDefault()
        locale0 = Locale.ROOT
        time_validator0.validate7(None, '<N"E', locale0, time_zone0)
        self.assertTrue(time_validator0.isStrict())
