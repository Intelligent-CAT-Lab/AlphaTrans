from __future__ import annotations
import time
import re
import os
from io import StringIO
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.codec.binary.CharSequenceUtils import *

# from src.test.org.apache.commons.codec.binary.CharSequenceUtils_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class CharSequenceUtils_ESTest(unittest.TestCase):

    def test9(self) -> None:
        charSequenceUtils0 = CharSequenceUtils()

    def test8(self) -> None:

        charBuffer0 = io.StringIO(3941)
        boolean0 = CharSequenceUtils.regionMatches(
            "", True, 3941, charBuffer0, 3941, -9
        )
        self.assertTrue(boolean0)

    def test7(self) -> None:

        charBuffer0 = ["\0"] * 3978
        charBuffer0[0] = "2"
        charBuffer0[1] = "2"
        boolean0 = self.regionMatches(charBuffer0, True, 0, charBuffer0, 33, 3978)
        self.assertFalse(boolean0)

    def test6(self) -> None:

        charBuffer0 = ["-"] * 3946
        charBuffer1 = charBuffer0.insert(0, "-")
        boolean0 = CharSequenceUtils.regionMatches(
            charBuffer0, False, 0, charBuffer1, 0, 3946
        )
        self.assertFalse(boolean0)

    def test5(self) -> None:

        try:
            CharSequenceUtils.regionMatches(None, False, 43, None, 43, 43)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.apache.commons.codec.binary.CharSequenceUtils", e)

    def test4(self) -> None:

        charBuffer0 = "&"

        try:
            self.assertFalse(
                CharSequenceUtils.regionMatches("&", True, 45, charBuffer0, 27, 27)
            )
        except StringIndexOutOfBoundsException:
            pass

    def test3(self) -> None:

        boolean0 = CharSequenceUtils.regionMatches("Mc`h*+", True, 101, "", 3880, 1100)
        self.assertFalse(boolean0)

    def test2(self) -> None:

        charBuffer0 = io.StringIO(3951)
        boolean0 = CharSequenceUtils.regionMatches(
            charBuffer0, True, 0, charBuffer0, 1186, 95
        )
        self.assertTrue(boolean0)

    def test1(self) -> None:

        charBuffer0 = bytearray(30)
        charArray0 = bytearray(7)
        charBuffer1 = memoryview(charArray0)

        try:
            CharSequenceUtils.regionMatches(charBuffer1, False, 4, charBuffer0, 4, 30)
            self.fail("Expecting exception: IndexOutOfBoundsException")

        except IndexError as e:
            self.verifyException("java.nio.Buffer", e)

    def test0(self) -> None:

        charBuffer0 = [""] * 3941
        charBuffer1 = self.put(charBuffer0, "-", "-")
        self.get(charBuffer0)
        boolean0 = self.regionMatches(charBuffer0, True, "-", charBuffer1, 28, 3941)
        self.assertFalse(boolean0)

    def put(self, cs: list, c1: str, c2: str) -> list:
        cs[0] = c1
        cs[1] = c2
        return cs

    def get(self, cs: list) -> None:
        cs.pop(0)

    def assertFalse(self, condition: bool) -> None:
        assert not condition
