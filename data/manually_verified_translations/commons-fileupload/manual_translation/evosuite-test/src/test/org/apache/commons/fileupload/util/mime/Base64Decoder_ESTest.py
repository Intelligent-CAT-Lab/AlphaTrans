from __future__ import annotations
import time
import re
import os
import typing
from typing import *
from io import BytesIO
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.fileupload.util.mime.Base64Decoder import *

# from src.test.org.apache.commons.fileupload.util.mime.Base64Decoder_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class Base64Decoder_ESTest(unittest.TestCase):

    def test8(self) -> None:

        byteArrayOutputStream0 = io.BytesIO()
        byteArray0 = bytearray(4)
        int0 = Base64Decoder.decode(byteArray0, byteArrayOutputStream0)
        self.assertEqual(0, int0)

    def test7(self) -> None:

        byteArrayOutputStream0 = io.BytesIO()
        byteArray0 = bytearray(4)
        byteArray0[0] = 103
        try:
            Base64Decoder.decode(byteArray0, byteArrayOutputStream0)
            self.fail("Expecting exception: IOException")

        except IOError as e:
            #
            # Invalid Base64 input: truncated
            #
            self.assertEqual(str(e), "Invalid Base64 input: truncated")

    def test6(self) -> None:

        byteArrayOutputStream0 = io.BytesIO()
        byteArray0 = bytearray(4)
        byteArray0[0] = 103
        byteArray0[1] = 103
        byteArray0[2] = 103
        byteArray0[3] = 61
        int0 = Base64Decoder.decode(byteArray0, byteArrayOutputStream0)
        self.assertEqual("\uFFFD\b", byteArrayOutputStream0.getvalue().decode())
        self.assertEqual(2, int0)

    def test5(self) -> None:

        byteArrayOutputStream0 = io.BytesIO()
        byteArray0 = bytearray(4)
        byteArray0[0] = 61
        byteArray0[1] = 61
        byteArray0[2] = 61
        byteArray0[3] = 61
        try:
            Base64Decoder.decode(byteArray0, byteArrayOutputStream0)
            self.fail("Expecting exception: IOException")

        except IOError as e:
            #
            # Invalid Base64 input: incorrect padding, first two bytes cannot be padding
            #
            self.assertEqual(
                str(e),
                "Invalid Base64 input: incorrect padding, first two bytes cannot be padding",
            )

    def test4(self) -> None:

        byteArrayOutputStream0 = io.BytesIO()
        byteArray0 = bytearray(4)
        byteArray0[0] = 103
        byteArray0[1] = 61
        byteArray0[2] = 103
        byteArray0[3] = 103
        try:
            Base64Decoder.decode(byteArray0, byteArrayOutputStream0)
            self.fail("Expecting exception: IOException")

        except IOError as e:
            #
            # Invalid Base64 input: incorrect padding, first two bytes cannot be padding
            #
            self.assertEqual(
                str(e),
                "Invalid Base64 input: incorrect padding, first two bytes cannot be padding",
            )

    def test3(self) -> None:

        byteArrayOutputStream0 = io.BytesIO()
        byteArray0 = bytearray(5)
        byteArray0[0] = 65
        byteArray0[1] = 65
        byteArray0[2] = 65
        byteArray0[3] = 65
        int0 = Base64Decoder.decode(byteArray0, byteArrayOutputStream0)
        self.assertEqual(3, len(byteArrayOutputStream0.getvalue()))
        self.assertEqual(3, int0)

    def test2(self) -> None:

        byteArrayOutputStream0 = io.BytesIO()
        byteArray0 = bytearray(4)
        byteArray0[0] = 104
        byteArray0[1] = 104
        byteArray0[2] = 61
        byteArray0[3] = 104
        try:
            Base64Decoder.decode(byteArray0, byteArrayOutputStream0)
            self.fail("Expecting exception: IOException")

        except IOError as e:
            #
            # Invalid Base64 input: incorrect padding, 4th byte must be padding if 3rd byte is
            #
            self.assertEqual(
                str(e),
                "Invalid Base64 input: incorrect padding, 4th byte must be padding if 3rd byte is",
            )

    def test1(self) -> None:

        try:
            Base64Decoder.decode(None, None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.assertIsInstance(e, TypeError)
            self.assertEqual(
                str(e), "decode() missing 1 required positional argument: 'out'"
            )

    def test0(self) -> None:

        byteArrayOutputStream0 = io.BytesIO()
        byteArray0 = bytearray(5)
        byteArray0[0] = 103
        byteArray0[1] = 115
        byteArray0[2] = 61
        byteArray0[4] = 61
        int0 = Base64Decoder.decode(byteArray0, byteArrayOutputStream0)
        self.assertEqual("\uFFFD", byteArrayOutputStream0.getvalue().decode())
        self.assertEqual(1, int0)
