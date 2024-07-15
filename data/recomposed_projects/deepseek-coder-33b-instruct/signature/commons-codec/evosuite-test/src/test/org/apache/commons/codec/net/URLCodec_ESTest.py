from __future__ import annotations
import time
import re
import sys
import os
import typing
from typing import *
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.codec.net.URLCodec import *

# from src.test.org.apache.commons.codec.net.URLCodec_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class URLCodec_ESTest(unittest.TestCase):

    def test82(self) -> None:
        uRLCodec0 = URLCodec.URLCodec1()
        string0 = uRLCodec0.getEncoding()
        self.assertEqual("UTF-8", string0)

    def test75(self) -> None:

        byteArray0 = bytearray()
        byteArray1 = URLCodec.encodeUrl(None, byteArray0)
        self.assertIsNotNone(byteArray1)
        self.assertNotEqual(byteArray1, byteArray0)

    def test74(self) -> None:

        byteArray0 = [0] * 6
        byteArray0[3] = -38
        bitSet0 = []
        byteArray1 = URLCodec.encodeUrl(bitSet0, byteArray0)
        self.assertEqual(18, len(byteArray1))

    def test72(self) -> None:

        uRLCodec0 = URLCodec.URLCodec1()
        try:
            uRLCodec0.decode1("f'f&Pxk/l+UpuzNX73", "f'f&Pxk/l+UpuzNX73")
            self.fail("Expecting exception: ValueError")

        except ValueError:
            pass

    def test71(self) -> None:

        uRLCodec0 = URLCodec.URLCodec1()
        string0 = uRLCodec0.encode1(None, None)
        self.assertIsNone(string0)

    def test70(self) -> None:

        uRLCodec0 = URLCodec.URLCodec1()
        string0 = uRLCodec0.encode2(None)
        self.assertIsNone(string0)

    def test67(self) -> None:

        uRLCodec0 = URLCodec.URLCodec1()
        object0 = uRLCodec0.encode3(None)
        self.assertIsNone(object0)

    def test64(self) -> None:

        uRLCodec0 = URLCodec("UTF-8")
        byteArray0 = [0] * 1
        byteArray1 = uRLCodec0.encode0(byteArray0)
        self.assertEqual([37, 48, 48], byteArray1)

    def test63(self) -> None:
        uRLCodec0 = URLCodec.URLCodec1()
        string0 = uRLCodec0.getDefaultCharset()
        self.assertEqual("UTF-8", string0)

    def test62(self) -> None:

        uRLCodec0 = URLCodec.URLCodec1()
        byteArray0 = [0] * 6
        byteArray1 = uRLCodec0.decode0(byteArray0)
        self.assertEqual([0, 0, 0, 0, 0, 0], byteArray1)

    def test61(self) -> None:

        byteArray0 = URLCodec.encodeUrl(None, None)
        self.assertIsNone(byteArray0)

    def test60(self) -> None:

        byteArray0 = [0] * 7
        byteArray0[3] = 32
        byteArray1 = URLCodec.encodeUrl(None, byteArray0)
        self.assertEqual(19, len(byteArray1))

    def test59(self) -> None:

        byteArray0 = [0] * 5
        byteArray0[0] = 1
        bitSet0 = BitSet.valueOf(byteArray0)
        byteArray1 = URLCodec.encodeUrl(bitSet0, byteArray0)
        self.assertEqual(byteArray1, [37, 48, 49, 0, 0, 0, 0])
        self.assertEqual(len(byteArray1), 7)

    def test58(self) -> None:

        byteArray0 = URLCodec.decodeUrl(None)
        self.assertIsNone(byteArray0)

    def test57(self) -> None:

        byteArray0 = [0] * 7
        byteArray0[1] = 43
        byteArray1 = URLCodec.decodeUrl(byteArray0)
        self.assertEqual([0, 32, 0, 0, 0, 0, 0], byteArray1)

    def test56(self) -> None:

        uRLCodec0 = URLCodec.URLCodec1()
        try:
            uRLCodec0.encode1("", "")
            self.fail("Expecting exception: ValueError")

        except ValueError:
            pass

    def test55(self) -> None:

        uRLCodec0 = URLCodec(";u ")
        try:
            uRLCodec0.encode2("T7<V;1")
            self.fail("Expecting exception: Exception")

        except Exception as e:
            self.verifyException("org.apache.commons.codec.net.URLCodec", e)

    def test54(self) -> None:

        uRLCodec0 = URLCodec.URLCodec1()
        string0 = uRLCodec0.decode1(None, None)
        self.assertIsNone(string0)

    def test53(self) -> None:

        uRLCodec0 = URLCodec("")
        try:
            uRLCodec0.decode2("")
            self.fail("Expecting exception: Exception")

        except Exception as e:
            self.verifyException("org.apache.commons.codec.net.URLCodec", e)

    def test52(self) -> None:

        uRLCodec0 = URLCodec.URLCodec1()
        string0 = uRLCodec0.decode2(None)
        self.assertIsNone(string0)

    def test51(self) -> None:

        uRLCodec0 = URLCodec.URLCodec1()
        object0 = uRLCodec0.encode3("org.apache.commons.codec.EncoderException")
        self.assertEqual("org.apache.commons.codec.EncoderException", object0)
        self.assertIsNotNone(object0)

    def test50(self) -> None:

        uRLCodec0 = URLCodec.URLCodec1()
        try:
            uRLCodec0.encode3(uRLCodec0)
            self.fail("Expecting exception: Exception")

        except Exception as e:
            # Objects of type org.apache.commons.codec.net.URLCodec cannot be URL encoded
            self.verifyException("org.apache.commons.codec.net.URLCodec", e)

    def test49(self) -> None:

        uRLCodec0 = URLCodec.URLCodec1()
        try:
            uRLCodec0.decode3(uRLCodec0)
            self.fail("Expecting exception: Exception")

        except Exception as e:
            # Objects of type org.apache.commons.codec.net.URLCodec cannot be URL decoded
            self.verifyException("org.apache.commons.codec.net.URLCodec", e)

    def test48(self) -> None:

        uRLCodec0 = URLCodec.URLCodec1()
        object0 = uRLCodec0.decode3(None)
        self.assertIsNone(object0)

    def test47(self) -> None:

        uRLCodec0 = URLCodec(None)

        with pytest.raises(TypeError):
            uRLCodec0.decode3("7}23EFK6iGGK ")

    def test40(self) -> None:

        uRLCodec0 = URLCodec.URLCodec1()
        byteArray0 = bytearray(5)
        byteArray0[4] = 37
        try:
            uRLCodec0.decode0(byteArray0)
            self.fail("Expecting exception: Exception")

        except Exception as e:
            #
            # Invalid URL encoding:
            #
            self.assertIsInstance(e, Exception)

    def test39(self) -> None:

        uRLCodec0 = URLCodec.URLCodec1()

        with pytest.raises(TypeError):
            uRLCodec0.decode1("", None)

    def test38(self) -> None:

        uRLCodec0 = URLCodec.URLCodec1()
        try:
            uRLCodec0.decode1("eGy%4Mx'v]B=>>", "eGy%4Mx'v]B=>>")
            self.fail("Expecting exception: Exception")

        except Exception as e:
            #
            # Invalid URL encoding: not a valid digit (radix 16): 77
            #
            self.verifyException("org.apache.commons.codec.net.Utils", e)

    def test37(self) -> None:

        uRLCodec0 = URLCodec(None)

        with pytest.raises(RuntimeError):
            uRLCodec0.decode2("v/bxk7u;csysg#G")

    def test36(self) -> None:

        byteArray0 = [37]

        try:
            URLCodec.decodeUrl(byteArray0)
            self.fail("Expecting exception: Exception")

        except Exception as e:
            #
            # Invalid URL encoding:
            #
            self.assertIsInstance(e, DecoderException)
            self.assertEqual(str(e), "Invalid URL encoding: ")

    def test30(self) -> None:

        uRLCodec0 = URLCodec.URLCodec1()
        # Undeclared exception in Java code
        try:
            uRLCodec0.encode1("", None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            pass

    def test29(self) -> None:

        uRLCodec0 = URLCodec(None)

        with pytest.raises(RuntimeError):
            uRLCodec0.encode2("hzlHZ")

    def test28(self) -> None:

        uRLCodec0 = URLCodec(None)
        try:
            uRLCodec0.encode3("t-|W")
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError:
            pass

    def test24(self) -> None:

        uRLCodec0 = URLCodec.URLCodec1()
        byteArray0 = bytearray()
        byteArray1 = uRLCodec0.decode0(byteArray0)
        self.assertIsNotNone(byteArray1)
        self.assertNotEqual(byteArray1, byteArray0)

    def test23(self) -> None:

        uRLCodec0 = URLCodec.URLCodec1()
        byteArray0 = uRLCodec0.decode0(None)
        self.assertIsNone(byteArray0)

    def test22(self) -> None:

        uRLCodec0 = URLCodec("")
        string0 = uRLCodec0.decode1("", "UTF-8")
        self.assertEqual("", string0)

    def test21(self) -> None:

        uRLCodec0 = URLCodec.URLCodec1()
        string0 = uRLCodec0.decode1("UTF-8", "UTF-8")
        self.assertEqual("UTF-8", string0)

    def test20(self) -> None:

        uRLCodec0 = URLCodec.URLCodec1()
        string0 = uRLCodec0.decode2("")
        assert string0 is not None
        assert string0 == ""

    def test19(self) -> None:

        uRLCodec0 = URLCodec.URLCodec1()
        string0 = uRLCodec0.decode2(" cannot be URL encoded")
        self.assertEqual(" cannot be URL encoded", string0)
        self.assertIsNotNone(string0)

    def test18(self) -> None:

        uRLCodec0 = URLCodec.URLCodec1()
        object0 = uRLCodec0.decode3("")
        self.assertIsNotNone(object0)
        self.assertEqual("", object0)

    def test17(self) -> None:

        byteArray0 = bytearray()
        byteArray1 = URLCodec.decodeUrl(byteArray0)
        self.assertEqual(0, len(byteArray1))

    def test10(self) -> None:

        uRLCodec0 = URLCodec.URLCodec1()
        byteArray0 = bytearray()
        byteArray1 = uRLCodec0.encode0(byteArray0)
        self.assertNotEqual(byteArray1, byteArray0)

    def test09(self) -> None:

        uRLCodec0 = URLCodec.URLCodec1()
        byteArray0 = uRLCodec0.encode0(None)
        self.assertIsNone(byteArray0)

    def test08(self) -> None:

        uRLCodec0 = URLCodec.URLCodec1()
        string0 = uRLCodec0.encode1("", "UTF-8")
        self.assertEqual("", string0)

    def test07(self) -> None:

        uRLCodec0 = URLCodec("UTF-8")
        string0 = uRLCodec0.encode1("?_w7cN%21%261n6~", "UTF-8")
        self.assertEqual("%3F_w7cN%21%261n6%7E", string0)

    def test06(self) -> None:

        uRLCodec0 = URLCodec.URLCodec1()
        string0 = uRLCodec0.encode2("")
        self.assertIsNotNone(string0)
        self.assertEqual("", string0)

    def test05(self) -> None:

        uRLCodec0 = URLCodec.URLCodec1()
        string0 = uRLCodec0.encode2("UTF-8")
        assert string0 is not None
        self.assertEqual("UTF-8", string0)

    def test04(self) -> None:
        uRLCodec0 = URLCodec("")
        string0 = uRLCodec0.getDefaultCharset()
        self.assertEqual("", string0)

    def test03(self) -> None:
        uRLCodec0 = URLCodec(None)
        string0 = uRLCodec0.getDefaultCharset()
        self.assertIsNone(string0)

    def test02(self) -> None:
        uRLCodec0 = URLCodec("")
        string0 = uRLCodec0.getEncoding()
        self.assertEqual("", string0)

    def test01(self) -> None:
        uRLCodec0 = URLCodec(None)
        string0 = uRLCodec0.getEncoding()
        self.assertIsNone(string0)
