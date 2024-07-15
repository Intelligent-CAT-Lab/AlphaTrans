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
from src.main.org.apache.commons.validator.routines.IntegerValidator import *

# from src.test.org.apache.commons.validator.routines.IntegerValidator_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class IntegerValidator_ESTest(unittest.TestCase):

    def test32(self) -> None:

        integerValidator0 = IntegerValidator.IntegerValidator1()
        integer0 = integerValidator0.validate1("-7", "")
        self.assertEqual(-7, integer0)
        self.assertTrue(integerValidator0.isStrict())
        self.assertIsNotNone(integer0)

    def test31(self) -> None:
        integerValidator0 = IntegerValidator.getInstance()
        boolean0 = integerValidator0.isInRange0((-3978), 201, 0)
        self.assertFalse(boolean0)

    def test30(self) -> None:

        integerValidator0 = IntegerValidator(False, 1000)
        locale0 = Locale.CANADA_FRENCH
        integer0 = integerValidator0.validate3("4M", "", locale0)
        self.assertIsNotNone(integer0)
        self.assertEqual(4, integer0)

    def test29(self) -> None:

        integerValidator0 = IntegerValidator(True, -1148)
        boolean0 = integerValidator0.maxValue1(integerValidator0.STANDARD_FORMAT, 646)
        self.assertTrue(boolean0)

    def test28(self) -> None:

        integerValidator0 = IntegerValidator(False, 1000)
        integer0 = integerValidator0.validate0("4M")
        self.assertIsNotNone(integer0)
        self.assertEqual(4, integer0)

    def test27(self) -> None:

        integerValidator0 = IntegerValidator(True, 589)
        boolean0 = integerValidator0.minValue1(integerValidator0.PERCENT_FORMAT, 3113)
        self.assertFalse(boolean0)

    def test26(self) -> None:

        integerValidator0 = IntegerValidator.IntegerValidator1()
        locale0 = Locale.CHINESE
        integer0 = integerValidator0.validate2("-7", locale0)
        self.assertEqual(-7, integer0)
        self.assertTrue(integerValidator0.isStrict())
        self.assertIsNotNone(integer0)

    def test25(self) -> None:

        integerValidator0 = IntegerValidator.IntegerValidator1()
        integer0 = Integer(0)
        boolean0 = integerValidator0.isInRange1(integer0, 0, 0)
        self.assertTrue(boolean0)
        self.assertTrue(integerValidator0.isStrict())
        self.assertEqual(0, integerValidator0.getFormatType())

    def test24(self) -> None:
        integerValidator0 = IntegerValidator.getInstance()
        boolean0 = integerValidator0.minValue0(0, -3978)
        self.assertTrue(boolean0)

    def test23(self) -> None:

        integerValidator0 = IntegerValidator.getInstance()
        boolean0 = integerValidator0.maxValue0(0, (-3911))
        self.assertFalse(boolean0)

    def test22(self) -> None:

        integerValidator0 = IntegerValidator.getInstance()
        dateFormat0 = MockDateFormat.getDateInstance(2)
        object0 = integerValidator0.processParsedValue(
            integerValidator0.STANDARD_FORMAT, dateFormat0
        )
        self.assertIsNone(object0)

    def test21(self) -> None:

        integerValidator0 = IntegerValidator(True, 589)
        boolean0 = integerValidator0.isInRange0(0, -1660, 174)
        self.assertTrue(boolean0)

    def test20(self) -> None:
        integerValidator0 = IntegerValidator(False, 0)
        boolean0 = integerValidator0.isInRange0(2, 1, 0)
        self.assertFalse(boolean0)

    def test19(self) -> None:

        integerValidator0 = IntegerValidator(False, -539)
        boolean0 = integerValidator0.minValue0(-539, 0)
        self.assertFalse(boolean0)

    def test18(self) -> None:

        integerValidator0 = IntegerValidator(True, 589)
        boolean0 = integerValidator0.maxValue0(3113, 3113)
        self.assertTrue(boolean0)

    def test17(self) -> None:

        integer_validator0 = IntegerValidator.IntegerValidator1()

        with self.assertRaises(RuntimeError):
            integer_validator0.isInRange1(None, -3461, -3461)

    def test16(self) -> None:

        integerValidator0 = IntegerValidator(False, -539)

        with pytest.raises(RuntimeError):
            integerValidator0.maxValue1(None, 0)

    def test15(self) -> None:

        integerValidator0 = IntegerValidator.IntegerValidator1()
        # Undeclared exception in Java code
        try:
            integerValidator0.minValue1(None, 0)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            # no message in exception (getMessage() returned null)
            self.verifyException(
                "org.apache.commons.validator.routines.IntegerValidator", e
            )

    def test14(self) -> None:

        integerValidator0 = IntegerValidator.getInstance()
        # Undeclared exception
        try:
            integerValidator0.validate1("`WUV*_<,j", "`WUV*_<,j")
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # Malformed pattern \"`WUV*_<,j\"
            self.verifyException("java.text.DecimalFormat", e)

    def test13(self) -> None:

        integerValidator0 = IntegerValidator.IntegerValidator1()
        locale0 = Locale.TAIWAN
        # Undeclared exception in Java code
        try:
            integerValidator0.validate3(
                "org.apache.commons.validator.routines.IntegerValidator",
                "org.apache.commons.validator.routines.IntegerValidator",
                locale0,
            )
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # Multiple decimal separators in pattern \"org.apache.commons.validator.routines.IntegerValidator\"
            self.verifyException("java.text.DecimalFormat", e)

    def test12(self) -> None:
        integerValidator0 = IntegerValidator.IntegerValidator1()
        boolean0 = integerValidator0.maxValue1(integerValidator0.PERCENT_FORMAT, 0)
        self.assertFalse(boolean0)
        self.assertTrue(integerValidator0.isStrict())
        self.assertEqual(0, integerValidator0.getFormatType())

    def test11(self) -> None:
        integerValidator0 = IntegerValidator.IntegerValidator1()
        boolean0 = integerValidator0.minValue1(integerValidator0.STANDARD_FORMAT, 0)
        self.assertTrue(integerValidator0.isStrict())
        self.assertTrue(boolean0)
        self.assertEqual(0, integerValidator0.getFormatType())

    def test10(self) -> None:

        integerValidator0 = IntegerValidator.getInstance()
        integer0 = integerValidator0.validate0("")
        self.assertIsNone(integer0)

    def test09(self) -> None:

        integerValidator0 = IntegerValidator.IntegerValidator1()
        integer0 = integerValidator0.validate0("0")
        assert integer0 is not None
        assert integerValidator0.isStrict()

    def test08(self) -> None:

        integerValidator0 = IntegerValidator.IntegerValidator1()
        integerValidator0.validate1("", "")
        self.assertEqual(0, integerValidator0.getFormatType())
        self.assertTrue(integerValidator0.isStrict())

    def test07(self) -> None:

        integerValidator0 = IntegerValidator(False, -927)
        integer0 = integerValidator0.validate1("2JQ7|2R m%", "")
        self.assertIsNotNone(integer0)
        self.assertEqual(2, int(integer0))

    def test06(self) -> None:

        integerValidator0 = IntegerValidator.getInstance()
        integer0 = integerValidator0.validate1("Z0Omz", "Z0Omz")
        self.assertEqual(0, integer0)

    def test05(self) -> None:

        integer_validator0 = IntegerValidator.IntegerValidator1()
        locale0 = Locale.GERMAN
        integer_validator0.validate2("jz'YeX0UKq0+,9i9N", locale0)
        self.assertEqual(0, integer_validator0.getFormatType())
        self.assertTrue(integer_validator0.isStrict())

    def test04(self) -> None:

        integerValidator0 = IntegerValidator.getInstance()
        locale0 = Locale.GERMANY
        integer0 = integerValidator0.validate2("9", locale0)
        self.assertIsNotNone(integer0)
        self.assertEqual(9, integer0)

    def test03(self) -> None:

        integerValidator0 = IntegerValidator.IntegerValidator1()
        locale0 = Locale.SIMPLIFIED_CHINESE
        integer0 = integerValidator0.validate2("0", locale0)
        self.assertIsNotNone(integer0)
        self.assertTrue(integerValidator0.isStrict())

    def test02(self) -> None:

        integerValidator0 = IntegerValidator.getInstance()
        locale0 = Locale.US
        integer0 = integerValidator0.validate3(None, None, locale0)
        self.assertIsNone(integer0)

    def test01(self) -> None:

        integerValidator0 = IntegerValidator.getInstance()
        locale0 = Locale.TAIWAN
        integer0 = integerValidator0.validate3(
            "xF0kV4gD7PJX9J", "xF0kV4gD7PJX9J", locale0
        )
        self.assertEqual(0, integer0)

    def test00(self) -> None:

        integer_validator0 = IntegerValidator.IntegerValidator1()
        boolean0 = integer_validator0.isInRange1(1, 1, -855)
        self.assertTrue(integer_validator0.isStrict())
        self.assertFalse(boolean0)
        self.assertEqual(0, integer_validator0.getFormatType())
