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
from src.main.org.apache.commons.codec.binary.Base32OutputStream import *

# from src.test.org.apache.commons.codec.binary.Base32OutputStream_ESTest_scaffolding import *
from src.main.org.apache.commons.codec.binary.BaseNCodecOutputStream import *

# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class Base32OutputStream_ESTest(unittest.TestCase):

    def test3(self) -> None:

        pipedOutputStream0 = io.BytesIO()
        baseNCodecOutputStream0 = Base32OutputStream.Base32OutputStream0(
            pipedOutputStream0
        )
        codecPolicy0 = CodecPolicy.LENIENT
        base32OutputStream0 = None
        try:
            base32OutputStream0 = Base32OutputStream(
                baseNCodecOutputStream0, True, 5618, None, codecPolicy0
            )
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            #
            # lineLength 5618 > 0, but lineSeparator is null
            #
            self.verifyException("org.apache.commons.codec.binary.Base32", e)

    def test2(self) -> None:

        mockPrintStream0 = io.StringIO()
        byteArray0 = bytearray(1)
        codecPolicy0 = CodecPolicy.STRICT
        base32OutputStream0 = Base32OutputStream(
            mockPrintStream0, False, 0, byteArray0, codecPolicy0
        )
        baseNCodecOutputStream0 = Base32OutputStream.Base32OutputStream2(
            base32OutputStream0, False, -4040, byteArray0
        )
        assert not baseNCodecOutputStream0.isStrictDecoding()

    def test1(self) -> None:

        mockPrintStream0 = io.StringIO()
        baseNCodecOutputStream0 = Base32OutputStream.Base32OutputStream1(
            mockPrintStream0, False
        )
        self.assertFalse(baseNCodecOutputStream0.isStrictDecoding())

    def test0(self) -> None:

        try:
            Base32OutputStream.Base32OutputStream2(None, True, 4, None)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # lineLength 4 > 0, but lineSeparator is null
            self.verifyException("org.apache.commons.codec.binary.Base32", e)
