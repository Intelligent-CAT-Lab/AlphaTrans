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
from src.main.org.apache.commons.codec.CodecPolicy import *
from src.main.org.apache.commons.codec.net.BCodec import *

# from src.test.org.apache.commons.codec.net.BCodec_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class BCodec_ESTest(unittest.TestCase):

    def test55(self) -> None:
        bCodec0 = BCodec.BCodec0()
        string0 = bCodec0.getDefaultCharset()
        self.assertEqual("UTF-8", string0)

    def test52(self) -> None:
        bCodec0 = BCodec.BCodec2("UTF-8")
        self.assertEqual("UTF-8", bCodec0.getDefaultCharset())

    def test49(self) -> None:
        bCodec0 = BCodec.BCodec0()
        boolean0 = bCodec0.isStrictDecoding()
        self.assertFalse(boolean0)

    def test48(self) -> None:

        charset0 = "UTF-8"
        codecPolicy0 = CodecPolicy.STRICT
        bCodec0 = BCodec(charset0, codecPolicy0)
        boolean0 = bCodec0.isStrictDecoding()
        self.assertTrue(boolean0)

    def test47(self) -> None:

        bCodec0 = BCodec.BCodec0()
        byteArray0 = bCodec0._doEncoding(None)
        self.assertIsNone(byteArray0)

    def test46(self) -> None:
        bCodec0 = BCodec.BCodec0()
        byteArray0 = bCodec0._doDecoding(None)
        self.assertIsNone(byteArray0)

    def test45(self) -> None:
        bCodec0 = BCodec.BCodec0()
        charset0 = "UTF-8"
        string0 = bCodec0.encode0(None, charset0)
        self.assertIsNone(string0)

    def test44(self) -> None:

        bCodec0 = BCodec.BCodec0()

        try:
            bCodec0.encode1("org.apache.commons.codecCodcPolicy", "")
            self.fail("Expecting exception: IllegalCharsetNameException")

        except UnicodeEncodeError as e:
            self.verifyException("java.nio.charset.Charset", e)

    def test43(self) -> None:
        bCodec0 = BCodec.BCodec0()
        string0 = bCodec0.encode1(None, None)
        self.assertIsNone(string0)

    def test42(self) -> None:
        bCodec0 = BCodec.BCodec0()
        string0 = bCodec0.encode2(None)
        self.assertIsNone(string0)

    def test41(self) -> None:

        bCodec0 = BCodec.BCodec0()
        string0 = bCodec0.decode0(None)
        self.assertIsNone(string0)

    def test40(self) -> None:
        bCodec0 = BCodec.BCodec0()
        object0 = bCodec0.encode3(None)
        self.assertIsNone(object0)

    def test38(self) -> None:

        bCodec0 = BCodec.BCodec0()
        object0 = bCodec0.decode1(None)
        self.assertIsNone(object0)

    def test37(self) -> None:

        bCodec0 = BCodec.BCodec0()
        object0 = bCodec0.decode1("=?UTF-8?B??=")
        self.assertEqual("", object0)

    def test36(self) -> None:
        bCodec0 = BCodec.BCodec0()
        charset0 = bCodec0.getCharset()
        self.assertEqual("UTF-8", charset0)

    def test34(self) -> None:
        bCodec0 = BCodec.BCodec0()
        charset0 = "UTF-8"
        string0 = bCodec0.encode0("", charset0)
        assert string0 is not None
        self.assertEqual("=?UTF-8?B??=", string0)

    def test33(self) -> None:
        bCodec0 = BCodec.BCodec1(None)
        try:
            bCodec0.encode2("|/VzA^TOX{m:Fc^$h2")
            self.fail("Expecting exception: RuntimeError")
        except Exception as e:
            pass

    def test32(self) -> None:

        bCodec0 = BCodec.BCodec0()
        try:
            bCodec0.decode0("")
            self.fail("Expecting exception: Exception")

        except Exception as e:
            #
            # RFC 1522 violation: malformed encoded content
            #
            self.verifyException("org.apache.commons.codec.net.RFC1522Codec", e)

    def test31(self) -> None:

        bCodec0 = BCodec.BCodec0()
        object0 = object()
        try:
            bCodec0.encode3(object0)
            self.fail("Expecting exception: Exception")

        except Exception as e:
            # Objects of type java.lang.Object cannot be encoded using BCodec
            self.verifyException("org.apache.commons.codec.net.BCodec", e)

    def test30(self) -> None:
        bCodec0 = BCodec.BCodec1(None)
        try:
            bCodec0.encode3("QYieMAk<yvxSkf")
            self.fail("Expecting exception: RuntimeError")
        except Exception as e:
            self.assertEqual(
                str(e), "Objects of type NoneType cannot be encoded using BCodec"
            )

    def test29(self) -> None:

        bCodec0 = BCodec.BCodec0()
        try:
            bCodec0.decode1(bCodec0)
            self.fail("Expecting exception: Exception")

        except Exception as e:
            #
            # Objects of type org.apache.commons.codec.net.BCodec cannot be decoded using BCodec
            #
            self.verifyException("org.apache.commons.codec.net.BCodec", e)

    def test28(self) -> None:

        # Undeclared exception
        try:
            BCodec.BCodec2(None)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # Null charset name
            self.verifyException("java.nio.charset.Charset", e)

    def test27(self) -> None:

        # Undeclared exception
        try:
            BCodec.BCodec2("|8")
            self.fail("Expecting exception: IllegalCharsetNameException")

        except IllegalCharsetNameException as e:
            #
            # |8
            #
            self.verifyException("java.nio.charset.Charset", e)

    def test26(self) -> None:

        # Undeclared exception
        try:
            BCodec.BCodec2("mXPI")
            self.fail("Expecting exception: UnsupportedCharsetException")

        except UnsupportedCharsetException as e:
            # mXPI
            self.verifyException("java.nio.charset.Charset", e)

    def test24(self) -> None:

        charset0 = "UTF-8"
        codecPolicy0 = CodecPolicy.STRICT
        bCodec0 = BCodec(charset0, codecPolicy0)
        byteArray0 = bytearray(11)
        byteArray0[1] = 86
        # Undeclared exception in Java code
        try:
            bCodec0._doDecoding(byteArray0)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # Strict decoding: Last encoded character (before the paddings if any) is a valid base 64 alphabet but not a possible encoding. Decoding requires at least two trailing 6-bit characters to create bytes.
            self.assertTrue("org.apache.commons.codec.binary.Base64" in str(e))

    def test21(self) -> None:
        bCodec0 = BCodec.BCodec0()
        try:
            bCodec0.encode0("", None)
            self.fail("Expecting exception: RuntimeError")
        except Exception as e:
            pass

    def test20(self) -> None:
        bCodec0 = BCodec.BCodec0()
        try:
            bCodec0.encode1("", None)
            self.fail("Expecting exception: ValueError")
        except ValueError as e:
            self.verifyException("java.nio.charset.Charset", e)

    def test19(self) -> None:

        bCodec0 = BCodec.BCodec0()

        with pytest.raises(UnsupportedCharsetException):
            bCodec0.encode1("A", "A")

        verifyException("java.nio.charset.Charset", UnsupportedCharsetException)

    def test18(self) -> None:

        bCodec0 = BCodec.BCodec1(None)
        try:
            bCodec0.getDefaultCharset()
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.assertEqual(str(e), "")
            self.assertEqual(type(e), RuntimeError)

    def test14(self) -> None:

        bCodec0 = BCodec.BCodec0()
        string0 = bCodec0.decode0("=?UTF-8?B??=")
        self.assertEqual("", string0)

    def test13(self) -> None:

        bCodec0 = BCodec.BCodec0()
        string0 = bCodec0.decode0("=?UTF-8?B?Xyt9XU4iQm03Ki0=?=")
        self.assertEqual('_+}]N"Bm7*-', string0)

    def test12(self) -> None:
        bCodec0 = BCodec.BCodec0()
        byteArray0 = bytearray(5)
        byteArray1 = bCodec0._doDecoding(byteArray0)
        self.assertEqual(0, len(byteArray1))

    def test11(self) -> None:

        charset0 = "UTF-8"
        codecPolicy0 = CodecPolicy.LENIENT
        bCodec0 = BCodec(charset0, codecPolicy0)
        byteArray0 = bytearray(8)
        byteArray0[1] = 73
        byteArray0[6] = 118
        byteArray1 = bCodec0._doDecoding(byteArray0)
        self.assertEqual(1, len(byteArray1))

    def test10(self) -> None:

        bCodec0 = BCodec.BCodec0()
        byteArray0 = bytearray()
        byteArray1 = bCodec0.doEncoding(byteArray0)
        self.assertEqual(bytearray(), byteArray1)

    def test09(self) -> None:

        bCodec0 = BCodec.BCodec0()
        byteArray0 = bytearray(2)
        byteArray1 = bCodec0.doEncoding(byteArray0)
        self.assertIsNot(byteArray1, byteArray0)

    def test04(self) -> None:
        bCodec0 = BCodec.BCodec0()
        string0 = bCodec0.encode1("UTF-8", "UTF-8")
        assert string0 is not None
        self.assertEqual("=?UTF-8?B?VVRGLTg=?=", string0)

    def test03(self) -> None:
        bCodec0 = BCodec.BCodec0()
        string0 = bCodec0.encode2('_+}]N"Bm7*-')
        self.assertEqual("=?UTF-8?B?Xyt9XU4iQm03Ki0=?=", string0)
        self.assertIsNotNone(string0)

    def test02(self) -> None:
        bCodec0 = BCodec.BCodec0()
        object0 = bCodec0.encode3("")
        self.assertEqual("=?UTF-8?B??=", object0)
        self.assertIsNotNone(object0)

    def test01(self) -> None:

        codecPolicy0 = CodecPolicy.LENIENT
        bCodec0 = BCodec(None, codecPolicy0)
        charset0 = bCodec0.getCharset()
        self.assertIsNone(charset0)

    def test00(self) -> None:
        bCodec0 = BCodec.BCodec0()
        string0 = bCodec0._getEncoding()
        self.assertEqual("B", string0)
