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
from src.main.org.apache.commons.codec.binary.Base64 import *

# from src.test.org.apache.commons.codec.binary.Base64_ESTest_scaffolding import *
from src.main.org.apache.commons.codec.binary.BaseNCodec import *

# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class Base64_ESTest(unittest.TestCase):

    def test67(self) -> None:

        bigInteger0 = pow(2, 32) - 1

        try:
            Base64.encodeInteger(bigInteger0)
            self.fail("Expecting exception: ValueError")
        except ValueError as e:
            self.assertEqual(str(e), "bigInteger cannot be None")

    def test66(self) -> None:

        # Undeclared exception
        try:
            Base64.decodeBase641(
                "Strict decoding: Last encoded character (before the paddings if any) is a valid base 64 alphabet but not a possible encoding. Expected the discarded bits from the character to be zero."
            )
            # fail("Expecting exception: ValueError")
            # Unstable assertion
        except ValueError as e:
            # lineSeparator must not contain base64 characters: [\rA]
            self.verifyException("org.apache.commons.codec.binary.Base64", e)

    def test65(self) -> None:

        byteArray0 = bytearray(1)
        try:
            Base64.encodeBase64URLSafeString(byteArray0)
            self.fail("Expecting exception: ValueError")
        except ValueError as e:
            verifyException("org.apache.commons.codec.binary.Base64", e)

    def test64(self) -> None:

        # Undeclared exception
        try:
            Base64.decodeBase641("")
            # fail("Expecting exception: ValueError")
            # Unstable assertion
        except ValueError as e:
            # lineSeparator must not contain base64 characters: [\rA]
            self.verifyException("org.apache.commons.codec.binary.Base64", e)

    def test63(self) -> None:

        try:
            Base64.isArrayByteBase64(None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.assertEqual(str(e), "RuntimeError")

    def test62(self) -> None:

        boolean0 = Base64.isBase642("bigInteger")
        self.assertTrue(boolean0)

    def test61(self) -> None:

        byteArray0 = Base64.encodeBase640(None)
        self.assertIsNone(byteArray0)

    def test60(self) -> None:

        byteArray0 = Base64.encodeBase64Chunked(None)
        self.assertIsNone(byteArray0)

    def test59(self) -> None:

        byteArray0 = [0] * 7

        try:
            Base64.encodeBase643(byteArray0, False, False, -1587)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            verifyException("org.apache.commons.codec.binary.Base64", e)

    def test58(self) -> None:

        boolean0 = Base64.isBase640(126)
        self.assertFalse(boolean0)

    def test57(self) -> None:

        byteArray0 = [0] * 8
        boolean0 = Base64.isBase641(byteArray0)
        self.assertFalse(boolean0)

    def test56(self) -> None:

        byteArray0 = [72, 10]
        boolean0 = Base64.isBase641(byteArray0)
        self.assertTrue(boolean0)

    def test55(self) -> None:

        base64_0 = Base64.Base642(116, None)
        baseNCodec_Context0 = Context()
        # Undeclared exception
        try:
            base64_0.decode1(None, 116, 116, baseNCodec_Context0)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            # no message in exception (getMessage() returned null)
            self.verifyException("org.apache.commons.codec.binary.Base64", e)

    def test54(self) -> None:

        try:
            Base64.decodeBase641("RtbgHi^")
            self.fail("Expecting exception: ValueError")
        except ValueError as e:
            verifyException("org.apache.commons.codec.binary.Base64", e)

    def test53(self) -> None:

        try:
            Base64.decodeBase641("Zi{<g25jm?e6Q=5")
            self.fail("Expecting exception: ValueError")
        except ValueError as e:
            verifyException("org.apache.commons.codec.binary.Base64", e)

    def test52(self) -> None:

        byteArray0 = bytearray(1)
        byteArray0[0] = -94

        try:
            Base64.decodeInteger(byteArray0)
            self.fail("Expecting exception: ValueError")
        except ValueError as e:
            self.verifyException("org.apache.commons.codec.binary.Base64", e)

    def test51(self) -> None:
        with pytest.raises(ValueError):
            Base64.Base643(-2279)
        verifyException("org.apache.commons.codec.binary.Base64", ValueError)

    def test50(self) -> None:
        byteArray0 = bytearray(2)
        try:
            Base64.Base644(True)
            pytest.fail("Expecting exception: ValueError")
        except ValueError as e:
            verifyException("org.apache.commons.codec.binary.Base64", e)

    def test49(self) -> None:

        try:
            Base64.decodeBase641("uPPEjbTH3]A")
            self.fail("Expecting exception: ValueError")
        except ValueError as e:
            verifyException("org.apache.commons.codec.binary.Base64", e)

    def test48(self) -> None:

        try:
            Base64.decodeBase641("y,;+h8YvMVftQiX4")
            self.fail("Expecting exception: ValueError")
        except ValueError as e:
            verifyException("org.apache.commons.codec.binary.Base64", e)

    def test47(self) -> None:

        bigInteger0 = 10
        byteArray0 = Base64.toIntegerBytes(bigInteger0)
        base64_0 = Base64.Base641(0, byteArray0, True)
        boolean0 = base64_0.isUrlSafe()
        self.assertTrue(boolean0)
        self.assertEqual(len(byteArray0), 1)

    def test46(self) -> None:

        byteArray0 = bytearray(1)
        try:
            Base64.encodeBase642(byteArray0, True, False)
            self.fail("Expecting exception: ValueError")
        except ValueError as e:
            self.verifyException("org.apache.commons.codec.binary.Base64", e)

    def test45(self) -> None:

        # Undeclared exception
        try:
            Base64.decodeBase641("org.apache.commons.codec.CodecPolicy")
            # fail("Expecting exception: ValueError")
            # Unstable assertion
        except ValueError as e:
            # lineSeparator must not contain base64 characters: [\rA]
            self.verifyException("org.apache.commons.codec.binary.Base64", e)

    def test44(self) -> None:

        bigInteger0 = BigInteger.ZERO
        byteArray0 = Base64.toIntegerBytes(bigInteger0)
        self.assertEqual(0, len(byteArray0))

        byteArray1 = Base64.encodeBase643(byteArray0, False, False, 0)
        self.assertEqual(0, len(byteArray1))

    def test43(self) -> None:

        byteArray0 = Base64.encodeBase643(None, True, True, -2458)
        self.assertIsNone(byteArray0)

    def test42(self) -> None:

        bigInteger0 = BigInteger.TEN

        try:
            Base64.encodeInteger(bigInteger0)
            self.fail("Expecting exception: ValueError")
        except ValueError as e:
            verifyException("org.apache.commons.codec.binary.Base64", e)

    def test41(self) -> None:

        boolean0 = Base64.isBase640(65)
        self.assertTrue(boolean0)

    def test40(self) -> None:

        boolean0 = Base64.isBase640((-84).to_bytes(1, "big", signed=True)[0])
        self.assertFalse(boolean0)

    def test39(self) -> None:

        boolean0 = Base64.isBase640(37)
        self.assertFalse(boolean0)

    def test38(self) -> None:

        boolean0 = Base64.isBase640(61)
        self.assertTrue(boolean0)

    def test37(self) -> None:

        codecPolicy0 = CodecPolicy.STRICT
        base64_0 = Base64((-1214), None, False, codecPolicy0)
        self.assertFalse(base64_0.isUrlSafe())

    def test36(self) -> None:

        byteArray0 = bytearray(0)
        codecPolicy0 = CodecPolicy.LENIENT
        base64_0 = Base64(0, byteArray0, False, codecPolicy0)
        self.assertFalse(base64_0.isUrlSafe())

    def test35(self) -> None:

        byteArray0 = [0] * 3
        codecPolicy0 = CodecPolicy.LENIENT
        base64_0 = Base64(736, byteArray0, True, codecPolicy0)
        self.assertTrue(base64_0.isUrlSafe())

    def test34(self) -> None:
        try:
            Base64.Base644(True)
            self.fail("Expecting exception: ValueError")
        except ValueError as e:
            verifyException("org.apache.commons.codec.binary.Base64", e)

    def test33(self) -> None:

        try:
            Base64.decodeBase641(") than the specified maximum size of ")
            self.fail("Expecting exception: ValueError")
        except ValueError as e:
            verifyException("org.apache.commons.codec.binary.Base64", e)

    def test32(self) -> None:

        try:
            Base64.decodeBase641("org.apa-he.comSons.codec.CodecPolicy")
            # fail("Expecting exception: ValueError")
            # Unstable assertion
        except ValueError as e:
            #
            # lineSeparator must not contain base64 characters: [\rA]
            #
            self.verifyException("org.apache.commons.codec.binary.Base64", e)

    def test31(self) -> None:

        byteArray0 = bytearray(9)
        base64_0 = Base64.Base642(27, byteArray0)
        baseNCodec_Context0 = Context()
        # Undeclared exception
        try:
            base64_0.encode2(byteArray0, 27, 27, baseNCodec_Context0)
            self.fail("Expecting exception: ArrayIndexOutOfBoundsException")

        except IndexError as e:
            # Index 27 out of bounds for length 9
            self.verifyException("org.apache.commons.codec.binary.Base64", e)

    def test30(self) -> None:
        byteArray0 = bytearray(0)
        try:
            Base64.Base643(28)
            pytest.fail("Expecting exception: ValueError")
        except ValueError as e:
            verifyException("org.apache.commons.codec.binary.Base64", e)

    def test29(self) -> None:

        try:
            Base64.encodeInteger(None)
            self.fail("Expecting exception: RuntimeError")

        except ValueError as e:
            self.assertEqual(str(e), "bigInteger cannot be None")

    def test28(self) -> None:

        try:
            Base64.isBase641(None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.assertEqual(str(e), "RuntimeError")

    def test27(self) -> None:

        try:
            Base64.isBase642(None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.assertEqual(str(e), "RuntimeError")

    def test26(self) -> None:

        try:
            Base64.toIntegerBytes(None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            # no message in exception (getMessage() returned null)
            # verifyException("org.apache.commons.codec.binary.Base64", e)
            self.assertIsInstance(e, TypeError)

    def test25(self) -> None:
        byteArray0 = bytearray(0)
        base64_0 = Base64.Base641(0, byteArray0, False)
        self.assertFalse(base64_0.isUrlSafe())

    def test24(self) -> None:

        # Undeclared exception handling
        try:
            Base64.decodeBase640(None)
            # Unstable assertion
            # self.fail("Expecting exception: ValueError")
        except ValueError as e:
            # lineSeparator must not contain base64 characters: [\rA]
            self.verifyException("org.apache.commons.codec.binary.Base64", e)

    def test23(self) -> None:

        # Undeclared exception
        try:
            Base64.decodeBase641(None)
            # fail("Expecting exception: ValueError")
            # Unstable assertion
        except ValueError as e:
            # lineSeparator must not contain base64 characters: [\rA]
            self.verifyException("org.apache.commons.codec.binary.Base64", e)

    def test22(self) -> None:

        byteArray0 = bytearray(1)
        byteArray0[0] = 29

        try:
            Base64.encodeBase640(byteArray0)
            self.fail("Expecting exception: ValueError")
        except ValueError as e:
            verifyException("org.apache.commons.codec.binary.Base64", e)

    def test21(self) -> None:

        byteArray0 = bytearray(9)
        byteArray0[2] = 106
        byteArray0[4] = 52
        byteArray0[5] = 52

        try:
            Base64.decodeInteger(byteArray0)
            self.fail("Expecting exception: ValueError")
        except ValueError as e:
            self.verifyException("org.apache.commons.codec.binary.Base64", e)

    def test20(self) -> None:

        byteArray0 = bytearray(0)
        byteArray1 = Base64.encodeBase640(byteArray0)
        byteArray2 = Base64.encodeBase642(byteArray1, True, False)
        self.assertTrue(byteArray1 == byteArray2)

    def test19(self) -> None:

        # Undeclared exception
        try:
            Base64.decodeBase641(")= x")
            # fail("Expecting exception: ValueError")
            # Unstable assertion
        except ValueError as e:
            # lineSeparator must not contain base64 characters: [\rA]
            self.verifyException("org.apache.commons.codec.binary.Base64", e)

    def test18(self) -> None:

        byteArray0 = Base64.encodeBase641(None, True)
        self.assertIsNone(byteArray0)

    def test17(self) -> None:

        byteArray0 = Base64.encodeBase642(None, False, False)
        self.assertIsNone(byteArray0)

    def test16(self) -> None:

        byteArray0 = bytearray(0)
        byteArray1 = Base64.encodeBase64Chunked(byteArray0)
        self.assertEqual(byteArray1, bytearray(0))

    def test15(self) -> None:

        byteArray0 = bytearray(1)
        try:
            Base64.encodeBase64Chunked(byteArray0)
            self.fail("Expecting exception: ValueError")
        except ValueError as e:
            verifyException("org.apache.commons.codec.binary.Base64", e)

    def test14(self) -> None:

        byteArray0 = bytearray(2)

        try:
            Base64.decodeBase640(byteArray0)
            self.fail("Expecting exception: ValueError")
        except ValueError as e:
            verifyException("org.apache.commons.codec.binary.Base64", e)

    def test13(self) -> None:
        string0 = Base64.encodeBase64String(None)
        self.assertIsNone(string0)

    def test12(self) -> None:

        byteArray0 = bytearray(7)
        try:
            Base64.encodeBase64URLSafe(byteArray0)
            self.fail("Expecting exception: ValueError")
        except ValueError as e:
            # lineSeparator must not contain base64 characters: [\rA]
            self.verifyException("org.apache.commons.codec.binary.Base64", e)

    def test11(self) -> None:

        byteArray0 = Base64.encodeBase64URLSafe(None)
        self.assertIsNone(byteArray0)

    def test10(self) -> None:

        bigInteger0 = BigInteger.ZERO
        byteArray0 = Base64.encodeInteger(bigInteger0)
        string0 = Base64.encodeBase64URLSafeString(byteArray0)
        self.assertEqual("", string0)

    def test09(self) -> None:

        string0 = Base64.encodeBase64URLSafeString(None)
        self.assertIsNone(string0)

    def test08(self) -> None:

        byteArray0 = [0] * 8
        boolean0 = Base64.isArrayByteBase64(byteArray0)
        self.assertFalse(boolean0)

    def test07(self) -> None:

        bigInteger0 = BigInteger(10)
        byteArray0 = Base64.toIntegerBytes(bigInteger0)
        boolean0 = Base64.isArrayByteBase64(byteArray0)
        self.assertTrue(boolean0)
        self.assertEqual(1, len(byteArray0))

    def test06(self) -> None:

        boolean0 = Base64.isBase642('56VOaaf))dx)"/:')
        self.assertFalse(boolean0)

    def test05(self) -> None:
        with pytest.raises(ValueError):
            Base64.Base645()
        verifyException("org.apache.commons.codec.binary.Base64", ValueError)

    def test04(self) -> None:

        byteArray0 = BaseNCodec.getChunkSeparator()
        try:
            Base64.encodeBase643(byteArray0, False, True, 4)
            self.fail("Expecting exception: ValueError")
        except ValueError as e:
            verifyException("org.apache.commons.codec.binary.Base64", e)

    def test03(self) -> None:

        boolean0 = Base64.isBase642("{iZ&Lz<")
        self.assertFalse(boolean0)

    def test02(self) -> None:

        byteArray0 = bytearray(1)
        codecPolicy0 = CodecPolicy.LENIENT
        base64_0 = Base64(0, byteArray0, True, codecPolicy0)
        baseNCodec_Context0 = Context()
        base64_0.decode1(byteArray0, 1492, 0, baseNCodec_Context0)
        self.assertTrue(base64_0.isUrlSafe())

    def test01(self) -> None:

        bigInteger0 = BigInteger(10)
        byteArray0 = Base64.toIntegerBytes(bigInteger0)
        base64_0 = Base64.Base641(0, byteArray0, True)
        base64_0.encode1(byteArray0, 0, 0)
        self.assertTrue(base64_0.isUrlSafe())

    def test00(self) -> None:

        byteArray0 = bytearray(1)
        byteArray0[0] = 123

        try:
            Base64.Base644(True)
            self.fail("Expecting exception: ValueError")
        except ValueError as e:
            verifyException("org.apache.commons.codec.binary.Base64", e)
