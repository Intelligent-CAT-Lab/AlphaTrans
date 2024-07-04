from __future__ import annotations
import math
import time
import locale
import re
import mock
import os
import decimal
import numbers
import unittest
import pytest
import io
import unittest

# from src.test.org.apache.commons.validator.routines.AbstractFormatValidator_ESTest_scaffolding import *
from src.main.org.apache.commons.validator.routines.BigDecimalValidator import *
from src.main.org.apache.commons.validator.routines.ByteValidator import *
from src.main.org.apache.commons.validator.routines.CalendarValidator import *
from src.main.org.apache.commons.validator.routines.DoubleValidator import *
from src.main.org.apache.commons.validator.routines.IntegerValidator import *
from src.main.org.apache.commons.validator.routines.LongValidator import *
from src.main.org.apache.commons.validator.routines.PercentValidator import *
from src.main.org.apache.commons.validator.routines.ShortValidator import *

# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class AbstractFormatValidator_ESTest(unittest.TestCase):

    def test40(self) -> None:

        percent_validator0 = PercentValidator.PercentValidator1()

        # Undeclared exception in Java code
        try:
            percent_validator0.isValid0("0.01")
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # Character array is missing \"e\" notation exponential mark.
            self.verifyException("java.math.BigDecimal", e)

    def test39(self) -> None:

        calendar_validator0 = CalendarValidator.CalendarValidator1()
        calendar0 = calendar_validator0.validate2("0.01", "0.01")
        locale0 = Locale.KOREAN
        string0 = calendar_validator0.format2(calendar0, locale0)
        self.assertTrue(calendar_validator0.isStrict())
        self.assertIsNotNone(string0)

    def test38(self) -> None:

        byte_validator0 = ByteValidator.getInstance()
        locale0 = Locale.GERMANY
        boolean0 = byte_validator0.isValid2("0.01", locale0)
        self.assertTrue(boolean0)

    def test37(self) -> None:

        doubleValidator0 = DoubleValidator.getInstance()
        double0 = doubleValidator0.validate1("0u|3+PO|MUPg N4", "0u|3+PO|MUPg N4")
        locale0 = Locale.ITALIAN
        string0 = doubleValidator0.format3(double0, "X?x64iTN-%bb9aYk`$", locale0)
        self.assertEqual("X?x64iTN-%bb9aYk`$0", string0)

    def test36(self) -> None:

        doubleValidator0 = DoubleValidator.getInstance()
        double0 = doubleValidator0.validate1("0u|3+PO|MUPg N4", "0u|3+PO|MUPg N4")
        string0 = doubleValidator0.format1(double0, "0u|3+PO|MUPg N4")
        self.assertEqual("0u|3+PO|MUPg N4", string0)

    def test35(self) -> None:

        percent_validator0 = PercentValidator.PercentValidator1()

        # Undeclared exception in Java code
        try:
            percent_validator0.format0(percent_validator0)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # Cannot format given Object as a Number
            self.verifyException("java.text.DecimalFormat", e)

    def test34(self) -> None:

        long_validator0 = LongValidator(False, 0)
        long_validator0.isValid1("0u|3+PO|MUPg N4", "0u|3+PO|MUPg N4")
        self.assertFalse(long_validator0.isStrict())

    def test33(self) -> None:

        doubleValidator0 = DoubleValidator.DoubleValidator1()
        double0 = doubleValidator0.validate0("4bpT=C'ajc}};")
        self.assertIsNone(double0)
        self.assertTrue(doubleValidator0.isStrict())

    def test32(self) -> None:
        bigDecimalValidator0 = BigDecimalValidator.BigDecimalValidator1(False)
        boolean0 = bigDecimalValidator0.isStrict()
        self.assertFalse(boolean0)

    def test31(self) -> None:

        percent_validator0 = PercentValidator.PercentValidator1()

        try:
            percent_validator0.format1(".,|h6zw,c=HFi", ".,|h6zw,c=HFi")
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            verifyException("java.text.DecimalFormat", e)

    def test30(self) -> None:

        bigDecimalValidator0 = BigDecimalValidator.BigDecimalValidator2()
        locale0 = Locale.CHINA

        with self.assertRaises(ValueError):
            bigDecimalValidator0.format2(locale0, locale0)

        verifyException("java.text.DecimalFormat", ValueError)

    def test29(self) -> None:

        percent_validator0 = PercentValidator.PercentValidator1()
        locale0 = Locale.JAPANESE

        try:
            percent_validator0.format3(
                locale0, "org.apache.commons.validator.routines.ByteValidator", locale0
            )
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            self.verifyException("java.text.DecimalFormat", e)

    def test28(self) -> None:

        integer_validator0 = IntegerValidator.IntegerValidator1()
        double0 = 2350.169
        choice_format0 = ChoiceFormat("=ZU]3XHwkq.")

        with pytest.raises(ArrayIndexOutOfBoundsException):
            integer_validator0.format4(double0, choice_format0)
            verifyException("java.text.ChoiceFormat", ArrayIndexOutOfBoundsException)

    def test27(self) -> None:

        calendar_validator0 = CalendarValidator.CalendarValidator1()
        message_format0 = MessageFormat("0.01")

        with pytest.raises(TypeError):
            calendar_validator0.format4("0.01", message_format0)
            self.fail("Expecting exception: TypeError")
        self.verifyException("java.text.MessageFormat", TypeError)

    def test26(self) -> None:

        percent_validator0 = PercentValidator.PercentValidator1()
        date_format0 = MockDateFormat.getDateInstance(1)

        # Undeclared exception in Java code
        try:
            percent_validator0.format4(None, date_format0)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # Cannot format given Object as a Date
            self.verifyException("java.text.DateFormat", e)

    def test25(self) -> None:

        percent_validator0 = PercentValidator.PercentValidator1()
        locale0 = Locale.KOREAN

        try:
            percent_validator0.format4(locale0, None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.verifyException(
                "org.apache.commons.validator.routines.AbstractFormatValidator", e
            )

    def test24(self) -> None:

        calendar_validator0 = CalendarValidator(False, 1868)
        try:
            calendar_validator0.isValid0("0u|3+PO|MUPg N4")
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # Illegal date style 1868
            self.verifyException("java.text.DateFormat", e)

    def test23(self) -> None:

        double_validator0 = DoubleValidator.getInstance()
        # Undeclared exception in Java code
        try:
            double_validator0.isValid1(
                "org.apache.commons.validator.routines.FloatValidator",
                "org.apache.commons.validator.routines.FloatValidator",
            )
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # Multiple decimal separators in pattern \"org.apache.commons.validator.routines.FloatValidator\"
            self.verifyException("java.text.DecimalFormat", e)

    def test22(self) -> None:

        locale0 = Locale.CANADA
        calendarValidator0 = CalendarValidator(False, 4880)

        with self.assertRaises(ValueError):
            calendarValidator0.isValid2("0.01", locale0)
            self.fail("Expecting exception: ValueError")

        self.verifyException("java.text.DateFormat", ValueError)

    def test21(self) -> None:

        percent_validator0 = PercentValidator(False)
        locale0 = Locale("0.01")

        # Undeclared exception in Java code.
        try:
            percent_validator0.isValid2("0.01", locale0)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # Character array is missing \"e\" notation exponential mark.
            self.verifyException("java.math.BigDecimal", e)

    def test20(self) -> None:

        percentValidator0 = PercentValidator.PercentValidator1()
        locale0 = Locale.FRENCH
        # Undeclared exception in Java code
        try:
            percentValidator0.isValid3("-L>4fzr',Jg]@qyT", "-L>4fzr',Jg]@qyT", locale0)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # Malformed pattern \"-L>4fzr',Jg]@qyT\"
            self.verifyException("java.text.DecimalFormat", e)

    def test19(self) -> None:

        percentValidator0 = PercentValidator.PercentValidator1()
        locale0 = "KOREA"
        # Undeclared exception in Java
        try:
            percentValidator0.isValid3("0.01", None, locale0)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # Character array is missing \"e\" notation exponential mark.
            self.verifyException("java.math.BigDecimal", e)

    def test18(self) -> None:

        calendar_validator0 = CalendarValidator.CalendarValidator1()
        locale0 = Locale.PRC
        number_format0 = NumberFormat.getInstance(locale0)

        try:
            calendar_validator0.parse("0,.01", number_format0)
            self.fail("Expecting exception: TypeError")

        except TypeError as e:
            self.verifyException(
                "org.apache.commons.validator.routines.CalendarValidator", e
            )

    def test17(self) -> None:

        percentValidator0 = PercentValidator.PercentValidator1()
        dateFormat0 = DateFormat.getDateInstance()

        # Undeclared exception in Java code, so we'll use a try-except block to catch the exception
        try:
            percentValidator0.parse(None, dateFormat0)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError:
            pass

    def test16(self) -> None:

        percentValidator0 = PercentValidator.PercentValidator1()
        numberFormat0 = NumberFormat.getPercentInstance()

        try:
            percentValidator0.parse("0.01", numberFormat0)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            self.verifyException("java.math.BigDecimal", e)

    def test15(self) -> None:
        doubleValidator0 = DoubleValidator.DoubleValidator1()
        double0 = float(0)
        doubleValidator0.format0(double0)
        self.assertTrue(doubleValidator0.isStrict())

    def test14(self) -> None:
        calendar_validator0 = CalendarValidator(False, -1)
        calendar_validator0.format0(None)
        self.assertFalse(calendar_validator0.isStrict())

    def test13(self) -> None:
        calendar_validator0 = CalendarValidator.getInstance()
        string0 = calendar_validator0.format1(None, "0.01")
        self.assertIsNone(string0)

    def test12(self) -> None:
        calendar_validator0 = CalendarValidator.CalendarValidator1()
        locale0 = Locale.FRANCE
        calendar_validator0.format2(None, locale0)
        self.assertTrue(calendar_validator0.isStrict())

    def test11(self) -> None:

        calendar_validator0 = CalendarValidator.CalendarValidator1()
        locale0 = Locale.JAPAN
        calendar_validator0.format3(None, "0.01", locale0)
        self.assertTrue(calendar_validator0.isStrict())

    def test10(self) -> None:

        calendar_validator0 = CalendarValidator.CalendarValidator1()
        message_format0 = MessageFormat("")
        calendar_validator0.format4(None, message_format0)
        self.assertTrue(calendar_validator0.isStrict())

    def test09(self) -> None:

        byte_validator0 = ByteValidator.ByteValidator1()
        locale0 = Locale.FRANCE
        message_format0 = MessageFormat("C[", locale0)
        byte_validator0.format4(None, message_format0)
        self.assertTrue(byte_validator0.isStrict())

    def test08(self) -> None:
        percentValidator0 = PercentValidator.PercentValidator1()
        boolean0 = percentValidator0.isStrict()
        self.assertTrue(boolean0)

    def test07(self) -> None:
        calendar_validator0 = CalendarValidator.CalendarValidator1()
        calendar_validator0.isValid0("0.01")
        self.assertTrue(calendar_validator0.isStrict())

    def test06(self) -> None:
        shortValidator0 = ShortValidator(False, -498)
        boolean0 = shortValidator0.isValid0("0.01")
        self.assertTrue(boolean0)

    def test05(self) -> None:

        percentValidator0 = PercentValidator.PercentValidator1()
        percentValidator0.isValid1(None, "")
        self.assertTrue(percentValidator0.isStrict())

    def test04(self) -> None:

        percentValidator0 = PercentValidator.PercentValidator1()
        locale0 = Locale.CHINA
        percentValidator0.isValid2("J?GpsD'fB/+vf#s7B|_", locale0)
        self.assertTrue(percentValidator0.isStrict())

    def test03(self) -> None:

        locale0 = Locale.CHINA
        doubleValidator0 = DoubleValidator(False, -1329)
        doubleValidator0.isValid3("#s 4-|J3aDQ4vKcvq", None, locale0)
        self.assertFalse(doubleValidator0.isStrict())

    def test02(self) -> None:

        calendar_validator0 = CalendarValidator.CalendarValidator1()
        locale0 = Locale.GERMANY
        calendar_validator0.isValid3("0,.01", "0,.01", locale0)
        self.assertTrue(calendar_validator0.isStrict())

    def test01(self) -> None:

        calendar_validator0 = CalendarValidator.getInstance()
        mock_simple_date_format0 = MockSimpleDateFormat("0.01")
        object0 = calendar_validator0.parse("0.01", mock_simple_date_format0)
        self.assertEqual(
            'org.evosuite.runtime.mock.java.util.MockGregorianCalendar[time=?,areFieldsSet=false,areAllFieldsSet=false,lenient=true,zone=sun.util.calendar.ZoneInfo[id="GMT",offset=0,dstSavings=0,useDaylight=false,transitions=0,lastRule=null],firstDayOfWeek=1,minimalDaysInFirstWeek=1,ERA=?,YEAR=?,MONTH=?,WEEK_OF_YEAR=?,WEEK_OF_MONTH=?,DAY_OF_MONTH=?,DAY_OF_YEAR=?,DAY_OF_WEEK=?,DAY_OF_WEEK_IN_MONTH=?,AM_PM=?,HOUR=?,HOUR_OF_DAY=?,MINUTE=?,SECOND=?,MILLISECOND=?,ZONE_OFFSET=?,DST_OFFSET=?]',
            object0.toString(),
        )

    def test00(self) -> None:

        calendar_validator0 = CalendarValidator.CalendarValidator1()
        locale0 = "JAPAN"
        format0 = calendar_validator0._getFormat1(locale0)
        calendar_validator0._parse("", format0)
        self.assertTrue(calendar_validator0.isStrict())
