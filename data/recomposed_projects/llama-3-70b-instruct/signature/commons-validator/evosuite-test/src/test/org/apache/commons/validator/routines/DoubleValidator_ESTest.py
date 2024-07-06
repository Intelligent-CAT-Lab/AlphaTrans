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
from src.main.org.apache.commons.validator.routines.DoubleValidator import *

# from src.test.org.apache.commons.validator.routines.DoubleValidator_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class DoubleValidator_ESTest(unittest.TestCase):

    def test35(self) -> None:

        double_validator0 = DoubleValidator.getInstance()
        # Undeclared exception in Java code
        try:
            double_validator0.isInRange1(None, 500.7975, 2)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            # no message in exception (getMessage() returned null)
            self.verifyException(
                "org.apache.commons.validator.routines.DoubleValidator", e
            )

    def test34(self) -> None:

        doubleValidator0 = DoubleValidator.getInstance()
        double0 = doubleValidator0.validate0("-6")
        self.assertAlmostEqual(-6.0, double0, delta=0.01)

    def test33(self) -> None:

        doubleValidator0 = DoubleValidator.getInstance()
        locale0 = Locale.KOREA
        double0 = doubleValidator0.validate2("0", locale0)
        self.assertAlmostEqual(0.0, double0, delta=0.01)

    def test32(self) -> None:

        doubleValidator0 = DoubleValidator.getInstance()
        locale0 = Locale.GERMAN
        double0 = doubleValidator0.validate3("", ".qEt'ma|$:@_&m-F}G", locale0)
        self.assertIsNone(double0)

    def test31(self) -> None:

        double_validator0 = DoubleValidator(False, 0)

        with pytest.raises(RuntimeError):
            double_validator0.maxValue1(None, 0)

    def test30(self) -> None:

        doubleValidator0 = DoubleValidator.getInstance()
        double0 = doubleValidator0.validate1("-6", None)
        self.assertAlmostEqual(-6.0, double0, 0.01)

    def test29(self) -> None:

        doubleValidator0 = DoubleValidator.getInstance()
        locale0 = Locale.PRC
        double0 = doubleValidator0.validate2("d@J}4=M@>*+7^", locale0)

        with pytest.raises(RuntimeError):
            doubleValidator0.minValue1(double0, 1403.955)
            verifyException("org.apache.commons.validator.routines.DoubleValidator", e)

    def test28(self) -> None:
        double_validator0 = DoubleValidator.DoubleValidator1()
        boolean0 = double_validator0.isInRange0(0.0, 864.5, 0.0)
        self.assertTrue(double_validator0.isStrict())
        self.assertFalse(boolean0)
        self.assertEqual(0, double_validator0.getFormatType())

    def test27(self) -> None:
        doubleValidator0 = DoubleValidator.getInstance()
        double0 = 1991.6069853998
        boolean0 = doubleValidator0.isInRange1(double0, 882.9135857012346, 2)
        self.assertFalse(boolean0)

    def test26(self) -> None:
        doubleValidator0 = DoubleValidator.getInstance()
        double0 = float(1)
        boolean0 = doubleValidator0.isInRange1(double0, 1, 2)
        self.assertTrue(boolean0)

    def test25(self) -> None:
        double_validator0 = DoubleValidator.DoubleValidator1()
        boolean0 = double_validator0.minValue0(0, 2)
        self.assertTrue(double_validator0.isStrict())
        self.assertFalse(boolean0)
        self.assertEqual(0, double_validator0.getFormatType())

    def test24(self) -> None:
        doubleValidator0 = DoubleValidator.getInstance()
        boolean0 = doubleValidator0.minValue0(0.0, 0.0)
        self.assertTrue(boolean0)

    def test23(self) -> None:
        double_validator0 = DoubleValidator.DoubleValidator1()
        boolean0 = double_validator0.maxValue0(213.570476998, 0.0)
        self.assertEqual(0, double_validator0.getFormatType())
        self.assertFalse(boolean0)
        self.assertTrue(double_validator0.isStrict())

    def test22(self) -> None:

        doubleValidator0 = DoubleValidator.getInstance()
        dateFormat0 = DateFormat.getInstance()
        object0 = doubleValidator0.processParsedValue(
            doubleValidator0.PERCENT_FORMAT, dateFormat0
        )
        object1 = doubleValidator0.processParsedValue(object0, dateFormat0)
        self.assertEqual(2.0, object1)

    def test21(self) -> None:
        double_validator0 = DoubleValidator.DoubleValidator1()
        boolean0 = double_validator0.isInRange0(0.0, 0.0, 213.570476998)
        self.assertTrue(boolean0)
        self.assertTrue(double_validator0.isStrict())
        self.assertEqual(0, double_validator0.getFormatType())

    def test20(self) -> None:
        double_validator0 = DoubleValidator.DoubleValidator1()
        boolean0 = double_validator0.isInRange0(864.5, 307.834243566, 0.0)
        self.assertFalse(boolean0)
        self.assertTrue(double_validator0.isStrict())
        self.assertEqual(0, double_validator0.getFormatType())

    def test19(self) -> None:

        doubleValidator0 = DoubleValidator.DoubleValidator1()
        mockSimpleDateFormat0 = MockSimpleDateFormat()

        with pytest.raises(TypeError):
            doubleValidator0.processParsedValue(doubleValidator0, mockSimpleDateFormat0)
            verifyException(
                "org.apache.commons.validator.routines.DoubleValidator", TypeError
            )

    def test18(self) -> None:

        double_validator0 = DoubleValidator.DoubleValidator1()
        locale0 = Locale.JAPAN
        date_format0 = MockDateFormat.getTimeInstance(2, locale0)

        with self.assertRaises(RuntimeError):
            double_validator0.processParsedValue(None, date_format0)

    def test17(self) -> None:

        double_validator0 = DoubleValidator.DoubleValidator1()
        # Undeclared exception in Java code
        try:
            double_validator0.validate1("'~<pJHYE0", "'~<pJHYE0")
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # Malformed pattern \"'~<pJHYE0\"
            self.verifyException("java.text.DecimalFormat", e)

    def test16(self) -> None:

        doubleValidator0 = DoubleValidator.DoubleValidator1()
        locale0 = Locale.ENGLISH
        # Undeclared exception in Java code
        try:
            doubleValidator0.validate3(
                "org.apache.commons.validator.routines.AbstractNumberValidator",
                "org.apache.commons.validator.routines.AbstractNumberValidator",
                locale0,
            )
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # Multiple decimal separators in pattern \"org.apache.commons.validator.routines.AbstractNumberValidator\"
            self.verifyException("java.text.DecimalFormat", e)

    def test15(self) -> None:
        doubleValidator0 = DoubleValidator.DoubleValidator1()
        double0 = float(2)
        boolean0 = doubleValidator0.maxValue1(double0, 0)
        self.assertTrue(doubleValidator0.isStrict())
        self.assertFalse(boolean0)
        self.assertEqual(0, doubleValidator0.getFormatType())

    def test14(self) -> None:
        doubleValidator0 = DoubleValidator.DoubleValidator1()
        double0 = float(0.0)
        boolean0 = doubleValidator0.maxValue1(double0, 3324.960294223781)
        self.assertTrue(boolean0)
        self.assertTrue(doubleValidator0.isStrict())
        self.assertEqual(0, doubleValidator0.getFormatType())

    def test13(self) -> None:
        doubleValidator0 = DoubleValidator.DoubleValidator1()
        double0 = -1521.473492029
        boolean0 = doubleValidator0.minValue1(double0, 1.0)
        self.assertTrue(doubleValidator0.isStrict())
        self.assertFalse(boolean0)
        self.assertEqual(0, doubleValidator0.getFormatType())

    def test12(self) -> None:
        doubleValidator0 = DoubleValidator(False, 0)
        double0 = float(2)
        boolean0 = doubleValidator0.minValue1(double0, 0)
        self.assertTrue(boolean0)

    def test11(self) -> None:

        doubleValidator0 = DoubleValidator.DoubleValidator1()
        doubleValidator0.validate0("")
        self.assertEqual(0, doubleValidator0.getFormatType())
        self.assertTrue(doubleValidator0.isStrict())

    def test10(self) -> None:

        doubleValidator0 = DoubleValidator(True, 2888)
        double0 = doubleValidator0.validate0("2")
        self.assertAlmostEqual(2.0, double0, delta=0.01)

    def test09(self) -> None:

        doubleValidator0 = DoubleValidator.getInstance()
        double0 = doubleValidator0.validate0("0")
        self.assertAlmostEqual(0.0, double0, delta=0.01)

    def test08(self) -> None:

        doubleValidator0 = DoubleValidator.DoubleValidator1()
        doubleValidator0.validate1("", "")
        self.assertTrue(doubleValidator0.isStrict())
        self.assertEqual(0, doubleValidator0.getFormatType())

    def test07(self) -> None:

        doubleValidator0 = DoubleValidator.getInstance()
        double0 = doubleValidator0.validate1("Nu1", "Nu")
        self.assertAlmostEqual(1.0, double0, delta=0.01)

    def test06(self) -> None:

        doubleValidator0 = DoubleValidator.DoubleValidator1()
        doubleValidator0.validate1("MkQ0}", "MkQ0}")
        self.assertEqual(0, doubleValidator0.getFormatType())
        self.assertTrue(doubleValidator0.isStrict())

    def test05(self) -> None:

        doubleValidator0 = DoubleValidator.getInstance()
        locale0 = Locale.JAPAN
        double0 = doubleValidator0.validate2("5", locale0)
        self.assertAlmostEqual(5.0, double0, delta=0.01)

    def test04(self) -> None:

        doubleValidator0 = DoubleValidator.DoubleValidator1()
        locale0 = Locale.ITALY
        double0 = doubleValidator0.validate3("-1.073.741.824", "", locale0)
        self.assertIsNotNone(double0)
        self.assertTrue(doubleValidator0.isStrict())

    def test03(self) -> None:

        doubleValidator0 = DoubleValidator.getInstance()
        locale0 = Locale.ENGLISH
        double0 = doubleValidator0.validate3("8", "", locale0)
        self.assertAlmostEqual(8.0, double0, delta=0.01)

    def test02(self) -> None:

        doubleValidator0 = DoubleValidator(False, 2143154043)
        locale0 = Locale("-NBXjFQf60;`31{", "-NBXjFQf60;`31{", "-NBXjFQf60;`31{")
        double0 = doubleValidator0.validate3(
            "-NBXjFQf60;`31{", "-NBXjFQf60;`31{", locale0
        )
        self.assertAlmostEqual(0.0, double0, delta=0.01)

    def test01(self) -> None:
        double_validator0 = DoubleValidator.DoubleValidator1()
        boolean0 = double_validator0.isInRange0(1, 1, 1)
        self.assertTrue(boolean0)
        self.assertEqual(0, double_validator0.getFormatType())
        self.assertTrue(double_validator0.isStrict())

    def test00(self) -> None:
        double_validator0 = DoubleValidator.DoubleValidator1()
        boolean0 = double_validator0.maxValue0(0.0, 0.0)
        self.assertEqual(0, double_validator0.getFormatType())
        self.assertTrue(boolean0)
        self.assertTrue(double_validator0.isStrict())
