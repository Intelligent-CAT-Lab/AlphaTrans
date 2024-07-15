from __future__ import annotations
import time
import re
import os
from io import BytesIO
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.codec.CodecPolicy import *
from src.main.org.apache.commons.codec.binary.Base16 import *
from src.main.org.apache.commons.codec.binary.Base32 import *
from src.main.org.apache.commons.codec.binary.Base64 import *
from src.main.org.apache.commons.codec.binary.BaseNCodec import *
from src.main.org.apache.commons.codec.binary.BaseNCodecInputStream import *

# from src.test.org.apache.commons.codec.binary.BaseNCodecInputStream_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class BaseNCodecInputStream_ESTest(unittest.TestCase):

    def test25(self) -> None:

        byteArray0 = bytearray(4)
        codecPolicy0 = CodecPolicy.STRICT
        base64_0 = Base64(756, byteArray0, False, codecPolicy0)
        pipedInputStream0 = io.BytesIO(b"")
        baseNCodecInputStream0 = BaseNCodecInputStream(
            pipedInputStream0, base64_0, False
        )
        baseNCodecInputStream0.mark(0)
        self.assertFalse(baseNCodecInputStream0.markSupported())

    def test24(self) -> None:

        base64_0 = Base64.Base645()
        inputStream0 = io.BytesIO()
        baseNCodecInputStream0 = BaseNCodecInputStream(inputStream0, base64_0, False)
        boolean0 = baseNCodecInputStream0.markSupported()
        self.assertFalse(boolean0)

    def test23(self) -> None:

        base64_0 = Base64.Base645()
        inputStream0 = io.BytesIO()
        baseNCodecInputStream0 = BaseNCodecInputStream(inputStream0, base64_0, True)
        try:
            baseNCodecInputStream0.reset()
            self.fail("Expecting exception: IOException")

        except IOError as e:
            # mark/reset not supported
            self.assertEqual(str(e), "mark/reset not supported")

    def test22(self) -> None:

        base64_0 = Base64.Base645()
        inputStream0 = io.BytesIO()
        baseNCodecInputStream0 = BaseNCodecInputStream(inputStream0, base64_0, True)
        boolean0 = baseNCodecInputStream0.isStrictDecoding()
        self.assertFalse(boolean0)

    def test21(self) -> None:

        pipedInputStream0 = io.BytesIO()
        base32_0 = Base32.Base323(47)
        baseNCodecInputStream0 = BaseNCodecInputStream(
            pipedInputStream0, base32_0, True
        )
        int0 = baseNCodecInputStream0.available()
        self.assertEqual(1, int0)

    def test20(self) -> None:

        base64_0 = Base64.Base645()
        inputStream0 = io.BytesIO(b"")
        baseNCodecInputStream0 = BaseNCodecInputStream(inputStream0, base64_0, True)
        baseNCodecInputStream0.skip(76)
        int0 = baseNCodecInputStream0.available()
        self.assertEqual(0, int0)

    def test19(self) -> None:

        byteArray0 = bytearray(8)
        byteArrayInputStream0 = io.BytesIO(byteArray0)
        base32_0 = Base32.Base324(4)
        baseNCodecInputStream0 = BaseNCodecInputStream(
            byteArrayInputStream0, base32_0, False
        )
        int0 = baseNCodecInputStream0.read0()
        self.assertEqual(0, baseNCodecInputStream0.available())
        self.assertEqual(-1, int0)

    def test18(self) -> None:

        inputStream0 = io.BytesIO()
        base64_0 = Base64.Base645()
        baseNCodecInputStream0 = BaseNCodecInputStream(inputStream0, base64_0, True)
        byteArray0 = bytearray(0)

        try:
            baseNCodecInputStream0.read1(byteArray0, -1, -1)
            self.fail("Expecting exception: IndexOutOfBoundsException")

        except IndexError as e:
            self.verifyException(
                "org.apache.commons.codec.binary.BaseNCodecInputStream", e
            )

    def test17(self) -> None:

        byteArray0 = bytearray(8)
        byteArrayInputStream0 = io.BytesIO(byteArray0)
        base32_0 = Base32.Base320()
        baseNCodecInputStream0 = BaseNCodecInputStream(
            byteArrayInputStream0, base32_0, False
        )

        try:
            baseNCodecInputStream0.read1(byteArray0, 76, -752)
            self.fail("Expecting exception: IndexOutOfBoundsException")

        except IndexError as e:
            self.verifyException(
                "org.apache.commons.codec.binary.BaseNCodecInputStream", e
            )

    def test16(self) -> None:

        base64_0 = Base64.Base645()
        inputStream0 = io.BytesIO()
        baseNCodecInputStream0 = BaseNCodecInputStream(inputStream0, base64_0, True)
        byteArray0 = bytearray(0)

        try:
            baseNCodecInputStream0.read1(byteArray0, 64, 64)
            self.fail("Expecting exception: IndexOutOfBoundsException")

        except IndexError as e:
            self.verifyException(
                "org.apache.commons.codec.binary.BaseNCodecInputStream", e
            )

    def test15(self) -> None:

        byteArray0 = bytearray(1)
        byteArrayInputStream0 = io.BytesIO(byteArray0)
        base64_0 = Base64.Base645()
        baseNCodecInputStream0 = BaseNCodecInputStream(
            byteArrayInputStream0, base64_0, True
        )

        # Undeclared exception in Java code
        try:
            baseNCodecInputStream0.read1(byteArray0, 1, 1)
            self.fail("Expecting exception: IndexOutOfBoundsException")

        except IndexError as e:
            # no message in exception (getMessage() returned null)
            self.verifyException(
                "org.apache.commons.codec.binary.BaseNCodecInputStream", e
            )

    def test14(self) -> None:

        byteArray0 = bytearray(8)
        byteArrayInputStream0 = io.BytesIO(byteArray0)
        codecPolicy0 = CodecPolicy.LENIENT
        base16_0 = Base16(True, codecPolicy0)
        baseNCodecInputStream0 = BaseNCodecInputStream(
            byteArrayInputStream0, base16_0, True
        )
        int0 = baseNCodecInputStream0.read1(byteArray0, 0, 0)
        self.assertEqual(0, int0)

    def test13(self) -> None:

        byteArray0 = bytearray(8)
        byteArrayInputStream0 = io.BytesIO(byteArray0)
        base64_0 = Base64(byteArrayInputStream0, Base64.Base645(), True)
        baseNCodecInputStream0 = BaseNCodecInputStream(
            byteArrayInputStream0, base64_0, True
        )
        long0 = baseNCodecInputStream0.skip(76)
        self.assertEqual(0, baseNCodecInputStream0.available())
        self.assertEqual(12, long0)

    def test12(self) -> None:

        base64_0 = Base64.Base645()
        inputStream0 = io.BytesIO()
        baseNCodecInputStream0 = BaseNCodecInputStream(inputStream0, base64_0, True)

        with self.assertRaises(ValueError):
            baseNCodecInputStream0.skip(-1273)
            self.fail("Expecting exception: ValueError")

    def test11(self) -> None:

        base64_0 = Base64.Base645()
        inputStream0 = io.BytesIO()
        baseNCodecInputStream0 = BaseNCodecInputStream(inputStream0, base64_0, False)
        long0 = baseNCodecInputStream0.skip(0)
        self.assertEqual(0, long0)

    def test10(self) -> None:

        byteArray0 = bytearray(8)
        byteArrayInputStream0 = io.BytesIO(byteArray0)
        base32_0 = Base32.Base324(4)
        baseNCodecInputStream0 = BaseNCodecInputStream(
            byteArrayInputStream0, base32_0, False
        )
        int0 = baseNCodecInputStream0.read1(byteArray0, 4, 1)
        self.assertEqual(0, len(byteArrayInputStream0.read()))
        self.assertEqual(-1, int0)

    def test09(self) -> None:

        byteArray0 = bytearray(8)
        byteArrayInputStream0 = io.BytesIO(byteArray0)
        codecPolicy0 = CodecPolicy.LENIENT
        base16_0 = Base16(True, codecPolicy0)
        baseNCodecInputStream0 = BaseNCodecInputStream(
            byteArrayInputStream0, base16_0, True
        )
        int0 = baseNCodecInputStream0.read1(byteArray0, 0, 1)
        self.assertEqual(0, len(byteArrayInputStream0.read()))
        self.assertEqual(1, int0)

    def test08(self) -> None:

        byteArray0 = bytearray(8)
        byteArrayInputStream0 = io.BytesIO(byteArray0)
        base32_0 = Base32.Base323(1)
        baseNCodecInputStream0 = BaseNCodecInputStream(
            byteArrayInputStream0, base32_0, True
        )
        baseNCodecInputStream0.read0()
        int0 = baseNCodecInputStream0.read1(byteArray0, 1, 1)
        self.assertEqual(0, len(byteArrayInputStream0.read()))
        self.assertEqual(1, int0)

    def test07(self) -> None:

        byteArray0 = bytearray(3)
        byteArrayInputStream0 = io.BytesIO(byteArray0)
        baseNCodecInputStream0 = BaseNCodecInputStream(
            byteArrayInputStream0, None, False
        )

        with self.assertRaises(RuntimeError):
            baseNCodecInputStream0.isStrictDecoding()
            self.fail("Expecting exception: RuntimeError")

    def test06(self) -> None:

        base64_0 = Base64.Base645()
        pipedInputStream0 = io.PipedInputStream()
        baseNCodecInputStream0 = BaseNCodecInputStream(
            pipedInputStream0, base64_0, True
        )
        try:
            baseNCodecInputStream0.read0()
            self.fail("Expecting exception: IOException")

        except io.IOException as e:
            #
            # Pipe not connected
            #
            self.verifyException("java.io.PipedInputStream", e)

    def test05(self) -> None:

        byteArray0 = bytearray(8)
        byteArrayInputStream0 = io.BytesIO(byteArray0)
        base16_0 = Base16.Base162()
        baseNCodecInputStream0 = BaseNCodecInputStream(
            byteArrayInputStream0, base16_0, False
        )

        try:
            baseNCodecInputStream0.read0()
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            self.verifyException("org.apache.commons.codec.binary.Base16", e)

    def test04(self) -> None:

        inputStream0 = io.BytesIO()
        baseNCodecInputStream0 = BaseNCodecInputStream(inputStream0, None, False)

        with pytest.raises(RuntimeError):
            baseNCodecInputStream0.read0()
            pytest.fail("Expecting exception: RuntimeError")

    def test03(self) -> None:

        base64_0 = Base64.Base645()
        pipedInputStream0 = io.BytesIO()
        baseNCodecInputStream0 = BaseNCodecInputStream(
            pipedInputStream0, base64_0, False
        )

        try:
            baseNCodecInputStream0.read1(None, 1416, 64)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.assertEqual(type(e), RuntimeError)

    def test02(self) -> None:

        base64_0 = Base64.Base645()
        pipedInputStream0 = io.PipedInputStream(64)
        baseNCodecInputStream0 = BaseNCodecInputStream(
            pipedInputStream0, base64_0, False
        )
        try:
            baseNCodecInputStream0.skip(76)
            self.fail("Expecting exception: IOException")

        except io.IOException as e:
            #
            # Pipe not connected
            #
            self.verifyException("java.io.PipedInputStream", e)

    def test01(self) -> None:

        base32_0 = Base32.Base324(201)
        baseNCodecInputStream0 = BaseNCodecInputStream(None, base32_0, False)

        try:
            baseNCodecInputStream0.skip(1893)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.verifyException(
                "org.apache.commons.codec.binary.BaseNCodecInputStream", e
            )

    def test00(self) -> None:

        byteArray0 = bytearray(8)
        byteArrayInputStream0 = io.BytesIO(byteArray0)
        codecPolicy0 = CodecPolicy.STRICT
        base16_0 = Base16(False, codecPolicy0)
        baseNCodecInputStream0 = BaseNCodecInputStream(
            byteArrayInputStream0, base16_0, True
        )
        boolean0 = baseNCodecInputStream0.isStrictDecoding()
        self.assertTrue(boolean0)
