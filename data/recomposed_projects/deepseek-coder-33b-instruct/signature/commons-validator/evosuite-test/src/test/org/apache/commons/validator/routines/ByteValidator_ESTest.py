from __future__ import annotations
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
from src.main.org.apache.commons.validator.routines.ByteValidator import *

# from src.test.org.apache.commons.validator.routines.ByteValidator_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class ByteValidator_ESTest(unittest.TestCase):

    def test35(self) -> None:

        byteValidator0 = ByteValidator.ByteValidator1()
        byte0 = byteValidator0.validate0("-128")
        assert byteValidator0.isStrict()
        assert byte0 is not None

    def test34(self) -> None:
        byteValidator0 = ByteValidator.getInstance()
        byte0 = -1
        boolean0 = byteValidator0.minValue1(byte0, -13)
        self.assertTrue(boolean0)

    def test33(self) -> None:

        byte_validator0 = ByteValidator(False, -3687)
        byte0 = byte_validator0.validate2("-1<qtb=o|", None)
        assert byte0 is not None
        assert byte0 == -1

    def test32(self) -> None:

        byte_validator0 = ByteValidator.ByteValidator1()
        # Undeclared exception in Java code
        try:
            byte_validator0.isInRange1(None, 0, 0)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            # no message in exception (getMessage() returned null)
            self.verifyException(
                "org.apache.commons.validator.routines.ByteValidator", e
            )

    def test31(self) -> None:
        byteValidator0 = ByteValidator(False, -1677)
        byte0 = bytes([1])
        boolean0 = byteValidator0.maxValue1(byte0, -17)
        self.assertFalse(boolean0)

    def test30(self) -> None:

        byte_validator0 = ByteValidator(False, -20)
        byte0 = byte_validator0.validate1("-1<qtb=o|", "")
        assert byte0 is not None
        assert byte0 == -1

    def test29(self) -> None:

        byteValidator0 = ByteValidator(False, -20)
        byte0 = byteValidator0.validate3(
            "org.apache.commons.validator.routines.AbstractFormatValidator",
            "i-.",
            None,
        )
        self.assertIsNone(byte0)

    def test28(self) -> None:

        byte_validator0 = ByteValidator.ByteValidator1()
        boolean0 = byte_validator0.isInRange0(0, 1, 0)
        self.assertTrue(byte_validator0.isStrict())
        self.assertEqual(0, byte_validator0.getFormatType())
        self.assertFalse(boolean0)

    def test27(self) -> None:

        byte_validator0 = ByteValidator.ByteValidator1()
        boolean0 = byte_validator0.isInRange0(1, 1, 0)
        self.assertTrue(byte_validator0.isStrict())
        self.assertFalse(boolean0)
        self.assertEqual(0, byte_validator0.getFormatType())

    def test26(self) -> None:
        byteValidator0 = ByteValidator.getInstance()
        byte0 = -1
        boolean0 = byteValidator0.minValue1(byte0, 78)
        self.assertFalse(boolean0)

    def test25(self) -> None:
        byteValidator0 = ByteValidator.getInstance()
        byte0 = -1
        boolean0 = byteValidator0.maxValue1(byte0, 43)
        self.assertTrue(boolean0)

    def test24(self) -> None:

        byteValidator0 = ByteValidator.getInstance()
        locale0 = Locale.CHINA
        decimalFormatSymbols0 = DecimalFormatSymbols(locale0)
        decimalFormat0 = DecimalFormat("802IsgFZlJ9", decimalFormatSymbols0)
        object0 = byteValidator0.processParsedValue(locale0, decimalFormat0)
        self.assertIsNone(object0)

    def test23(self) -> None:

        byteValidator0 = ByteValidator(False, -957)
        byte0 = byteValidator0.validate0("-150yqtz-7")
        self.assertIsNone(byte0)

    def test22(self) -> None:

        byteValidator0 = ByteValidator(False, -937)
        byte0 = byteValidator0.validate0("97E9et")
        self.assertIsNone(byte0)

    def test21(self) -> None:
        byteValidator0 = ByteValidator.getInstance()
        boolean0 = byteValidator0.minValue0(0, 56)
        self.assertFalse(boolean0)

    def test20(self) -> None:
        byteValidator0 = ByteValidator(True, 3901)
        boolean0 = byteValidator0.minValue0(-4, -4)
        self.assertTrue(boolean0)

    def test19(self) -> None:
        byteValidator0 = ByteValidator.ByteValidator1()
        boolean0 = byteValidator0.maxValue0(1, -20)
        self.assertTrue(byteValidator0.isStrict())
        self.assertEqual(0, byteValidator0.getFormatType())
        self.assertFalse(boolean0)

    def test18(self) -> None:
        byteValidator0 = ByteValidator.ByteValidator1()
        boolean0 = byteValidator0.maxValue0(-65, -65)
        self.assertEqual(0, byteValidator0.getFormatType())
        self.assertTrue(byteValidator0.isStrict())
        self.assertTrue(boolean0)

    def test17(self) -> None:
        byteValidator0 = ByteValidator.getInstance()
        with pytest.raises(RuntimeError):
            byteValidator0.maxValue1(None, 27)

    def test16(self) -> None:
        byteValidator0 = ByteValidator.getInstance()
        try:
            byteValidator0.minValue1(None, 29)
            self.fail("Expecting exception: RuntimeError")
        except RuntimeError as e:
            verifyException("org.apache.commons.validator.routines.ByteValidator", e)

    def test15(self) -> None:

        byteValidator0 = ByteValidator.getInstance()
        # Undeclared exception in Java code
        try:
            byteValidator0.validate1("hRM ;v/%p;yL", "hRM ;v/%p;yL")
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # Unquoted special character ';' in pattern \"hRM ;v/%p;yL\"
            self.verifyException("java.text.DecimalFormat", e)

    def test14(self) -> None:

        byteValidator0 = ByteValidator.ByteValidator1()
        locale0 = Locale.SIMPLIFIED_CHINESE
        # Undeclared exception in Java code
        try:
            byteValidator0.validate3(
                "org.apache.commons.validator.routines.AbstractNumberValidator",
                "org.apache.commons.validator.routines.AbstractNumberValidator",
                locale0,
            )
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # Multiple decimal separators in pattern \"org.apache.commons.validator.routines.AbstractNumberValidator\"
            self.verifyException("java.text.DecimalFormat", e)

    def test13(self) -> None:

        byteValidator0 = ByteValidator.getInstance()
        byte0 = b"\x68"
        boolean0 = byteValidator0.isInRange1(byte0, b"\x01", b"\x00")
        self.assertFalse(boolean0)

    def test12(self) -> None:

        byte_validator0 = ByteValidator.ByteValidator1()
        byte0 = -90
        boolean0 = byte_validator0.isInRange1(byte0, -90, -9)
        self.assertTrue(byte_validator0.isStrict())
        self.assertEqual(0, byte_validator0.getFormatType())
        self.assertTrue(boolean0)

    def test11(self) -> None:

        byteValidator0 = ByteValidator(False, -20)
        byte0 = byteValidator0.validate0("0?f,`I")
        self.assertEqual(0, byte0)

    def test10(self) -> None:

        byteValidator0 = ByteValidator.getInstance()
        byte0 = byteValidator0.validate1("ylUG[hc |a", "ylUG[hc |a")
        self.assertIsNone(byte0)

    def test09(self) -> None:

        byte_validator0 = ByteValidator.ByteValidator1()
        byte0 = byte_validator0.validate1(" 7", None)
        self.assertEqual(7, byte0)
        self.assertIsNotNone(byte0)
        self.assertTrue(byte_validator0.isStrict())

    def test08(self) -> None:

        byte_validator0 = ByteValidator.ByteValidator1()
        byte0 = byte_validator0.validate1("hXtgcg9W`W0}", "hXtgcg9W`W0}")
        self.assertEqual(0, byte_validator0.getFormatType())
        self.assertIsNotNone(byte0)
        self.assertTrue(byte_validator0.isStrict())

    def test07(self) -> None:

        byte_validator0 = ByteValidator.ByteValidator1()
        locale0 = Locale.TRADITIONAL_CHINESE
        byte_validator0.validate2(
            "org.apache.commons.validator.routines.ByteValidator", locale0
        )
        self.assertEqual(0, byte_validator0.getFormatType())
        self.assertTrue(byte_validator0.isStrict())

    def test06(self) -> None:

        byteValidator0 = ByteValidator(False, -1677)
        locale0 = Locale.TAIWAN
        byte0 = byteValidator0.validate2("1", locale0)
        self.assertIsNotNone(byte0)
        self.assertEqual(1, byte0)

    def test05(self) -> None:

        locale0 = Locale.ITALY
        byteValidator0 = ByteValidator(False, -2665)
        byte0 = byteValidator0.validate2('0tdXImsg"Zp', locale0)
        self.assertEqual(0, byte0)

    def test04(self) -> None:

        byteValidator0 = ByteValidator(False, -3687)
        locale0 = Locale.CHINA
        byte0 = byteValidator0.validate3("-1<qtb=o|", "", locale0)
        self.assertEqual(-1, byte0)
        self.assertIsNotNone(byte0)

    def test03(self) -> None:

        byteValidator0 = ByteValidator(False, -1677)
        locale0 = Locale.TAIWAN
        byte0 = byteValidator0.validate3("1", "", locale0)
        self.assertIsNotNone(byte0)
        self.assertEqual(1, byte0)

    def test02(self) -> None:

        byte_validator0 = ByteValidator.ByteValidator1()
        locale0 = Locale.CHINA
        byte0 = byte_validator0.validate3("80?ImsgFZlJ9", "80?ImsgFZlJ9", locale0)
        self.assertTrue(byte_validator0.isStrict())
        self.assertIsNotNone(byte0)
        self.assertEqual(0, byte_validator0.getFormatType())

    def test01(self) -> None:

        byte_validator0 = ByteValidator.ByteValidator1()
        boolean0 = byte_validator0.isInRange0(-84, -84, -84)
        self.assertTrue(byte_validator0.isStrict())
        self.assertEqual(0, byte_validator0.getFormatType())
        self.assertTrue(boolean0)

    def test00(self) -> None:

        byteValidator0 = ByteValidator.getInstance()
        byte0 = byteValidator0.validate0("127")
        assert byte0 is not None
        assert byte0 == b"\x7f"
