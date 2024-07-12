from __future__ import annotations
import time
import re
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.codec.net.QCodec import *

# from src.test.org.apache.commons.codec.net.QCodec_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class QCodec_ESTest(unittest.TestCase):

    def test52(self) -> None:
        qCodec0 = QCodec.QCodec2()
        qCodec0.getDefaultCharset()
        self.assertFalse(qCodec0.isEncodeBlanks())

    def test51(self) -> None:
        qCodec0 = QCodec.QCodec2()
        boolean0 = qCodec0.isEncodeBlanks()
        self.assertFalse(boolean0)

    def test50(self) -> None:
        qCodec0 = QCodec.QCodec0("UTF-8")
        self.assertFalse(qCodec0.isEncodeBlanks())

    def test47(self) -> None:

        charset0 = "UTF-8"
        qCodec0 = QCodec(-586, " cannot be quoted-printable encoded", charset0)
        string0 = qCodec0.encode2(" cannot be quoted-printable encoded")
        self.assertEqual("=?UTF-8?Q? cannot be quoted-printable encoded?=", string0)
        self.assertIsNotNone(string0)

    def test46(self) -> None:

        qCodec0 = QCodec.QCodec2()
        qCodec0.doEncoding(None)
        self.assertFalse(qCodec0.isEncodeBlanks())

    def test45(self) -> None:

        qCodec0 = QCodec.QCodec2()
        qCodec0.doDecoding(None)
        self.assertFalse(qCodec0.isEncodeBlanks())

    def test44(self) -> None:

        qCodec0 = QCodec.QCodec2()
        string0 = qCodec0.decode0("=?UTF-8?Q?org.apache.commons.codec.net.QCodec?=")
        self.assertFalse(qCodec0.isEncodeBlanks())
        self.assertIsNotNone(string0)

    def test43(self) -> None:

        charset0 = "UTF-8"  # Charset.defaultCharset()
        qCodec0 = QCodec(1288, "s%Xm_*i,urfC9'<4iP'", charset0)
        qCodec0.encode0(None, charset0)  # (String) null
        self.assertFalse(qCodec0.isEncodeBlanks())

    def test42(self) -> None:
        qCodec0 = QCodec.QCodec2()
        string0 = qCodec0.encode1("UTF-8", "UTF-8")
        self.assertEqual("=?UTF-8?Q?UTF-8?=", string0)
        self.assertIsNotNone(string0)
        self.assertFalse(qCodec0.isEncodeBlanks())

    def test41(self) -> None:
        qCodec0 = QCodec.QCodec2()
        qCodec0.encode1(None, "")
        self.assertFalse(qCodec0.isEncodeBlanks())

    def test39(self) -> None:

        qCodec0 = QCodec.QCodec2()
        qCodec0.decode0(None)
        self.assertFalse(qCodec0.isEncodeBlanks())

    def test36(self) -> None:

        qCodec0 = QCodec.QCodec2()
        object0 = qCodec0.decode1("=?UTF-8?Q??=")
        self.assertIsNotNone(object0)
        self.assertFalse(qCodec0.isEncodeBlanks())

    def test35(self) -> None:

        qCodec0 = QCodec.QCodec2()

        try:
            qCodec0.decode1(qCodec0)
            self.fail("Expecting exception: Exception")

        except Exception as e:
            # Objects of type org.apache.commons.codec.net.QCodec cannot be decoded using Q codec
            self.verifyException("org.apache.commons.codec.net.QCodec", e)

    def test34(self) -> None:

        charset0 = "UTF-8"  # Default charset in Python
        qCodec0 = QCodec(41, None, charset0)
        qCodec0.getCharset()
        self.assertFalse(qCodec0.isEncodeBlanks())

    def test33(self) -> None:

        charset0 = "UTF-8"  # Default charset in Python is UTF-8
        qCodec0 = QCodec(1, "", charset0)
        self.assertFalse(qCodec0.isEncodeBlanks())

    def test32(self) -> None:

        charset0 = "UTF-8"
        qCodec0 = QCodec(1, "s%Xm_*i,urfC9'<4iP'", charset0)
        string0 = qCodec0.encode0("", charset0)
        self.assertFalse(qCodec0.isEncodeBlanks())
        self.assertEqual("=?UTF-8?Q??=", string0)
        self.assertIsNotNone(string0)

    def test31(self) -> None:

        qCodec0 = QCodec(60, "org.apache.commons.codec.net.QuotedPrintableCodec", None)

        with pytest.raises(RuntimeError):
            qCodec0.encode2("org.apache.commons.codec.net.Utils")

    def test30(self) -> None:

        charset0 = "UTF-8"  # Default charset in Python
        qCodec0 = QCodec(-476, None, charset0)
        qCodec0.encode2(None)
        self.assertFalse(qCodec0.isEncodeBlanks())

    def test29(self) -> None:
        qCodec0 = QCodec.QCodec2()
        object0 = qCodec0.encode3("")
        self.assertEqual("=?UTF-8?Q??=", object0)
        self.assertIsNotNone(object0)
        self.assertFalse(qCodec0.isEncodeBlanks())

    def test28(self) -> None:
        qCodec0 = QCodec.QCodec2()
        qCodec0.encode3(None)
        self.assertFalse(qCodec0.isEncodeBlanks())

    def test27(self) -> None:

        qCodec0 = QCodec.QCodec2()
        object0 = object()
        try:
            qCodec0.encode3(object0)
            self.fail("Expecting exception: Exception")

        except Exception as e:
            # Objects of type java.lang.Object cannot be encoded using Q codec
            self.verifyException("org.apache.commons.codec.net.QCodec", e)

    def test26(self) -> None:

        qCodec0 = QCodec.QCodec2()
        qCodec0.decode1(None)
        self.assertFalse(qCodec0.isEncodeBlanks())

    def test25(self) -> None:

        # Undeclared exception
        try:
            QCodec.QCodec0(None)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # Null charset name
            self.verifyException("java.nio.charset.Charset", e)

    def test24(self) -> None:

        # Undeclared exception
        try:
            QCodec.QCodec0("")
            self.fail("Expecting exception: IllegalCharsetNameException")

        except IllegalCharsetNameException as e:
            #
            #
            #
            self.verifyException("java.nio.charset.Charset", e)

    def test23(self) -> None:

        # Undeclared exception
        try:
            QCodec.QCodec0("org.apache.commons.codec.EncoderException")
            self.fail("Expecting exception: UnsupportedCharsetException")

        except UnsupportedCharsetException as e:
            # org.apache.commons.codec.EncoderException
            self.verifyException("java.nio.charset.Charset", e)

    def test20(self) -> None:

        qCodec0 = QCodec.QCodec2()
        try:
            qCodec0.decode0("wMj")
            self.fail("Expecting exception: Exception")

        except Exception as e:
            #
            # RFC 1522 violation: malformed encoded content
            #
            self.verifyException("org.apache.commons.codec.net.RFC1522Codec", e)

    def test19(self) -> None:

        qCodec0 = QCodec.QCodec2()
        byteArray0 = bytearray(1)
        byteArray0[0] = 61

        try:
            qCodec0._doDecoding(byteArray0)
            self.fail("Expecting exception: Exception")

        except Exception as e:
            # Invalid quoted-printable encoding
            self.verifyException("org.apache.commons.codec.net.QuotedPrintableCodec", e)

    def test16(self) -> None:
        qCodec0 = QCodec.QCodec2()
        try:
            qCodec0.encode0("pJE)/|2", None)
            self.fail("Expecting exception: RuntimeError")
        except Exception as e:
            pass

    def test15(self) -> None:

        qCodec0 = QCodec.QCodec2()
        # Undeclared exception in Java code
        try:
            qCodec0.encode1("4djD", None)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # Null charset name
            self.verifyException("java.nio.charset.Charset", e)

    def test14(self) -> None:

        qCodec0 = QCodec.QCodec2()

        # Undeclared exception in Java, so we use a try-except block to catch the exception
        try:
            qCodec0.encode1("Objects of type ", "Objects of type ")
            self.fail("Expecting exception: IllegalCharsetNameException")

        except ValueError as e:
            # Objects of type
            #
            self.verifyException("java.nio.charset.Charset", e)

    def test13(self) -> None:

        qCodec0 = QCodec.QCodec2()
        try:
            qCodec0.encode1("4djD", "4djD")
            self.fail("Expecting exception: UnsupportedCharsetException")
        except UnsupportedCharsetException as e:
            self.verifyException("java.nio.charset.Charset", e)

    def test12(self) -> None:

        qCodec0 = QCodec(-224, ")?R<cq2o", None)
        try:
            qCodec0.encode3("v")
            self.fail("Expecting exception: RuntimeError")
        except RuntimeError:
            pass

    def test11(self) -> None:

        qCodec0 = QCodec(23, "3O%", None)

        try:
            qCodec0.getDefaultCharset()
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.assertEqual(str(type(e)), "<class 'RuntimeError'>")

    def test07(self) -> None:

        qCodec0 = QCodec.QCodec2()
        string0 = qCodec0.decode0("=?UTF-8?Q??=")
        self.assertFalse(qCodec0.isEncodeBlanks())
        self.assertIsNotNone(string0)

    def test06(self) -> None:

        qCodec0 = QCodec.QCodec2()
        byteArray0 = bytearray()
        qCodec0.doDecoding(byteArray0)
        assert not qCodec0.isEncodeBlanks()

    def test05(self) -> None:

        qCodec0 = QCodec.QCodec2()
        byteArray0 = bytearray()
        byteArray1 = bytearray(qCodec0.doEncoding(byteArray0))

        self.assertIsNotNone(byteArray1)
        self.assertNotEqual(byteArray1, byteArray0)
        self.assertFalse(qCodec0.isEncodeBlanks())

    def test04(self) -> None:

        qCodec0 = QCodec.QCodec2()
        byteArray0 = bytearray(4)
        byteArray1 = qCodec0.doEncoding(byteArray0)
        self.assertIsNotNone(byteArray1)
        self.assertEqual(12, len(byteArray1))
        self.assertFalse(qCodec0.isEncodeBlanks())

    def test03(self) -> None:

        qCodec0 = QCodec(256, "K^G'n\"74t", None)
        qCodec0.getCharset()
        self.assertFalse(qCodec0.isEncodeBlanks())

    def test02(self) -> None:
        qCodec0 = QCodec.QCodec2()
        qCodec0.getEncoding()
        self.assertFalse(qCodec0.isEncodeBlanks())

    def test01(self) -> None:

        qCodec0 = QCodec.QCodec2()
        self.assertFalse(qCodec0.isEncodeBlanks())

        qCodec0.setEncodeBlanks(True)
        boolean0 = qCodec0.isEncodeBlanks()
        self.assertTrue(boolean0)

    def test00(self) -> None:

        qCodec0 = QCodec.QCodec2()
        byteArray0 = bytearray(6)
        byteArray0[0] = 120
        byteArray0[1] = 95
        byteArray1 = qCodec0.doDecoding(byteArray0)
        self.assertFalse(qCodec0.isEncodeBlanks())
        self.assertEqual(byteArray1, bytearray([120, 32, 0, 0, 0, 0]))
