from __future__ import annotations
import time
import re
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.codec.digest.PureJavaCrc32C import *

# from src.test.org.apache.commons.codec.digest.PureJavaCrc32C_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class PureJavaCrc32C_ESTest(unittest.TestCase):

    def test19(self) -> None:

        pureJavaCrc32C0 = PureJavaCrc32C()
        long0 = pureJavaCrc32C0.getValue()
        self.assertEqual(0, long0)

    def test18(self) -> None:

        pureJavaCrc32C0 = PureJavaCrc32C()
        pureJavaCrc32C0.update1(2536)
        self.assertEqual(999596932, pureJavaCrc32C0.getValue())

    def test16(self) -> None:

        pureJavaCrc32C0 = PureJavaCrc32C()
        byteArray0 = [0] * 4

        with pytest.raises(IndexError):
            pureJavaCrc32C0.update0(byteArray0, 7, 7)

    def test15(self) -> None:

        pureJavaCrc32C0 = PureJavaCrc32C()
        byteArray0 = [0] * 14

        with self.assertRaises(ArrayIndexOutOfBoundsException):
            pureJavaCrc32C0.update0(byteArray0, 0, 1695)

    def test14(self) -> None:

        pureJavaCrc32C0 = PureJavaCrc32C()
        byteArray0 = [0] * 6
        pureJavaCrc32C0.update0(byteArray0, 1, 1)
        self.assertEqual(1383945041, pureJavaCrc32C0.getValue())

    def test13(self) -> None:

        pureJavaCrc32C0 = PureJavaCrc32C()
        byteArray0 = [0] * 5
        pureJavaCrc32C0.update0(byteArray0, 2, 2)
        self.assertEqual(4049696722, pureJavaCrc32C0.getValue())

    def test12(self) -> None:

        pureJavaCrc32C0 = PureJavaCrc32C()
        byteArray0 = [0] * 5

        with self.assertRaises(ArrayIndexOutOfBoundsException):
            pureJavaCrc32C0.update0(byteArray0, -1923, 3)

    def test11(self) -> None:

        pureJavaCrc32C0 = PureJavaCrc32C()
        byteArray0 = [0] * 8

        with pytest.raises(IndexError):
            pureJavaCrc32C0.update0(byteArray0, 329, 4)

    def test10(self) -> None:

        byteArray0 = [0] * 5
        pureJavaCrc32C0 = PureJavaCrc32C()

        try:
            pureJavaCrc32C0.update0(byteArray0, 5, 5)
            self.fail("Expecting exception: ArrayIndexOutOfBoundsException")

        except IndexError as e:
            # Index 5 out of bounds for length 5
            self.verifyException("org.apache.commons.codec.digest.PureJavaCrc32C", e)

    def test09(self) -> None:

        pureJavaCrc32C0 = PureJavaCrc32C()
        byteArray0 = [0] * 4

        with pytest.raises(IndexError):
            pureJavaCrc32C0.update0(byteArray0, 0, 6)

    def test08(self) -> None:

        pureJavaCrc32C0 = PureJavaCrc32C()
        byteArray0 = bytearray(5)
        pureJavaCrc32C0.update0(byteArray0, 0, 0)
        self.assertEqual(0, pureJavaCrc32C0.getValue())

    def test07(self) -> None:

        pureJavaCrc32C0 = PureJavaCrc32C()
        pureJavaCrc32C0.reset()
        self.assertEqual(0, pureJavaCrc32C0.getValue())

    def test06(self) -> None:

        pureJavaCrc32C0 = PureJavaCrc32C()
        try:
            pureJavaCrc32C0.update0(None, 708, 708)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.verifyException("org.apache.commons.codec.digest.PureJavaCrc32C", e)

    def test05(self) -> None:

        pureJavaCrc32C0 = PureJavaCrc32C()
        pureJavaCrc32C0.update1(0)
        long0 = pureJavaCrc32C0.getValue()
        self.assertEqual(1383945041, long0)

    def test03(self) -> None:

        pureJavaCrc32C0 = PureJavaCrc32C()
        byteArray0 = [0] * 2
        byteArray0[0] = 9

        with pytest.raises(ArrayIndexOutOfBoundsException):
            pureJavaCrc32C0.update0(byteArray0, 0, 1928)

    def test02(self) -> None:

        pureJavaCrc32C0 = PureJavaCrc32C()
        byteArray0 = bytearray(6)
        byteArray0[1] = 24

        with pytest.raises(IndexError):
            pureJavaCrc32C0.update0(byteArray0, 0, 1695)

    def test01(self) -> None:

        pureJavaCrc32C0 = PureJavaCrc32C()
        byteArray0 = [0] * 6
        byteArray0[2] = 7

        try:
            pureJavaCrc32C0.update0(byteArray0, 0, 1695)
            self.fail("Expecting exception: ArrayIndexOutOfBoundsException")

        except IndexError as e:
            # Index 6 out of bounds for length 6
            self.verifyException("org.apache.commons.codec.digest.PureJavaCrc32C", e)

    def test00(self) -> None:

        pureJavaCrc32C0 = PureJavaCrc32C()
        byteArray0 = bytearray(6)
        byteArray0[3] = -34

        try:
            pureJavaCrc32C0.update0(byteArray0, 0, 1695)
            self.fail("Expecting exception: ArrayIndexOutOfBoundsException")

        except IndexError as e:
            # Index 6 out of bounds for length 6
            self.assertEqual(str(e), "list index out of range")
