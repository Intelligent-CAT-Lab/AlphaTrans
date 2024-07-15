from __future__ import annotations
import time
import re
import mock
import os
from io import BytesIO
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.codec.CodecPolicy import *
from src.main.org.apache.commons.codec.binary.Base64OutputStream import *

# from src.test.org.apache.commons.codec.binary.Base64OutputStream_ESTest_scaffolding import *
from src.main.org.apache.commons.codec.binary.BaseNCodecOutputStream import *

# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class Base64OutputStream_ESTest(unittest.TestCase):

    def test4(self) -> None:

        byteArray0 = bytearray(0)
        codecPolicy0 = CodecPolicy.LENIENT
        base64OutputStream0 = Base64OutputStream(
            None, False, 0, byteArray0, codecPolicy0
        )
        self.assertFalse(base64OutputStream0.isStrictDecoding())

    def test3(self) -> None:

        baseNCodecOutputStream0 = Base64OutputStream.Base64OutputStream2(
            None, True, -907, None
        )
        assert not baseNCodecOutputStream0.isStrictDecoding()

    def test2(self) -> None:

        baseNCodecOutputStream0 = Base64OutputStream.Base64OutputStream0(None)
        byteArray0 = bytearray(1)
        byteArray0[0] = 66
        codecPolicy0 = CodecPolicy.LENIENT
        base64OutputStream0 = None
        try:
            base64OutputStream0 = Base64OutputStream(
                baseNCodecOutputStream0, True, 1074, byteArray0, codecPolicy0
            )
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            #
            # lineSeparator must not contain base64 characters: [B]
            #
            self.verifyException("org.apache.commons.codec.binary.Base64", e)

    def test1(self) -> None:

        mockFileOutputStream0 = io.BytesIO(
            b"Parameter supplied to Base-N decode is not a byte[] or a String"
        )
        baseNCodecOutputStream0 = Base64OutputStream.Base64OutputStream1(
            mockFileOutputStream0, False
        )
        assert not baseNCodecOutputStream0.isStrictDecoding()

    def test0(self) -> None:

        byteArrayOutputStream0 = io.BytesIO()
        byteArray0 = bytearray(1)
        byteArray0[0] = 116

        try:
            Base64OutputStream.Base64OutputStream2(
                byteArrayOutputStream0, False, 0, byteArray0
            )
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            verifyException("org.apache.commons.codec.binary.Base64", e)
