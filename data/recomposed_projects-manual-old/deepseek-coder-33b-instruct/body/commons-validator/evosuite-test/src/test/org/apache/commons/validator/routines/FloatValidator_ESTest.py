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
from src.main.org.apache.commons.validator.routines.FloatValidator import *

# from src.test.org.apache.commons.validator.routines.FloatValidator_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class FloatValidator_ESTest(unittest.TestCase):

    def test33(self) -> None:
        floatValidator0 = FloatValidator.getInstance()
        float0 = float(0)
        boolean0 = floatValidator0.maxValue1(float0, 0.0)
        self.assertTrue(boolean0)

    def test32(self) -> None:

        float_validator0 = FloatValidator.FloatValidator1()
        locale0 = Locale.GERMAN
        float0 = float_validator0.validate3("", "<r=", locale0)

        with pytest.raises(RuntimeError):
            float_validator0.isInRange1(float0, 2, (-3031.87))
            verifyException(
                "org.apache.commons.validator.routines.FloatValidator", RuntimeError
            )

    def test31(self) -> None:

        floatValidator0 = FloatValidator(False, 1551)
        float0 = floatValidator0.validate1('-6"6zi#Y1gvA\f1+', "")
        self.assertAlmostEqual(-6.0, float0, delta=0.01)
        self.assertIsNotNone(float0)

    def test30(self) -> None:

        float_validator0 = FloatValidator(False, 2)
        float0 = float_validator0.validate0("-141,900%")
        self.assertIsNotNone(float0)
        self.assertAlmostEqual(-1419.0, float0, delta=0.01)

    def test29(self) -> None:

        floatValidator0 = FloatValidator(False, 2)
        locale0 = Locale.ITALY
        float0 = floatValidator0.validate2("K#u*bjc>|A", locale0)
        self.assertIsNone(float0)

    def test28(self) -> None:
        floatValidator0 = FloatValidator.getInstance()
        float0 = float(0)
        boolean0 = floatValidator0.minValue1(float0, -2085.01)
        self.assertTrue(boolean0)

    def test27(self) -> None:
        float_validator0 = FloatValidator.FloatValidator1()
        boolean0 = float_validator0.isInRange0((-646.1517), 914.7, (-646.1517))
        self.assertTrue(float_validator0.isStrict())
        self.assertFalse(boolean0)
        self.assertEqual(0, float_validator0.getFormatType())

    def test26(self) -> None:
        float_validator0 = FloatValidator.FloatValidator1()
        boolean0 = float_validator0.isInRange0(3248, 0.0, -1865.69)
        self.assertTrue(float_validator0.isStrict())
        self.assertFalse(boolean0)
        self.assertEqual(0, float_validator0.getFormatType())

    def test25(self) -> None:
        floatValidator0 = FloatValidator(True, 1737)
        boolean0 = floatValidator0.minValue0((-3946.0972), (-1.0))
        self.assertFalse(boolean0)

    def test24(self) -> None:
        float0 = float(430.0439)
        floatValidator0 = FloatValidator.getInstance()
        boolean0 = floatValidator0.maxValue1(float0, 0.0)
        self.assertFalse(boolean0)

    def test23(self) -> None:

        floatValidator0 = FloatValidator(False, -198)
        locale0 = Locale.FRANCE
        float0 = floatValidator0.validate3('4[^"Z_V=', "", locale0)
        self.assertIsNotNone(float0)
        self.assertAlmostEqual(4.0, float0, delta=0.01)

    def test22(self) -> None:

        floatValidator0 = FloatValidator(True, -2069)
        float0 = floatValidator0.validate2("0", None)
        assert float0 is not None
        self.assertAlmostEqual(0.0, float0, delta=0.01)

    def test21(self) -> None:
        floatValidator0 = FloatValidator(True, 1737)
        boolean0 = floatValidator0.minValue0(0.0, 0.0)
        self.assertTrue(boolean0)

    def test20(self) -> None:
        floatValidator0 = FloatValidator(False, -1442)
        boolean0 = floatValidator0.maxValue0(0.0, -869.225)
        self.assertFalse(boolean0)

    def test19(self) -> None:
        floatValidator0 = FloatValidator(True, 1737)
        boolean0 = floatValidator0.maxValue0(0.0, 653.31464)
        self.assertTrue(boolean0)

    def test18(self) -> None:

        float_validator0 = FloatValidator.getInstance()
        try:
            float_validator0.maxValue1(None, -711.0)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.assertEqual(str(e), "RuntimeError")
            self.verifyException(
                "org.apache.commons.validator.routines.FloatValidator", e
            )

    def test17(self) -> None:

        floatValidator0 = FloatValidator.getInstance()
        decimalFormat0 = DecimalFormat()

        with pytest.raises(TypeError):
            floatValidator0.processParsedValue(decimalFormat0, decimalFormat0)
            self.fail("Expecting exception: TypeError")

        verifyException(
            "org.apache.commons.validator.routines.FloatValidator", TypeError
        )

    def test16(self) -> None:

        floatValidator0 = FloatValidator.getInstance()

        with self.assertRaises(RuntimeError):
            floatValidator0.processParsedValue(None, None)

    def test15(self) -> None:

        floatValidator0 = FloatValidator.FloatValidator1()
        # Undeclared exception in Java code
        try:
            floatValidator0.validate1(
                "org.apache.commons.validator.routines.AbstractFormatValidator",
                "org.apache.commons.validator.routines.AbstractFormatValidator",
            )
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # Multiple decimal separators in pattern \"org.apache.commons.validator.routines.AbstractFormatValidator\"
            self.verifyException("java.text.DecimalFormat", e)

    def test14(self) -> None:

        float_validator0 = FloatValidator.FloatValidator1()
        locale0 = Locale.FRANCE
        # Undeclared exception in Java code
        try:
            float_validator0.validate3("F'G.", "F'G.", locale0)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # Malformed pattern \"F'G.\"
            self.verifyException("java.text.DecimalFormat", e)

    def test13(self) -> None:

        float0 = float(0.0)
        floatValidator0 = FloatValidator.FloatValidator1()
        boolean0 = floatValidator0.isInRange1(
            float0, float(-978.07104), float(-107.714)
        )
        self.assertEqual(0, floatValidator0.getFormatType())
        self.assertTrue(floatValidator0.isStrict())
        self.assertFalse(boolean0)

    def test12(self) -> None:

        float0 = float(0.0)
        floatValidator0 = FloatValidator.FloatValidator1()
        boolean0 = floatValidator0.isInRange1(float0, 0.0, 0.0)
        self.assertEqual(0, floatValidator0.getFormatType())
        self.assertTrue(boolean0)
        self.assertTrue(floatValidator0.isStrict())

    def test11(self) -> None:
        float_validator0 = FloatValidator.FloatValidator1()
        float0 = float(0)
        boolean0 = float_validator0.minValue1(float0, 2324.5425)
        self.assertTrue(float_validator0.isStrict())
        self.assertEqual(0, float_validator0.getFormatType())
        self.assertFalse(boolean0)

    def test10(self) -> None:

        floatValidator0 = FloatValidator.FloatValidator1()
        floatValidator0.validate0(
            "org.apache.commons.validator.routines.AbstractFormatValidator"
        )
        self.assertTrue(floatValidator0.isStrict())
        self.assertEqual(0, floatValidator0.getFormatType())

    def test09(self) -> None:

        floatValidator0 = FloatValidator(False, 0)
        float0 = floatValidator0.validate0("3qjX3d<,g")
        assert float0 is not None
        self.assertAlmostEqual(3.0, float0, delta=0.01)

    def test08(self) -> None:

        floatValidator0 = FloatValidator(False, -1)
        float0 = floatValidator0.validate0(",0L")
        assert float0 is not None
        self.assertAlmostEqual(0.0, float0, delta=0.01)

    def test07(self) -> None:

        floatValidator0 = FloatValidator(True, 0)
        float0 = floatValidator0.validate1("", "")
        self.assertIsNone(float0)

    def test06(self) -> None:

        float_validator0 = FloatValidator.FloatValidator1()
        float0 = float_validator0.validate1("7", "")
        self.assertIsNotNone(float0)
        self.assertAlmostEqual(7.0, float0, delta=0.01)
        self.assertTrue(float_validator0.isStrict())

    def test05(self) -> None:

        floatValidator0 = FloatValidator.getInstance()
        float0 = floatValidator0.validate1("maOo4 0tqozKRq[", "maOo4 0tqozKRq[")
        self.assertAlmostEqual(0.0, float0, delta=0.01)
        self.assertIsNotNone(float0)

    def test04(self) -> None:

        floatValidator0 = FloatValidator(False, 2)
        locale0 = Locale.ITALY
        float0 = floatValidator0.validate2("-141,900%", locale0)
        self.assertIsNotNone(float0)
        self.assertAlmostEqual(-1.419, float0, delta=0.01)

    def test03(self) -> None:

        float_validator0 = FloatValidator(True, -100)
        locale0 = Locale.JAPAN
        float0 = float_validator0.validate2("2", locale0)
        self.assertAlmostEqual(2.0, float0, delta=0.01)
        self.assertIsNotNone(float0)

    def test02(self) -> None:

        float_validator0 = FloatValidator.getInstance()
        locale0 = Locale.US
        float0 = float_validator0.validate3(
            "maOo4 0tqozKRq[", "maOo4 0tqozKRq[", locale0
        )
        self.assertAlmostEqual(0.0, float0, delta=0.01)
        self.assertIsNotNone(float0)

    def test01(self) -> None:

        float_validator0 = FloatValidator.FloatValidator1()
        decimal_format0 = DecimalFormat()
        object0 = float_validator0.processParsedValue(0, decimal_format0)
        self.assertTrue(float_validator0.isStrict())
        self.assertEqual(0.0, object0)
        self.assertIsNotNone(object0)
        self.assertEqual(0, float_validator0.getFormatType())

    def test00(self) -> None:
        floatValidator0 = FloatValidator(True, 871)
        boolean0 = floatValidator0.isInRange0(871, 871, 4479.0)
        self.assertTrue(boolean0)
