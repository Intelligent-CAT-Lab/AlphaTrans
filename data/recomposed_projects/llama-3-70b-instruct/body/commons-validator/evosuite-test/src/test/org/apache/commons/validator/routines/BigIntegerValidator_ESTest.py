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
from src.main.org.apache.commons.validator.routines.BigIntegerValidator import *

# from src.test.org.apache.commons.validator.routines.BigIntegerValidator_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class BigIntegerValidator_ESTest(unittest.TestCase):

    def test30(self) -> None:

        bigIntegerValidator0 = BigIntegerValidator.getInstance()
        try:
            bigIntegerValidator0.validate1(
                "org.apache.commons.validator.routines.BigIntegerValidator",
                "org.apache.commons.validator.routines.BigIntegerValidator",
            )
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            self.verifyException("java.text.DecimalFormat", e)

    def test29(self) -> None:
        bigIntegerValidator0 = BigIntegerValidator.BigIntegerValidator1()
        bigInteger0 = BigInteger.ZERO
        boolean0 = bigIntegerValidator0.isInRange(bigInteger0, (-1), (-1))
        self.assertTrue(bigIntegerValidator0.isStrict())
        self.assertEqual(0, bigIntegerValidator0.getFormatType())
        self.assertFalse(boolean0)

    def test28(self) -> None:

        bigIntegerValidator0 = BigIntegerValidator.getInstance()
        bigInteger0 = bigIntegerValidator0.validate3("-FaZuq>?^+529", "FaZuq>?^+", None)
        self.assertEqual(-529, bigInteger0)

    def test27(self) -> None:

        bigIntegerValidator0 = BigIntegerValidator.getInstance()
        locale0 = Locale.FRANCE
        bigInteger0 = bigIntegerValidator0.validate2("-FaZuq>?^+529", locale0)
        self.assertIsNone(bigInteger0)

    def test26(self) -> None:

        bigIntegerValidator0 = BigIntegerValidator.getInstance()
        bigInteger0 = bigIntegerValidator0.validate0(
            "org.apache.commons.validator.routines.AbstractFormatValidator"
        )
        self.assertIsNone(bigInteger0)

    def test25(self) -> None:
        bigIntegerValidator0 = BigIntegerValidator(True, 1513)
        bigInteger0 = BigInteger.ZERO
        boolean0 = bigIntegerValidator0.isInRange(bigInteger0, 1, 0)
        self.assertFalse(boolean0)

    def test24(self) -> None:
        bigIntegerValidator0 = BigIntegerValidator.getInstance()
        bigInteger0 = BigInteger.ZERO
        boolean0 = bigIntegerValidator0.isInRange(bigInteger0, 0, 0)
        self.assertTrue(boolean0)

    def test23(self) -> None:
        bigIntegerValidator0 = BigIntegerValidator.getInstance()
        bigInteger0 = BigInteger.ONE
        boolean0 = bigIntegerValidator0.minValue(bigInteger0, 2)
        self.assertFalse(boolean0)

    def test22(self) -> None:
        bigIntegerValidator0 = BigIntegerValidator.BigIntegerValidator1()
        bigInteger0 = BigInteger.ZERO
        boolean0 = bigIntegerValidator0.minValue(bigInteger0, 0)
        self.assertEqual(0, bigIntegerValidator0.getFormatType())
        self.assertTrue(bigIntegerValidator0.isStrict())
        self.assertTrue(boolean0)

    def test21(self) -> None:
        bigIntegerValidator0 = BigIntegerValidator.getInstance()
        bigInteger0 = BigInteger.TEN
        boolean0 = bigIntegerValidator0.maxValue(bigInteger0, 2)
        self.assertFalse(boolean0)

    def test20(self) -> None:
        bigInteger0 = BigInteger.TWO
        bigIntegerValidator0 = BigIntegerValidator.BigIntegerValidator1()
        boolean0 = bigIntegerValidator0.maxValue(bigInteger0, 2)
        self.assertTrue(boolean0)
        self.assertTrue(bigIntegerValidator0.isStrict())
        self.assertEqual(0, bigIntegerValidator0.getFormatType())

    def test19(self) -> None:

        bigIntegerValidator0 = BigIntegerValidator.getInstance()
        # Undeclared exception in Java code
        try:
            bigIntegerValidator0.isInRange(None, 0, 0)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            # no message in exception (getMessage() returned null)
            self.verifyException(
                "org.apache.commons.validator.routines.BigIntegerValidator", e
            )

    def test18(self) -> None:

        bigIntegerValidator0 = BigIntegerValidator.getInstance()
        # Undeclared exception in Java code
        try:
            bigIntegerValidator0.maxValue(None, -3278)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            # no message in exception (getMessage() returned null)
            self.verifyException(
                "org.apache.commons.validator.routines.BigIntegerValidator", e
            )

    def test17(self) -> None:

        bigIntegerValidator0 = BigIntegerValidator.BigIntegerValidator1()
        # Undeclared exception in Java code
        try:
            bigIntegerValidator0.minValue(None, 0)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            # no message in exception (getMessage() returned null)
            self.verifyException(
                "org.apache.commons.validator.routines.BigIntegerValidator", e
            )

    def test16(self) -> None:

        bigIntegerValidator0 = BigIntegerValidator.BigIntegerValidator1()
        dateFormat0 = DateFormat.getTimeInstance(2)
        object0 = object()

        with pytest.raises(TypeError):
            bigIntegerValidator0.processParsedValue(object0, dateFormat0)
            verifyException(
                "org.apache.commons.validator.routines.BigIntegerValidator", TypeError
            )

    def test15(self) -> None:

        bigIntegerValidator0 = BigIntegerValidator.BigIntegerValidator1()
        dateFormat0 = DateFormat.getInstance()

        with pytest.raises(RuntimeError):
            bigIntegerValidator0.processParsedValue(None, dateFormat0)

    def test14(self) -> None:

        bigIntegerValidator0 = BigIntegerValidator.getInstance()
        # Undeclared exception in Java code
        try:
            bigIntegerValidator0.validate3(
                "org.apache.commons.validator.routines.AbstractFormatValidator",
                "org.apache.commons.validator.routines.AbstractFormatValidator",
                None,
            )
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # Multiple decimal separators in pattern "org.apache.commons.validator.routines.AbstractFormatValidator"
            self.verifyException("java.text.DecimalFormat", e)

    def test13(self) -> None:

        bigIntegerValidator0 = BigIntegerValidator.BigIntegerValidator1()
        decimalFormat0 = bigIntegerValidator0.getFormat1(None)
        bigInteger0 = BigInteger.ZERO
        bigIntegerValidator0.processParsedValue(bigInteger0, decimalFormat0)
        self.assertTrue(bigIntegerValidator0.isStrict())
        self.assertEqual("#,##0.###", decimalFormat0.toLocalizedPattern())

    def test12(self) -> None:

        bigIntegerValidator0 = BigIntegerValidator(False, -2052)
        bigInteger0 = bigIntegerValidator0.validate0("8")
        self.assertEqual(8, bigInteger0)

    def test11(self) -> None:

        bigIntegerValidator0 = BigIntegerValidator.BigIntegerValidator1()
        bigInteger0 = bigIntegerValidator0.validate0("0")
        self.assertIsNotNone(bigInteger0)
        self.assertTrue(bigIntegerValidator0.isStrict())

    def test10(self) -> None:

        bigIntegerValidator0 = BigIntegerValidator.BigIntegerValidator1()
        bigInteger0 = bigIntegerValidator0.validate1("3", "")
        assert bigInteger0 is not None
        assert bigIntegerValidator0.isStrict()

    def test09(self) -> None:

        bigIntegerValidator0 = BigIntegerValidator(True, 0)
        bigInteger0 = bigIntegerValidator0.validate1("cxD0gTp~T@%]V7", "cxD0gTp~T@%]V7")
        self.assertEqual(0, bigInteger0)

    def test08(self) -> None:

        bigIntegerValidator0 = BigIntegerValidator.BigIntegerValidator1()
        bigIntegerValidator0.validate1("", "")
        self.assertEqual(0, bigIntegerValidator0.getFormatType())
        self.assertTrue(bigIntegerValidator0.isStrict())

    def test07(self) -> None:

        bigIntegerValidator0 = BigIntegerValidator.getInstance()
        locale0 = Locale.ENGLISH
        bigInteger0 = bigIntegerValidator0.validate2("6", locale0)
        self.assertEqual(6, bigInteger0)

    def test06(self) -> None:

        bigIntegerValidator0 = BigIntegerValidator.BigIntegerValidator1()
        bigInteger0 = bigIntegerValidator0.validate2("0", None)
        self.assertTrue(bigIntegerValidator0.isStrict())
        self.assertIsNotNone(bigInteger0)

    def test05(self) -> None:

        bigIntegerValidator0 = BigIntegerValidator.getInstance()
        locale0 = Locale.CHINA
        bigInteger0 = bigIntegerValidator0.validate3("5", None, locale0)
        self.assertEqual(5, bigInteger0)

    def test04(self) -> None:

        bigIntegerValidator0 = BigIntegerValidator.BigIntegerValidator1()
        bigIntegerValidator0.validate3("0", "0", None)
        self.assertTrue(bigIntegerValidator0.isStrict())
        self.assertEqual(0, bigIntegerValidator0.getFormatType())

    def test03(self) -> None:

        bigIntegerValidator0 = BigIntegerValidator.BigIntegerValidator1()
        bigIntegerValidator0.validate3("+", "+", None)
        self.assertTrue(bigIntegerValidator0.isStrict())
        self.assertEqual(0, bigIntegerValidator0.getFormatType())

    def test02(self) -> None:
        bigIntegerValidator0 = BigIntegerValidator.BigIntegerValidator1()
        bigInteger0 = BigInteger.ZERO
        boolean0 = bigIntegerValidator0.isInRange(bigInteger0, 0, 2192)
        self.assertEqual(0, bigIntegerValidator0.getFormatType())
        self.assertTrue(boolean0)
        self.assertTrue(bigIntegerValidator0.isStrict())

    def test01(self) -> None:
        bigIntegerValidator0 = BigIntegerValidator.getInstance()
        bigInteger0 = 10
        boolean0 = bigIntegerValidator0.minValue(bigInteger0, 2)
        self.assertTrue(boolean0)

    def test00(self) -> None:
        bigIntegerValidator0 = BigIntegerValidator.getInstance()
        bigInteger0 = BigInteger.TEN
        boolean0 = bigIntegerValidator0.maxValue(bigInteger0, 13)
        self.assertTrue(boolean0)
