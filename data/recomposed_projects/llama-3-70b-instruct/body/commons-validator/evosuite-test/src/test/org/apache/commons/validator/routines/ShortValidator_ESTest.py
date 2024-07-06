from __future__ import annotations
import time
import locale
import re
import mock
import os
import decimal
import typing
from typing import *
import numbers
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.validator.routines.ShortValidator import *

# from src.test.org.apache.commons.validator.routines.ShortValidator_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class ShortValidator_ESTest(unittest.TestCase):

    def test36(self) -> None:

        shortValidator0 = ShortValidator.getInstance()
        locale0 = Locale.CHINESE
        short0 = shortValidator0.validate3("-2,308", "", locale0)
        self.assertEqual(short(-2308), short0)
        self.assertIsNotNone(short0)

    def test35(self) -> None:
        shortValidator0 = ShortValidator.ShortValidator1()
        short0 = -3876
        boolean0 = shortValidator0.minValue1(short0, -3876)
        self.assertTrue(shortValidator0.isStrict())
        self.assertEqual(0, shortValidator0.getFormatType())
        self.assertTrue(boolean0)

    def test34(self) -> None:

        shortValidator0 = ShortValidator.getInstance()
        short0 = shortValidator0.validate1('J"+(w-=w(V>', "")
        self.assertIsNone(short0)

    def test33(self) -> None:

        short_validator0 = ShortValidator.ShortValidator1()
        short0 = -2807
        boolean0 = short_validator0.isInRange1(short0, -2807, -2807)
        self.assertEqual(0, short_validator0.getFormatType())
        self.assertTrue(boolean0)
        self.assertTrue(short_validator0.isStrict())

    def test32(self) -> None:

        shortValidator0 = ShortValidator.getInstance()
        short0 = shortValidator0.validate0("-2,322")
        assert short0 is not None
        assert short0 == -2322

    def test31(self) -> None:

        shortValidator0 = ShortValidator(False, -5750)
        locale0 = Locale.FRENCH
        short0 = shortValidator0.validate2("-1", locale0)
        assert short0 is not None
        assert short0 == -1

    def test30(self) -> None:

        shortValidator0 = ShortValidator(False, -2381)
        dateFormat0 = DateFormat.getDateTimeInstance(2, 1)
        short0 = shortValidator0.processParsedValue(0, dateFormat0)
        self.assertIsNotNone(short0)

        boolean0 = shortValidator0.maxValue1(short0, -1)
        self.assertFalse(boolean0)

    def test29(self) -> None:
        shortValidator0 = ShortValidator.ShortValidator1()
        boolean0 = shortValidator0.isInRange0(2239, 1, -227)
        self.assertEqual(0, shortValidator0.getFormatType())
        self.assertFalse(boolean0)
        self.assertTrue(shortValidator0.isStrict())

    def test28(self) -> None:
        shortValidator0 = ShortValidator(False, 1497)
        boolean0 = shortValidator0.minValue0(-828, 0)
        self.assertFalse(boolean0)

    def test27(self) -> None:
        shortValidator0 = ShortValidator.getInstance()
        short0 = short(1359)
        boolean0 = shortValidator0.maxValue1(short0, short(1359))
        self.assertTrue(boolean0)

    def test26(self) -> None:

        short_validator0 = ShortValidator.ShortValidator1()
        integer0 = -2147416048
        date_format0 = DateFormat.getDateTimeInstance()
        object0 = short_validator0.processParsedValue(integer0, date_format0)
        self.assertTrue(short_validator0.isStrict())
        self.assertIsNone(object0)
        self.assertEqual(0, short_validator0.getFormatType())

    def test25(self) -> None:

        short_validator0 = ShortValidator.ShortValidator1()
        integer0 = Integer(2147416545)
        mock_simple_date_format0 = MockSimpleDateFormat()
        object0 = short_validator0.processParsedValue(
            integer0, mock_simple_date_format0
        )
        self.assertIsNone(object0)
        self.assertEqual(0, short_validator0.getFormatType())
        self.assertTrue(short_validator0.isStrict())

    def test24(self) -> None:
        shortValidator0 = ShortValidator.ShortValidator1()
        boolean0 = shortValidator0.isInRange0(-851, 0, 0)
        self.assertEqual(0, shortValidator0.getFormatType())
        self.assertTrue(shortValidator0.isStrict())
        self.assertFalse(boolean0)

    def test23(self) -> None:
        shortValidator0 = ShortValidator.ShortValidator1()
        boolean0 = shortValidator0.isInRange0(0, 0, 4417)
        self.assertTrue(boolean0)
        self.assertEqual(0, shortValidator0.getFormatType())
        self.assertTrue(shortValidator0.isStrict())

    def test22(self) -> None:
        shortValidator0 = ShortValidator.ShortValidator1()
        boolean0 = shortValidator0.minValue0(100, 100)
        self.assertTrue(boolean0)
        self.assertTrue(shortValidator0.isStrict())
        self.assertEqual(0, shortValidator0.getFormatType())

    def test21(self) -> None:
        shortValidator0 = ShortValidator.getInstance()
        boolean0 = shortValidator0.maxValue0(113, -1615)
        self.assertFalse(boolean0)

    def test20(self) -> None:
        shortValidator0 = ShortValidator.ShortValidator1()
        boolean0 = shortValidator0.maxValue0(-1398, 4743)
        self.assertTrue(shortValidator0.isStrict())
        self.assertTrue(boolean0)
        self.assertEqual(0, shortValidator0.getFormatType())

    def test19(self) -> None:

        short_validator0 = ShortValidator.getInstance()

        with self.assertRaises(RuntimeError):
            short_validator0.isInRange1(None, 28, 1)

    def test18(self) -> None:

        short_validator0 = ShortValidator.getInstance()
        # Undeclared exception in Java code
        try:
            short_validator0.maxValue1(None, -4720)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            # no message in exception (getMessage() returned null)
            self.verifyException(
                "org.apache.commons.validator.routines.ShortValidator", e
            )

    def test17(self) -> None:

        shortValidator0 = ShortValidator.getInstance()
        mockSimpleDateFormat0 = MockSimpleDateFormat()

        # Undeclared exception in Java code
        try:
            shortValidator0.processParsedValue(
                mockSimpleDateFormat0, mockSimpleDateFormat0
            )
            self.fail("Expecting exception: TypeError")

        except TypeError as e:
            # class org.evosuite.runtime.mock.java.text.MockSimpleDateFormat cannot be cast to class java.lang.Number
            self.verifyException(
                "org.apache.commons.validator.routines.ShortValidator", e
            )

    def test16(self) -> None:

        shortValidator0 = ShortValidator.ShortValidator1()

        with pytest.raises(RuntimeError):
            shortValidator0.processParsedValue(None, None)
            self.fail("Expecting exception: RuntimeError")

        verifyException(
            "org.apache.commons.validator.routines.ShortValidator", RuntimeError
        )

    def test15(self) -> None:

        shortValidator0 = ShortValidator.ShortValidator1()
        # Undeclared exception in Java code
        try:
            shortValidator0.validate1(
                "org.apache.commons.validator.routines.AbstractFormatValidator",
                "org.apache.commons.validator.routines.AbstractFormatValidator",
            )
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # Multiple decimal separators in pattern \"org.apache.commons.validator.routines.AbstractFormatValidator\"
            self.verifyException("java.text.DecimalFormat", e)

    def test14(self) -> None:

        shortValidator0 = ShortValidator.ShortValidator1()
        locale0 = Locale.ITALIAN
        # Undeclared exception in Java code
        try:
            shortValidator0.validate3(
                "org.apache.commons.validator.routines.AbstractFormatValidator",
                "org.apache.commons.validator.routines.AbstractFormatValidator",
                locale0,
            )
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # Multiple decimal separators in pattern \"org.apache.commons.validator.routines.AbstractFormatValidator\"
            self.verifyException("java.text.DecimalFormat", e)

    def test13(self) -> None:
        shortValidator0 = ShortValidator.ShortValidator1()
        short0 = -3876
        boolean0 = shortValidator0.minValue1(short0, -1)
        self.assertFalse(boolean0)
        self.assertTrue(shortValidator0.isStrict())
        self.assertEqual(0, shortValidator0.getFormatType())

    def test12(self) -> None:

        shortValidator0 = ShortValidator.ShortValidator1()
        short0 = shortValidator0.validate0("5+7k4BP#f|U&C-gu\u0003")
        self.assertIsNone(short0)
        self.assertEqual(0, shortValidator0.getFormatType())

    def test11(self) -> None:

        shortValidator0 = ShortValidator.getInstance()
        short0 = shortValidator0.validate0("4")
        self.assertEqual(4, short0)
        self.assertIsNotNone(short0)

    def test10(self) -> None:

        shortValidator0 = ShortValidator.getInstance()
        short0 = shortValidator0.validate0("0")
        self.assertEqual(0, short0)

    def test09(self) -> None:

        shortValidator0 = ShortValidator.getInstance()
        short0 = shortValidator0.validate1("4", "")
        self.assertEqual(4, short0)
        self.assertIsNotNone(short0)

    def test08(self) -> None:

        short_validator0 = ShortValidator.ShortValidator1()
        short_validator0.validate1("p}0G", "p}0G")
        self.assertTrue(short_validator0.isStrict())
        self.assertEqual(0, short_validator0.getFormatType())

    def test07(self) -> None:

        shortValidator0 = ShortValidator.getInstance()
        locale0 = Locale.GERMAN
        short0 = shortValidator0.validate2(
            "org.apache.commons.validator.routines.AbstractNumberValidator", locale0
        )
        self.assertIsNone(short0)

    def test06(self) -> None:

        shortValidator0 = ShortValidator(False, 1000)
        short0 = shortValidator0.validate2("8B8", None)
        self.assertEqual(8, short0)
        self.assertIsNotNone(short0)

    def test05(self) -> None:

        shortValidator0 = ShortValidator.getInstance()
        locale0 = Locale.KOREA
        short0 = shortValidator0.validate2("0", locale0)
        self.assertEqual(0, short0)

    def test04(self) -> None:

        shortValidator0 = ShortValidator.getInstance()
        locale0 = Locale.forLanguageTag("")
        short0 = shortValidator0.validate3("", "", locale0)
        self.assertIsNone(short0)

    def test03(self) -> None:

        shortValidator0 = ShortValidator.getInstance()
        locale0 = Locale.FRENCH
        short0 = shortValidator0.validate3("4", "", locale0)
        assert short0 is not None
        assert short0 == 4

    def test02(self) -> None:

        shortValidator0 = ShortValidator.getInstance()
        locale0 = Locale.KOREA
        short0 = shortValidator0.validate3("0", None, locale0)
        self.assertEqual(0, short0)

    def test01(self) -> None:

        short_validator0 = ShortValidator.ShortValidator1()
        short0 = -2807
        boolean0 = short_validator0.isInRange1(short0, 1230, 2024)
        self.assertTrue(short_validator0.isStrict())
        self.assertEqual(0, short_validator0.getFormatType())
        self.assertFalse(boolean0)

    def test00(self) -> None:
        shortValidator0 = ShortValidator.ShortValidator1()
        boolean0 = shortValidator0.minValue0(-2609, -4336)
        self.assertTrue(boolean0)
        self.assertEqual(0, shortValidator0.getFormatType())
        self.assertTrue(shortValidator0.isStrict())
