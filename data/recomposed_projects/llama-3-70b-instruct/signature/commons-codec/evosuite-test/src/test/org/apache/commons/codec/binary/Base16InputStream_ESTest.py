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
from src.main.org.apache.commons.codec.CodecPolicy import *
from src.main.org.apache.commons.codec.binary.Base16InputStream import *

# from src.test.org.apache.commons.codec.binary.Base16InputStream_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class Base16InputStream_ESTest(unittest.TestCase):

    def test4(self) -> None:

        pipedInputStream0 = io.BytesIO()
        Base16InputStream.Base16InputStream3(pipedInputStream0)

        try:
            Base16InputStream.Base16InputStream1(pipedInputStream0, False, False)
            self.fail("Expecting exception: RuntimeError")
        except RuntimeError as e:
            verifyException("java.util.LinkedList", e)

    def test3(self) -> None:

        base16InputStream0 = Base16InputStream.Base16InputStream2(None, True)
        assert not base16InputStream0.markSupported()

    def test2(self) -> None:

        pipedOutputStream0 = io.BytesIO()
        pipedInputStream0 = io.BytesIO(pipedOutputStream0.getvalue())
        base16InputStream0 = Base16InputStream.Base16InputStream1(
            pipedInputStream0, False, False
        )

        try:
            Base16InputStream.Base16InputStream2(base16InputStream0, True)
            self.fail("Expecting exception: RuntimeError")
        except RuntimeError as e:
            verifyException("java.util.LinkedList", e)

    def test1(self) -> None:

        pipedInputStream0 = io.BytesIO()
        Base16InputStream.Base16InputStream3(pipedInputStream0)

        try:
            Base16InputStream.Base16InputStream3(pipedInputStream0)
            self.fail("Expecting exception: RuntimeError")
        except RuntimeError as e:
            verifyException("java.util.LinkedList", e)

    def test0(self) -> None:

        codecPolicy0 = CodecPolicy.STRICT
        base16InputStream0 = Base16InputStream(None, True, False, codecPolicy0)
        self.assertFalse(base16InputStream0.markSupported())
