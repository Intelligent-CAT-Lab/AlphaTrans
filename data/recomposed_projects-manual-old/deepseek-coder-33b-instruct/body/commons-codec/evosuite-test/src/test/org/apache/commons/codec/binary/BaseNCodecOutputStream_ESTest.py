from __future__ import annotations
import time
import re
import mock
import os
from io import BytesIO
from io import StringIO
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.codec.CodecPolicy import *
from src.main.org.apache.commons.codec.binary.Base16 import *
from src.main.org.apache.commons.codec.binary.Base32 import *
from src.main.org.apache.commons.codec.binary.Base64 import *
from src.main.org.apache.commons.codec.binary.BaseNCodec import *
from src.main.org.apache.commons.codec.binary.BaseNCodecOutputStream import *

# from src.test.org.apache.commons.codec.binary.BaseNCodecOutputStream_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class BaseNCodecOutputStream_ESTest(unittest.TestCase):

    def test25(self) -> None:

        pipedOutputStream0 = io.BytesIO()
        base16_0 = Base16.Base162()
        baseNCodecOutputStream0 = BaseNCodecOutputStream(
            pipedOutputStream0, base16_0, True
        )
        try:
            baseNCodecOutputStream0.write(76)
            self.fail("Expecting exception: IOException")

        except IOError as e:
            # Pipe not connected
            self.verifyException("java.io.PipedOutputStream", e)

    def test24(self) -> None:

        mockFileOutputStream0 = io.StringIO("zpB<J*VSf#j>|7")
        mockPrintStream0 = io.TextIOWrapper(mockFileOutputStream0)
        base16_0 = Base16.Base161(True)
        baseNCodecOutputStream0 = BaseNCodecOutputStream(
            mockPrintStream0, base16_0, True
        )
        boolean0 = baseNCodecOutputStream0.isStrictDecoding()
        self.assertFalse(boolean0)

    def test23(self) -> None:

        pipedOutputStream0 = io.BytesIO()
        byteArray0 = bytearray()
        codecPolicy0 = CodecPolicy.STRICT
        base64_0 = Base64(76, byteArray0, False, codecPolicy0)
        baseNCodecOutputStream0 = BaseNCodecOutputStream(
            pipedOutputStream0, base64_0, False
        )
        baseNCodecOutputStream0.close()
        self.assertTrue(baseNCodecOutputStream0.isStrictDecoding())

    def test22(self) -> None:

        pipedOutputStream0 = io.BytesIO()
        base32_0 = Base32.Base321(True)
        baseNCodecOutputStream0 = BaseNCodecOutputStream(
            pipedOutputStream0, base32_0, True
        )
        baseNCodecOutputStream0.write(76)
        try:
            baseNCodecOutputStream0.close()
            self.fail("Expecting exception: IOException")

        except IOError as e:
            # Pipe not connected
            self.verifyException("java.io.PipedOutputStream", e)

    def test21(self) -> None:

        pipedOutputStream0 = io.BytesIO()
        byteArray0 = bytearray(2)
        base64_0 = Base64.Base645()
        baseNCodecOutputStream0 = BaseNCodecOutputStream(
            pipedOutputStream0, base64_0, False
        )

        try:
            baseNCodecOutputStream0.write0(byteArray0, -124, 76)
            self.fail("Expecting exception: IndexOutOfBoundsException")

        except IndexError as e:
            self.verifyException(
                "org.apache.commons.codec.binary.BaseNCodecOutputStream", e
            )

    def test20(self) -> None:

        pipedOutputStream0 = io.BytesIO()
        base32_0 = Base32.Base321(True)
        baseNCodecOutputStream0 = BaseNCodecOutputStream(
            pipedOutputStream0, base32_0, True
        )
        byteArray0 = bytearray(2)

        try:
            baseNCodecOutputStream0.write0(byteArray0, 76, -75)
            self.fail("Expecting exception: IndexOutOfBoundsException")

        except IndexError as e:
            self.verifyException(
                "org.apache.commons.codec.binary.BaseNCodecOutputStream", e
            )

    def test19(self) -> None:

        mockFile0 = MockFile("I", "I")
        mockPrintStream0 = MockPrintStream(mockFile0)
        base32_0 = Base32.Base321(True)
        baseNCodecOutputStream0 = BaseNCodecOutputStream(
            mockPrintStream0, base32_0, False
        )
        byteArray0 = bytearray(5)
        # Undeclared exception in Java
        try:
            baseNCodecOutputStream0.write0(byteArray0, 76, 866)
            self.fail("Expecting exception: IndexOutOfBoundsException")

        except IndexError as e:
            # no message in exception (getMessage() returned null)
            self.verifyException(
                "org.apache.commons.codec.binary.BaseNCodecOutputStream", e
            )

    def test18(self) -> None:

        pipedOutputStream0 = io.BytesIO()
        base32_0 = Base32.Base322(True, 0)
        baseNCodecOutputStream0 = BaseNCodecOutputStream(
            pipedOutputStream0, base32_0, True
        )
        byteArray0 = bytearray()

        try:
            baseNCodecOutputStream0.write0(byteArray0, 0, 64)
            self.fail("Expecting exception: IndexOutOfBoundsException")

        except IndexError as e:
            self.verifyException(
                "org.apache.commons.codec.binary.BaseNCodecOutputStream", e
            )

    def test17(self) -> None:

        pipedOutputStream0 = io.BytesIO()
        base32_0 = Base32.Base320()
        baseNCodecOutputStream0 = BaseNCodecOutputStream(
            pipedOutputStream0, base32_0, True
        )
        byteArray0 = bytearray(2)
        baseNCodecOutputStream0.write0(byteArray0, 0, 0)
        self.assertEqual(2, len(byteArray0))

    def test16(self) -> None:

        pipedOutputStream0 = io.BytesIO()
        byteArray0 = bytearray()
        codecPolicy0 = CodecPolicy.STRICT
        base64_0 = Base64(76, byteArray0, False, codecPolicy0)
        baseNCodecOutputStream0 = BaseNCodecOutputStream(
            pipedOutputStream0, base64_0, False
        )
        baseNCodecOutputStream0.write(76)

        try:
            baseNCodecOutputStream0.close()
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            self.verifyException("org.apache.commons.codec.binary.Base64", e)

    def test15(self) -> None:

        mockFile0 = MockFile("I", "I")
        mockPrintStream0 = MockPrintStream(mockFile0)
        base32_0 = Base32.Base321(True)
        baseNCodecOutputStream0 = BaseNCodecOutputStream(
            mockPrintStream0, base32_0, False
        )
        baseNCodecOutputStream0.flush0()
        self.assertFalse(baseNCodecOutputStream0.isStrictDecoding())

    def test14(self) -> None:

        mockFile0 = MockFile("I")
        mockPrintStream0 = MockPrintStream(mockFile0)
        base32_0 = Base32.Base322(True, 0)
        baseNCodecOutputStream0 = BaseNCodecOutputStream(
            mockPrintStream0, base32_0, True
        )
        baseNCodecOutputStream0.write1(0)
        self.assertFalse(baseNCodecOutputStream0.isStrictDecoding())

    def test13(self) -> None:

        mockFile0 = MockFile("I", "I")
        mockPrintStream0 = MockPrintStream(mockFile0)
        base32_0 = Base32.Base321(True)
        baseNCodecOutputStream0 = BaseNCodecOutputStream(
            mockPrintStream0, base32_0, False
        )
        baseNCodecOutputStream0.eof()
        self.assertFalse(baseNCodecOutputStream0.isStrictDecoding())

    def test12(self) -> None:

        mockFile0 = io.StringIO("I")
        mockPrintStream0 = io.TextIOWrapper(mockFile0)
        base32_0 = Base32.Base322(True, 0)
        baseNCodecOutputStream0 = BaseNCodecOutputStream(
            mockPrintStream0, base32_0, True
        )
        byteArray0 = bytearray(5)
        baseNCodecOutputStream0.write0(byteArray0, 0, 1)
        self.assertEqual(byteArray0, bytearray([0, 0, 0, 0, 0]))

    def test11(self) -> None:

        mockFileOutputStream0 = io.BytesIO()
        base16_0 = Base16(mockFileOutputStream0, BaseNCodec(), False)
        baseNCodecOutputStream0 = BaseNCodecOutputStream(
            mockFileOutputStream0, base16_0, False
        )
        byteArray0 = bytearray(4)
        # Undeclared exception in Java
        try:
            baseNCodecOutputStream0.write0(byteArray0, 1, 1)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            #
            # Invalid octet in encoded value: 0
            #
            self.assertEqual(str(e), "Offset and length exceed array length")

    def test10(self) -> None:

        pipedOutputStream0 = io.BytesIO()
        baseNCodecOutputStream0 = BaseNCodecOutputStream(pipedOutputStream0, None, True)

        try:
            baseNCodecOutputStream0.close()
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.assertEqual(str(e.__class__), "<class 'RuntimeError'>")

    def test09(self) -> None:

        outputStream0 = io.BytesIO()
        baseNCodecOutputStream0 = BaseNCodecOutputStream(outputStream0, None, True)

        try:
            baseNCodecOutputStream0.eof()
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.assertEqual(str(e), "")
            self.assertIsInstance(e, RuntimeError)

    def test08(self) -> None:

        base32_0 = Base32.Base322(True, 62)
        baseNCodecOutputStream0 = BaseNCodecOutputStream(None, base32_0, True)

        try:
            baseNCodecOutputStream0.flush0()
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.verifyException(
                "org.apache.commons.codec.binary.BaseNCodecOutputStream", e
            )

    def test07(self) -> None:

        pipedOutputStream0 = io.BytesIO()
        base16_0 = Base16.Base162()
        baseNCodecOutputStream0 = BaseNCodecOutputStream(
            pipedOutputStream0, base16_0, False
        )

        with self.assertRaises(ValueError) as context:
            baseNCodecOutputStream0.write(64)

        self.assertTrue("Expecting exception: ValueError" in str(context.exception))
        self.assertTrue("Invalid octet in encoded value: 64" in str(context.exception))
        self.assertTrue(
            "org.apache.commons.codec.binary.Base16" in str(context.exception)
        )

    def test06(self) -> None:

        pipedOutputStream0 = io.BytesIO()
        baseNCodecOutputStream0 = BaseNCodecOutputStream(pipedOutputStream0, None, True)

        with pytest.raises(RuntimeError):
            baseNCodecOutputStream0.write(-1094)
            self.fail("Expecting exception: RuntimeError")

    def test05(self) -> None:

        pipedOutputStream0 = io.BytesIO()
        base32_0 = Base32.Base322(True, 0)
        byteArray0 = bytearray(9)
        baseNCodecOutputStream0 = BaseNCodecOutputStream(
            pipedOutputStream0, base32_0, True
        )
        try:
            baseNCodecOutputStream0.write0(byteArray0, 0, 9)
            self.fail("Expecting exception: IOException")

        except IOError as e:
            # Pipe not connected
            self.verifyException("java.io.PipedOutputStream", e)

    def test04(self) -> None:

        pipedOutputStream0 = io.BytesIO()
        base32_0 = Base32.Base320()
        baseNCodecOutputStream0 = BaseNCodecOutputStream(
            pipedOutputStream0, base32_0, False
        )

        with self.assertRaises(ValueError):
            baseNCodecOutputStream0.write0(None, 76, 64)

    def test03(self) -> None:

        pipedOutputStream0 = io.BytesIO()
        base16_0 = Base16.Base162()
        baseNCodecOutputStream0 = BaseNCodecOutputStream(
            pipedOutputStream0, base16_0, True
        )
        try:
            baseNCodecOutputStream0.write1(64)
            self.fail("Expecting exception: IOException")

        except IOError as e:
            # Pipe not connected
            self.verifyException("java.io.PipedOutputStream", e)

    def test02(self) -> None:

        pipedOutputStream0 = io.BytesIO()
        mockPrintStream0 = pipedOutputStream0
        base16_0 = Base16.Base162()
        baseNCodecOutputStream0 = BaseNCodecOutputStream(
            mockPrintStream0, base16_0, False
        )

        try:
            baseNCodecOutputStream0.write1(4455)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            self.assertEqual(str(e), "i must be non-negative")

    def test01(self) -> None:

        baseNCodecOutputStream0 = BaseNCodecOutputStream(None, None, False)

        try:
            baseNCodecOutputStream0.write1(73)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.verifyException(
                "org.apache.commons.codec.binary.BaseNCodecOutputStream", e
            )

    def test00(self) -> None:

        mockFileOutputStream0 = io.BytesIO()
        byteArray0 = bytearray(8)
        codecPolicy0 = CodecPolicy.STRICT
        base64_0 = Base64(51, byteArray0, False, codecPolicy0)
        baseNCodecOutputStream0 = BaseNCodecOutputStream(
            mockFileOutputStream0, base64_0, False
        )
        boolean0 = baseNCodecOutputStream0.isStrictDecoding()
        self.assertTrue(boolean0)
