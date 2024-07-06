from __future__ import annotations
import time
import re
import mock
import os
import typing
from typing import *
from io import BytesIO
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.codec.CodecPolicy import *
from src.main.org.apache.commons.codec.binary.Base16OutputStream import *

# from src.test.org.apache.commons.codec.binary.Base16OutputStream_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class Base16OutputStream_ESTest(unittest.TestCase):

    def test5(self) -> None:

        base16OutputStream0 = Base16OutputStream.Base16OutputStream3(None)

        try:
            Base16OutputStream.Base16OutputStream1(base16OutputStream0, False, False)
            self.fail("Expecting exception: RuntimeError")
        except RuntimeError as e:
            self.verifyException("java.util.LinkedList", e)

    def test4(self) -> None:

        pipedOutputStream0 = io.BytesIO()
        base16OutputStream0 = Base16OutputStream.Base16OutputStream3(pipedOutputStream0)

        try:
            Base16OutputStream.Base16OutputStream2(base16OutputStream0, False)
            self.fail("Expecting exception: RuntimeError")
        except RuntimeError as e:
            verifyException("java.util.LinkedList", e)

    def test3(self) -> None:

        pipedOutputStream0 = io.BytesIO()
        Base16OutputStream.Base16OutputStream3(pipedOutputStream0)
        # Undeclared exception in Python is replaced with a ValueError
        try:
            Base16OutputStream.Base16OutputStream3(pipedOutputStream0)
            self.fail("Expecting exception: ValueError")
        except ValueError as e:
            # no message in exception (getMessage() returned null)
            # verifyException("java.util.LinkedList", e)
            # In Python, we can use assert to verify the exception
            assert isinstance(e, ValueError), "Expecting exception: ValueError"

    def test2(self) -> None:

        base16OutputStream0 = Base16OutputStream.Base16OutputStream1(None, True, True)
        assert not base16OutputStream0.isStrictDecoding()

    def test1(self) -> None:

        base16OutputStream0 = Base16OutputStream.Base16OutputStream2(None, False)
        assert not base16OutputStream0.isStrictDecoding()

    def test0(self) -> None:

        outputStream0 = io.BytesIO()
        mockPrintStream0 = MockPrintStream(outputStream0, True)
        codecPolicy0 = CodecPolicy.LENIENT
        base16OutputStream0 = Base16OutputStream(
            mockPrintStream0, False, True, codecPolicy0
        )
        self.assertFalse(base16OutputStream0.isStrictDecoding())
