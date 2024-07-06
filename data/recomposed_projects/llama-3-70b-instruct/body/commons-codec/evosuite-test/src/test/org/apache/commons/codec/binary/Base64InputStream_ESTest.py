from __future__ import annotations
import time
import re
import mock
import os
import enum
from io import BytesIO
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.codec.CodecPolicy import *
from src.main.org.apache.commons.codec.binary.Base64InputStream import *

# from src.test.org.apache.commons.codec.binary.Base64InputStream_ESTest_scaffolding import *
from src.main.org.apache.commons.codec.binary.BaseNCodecInputStream import *

# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *
# from src.main.org.evosuite.runtime.ViolatedAssumptionAnswer import *
# from src.main.org.evosuite.shaded.org.mockito.Mockito import *
# from src.main.org.evosuite.shaded.org.mockito.stubbing.Answer import *
# from src.main.org.evosuite.shaded.org.mockito.stubbing.Stubber import *


class Base64InputStream_ESTest(unittest.TestCase):

    def test4(self) -> None:

        baseNCodecInputStream0 = Base64InputStream.Base64InputStream0(None)
        self.assertEqual(1, baseNCodecInputStream0.available())

    def test3(self) -> None:

        enumeration0 = unittest.mock.Mock(spec=Enumeration)
        enumeration0.hasMoreElements.return_value = False
        sequenceInputStream0 = SequenceInputStream(enumeration0)
        byteArray0 = bytearray(5)
        baseNCodecInputStream0 = Base64InputStream.Base64InputStream2(
            sequenceInputStream0, True, 752, byteArray0
        )
        self.assertFalse(baseNCodecInputStream0.markSupported())

    def test2(self) -> None:

        pipedInputStream0 = io.BytesIO()
        byteArray0 = bytearray(4)
        codecPolicy0 = CodecPolicy.STRICT
        base64InputStream0 = Base64InputStream(
            pipedInputStream0, False, 0, byteArray0, codecPolicy0
        )
        dataInputStream0 = io.BufferedReader(base64InputStream0)
        baseNCodecInputStream0 = Base64InputStream.Base64InputStream1(
            dataInputStream0, False
        )
        self.assertEqual(1, baseNCodecInputStream0.available())

    def test1(self) -> None:

        byteArray0 = bytearray(1)
        byteArray0[0] = 56
        codecPolicy0 = CodecPolicy.LENIENT
        base64InputStream0 = None
        try:
            base64InputStream0 = Base64InputStream(
                None, True, 0, byteArray0, codecPolicy0
            )
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # lineSeparator must not contain base64 characters: [8]
            self.verifyException("org.apache.commons.codec.binary.Base64", e)

    def test0(self) -> None:

        byteArray0 = bytearray(2)
        byteArray0[0] = 65

        try:
            Base64InputStream.Base64InputStream2(None, True, 0, byteArray0)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # lineSeparator must not contain base64 characters: [A\u0000]
            self.verifyException("org.apache.commons.codec.binary.Base64", e)
