from __future__ import annotations
import time
import re
import os
import typing
from typing import *
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.codec.binary.StringUtils import *

# from src.test.org.apache.commons.codec.binary.StringUtils_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class StringUtils_ESTest(unittest.TestCase):

    def test49(self) -> None:

        byteArray0 = StringUtils.getBytesUtf16Be(
            "org.apache.commons.codec.binary.CharSequenceUtils"
        )
        self.assertEqual(98, len(byteArray0))

    def test48(self) -> None:
        try:
            StringUtils.getBytesUnchecked(
                "", "org.apache.commons.codec.binary.StringUtils"
            )
            self.fail("Expecting exception: RuntimeError")
        except RuntimeError as e:
            verifyException("org.apache.commons.codec.binary.StringUtils", e)

    def test47(self) -> None:

        byteArray0 = StringUtils.getBytesUtf16Le("n8")
        string0 = StringUtils.newStringUsAscii(byteArray0)
        self.assertEqual("n\u00008\u0000", string0)

    def test46(self) -> None:

        byteArray0 = StringUtils.getBytesUtf16Le("n8")
        string0 = StringUtils.newStringIso8859_1(byteArray0)
        self.assertEqual("n\u00008\u0000", string0)

    def test45(self) -> None:

        byteArray0 = StringUtils.getBytesUsAscii(None)
        self.assertIsNone(byteArray0)

    def test44(self) -> None:
        string0 = StringUtils.newStringUtf16Le(None)
        self.assertIsNone(string0)

    def test43(self) -> None:

        byteArray0 = StringUtils.getBytesUtf16Le("n8")
        string0 = StringUtils.newStringUtf16Be(byteArray0)
        self.assertEqual("\u6E00\u3800", string0)

    def test42(self) -> None:

        byteArray0 = [0] * 11
        string0 = StringUtils.newStringUtf16(byteArray0)
        self.assertEqual("\u0000\u0000\u0000\u0000\u0000\uFFFD", string0)

    def test41(self) -> None:
        stringUtils0 = StringUtils()

    def test40(self) -> None:

        byteArray0 = StringUtils.getBytesIso8859_1("scS")
        self.assertEqual(byteArray0, [115, 99, 83])

    def test39(self) -> None:

        byteArray0 = StringUtils.getBytesUtf8("\uFFFD")
        self.assertEqual(byteArray0, [239, 191, 189])

    def test38(self) -> None:

        byteBuffer0 = StringUtils.getByteBufferUtf8("lHYy }zC?J#&[EU#4")
        self.assertEqual(0, byteBuffer0.position())

    def test37(self) -> None:

        byteArray0 = StringUtils.getBytesUtf16(
            "org.apache.commons.codec.binary.CharSequenceUtils"
        )
        self.assertEqual(100, len(byteArray0))

    def test36(self) -> None:
        string0 = StringUtils.newStringUtf8(None)
        self.assertIsNone(string0)

    def test35(self) -> None:

        charBuffer0 = "n8"
        boolean0 = StringUtils.equals(charBuffer0, "\u6E00\u3800")
        self.assertFalse(boolean0)

    def test34(self) -> None:

        boolean0 = StringUtils.equals("\uFFFD", "\uFFFD")
        self.assertTrue(boolean0)

    def test33(self) -> None:

        charBuffer0 = "p1..zU2sc"
        boolean0 = StringUtils.equals(None, charBuffer0)
        self.assertFalse(boolean0)

    def test32(self) -> None:

        boolean0 = StringUtils.equals("t", None)
        self.assertFalse(boolean0)

    def test31(self) -> None:

        charArray0 = ["\u0000"] * 4
        charBuffer0 = "".join(charArray0)
        boolean0 = StringUtils.equals(
            "\u0000\u0000\u0000\u0000\u0000\uFFFD", charBuffer0
        )
        self.assertFalse(boolean0)

    def test30(self) -> None:

        boolean0 = StringUtils.equals("gVVVAmed#(?:g6$k>%", "L/RhaZ5")
        self.assertFalse(boolean0)

    def test29(self) -> None:

        charBuffer0 = "p1p:{z*U2sc"
        boolean0 = StringUtils.equals("p1p:{z*U2sc", charBuffer0)
        self.assertTrue(boolean0)

    def test28(self) -> None:

        byteBuffer0 = StringUtils.getByteBufferUtf8(None)
        self.assertIsNone(byteBuffer0)

    def test27(self) -> None:
        byteArray0 = StringUtils.getBytesUnchecked(None, None)
        self.assertIsNone(byteArray0)

    def test26(self) -> None:
        byteArray0 = bytearray(0)
        try:
            StringUtils.newString1(byteArray0, " U?Cxe`>r")
            self.fail("Expecting exception: RuntimeError")
        except ValueError as e:
            self.verifyException("org.apache.commons.codec.binary.StringUtils", e)

    def test25(self) -> None:
        string0 = StringUtils.newString1(None, "")
        self.assertIsNone(string0)

    def test24(self) -> None:
        try:
            StringUtils.getBytesUnchecked(")6-mfS/n", None)
            self.fail("Expecting exception: RuntimeError")
        except TypeError:
            pass

    def test23(self) -> None:
        byteArray0 = bytearray(0)
        try:
            StringUtils.newString1(byteArray0, None)
            self.fail("Expecting exception: RuntimeError")
        except TypeError:
            pass

    def test22(self) -> None:

        byteArray0 = StringUtils.getBytesIso8859_1("")
        self.assertEqual(0, len(byteArray0))

    def test21(self) -> None:

        byteArray0 = StringUtils.getBytesIso8859_1(None)
        self.assertIsNone(byteArray0)

    def test20(self) -> None:

        byteArray0 = StringUtils.getBytesUsAscii("")
        string0 = StringUtils.newStringIso8859_1(byteArray0)
        self.assertEqual("", string0)

    def test19(self) -> None:

        byteArray0 = StringUtils.getBytesUsAscii(
            "org.apache.commons.codec.binary.StringUtils"
        )
        self.assertEqual(43, len(byteArray0))

    def test18(self) -> None:

        byteArray0 = StringUtils.getBytesUtf16("")
        self.assertEqual([], byteArray0)

    def test17(self) -> None:

        byteArray0 = StringUtils.getBytesUtf16(None)
        self.assertIsNone(byteArray0)

    def test16(self) -> None:

        byteArray0 = StringUtils.getBytesUtf16Be("")
        self.assertEqual(0, len(byteArray0))

    def test15(self) -> None:

        byteArray0 = StringUtils.getBytesUtf16Be(None)
        self.assertIsNone(byteArray0)

    def test14(self) -> None:

        byteArray0 = StringUtils.getBytesUtf16Le("")
        self.assertEqual([], byteArray0)

    def test13(self) -> None:

        byteArray0 = StringUtils.getBytesUtf16Le(None)
        self.assertIsNone(byteArray0)

    def test12(self) -> None:

        byteArray0 = StringUtils.getBytesUtf8("")
        string0 = StringUtils.newStringUsAscii(byteArray0)
        self.assertEqual("", string0)

    def test11(self) -> None:

        byteArray0 = StringUtils.getBytesUtf8(None)
        self.assertIsNone(byteArray0)

    def test10(self) -> None:
        string0 = StringUtils.newStringIso8859_1(None)
        self.assertIsNone(string0)

    def test09(self) -> None:
        string0 = StringUtils.newStringUsAscii(None)
        self.assertIsNone(string0)

    def test08(self) -> None:

        byteArray0 = StringUtils.getBytesUtf8("")
        string0 = StringUtils.newStringUtf16(byteArray0)
        self.assertEqual("", string0)

    def test07(self) -> None:
        string0 = StringUtils.newStringUtf16(None)
        self.assertIsNone(string0)

    def test06(self) -> None:
        byteArray0 = bytearray()
        string0 = StringUtils.newStringUtf16Be(byteArray0)
        self.assertEqual("", string0)

    def test05(self) -> None:
        string0 = StringUtils.newStringUtf16Be(None)
        self.assertIsNone(string0)

    def test04(self) -> None:

        byteArray0 = StringUtils.getBytesUtf8("")
        string0 = StringUtils.newStringUtf16Le(byteArray0)
        self.assertEqual("", string0)

    def test03(self) -> None:

        byteArray0 = [0] * 7
        string0 = StringUtils.newStringUtf16Le(byteArray0)
        self.assertEqual("\u0000\u0000\u0000\uFFFD", string0)

    def test02(self) -> None:
        byteArray0 = bytearray()
        string0 = StringUtils.newStringUtf8(byteArray0)
        self.assertEqual("", string0)

    def test01(self) -> None:
        byteArray0 = [0] * 6
        string0 = StringUtils.newStringUtf8(byteArray0)
        self.assertEqual("\u0000\u0000\u0000\u0000\u0000\u0000", string0)

    def test00(self) -> None:

        charBuffer0 = ""
        boolean0 = StringUtils.equals(charBuffer0, "\u00FD\u00FF")
        self.assertFalse(boolean0)
