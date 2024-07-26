from __future__ import annotations
import time
import re
import os
from io import BytesIO
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.fileupload.util.mime.QuotedPrintableDecoder import *

# from src.test.org.apache.commons.fileupload.util.mime.QuotedPrintableDecoder_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class QuotedPrintableDecoder_ESTest(unittest.TestCase):

    def test9(self) -> None:

        byteArrayOutputStream0 = io.BytesIO()
        byteArray0 = bytearray(1)
        byteArray0[0] = 95
        int0 = QuotedPrintableDecoder.decode(byteArray0, byteArrayOutputStream0)
        self.assertEqual(1, len(byteArrayOutputStream0.getvalue()))
        self.assertEqual(0, int0)

    def test8(self) -> None:

        byteArrayOutputStream0 = io.BytesIO(b"\x00" * 61)
        byteArray0 = bytearray(3)
        byteArray0[0] = 61

        try:
            QuotedPrintableDecoder.decode(byteArray0, byteArrayOutputStream0)
            self.fail("Expecting exception: IOException")

        except IOError as e:
            # Invalid quoted printable encoding: not a valid hex digit: 0
            self.assertEqual(
                str(e), "Invalid quoted printable encoding; not a valid hex digit: 0"
            )

    def test7(self) -> None:

        byteArrayOutputStream0 = io.BytesIO(b"\x3D")
        byteArray0 = bytearray(b"\x3D")

        try:
            QuotedPrintableDecoder.decode(byteArray0, byteArrayOutputStream0)
            self.fail("Expecting exception: IOException")

        except IOError as e:
            #
            # Invalid quoted printable encoding; truncated escape sequence
            #
            self.assertEqual(
                str(e), "Invalid quoted printable encoding; truncated escape sequence"
            )

    def test6(self) -> None:

        byteArrayOutputStream0 = io.BytesIO()
        byteArray0 = bytearray(3)
        byteArray0[0] = 61
        byteArray0[1] = 13
        try:
            QuotedPrintableDecoder.decode(byteArray0, byteArrayOutputStream0)
            self.fail("Expecting exception: IOException")

        except IOError as e:
            #
            # Invalid quoted printable encoding; CR must be followed by LF
            #
            self.assertEqual(
                str(e), "Invalid quoted printable encoding; CR must be followed by LF"
            )

    def test5(self) -> None:

        byteArrayOutputStream0 = io.BytesIO(b"")
        byteArray0 = bytearray(6)
        byteArray0[1] = 61
        byteArray0[2] = 51
        try:
            QuotedPrintableDecoder.decode(byteArray0, byteArrayOutputStream0)
            self.fail("Expecting exception: IOException")

        except IOError as e:
            #
            # Invalid quoted printable encoding: not a valid hex digit: 0
            #
            self.assertEqual(
                str(e), "Invalid quoted printable encoding; not a valid hex digit: 0"
            )

    def test4(self) -> None:

        byteArray0 = bytearray(8)

        try:
            QuotedPrintableDecoder.decode(byteArray0, None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.assertEqual(str(e), "")
            self.assertEqual(type(e).__name__, "RuntimeError")

    def test3(self) -> None:

        byteArray0 = bytearray(6)
        byteArray0[1] = 95
        byteArrayOutputStream0 = io.BytesIO()
        int0 = QuotedPrintableDecoder.decode(byteArray0, byteArrayOutputStream0)
        self.assertEqual(6, len(byteArrayOutputStream0.getvalue()))
        self.assertEqual(5, int0)

    def test2(self) -> None:

        byteArray0 = bytearray(6)
        byteArray0[0] = 97
        byteArrayOutputStream0 = io.BytesIO()
        int0 = QuotedPrintableDecoder.decode(byteArray0, byteArrayOutputStream0)
        self.assertEqual(6, len(byteArrayOutputStream0.getvalue()))
        self.assertEqual(6, int0)

    def test1(self) -> None:

        byteArray0 = bytearray(3)
        byteArray0[1] = 61
        byteArrayOutputStream0 = io.BytesIO(61)
        try:
            QuotedPrintableDecoder.decode(byteArray0, byteArrayOutputStream0)
            self.fail("Expecting exception: IOException")

        except IOError as e:
            #
            # Invalid quoted printable encoding; truncated escape sequence
            #
            self.assertEqual(
                str(e), "Invalid quoted printable encoding; truncated escape sequence"
            )

    def test0(self) -> None:

        byteArrayOutputStream0 = io.BytesIO()
        byteArray0 = bytearray(9)
        byteArray0[3] = 61
        byteArray0[4] = 13
        byteArray0[5] = 13
        try:
            QuotedPrintableDecoder.decode(byteArray0, byteArrayOutputStream0)
            self.fail("Expecting exception: IOException")

        except IOError as e:
            #
            # Invalid quoted printable encoding; CR must be followed by LF
            #
            self.assertEqual(
                str(e), "Invalid quoted printable encoding; CR must be followed by LF"
            )
