from __future__ import annotations
import time
import locale
import re
import os
import decimal
import typing
from typing import *
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.validator.routines.LongValidator import *

# from src.test.org.apache.commons.validator.routines.LongValidator_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class LongValidator_ESTest(unittest.TestCase):

    def test33(self) -> None:
        longValidator0 = LongValidator.getInstance()
        long0 = Long(1)
        boolean0 = longValidator0.maxValue1(long0, -5388)
        self.assertFalse(boolean0)

    def test32(self) -> None:

        longValidator0 = LongValidator(False, -2697)
        long0 = longValidator0.validate1("1I{}iN5uj", "")
        self.assertEqual(1, long0)

    def test31(self) -> None:

        long_validator0 = LongValidator.LongValidator1()
        locale0 = Locale.CANADA_FRENCH
        # Undeclared exception in Java code
        try:
            long_validator0.validate3(
                ".CEhuN|Kc?8.]wYfeV", ".CEhuN|Kc?8.]wYfeV", locale0
            )
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # Multiple decimal separators in pattern \".CEhuN|Kc?8.]wYfeV\"
            self.verifyException("java.text.DecimalFormat", e)

    def test30(self) -> None:

        long_validator0 = LongValidator.LongValidator1()
        try:
            long_validator0.isInRange1(None, 1926, 1)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.assertIsInstance(e, RuntimeError)
            self.verifyException(
                "org.apache.commons.validator.routines.LongValidator", e
            )

    def test29(self) -> None:

        longValidator0 = LongValidator(False, -2697)
        long0 = longValidator0.validate0('bez("K')
        self.assertIsNone(long0)

    def test28(self) -> None:
        longValidator0 = LongValidator.LongValidator1()
        long0 = Long(2)
        boolean0 = longValidator0.minValue1(long0, 1959)
        self.assertFalse(boolean0)
        self.assertEqual(0, longValidator0.getFormatType())
        self.assertTrue(longValidator0.isStrict())

    def test27(self) -> None:

        longValidator0 = LongValidator(False, -1)
        locale0 = Locale.TAIWAN
        long0 = longValidator0.validate2("-2OPxiA(JC1X", locale0)
        self.assertEqual(-2, long0)

    def test26(self) -> None:
        long_validator0 = LongValidator.LongValidator1()
        boolean0 = long_validator0.isInRange0(1899, 1, 1899)
        self.assertTrue(long_validator0.isStrict())
        self.assertTrue(boolean0)
        self.assertEqual(0, long_validator0.getFormatType())

    def test25(self) -> None:
        longValidator0 = LongValidator.getInstance()
        long0 = long(2)
        boolean0 = longValidator0.isInRange1(long0, 0, 0)
        self.assertFalse(boolean0)

    def test24(self) -> None:
        longValidator0 = LongValidator.getInstance()
        long0 = long(0)
        boolean0 = longValidator0.maxValue1(long0, 0)
        self.assertTrue(boolean0)

    def test23(self) -> None:

        long_validator0 = LongValidator.getInstance()
        locale0 = Locale.CANADA
        object0 = long_validator0.processParsedValue(locale0, None)
        self.assertIsNone(object0)

    def test22(self) -> None:
        long_validator0 = LongValidator.LongValidator1()
        boolean0 = long_validator0.isInRange0(1, 2113, 31)
        self.assertFalse(boolean0)
        self.assertTrue(long_validator0.isStrict())
        self.assertEqual(0, long_validator0.getFormatType())

    def test21(self) -> None:
        longValidator0 = LongValidator(False, 2210)
        boolean0 = longValidator0.isInRange0(1821, -1957, -1544)
        self.assertFalse(boolean0)

    def test20(self) -> None:
        longValidator0 = LongValidator.getInstance()
        boolean0 = longValidator0.minValue0(0, 1)
        self.assertFalse(boolean0)

    def test19(self) -> None:
        long_validator0 = LongValidator.LongValidator1()
        boolean0 = long_validator0.maxValue0(0, 0)
        self.assertTrue(long_validator0.isStrict())
        self.assertEqual(0, long_validator0.getFormatType())
        self.assertTrue(boolean0)

    def test18(self) -> None:
        longValidator0 = LongValidator(False, 2210)
        boolean0 = longValidator0.maxValue0((-1957), (-3115))
        self.assertFalse(boolean0)

    def test17(self) -> None:

        long_validator0 = LongValidator.LongValidator1()
        # Undeclared exception in Java code
        try:
            long_validator0.maxValue1(None, 2210)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            # no message in exception (getMessage() returned null)
            self.verifyException(
                "org.apache.commons.validator.routines.LongValidator", e
            )

    def test16(self) -> None:

        long_validator0 = LongValidator.getInstance()
        # Undeclared exception in Java code
        try:
            long_validator0.minValue1(None, 0)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            # no message in exception (getMessage() returned null)
            self.verifyException(
                "org.apache.commons.validator.routines.LongValidator", e
            )

    def test15(self) -> None:

        long_validator0 = LongValidator.LongValidator1()
        # Undeclared exception in Java code
        try:
            long_validator0.validate1(
                "org.apache.commons.validator.routines.LongValidator",
                "org.apache.commons.validator.routines.LongValidator",
            )
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # Multiple decimal separators in pattern \"org.apache.commons.validator.routines.LongValidator\"
            self.verifyException("java.text.DecimalFormat", e)

    def test14(self) -> None:
        longValidator0 = LongValidator.getInstance()
        long0 = long(0)
        boolean0 = longValidator0.isInRange1(long0, 0, 0)
        self.assertTrue(boolean0)

    def test13(self) -> None:
        longValidator0 = LongValidator(True, 0)
        long0 = Long(2)
        boolean0 = longValidator0.minValue1(long0, 0)
        self.assertTrue(boolean0)

    def test12(self) -> None:

        long_validator0 = LongValidator.LongValidator1()
        long0 = long_validator0.validate0("8")
        self.assertIsNotNone(long0)
        self.assertTrue(long_validator0.isStrict())

    def test11(self) -> None:

        longValidator0 = LongValidator(False, -640)
        long0 = longValidator0.validate0("0")
        self.assertEqual(0, long0)

    def test10(self) -> None:

        longValidator0 = LongValidator(False, 2210)
        long0 = longValidator0.validate1(".", ".")
        self.assertIsNone(long0)

    def test09(self) -> None:

        longValidator0 = LongValidator.LongValidator1()
        long0 = longValidator0.validate1('"sAVHn[k5}0N', '"sAVHn[k5}0N')
        self.assertEqual(0, longValidator0.getFormatType())
        self.assertTrue(longValidator0.isStrict())
        self.assertIsNotNone(long0)

    def test08(self) -> None:

        long_validator0 = LongValidator.LongValidator1()
        long_validator0.validate2("", None)
        self.assertEqual(0, long_validator0.getFormatType())
        self.assertTrue(long_validator0.isStrict())

    def test07(self) -> None:

        longValidator0 = LongValidator.LongValidator1()
        long0 = longValidator0.validate2("1", None)
        self.assertIsNotNone(long0)
        self.assertTrue(longValidator0.isStrict())

    def test06(self) -> None:

        longValidator0 = LongValidator.getInstance()
        locale0 = Locale.ROOT
        long0 = longValidator0.validate2("0", locale0)
        self.assertEqual(0, long0)

    def test05(self) -> None:

        long_validator0 = LongValidator.LongValidator1()
        long_validator0.validate3("", "", None)
        self.assertEqual(0, long_validator0.getFormatType())
        self.assertTrue(long_validator0.isStrict())

    def test04(self) -> None:

        long_validator0 = LongValidator.LongValidator1()
        long0 = long_validator0.validate3("1", "", None)
        self.assertIsNotNone(long0)
        self.assertTrue(long_validator0.isStrict())

    def test03(self) -> None:

        long_validator0 = LongValidator.LongValidator1()
        locale0 = Locale.CHINESE
        long0 = long_validator0.validate3("htrI]FlHmufbZ0R", "htrI]FlHmufbZ0R", locale0)
        self.assertIsNotNone(long0)
        self.assertTrue(long_validator0.isStrict())
        self.assertEqual(0, long_validator0.getFormatType())

    def test02(self) -> None:
        longValidator0 = LongValidator.getInstance()
        long0 = long(2)
        boolean0 = longValidator0.isInRange1(long0, 1, 3243)
        self.assertTrue(boolean0)

    def test01(self) -> None:
        long_validator0 = LongValidator.LongValidator1()
        boolean0 = long_validator0.minValue0(2113, 2113)
        self.assertTrue(long_validator0.isStrict())
        self.assertTrue(boolean0)
        self.assertEqual(0, long_validator0.getFormatType())

    def test00(self) -> None:
        long_validator0 = LongValidator.LongValidator1()
        boolean0 = long_validator0.maxValue0(0, 1436)
        self.assertTrue(long_validator0.isStrict())
        self.assertEqual(0, long_validator0.getFormatType())
        self.assertTrue(boolean0)
