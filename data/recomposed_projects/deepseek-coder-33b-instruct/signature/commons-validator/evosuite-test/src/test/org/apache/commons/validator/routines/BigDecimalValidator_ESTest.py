from __future__ import annotations
import math
import time
import locale
import re
import os
import decimal
import typing
from typing import *
import numbers
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.validator.routines.BigDecimalValidator import *

# from src.test.org.apache.commons.validator.routines.BigDecimalValidator_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class BigDecimalValidator_ESTest(unittest.TestCase):

    def test29(self) -> None:

        bigDecimalValidator0 = BigDecimalValidator.BigDecimalValidator2()
        bigDecimalValidator0.validate1("d%j}/43h0", "d%j}/43h0")
        self.assertTrue(bigDecimalValidator0.isAllowFractions())
        self.assertTrue(bigDecimalValidator0.isStrict())
        self.assertEqual(0, bigDecimalValidator0.getFormatType())

    def test28(self) -> None:

        bigDecimalValidator0 = BigDecimalValidator.getInstance()
        locale0 = Locale("", ")Ur/p&]fO", "")
        bigDecimal0 = bigDecimalValidator0.validate3(None, "", locale0)
        self.assertIsNone(bigDecimal0)

    def test27(self) -> None:

        bigDecimalValidator0 = BigDecimalValidator.getInstance()
        locale0 = Locale("", ")Ur/p&]fO", "")
        bigDecimal0 = bigDecimalValidator0.validate2("0", locale0)
        self.assertEqual(0, bigDecimal0.byteValue())

    def test26(self) -> None:

        bigDecimalValidator0 = BigDecimalValidator.getInstance()
        bigDecimal0 = bigDecimalValidator0.validate0(None)
        self.assertIsNone(bigDecimal0)

    def test25(self) -> None:
        bigDecimalValidator0 = BigDecimalValidator(False, 0, False)
        bigInteger0 = BigInteger.ZERO
        bigDecimal0 = BigDecimal(bigInteger0)
        boolean0 = bigDecimalValidator0.isInRange(bigDecimal0, 1.0, 1.0)
        self.assertFalse(boolean0)

    def test24(self) -> None:
        bigDecimalValidator0 = BigDecimalValidator.BigDecimalValidator2()
        bigDecimal0 = decimal.Decimal(0)
        boolean0 = bigDecimalValidator0.isInRange(bigDecimal0, 0.0, 0.0)
        self.assertEqual(0, bigDecimalValidator0.getFormatType())
        self.assertTrue(bigDecimalValidator0.isAllowFractions())
        self.assertTrue(boolean0)
        self.assertTrue(bigDecimalValidator0.isStrict())

    def test23(self) -> None:

        bigDecimalValidator0 = BigDecimalValidator.BigDecimalValidator1(True)
        bigDecimal0 = decimal.Decimal(1)
        boolean0 = bigDecimalValidator0.minValue(bigDecimal0, 4370.090111)
        self.assertEqual(0, bigDecimalValidator0.getFormatType())
        self.assertTrue(bigDecimalValidator0.isAllowFractions())
        self.assertFalse(boolean0)
        self.assertTrue(bigDecimalValidator0.isStrict())

    def test22(self) -> None:
        bigDecimalValidator0 = BigDecimalValidator.getInstance()
        bigDecimal0 = decimal.Decimal(1)
        boolean0 = bigDecimalValidator0.minValue(bigDecimal0, 0.0)
        self.assertTrue(boolean0)

    def test21(self) -> None:
        bigDecimalValidator0 = BigDecimalValidator.getInstance()
        bigDecimal0 = decimal.Decimal(10)
        boolean0 = bigDecimalValidator0.maxValue(bigDecimal0, -3036.19)
        self.assertFalse(boolean0)

    def test20(self) -> None:
        bigDecimalValidator0 = BigDecimalValidator(False, 0, False)
        bigInteger0 = BigInteger.ZERO
        bigDecimal0 = BigDecimal(bigInteger0)
        boolean0 = bigDecimalValidator0.maxValue(bigDecimal0, 0.0)
        self.assertTrue(boolean0)

    def test19(self) -> None:

        bigDecimalValidator0 = BigDecimalValidator.BigDecimalValidator1(False)
        # Undeclared exception in Java code
        try:
            bigDecimalValidator0.validate1(".2G(N)&,w'", None)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # Character array is missing \"e\" notation exponential mark.
            self.verifyException("java.math.BigDecimal", e)

    def test18(self) -> None:

        bigDecimalValidator0 = BigDecimalValidator.getInstance()
        try:
            bigDecimalValidator0.isInRange(
                None, -2228.5200035708503, -2228.5200035708503
            )
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException(
                "org.apache.commons.validator.routines.BigDecimalValidator", e
            )

    def test17(self) -> None:

        bigDecimalValidator0 = BigDecimalValidator(False, 0, False)

        try:
            bigDecimalValidator0.maxValue(None, -1470.8376603958777)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException(
                "org.apache.commons.validator.routines.BigDecimalValidator", e
            )

    def test16(self) -> None:

        bigDecimalValidator0 = BigDecimalValidator.BigDecimalValidator2()
        try:
            bigDecimalValidator0.minValue(None, 387.395468228518)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.verifyException(
                "org.apache.commons.validator.routines.BigDecimalValidator", e
            )

    def test15(self) -> None:

        bigDecimalValidator0 = BigDecimalValidator.BigDecimalValidator2()
        dateFormat0 = MockDateFormat.getDateInstance(2)

        with pytest.raises(RuntimeError):
            bigDecimalValidator0.processParsedValue(None, dateFormat0)

    def test14(self) -> None:

        bigDecimalValidator0 = BigDecimalValidator.BigDecimalValidator2()
        dateFormat0 = MockDateFormat.getDateInstance(2)

        try:
            bigDecimalValidator0.processParsedValue(bigDecimalValidator0, dateFormat0)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            verifyException("java.math.BigDecimal", e)

    def test13(self) -> None:

        bigDecimalValidator0 = BigDecimalValidator.getInstance()
        # Undeclared exception
        try:
            bigDecimalValidator0.validate1("nHAV}[5m=r'VmU.", "nHAV}[5m=r'VmU.")
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # Malformed pattern \"nHAV}[5m=r'VmU.\"
            self.verifyException("java.text.DecimalFormat", e)

    def test12(self) -> None:

        bigDecimalValidator0 = BigDecimalValidator.BigDecimalValidator2()
        locale0 = Locale.GERMANY
        # Undeclared exception in Python
        try:
            bigDecimalValidator0.validate3(
                "qqs;{&.YB%>}yvPc", "qqs;{&.YB%>}yvPc", locale0
            )
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            #
            # Unquoted special character ';' in pattern \"qqs;{&.YB%>}yvPc\"
            #
            self.verifyException("java.text.DecimalFormat", e)

    def test11(self) -> None:

        bigDecimalValidator0 = BigDecimalValidator.getInstance()
        bigDecimal0 = bigDecimalValidator0.validate0("8")
        self.assertEqual(8, bigDecimal0)

    def test10(self) -> None:

        bigDecimalValidator0 = BigDecimalValidator.getInstance()
        bigDecimal0 = bigDecimalValidator0.validate0("0")
        self.assertEqual(0, bigDecimal0)

    def test09(self) -> None:

        bigDecimalValidator0 = BigDecimalValidator(False, 0, False)
        bigDecimal0 = bigDecimalValidator0.validate1("9wz0bw~*SW.v3v6JN:[", "")
        self.assertEqual(9, bigDecimal0)
        self.assertIsNotNone(bigDecimal0)

    def test08(self) -> None:

        bigDecimalValidator0 = BigDecimalValidator(False, 0, False)
        bigDecimal0 = bigDecimalValidator0.validate1("", "")
        self.assertIsNone(bigDecimal0)

    def test07(self) -> None:

        bigDecimalValidator0 = BigDecimalValidator.getInstance()
        locale0 = Locale.PRC
        bigDecimal0 = bigDecimalValidator0.validate2("8", locale0)
        self.assertEqual(8, bigDecimal0.shortValue())

    def test06(self) -> None:

        bigDecimalValidator0 = BigDecimalValidator.BigDecimalValidator2()
        locale0 = Locale.CHINESE
        bigDecimalValidator0.validate2("haQYd c~P", locale0)
        self.assertTrue(bigDecimalValidator0.isAllowFractions())
        self.assertEqual(0, bigDecimalValidator0.getFormatType())
        self.assertTrue(bigDecimalValidator0.isStrict())

    def test05(self) -> None:

        bigDecimalValidator0 = BigDecimalValidator.BigDecimalValidator1(False)
        bigDecimal0 = bigDecimalValidator0.validate3("7LFLt2LU", "", None)
        self.assertIsNotNone(bigDecimal0)
        self.assertTrue(bigDecimalValidator0.isAllowFractions())
        self.assertEqual(7, bigDecimal0)

    def test04(self) -> None:

        bigDecimalValidator0 = BigDecimalValidator.BigDecimalValidator1(True)
        locale0 = Locale.TRADITIONAL_CHINESE
        bigDecimalValidator0.validate3(
            "uerw0SvYKHsnSW9WTj", "uerw0SvYKHsnSW9WTj", locale0
        )
        self.assertTrue(bigDecimalValidator0.isAllowFractions())
        self.assertEqual(0, bigDecimalValidator0.getFormatType())
        self.assertTrue(bigDecimalValidator0.isStrict())

    def test03(self) -> None:
        bigDecimalValidator0 = BigDecimalValidator.BigDecimalValidator2()
        bigDecimal0 = decimal.Decimal(1)
        boolean0 = bigDecimalValidator0.isInRange(bigDecimal0, 1, -1640.0)
        self.assertTrue(bigDecimalValidator0.isStrict())
        self.assertEqual(0, bigDecimalValidator0.getFormatType())
        self.assertFalse(boolean0)
        self.assertTrue(bigDecimalValidator0.isAllowFractions())

    def test02(self) -> None:

        bigDecimalValidator0 = BigDecimalValidator.BigDecimalValidator1(False)
        bigDecimal0 = decimal.Decimal(1)
        boolean0 = bigDecimalValidator0.isInRange(bigDecimal0, -643.0, 2.0)
        self.assertEqual(0, bigDecimalValidator0.getFormatType())
        self.assertTrue(bigDecimalValidator0.isAllowFractions())
        self.assertFalse(bigDecimalValidator0.isStrict())
        self.assertTrue(boolean0)

    def test01(self) -> None:
        bigDecimalValidator0 = BigDecimalValidator.BigDecimalValidator2()
        bigDecimal0 = decimal.Decimal(0)
        boolean0 = bigDecimalValidator0.minValue(bigDecimal0, 0.0)
        self.assertEqual(0, bigDecimalValidator0.getFormatType())
        self.assertTrue(bigDecimalValidator0.isAllowFractions())
        self.assertTrue(bigDecimalValidator0.isStrict())
        self.assertTrue(boolean0)

    def test00(self) -> None:
        bigDecimalValidator0 = BigDecimalValidator(False, 0, False)
        bigDecimal0 = decimal.Decimal(1)
        boolean0 = bigDecimalValidator0.maxValue(bigDecimal0, 2)
        self.assertTrue(boolean0)
