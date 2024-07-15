from __future__ import annotations
import time
import re
import os
from io import BytesIO
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.codec.Charsets import *

# from src.test.org.apache.commons.codec.Charsets_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class Charsets_ESTest(unittest.TestCase):

    def test5(self) -> None:

        charsets0 = Charsets()
        charset0 = Charsets.toCharset0(charsets0.UTF_16)
        self.assertEqual("UTF-16", charset0)

    def test4(self) -> None:

        charset0 = io.open(io.BytesIO()).encoding
        charset1 = Charsets.toCharset0(charset0)
        self.assertEqual("UTF-8", charset1)

    def test3(self) -> None:
        charset0 = Charsets.toCharset0(None)
        self.assertTrue(io.open(io.BytesIO(), encoding=charset0).readable())

    def test2(self) -> None:

        try:
            Charsets.toCharset1("RrMi)Z.+~")
            self.fail("Expecting exception: IllegalCharsetNameException")

        except Exception as e:
            self.assertEqual(str(e), "Expecting exception: IllegalCharsetNameException")
            self.verifyException("java.nio.charset.Charset", e)

    def test1(self) -> None:

        charset0 = Charsets.toCharset1(None)
        self.assertEqual("UTF-8", charset0)

    def test0(self) -> None:

        # Undeclared exception
        try:
            Charsets.toCharset1("6")
            self.fail("Expecting exception: UnsupportedCharsetException")

        except UnsupportedCharsetException as e:
            # 6
            self.verifyException("java.nio.charset.Charset", e)
