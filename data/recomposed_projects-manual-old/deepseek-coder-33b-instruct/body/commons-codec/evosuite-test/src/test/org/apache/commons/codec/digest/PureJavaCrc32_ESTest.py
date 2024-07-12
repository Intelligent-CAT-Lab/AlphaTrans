from __future__ import annotations
import time
import re
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.codec.digest.PureJavaCrc32 import *

# from src.test.org.apache.commons.codec.digest.PureJavaCrc32_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class PureJavaCrc32_ESTest(unittest.TestCase):

    def test18(self) -> None:

        pureJavaCrc32_0 = PureJavaCrc32()
        long0 = pureJavaCrc32_0.getValue()
        self.assertEqual(0, long0)

    def test17(self) -> None:

        pureJavaCrc32_0 = PureJavaCrc32()
        pureJavaCrc32_0.reset()
        self.assertEqual(0, pureJavaCrc32_0.getValue())

    def test16(self) -> None:

        pureJavaCrc32_0 = PureJavaCrc32()
        pureJavaCrc32_0.update1(1380)
        long0 = pureJavaCrc32_0.getValue()
        self.assertEqual(2564639436, long0)

    def test14(self) -> None:

        pureJavaCrc32_0 = PureJavaCrc32()
        try:
            pureJavaCrc32_0.update0(None, -1, -1)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.assertIsInstance(e, RuntimeError)
            self.verifyException("org.apache.commons.codec.digest.PureJavaCrc32", e)

    def test13(self) -> None:

        pureJavaCrc32_0 = PureJavaCrc32()
        byteArray0 = [0] * 13

        with self.assertRaises(ArrayIndexOutOfBoundsException):
            pureJavaCrc32_0.update0(byteArray0, 0, 3044)

    def test12(self) -> None:

        pureJavaCrc32_0 = PureJavaCrc32()
        byteArray0 = bytearray(7)
        pureJavaCrc32_0.update0(byteArray0, 1, 1)
        self.assertEqual(3523407757, pureJavaCrc32_0.getValue())

    def test11(self) -> None:

        pureJavaCrc32_0 = PureJavaCrc32()
        byteArray0 = [0] * 11

        with self.assertRaises(ArrayIndexOutOfBoundsException):
            pureJavaCrc32_0.update0(byteArray0, -2542, -2542)

    def test10(self) -> None:

        pureJavaCrc32_0 = PureJavaCrc32()
        byteArray0 = [0]

        with self.assertRaises(ArrayIndexOutOfBoundsException):
            pureJavaCrc32_0.update0(byteArray0, 0, -1381)

    def test09(self) -> None:

        pureJavaCrc32_0 = PureJavaCrc32()
        byteArray0 = [0] * 3

        with self.assertRaises(ArrayIndexOutOfBoundsException):
            pureJavaCrc32_0.update0(byteArray0, -12, -12)

    def test08(self) -> None:

        pureJavaCrc32_0 = PureJavaCrc32()
        byteArray0 = bytearray(13)
        pureJavaCrc32_0.update0(byteArray0, 5, 5)
        self.assertEqual(3324180253, pureJavaCrc32_0.getValue())

    def test07(self) -> None:

        pureJavaCrc32_0 = PureJavaCrc32()
        byteArray0 = [0] * 7

        with self.assertRaises(ArrayIndexOutOfBoundsException):
            pureJavaCrc32_0.update0(byteArray0, -2, -2)

    def test06(self) -> None:

        pureJavaCrc32_0 = PureJavaCrc32()
        byteArray0 = bytearray(2)
        pureJavaCrc32_0.update0(byteArray0, 0, 0)
        self.assertEqual(0, pureJavaCrc32_0.getValue())

    def test04(self) -> None:

        pureJavaCrc32_0 = PureJavaCrc32()
        byteArray0 = bytearray(5)
        byteArray0[1] = -57

        try:
            pureJavaCrc32_0.update0(byteArray0, 1, 3425)
            self.fail("Expecting exception: ArrayIndexOutOfBoundsException")

        except IndexError as e:
            # Index 5 out of bounds for length 5
            self.assertEqual(str(e), "array index out of range")

    def test03(self) -> None:

        pureJavaCrc32_0 = PureJavaCrc32()
        byteArray0 = bytearray(5)
        byteArray0[2] = -60

        try:
            pureJavaCrc32_0.update0(byteArray0, 1, 3425)
            self.fail("Expecting exception: ArrayIndexOutOfBoundsException")

        except IndexError as e:
            # Index 5 out of bounds for length 5
            self.assertEqual(str(e), "array index out of range")

    def test02(self) -> None:

        pureJavaCrc32_0 = PureJavaCrc32()
        byteArray0 = bytearray(9)
        byteArray0[2] = -1

        try:
            pureJavaCrc32_0.update0(byteArray0, 0, 79)
            self.fail("Expecting exception: ArrayIndexOutOfBoundsException")

        except IndexError as e:
            # Index 9 out of bounds for length 9
            self.assertEqual(str(e), "list index out of range")

    def test01(self) -> None:

        pureJavaCrc32_0 = PureJavaCrc32()
        byteArray0 = [0] * 6
        byteArray0[3] = 118

        try:
            pureJavaCrc32_0.update0(byteArray0, 0, 14)
            self.fail("Expecting exception: ArrayIndexOutOfBoundsException")

        except IndexError as e:
            # Index 6 out of bounds for length 6
            self.assertEqual(str(e), "list index out of range")

    def test00(self) -> None:

        pureJavaCrc32_0 = PureJavaCrc32()
        byteArray0 = bytearray(8)
        byteArray0[4] = -1

        try:
            pureJavaCrc32_0.update0(byteArray0, 0, 1172266101)
            self.fail("Expecting exception: ArrayIndexOutOfBoundsException")

        except IndexError as e:
            # Index 8 out of bounds for length 8
            self.assertEqual(str(e), "list index out of range")
