from __future__ import annotations
import time
import re
import os
import typing
from typing import *
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.codec.digest.UnixCrypt import *

# from src.test.org.apache.commons.codec.digest.UnixCrypt_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class UnixCrypt_ESTest(unittest.TestCase):

    def test11(self) -> None:

        string0 = UnixCrypt.crypt2("org.apache.commons.codec.digest.UnixCrypt")
        #  // Unstable assertion: assertEquals("ARBcKHh7BMo8.", string0);

    def test10(self) -> None:

        string0 = UnixCrypt.crypt3("..", "..")
        self.assertEqual("..sNoJOH91ERI", string0)

    def test09(self) -> None:
        unixCrypt0 = UnixCrypt()

    def test08(self) -> None:

        byteArray0 = [0] * 3
        try:
            UnixCrypt.crypt1(byteArray0, "")
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            self.assertEqual(str(e), "Invalid salt value: ")

    def test07(self) -> None:

        byteArray0 = [0] * 9
        string0 = UnixCrypt.crypt0(byteArray0)
        # Unstable assertion: self.assertEqual("U4gQu2rzuwCF2", string0)

    def test06(self) -> None:

        byteArray0 = bytearray()
        string0 = UnixCrypt.crypt1(byteArray0, None)
        # Unstable assertion: self.assertEqual("9Jn9vDMro3n76", string0)

    def test05(self) -> None:

        byteArray0 = [0] * 9
        string0 = UnixCrypt.crypt1(byteArray0, "mHlZflitwujn6")
        self.assertEqual("mHYbZxQKNLOi6", string0)

    def test04(self) -> None:

        try:
            UnixCrypt.crypt0(None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.assertEqual(str(e), "")
            self.assertEqual(type(e), RuntimeError)

    def test03(self) -> None:

        try:
            UnixCrypt.crypt1(None, "mUI1f7..XM6XE")
            self.fail("Expecting exception: RuntimeError")

        except TypeError as e:
            self.assertEqual(str(e), "RuntimeError")

    def test02(self) -> None:

        try:
            UnixCrypt.crypt2(None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.assertEqual(str(e), "Expecting exception: RuntimeError")

    def test01(self) -> None:

        try:
            UnixCrypt.crypt3("X/pr'wX(B{Vh3w)BU", "X/pr'wX(B{Vh3w)BU")
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            #
            # Invalid salt value: X/pr'wX(B{Vh3w)BU
            #
            self.verifyException("org.apache.commons.codec.digest.UnixCrypt", e)

    def test00(self) -> None:

        try:
            UnixCrypt.crypt3(None, None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.assertEqual(str(e), "")
            self.assertEqual(type(e), RuntimeError)
