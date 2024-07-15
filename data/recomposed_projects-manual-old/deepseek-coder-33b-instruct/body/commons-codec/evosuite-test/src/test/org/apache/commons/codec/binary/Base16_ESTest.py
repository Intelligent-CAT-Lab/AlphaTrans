from __future__ import annotations
import time
import re
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.codec.CodecPolicy import *
from src.main.org.apache.commons.codec.binary.Base16 import *

# from src.test.org.apache.commons.codec.binary.Base16_ESTest_scaffolding import *
from src.main.org.apache.commons.codec.binary.BaseNCodec import *

# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class Base16_ESTest(unittest.TestCase):

    def test25(self) -> None:

        base16_0 = Base16.Base162()
        baseNCodec_Context0 = Context()
        base16_0.encode2(None, -828, -3015, baseNCodec_Context0)
        base16_0.decode1(None, 10, 10, baseNCodec_Context0)
        self.assertEqual(64, BaseNCodec.PEM_CHUNK_SIZE)

    def test24(self) -> None:

        base16_0 = Base16.Base161(True)
        byteArray0 = bytearray(6)
        byteArray0[1] = 103
        boolean0 = base16_0._containsAlphabetOrPad(byteArray0)
        self.assertFalse(boolean0)

    def test23(self) -> None:

        base16_0 = Base16.Base162()
        baseNCodec_Context0 = Context()
        byteArray0 = bytearray(9)
        byteArray0[2] = 50
        byteArray0[3] = 66
        byteArray0[4] = 50
        base16_0.decode1(byteArray0, 3, 3, baseNCodec_Context0)

        # Undeclared exception in Java code
        try:
            base16_0.decode1(byteArray0, -1, 0, baseNCodec_Context0)
            self.fail("Expecting exception: ArrayIndexOutOfBoundsException")

        except IndexError as e:
            # Index -1 out of bounds for length 9
            self.assertEqual(str(e), "array index out of range")

    def test21(self) -> None:

        base16_0 = Base16.Base161(False)
        baseNCodec_Context0 = Context()
        byteArray0 = bytearray(1)
        byteArray0[0] = (-59).to_bytes(1, "big", signed=True)[0]

        try:
            base16_0.decode1(byteArray0, 0, 7, baseNCodec_Context0)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # Invalid octet in encoded value: -59
            self.verifyException("org.apache.commons.codec.binary.Base16", e)

    def test20(self) -> None:

        base16_0 = Base16.Base162()
        byteArray0 = bytearray()
        baseNCodec_Context0 = Context()
        base16_0.decode1(byteArray0, -46, -46, baseNCodec_Context0)
        base16_0.encode2(byteArray0, -46, 102, baseNCodec_Context0)
        self.assertEqual(76, BaseNCodec.MIME_CHUNK_SIZE)

    def test19(self) -> None:

        base16_0 = Base16.Base162()
        byteArray0 = [0] * 3
        baseNCodec_Context0 = Context()

        try:
            base16_0.encode2(byteArray0, 7, 2147483639, baseNCodec_Context0)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            self.assertEqual(
                str(e), "Input length exceeds maximum size for encoded data: 2147483639"
            )

    def test18(self) -> None:
        base16_0 = Base16.Base162()
        boolean0 = base16_0.isInAlphabet0(bytearray([-66])[0])
        self.assertFalse(boolean0)

    def test17(self) -> None:

        base16_0 = Base16.Base162()
        byteArray0 = bytearray(1)
        boolean0 = base16_0._containsAlphabetOrPad(byteArray0)
        self.assertFalse(boolean0)

    def test16(self) -> None:
        base16_0 = Base16.Base162()
        boolean0 = base16_0.isInAlphabet0(65)
        self.assertTrue(boolean0)

    def test15(self) -> None:

        codecPolicy0 = CodecPolicy.STRICT
        base16_0 = Base16(False, codecPolicy0)
        byteArray0 = bytearray()
        baseNCodec_Context0 = Context()
        baseNCodec_Context0.ibitWorkArea = 64

        try:
            base16_0.decode1(byteArray0, -3695, -3695, baseNCodec_Context0)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            self.verifyException("org.apache.commons.codec.binary.Base16", e)

    def test14(self) -> None:

        codecPolicy0 = CodecPolicy.STRICT
        base16_0 = Base16(True, codecPolicy0)
        self.assertEqual(76, BaseNCodec.MIME_CHUNK_SIZE)

    def test13(self) -> None:

        base16_0 = None
        try:
            base16_0 = Base16(False, None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            # codecPolicy
            # verifyException("java.util.Objects", e)
            self.assertIsInstance(e, RuntimeError)

    def test12(self) -> None:

        base16_0 = Base16.Base162()

        try:
            base16_0.decode1(None, 50, 50, None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.assertEqual(str(e.__class__), "<class 'RuntimeError'>")

    def test11(self) -> None:

        base16_0 = Base16.Base162()
        byteArray0 = bytearray(0)
        baseNCodec_Context0 = Context()

        try:
            base16_0.encode2(byteArray0, 2, 2, baseNCodec_Context0)
            self.fail("Expecting exception: ArrayIndexOutOfBoundsException")

        except IndexError as e:
            # Index 2 out of bounds for length 0
            self.assertEqual(str(e), "list index out of range")

    def test10(self) -> None:

        base16_0 = Base16.Base162()
        byteArray0 = [0] * 23

        try:
            base16_0.encode2(byteArray0, -1326, -1326, None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.assertIsInstance(e, RuntimeError)
            self.assertEqual(str(e), "RuntimeError")

    def test08(self) -> None:

        base16_0 = Base16.Base161(False)
        baseNCodec_Context0 = Context()
        baseNCodec_Context0.ibitWorkArea = -2088
        base16_0.decode1(None, 380, -3898, baseNCodec_Context0)
        self.assertEqual(BaseNCodec.PEM_CHUNK_SIZE, 64)

    def test07(self) -> None:

        base16_0 = Base16.Base161(False)
        baseNCodec_Context0 = Context()
        baseNCodec_Context0.ibitWorkArea = -2088
        byteArray0 = bytearray(8)

        try:
            base16_0.decode1(byteArray0, 25, 74, baseNCodec_Context0)
            self.fail("Expecting exception: ArrayIndexOutOfBoundsException")

        except IndexError as e:
            self.assertEqual(str(e), "array index out of range")

    def test06(self) -> None:

        base16_0 = Base16.Base161(False)
        baseNCodec_Context0 = Context()
        byteArray0 = bytearray(3)

        try:
            base16_0.decode1(byteArray0, -1459, 1, baseNCodec_Context0)
            self.fail("Expecting exception: ArrayIndexOutOfBoundsException")

        except IndexError as e:
            self.assertEqual(str(e), "array index out of range")

    def test05(self) -> None:

        base16_0 = Base16.Base162()
        byteArray0 = [0]
        baseNCodec_Context0 = Context()
        baseNCodec_Context0.ibitWorkArea = 76

        try:
            base16_0.decode1(byteArray0, 49, 49, baseNCodec_Context0)
            self.fail("Expecting exception: ArrayIndexOutOfBoundsException")

        except IndexError as e:
            self.assertEqual(str(e), "array index out of range")

    def test04(self) -> None:

        byteArray0 = bytearray(6)
        byteArray0[0] = 71
        base16_0 = Base16.Base161(False)
        # Undeclared exception in Java
        try:
            base16_0.decode0(byteArray0)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            #
            # Invalid octet in encoded value: 71
            #
            self.verifyException("org.apache.commons.codec.binary.Base16", e)

    def test03(self) -> None:

        base16_0 = Base16.Base161(False)
        baseNCodec_Context0 = Context()
        base16_0.encode2(None, 10, 0, baseNCodec_Context0)
        self.assertEqual(BaseNCodec.MIME_CHUNK_SIZE, 76)

    def test02(self) -> None:

        base16_0 = Base16.Base162()
        baseNCodec_Context0 = Context()
        base16_0.encode2(None, 2147483639, 9, baseNCodec_Context0)
        self.assertEqual(76, BaseNCodec.MIME_CHUNK_SIZE)

    def test00(self) -> None:

        base16_0 = Base16.Base161(False)
        byteArray0 = bytearray(7)
        byteArray0[4] = -59
        string0 = base16_0.encodeAsString(byteArray0)
        self.assertEqual("00000000C50000", string0)
