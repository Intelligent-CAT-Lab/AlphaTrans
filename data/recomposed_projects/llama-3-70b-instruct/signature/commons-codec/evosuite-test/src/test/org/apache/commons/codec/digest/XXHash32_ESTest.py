from __future__ import annotations
import time
import re
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.codec.digest.XXHash32 import *

# from src.test.org.apache.commons.codec.digest.XXHash32_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class XXHash32_ESTest(unittest.TestCase):

    def test12(self) -> None:

        xXHash32_0 = XXHash32.XXHash321()
        xXHash32_0.reset()
        self.assertEqual(46947589, xXHash32_0.getValue())

    def test11(self) -> None:

        xXHash32_0 = XXHash32.XXHash321()
        byteArray0 = bytearray(7)
        xXHash32_0.update1(byteArray0, 17, -53)
        self.assertEqual(46947589, xXHash32_0.getValue())

    def test10(self) -> None:

        xXHash32_0 = XXHash32.XXHash321()
        byteArray0 = bytearray(32)
        xXHash32_0.update0(0)

        try:
            xXHash32_0.update1(byteArray0, 16, 24)
            self.fail("Expecting exception: ArrayIndexOutOfBoundsException")

        except IndexError:
            pass

    def test09(self) -> None:

        xXHash32_0 = XXHash32.XXHash321()
        byteArray0 = bytearray(37)
        xXHash32_0.update1(byteArray0, 11, 11)
        long0 = xXHash32_0.getValue()
        self.assertEqual(632180237, long0)

    def test08(self) -> None:

        xXHash32_0 = XXHash32.XXHash321()

        try:
            xXHash32_0.update1(None, 3191, 3191)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.verifyException("org.apache.commons.codec.digest.XXHash32", e)

    def test06(self) -> None:

        xXHash32_0 = XXHash32(723)
        byteArray0 = [0] * 9
        xXHash32_0.update1(byteArray0, 1799, 0)
        self.assertEqual(2679648573, xXHash32_0.getValue())

    def test05(self) -> None:

        byteArray0 = bytearray(32)
        xXHash32_0 = XXHash32(-668)
        xXHash32_0.update1(byteArray0, 16, 16)
        long0 = xXHash32_0.getValue()
        self.assertEqual(1895327912, long0)

    def test04(self) -> None:

        xXHash32_0 = XXHash32(723)
        byteArray0 = [0] * 9
        xXHash32_0.update1(byteArray0, 0, 7)
        xXHash32_0.update0(-2204)
        long0 = xXHash32_0.getValue()
        self.assertEqual(2763811559, long0)

    def test03(self) -> None:

        xXHash32_0 = XXHash32(0)
        xXHash32_0.update0(1)
        long0 = xXHash32_0.getValue()
        self.assertEqual(949155633, long0)

    def test02(self) -> None:

        xXHash32_0 = XXHash32(723)
        byteArray0 = bytearray(9)
        byteArray0[1] = 1
        xXHash32_0.update1(byteArray0, 0, 7)
        long0 = xXHash32_0.getValue()
        self.assertEqual(686811741, long0)

    def test01(self) -> None:

        xXHash32_0 = XXHash32.XXHash321()
        byteArray0 = bytearray(8)
        byteArray0[6] = -29

        try:
            xXHash32_0.update1(byteArray0, 0, 4311)
            self.fail("Expecting exception: ArrayIndexOutOfBoundsException")

        except IndexError as e:
            self.assertEqual(str(e), "array index out of range")

    def test00(self) -> None:

        xXHash32_0 = XXHash32.XXHash321()
        byteArray0 = bytearray(8)
        byteArray0[0] = -29

        try:
            xXHash32_0.update1(byteArray0, 0, 4311)
            self.fail("Expecting exception: ArrayIndexOutOfBoundsException")

        except IndexError as e:
            self.assertEqual(str(e), "array index out of range")
