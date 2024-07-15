from __future__ import annotations
import time
import re
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.codec.net.PercentCodec import *

# from src.test.org.apache.commons.codec.net.PercentCodec_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class PercentCodec_ESTest(unittest.TestCase):

    def test26(self) -> None:

        percentCodec0 = PercentCodec(0, True, None)
        byteArray0 = bytearray(10)
        byteArray1 = percentCodec0.encode0(byteArray0)
        self.assertIs(byteArray1, byteArray0)
        self.assertIsNotNone(byteArray1)

    def test25(self) -> None:

        byteArray0 = [0] * 5
        percentCodec0 = PercentCodec(0, False, byteArray0)
        byteArray1 = percentCodec0.encode0(None)
        self.assertIsNone(byteArray1)

    def test24(self) -> None:

        byteArray0 = [0] * 7
        percentCodec0 = PercentCodec(0, True, byteArray0)
        byteArray1 = [0] * 7
        byteArray1[0] = 32
        byteArray2 = percentCodec0.encode0(byteArray1)
        self.assertEqual(19, len(byteArray2))

    def test23(self) -> None:

        byteArray0 = [0] * 7
        percentCodec0 = PercentCodec(0, True, byteArray0)
        byteArray1 = [0] * 7
        byteArray1[3] = 14
        byteArray2 = percentCodec0.encode0(byteArray1)
        self.assertEqual(19, len(byteArray2))

    def test22(self) -> None:

        byteArray0 = [0] * 7
        percentCodec0 = PercentCodec(0, True, byteArray0)
        byteArray1 = percentCodec0.encode0(byteArray0)
        byteArray2 = percentCodec0.encode0(byteArray1)
        self.assertEqual(35, len(byteArray2))

    def test21(self) -> None:

        percentCodec0 = PercentCodec(1301, True, None)
        byteArray0 = percentCodec0.decode0(None)
        self.assertIsNone(byteArray0)

    def test19(self) -> None:

        byteArray0 = [0] * 3
        percentCodec0 = PercentCodec(0, True, byteArray0)
        byteArray1 = [0] * 3
        byteArray1[2] = 43
        byteArray2 = percentCodec0.decode0(byteArray1)
        self.assertEqual([0, 0, 32], byteArray2)

    def test16(self) -> None:

        byteArray0 = bytearray(0)
        percentCodec0 = PercentCodec(2611, True, byteArray0)
        byteArray1 = percentCodec0.encode0(byteArray0)
        self.assertIs(byteArray1, byteArray0)

    def test15(self) -> None:

        byteArray0 = bytearray(5)
        percentCodec0 = PercentCodec(0, True, byteArray0)
        object0 = object()
        try:
            percentCodec0.encode1(object0)
            self.fail("Expecting exception: Exception")

        except Exception as e:
            # Objects of type java.lang.Object cannot be Percent encoded
            self.verifyException("org.apache.commons.codec.net.PercentCodec", e)

    def test14(self) -> None:

        byteArray0 = bytearray(0)
        percentCodec0 = PercentCodec(0, False, byteArray0)
        object0 = percentCodec0.encode1(None)
        self.assertIsNone(object0)

    def test13(self) -> None:

        byteArray0 = bytearray(18)
        percentCodec0 = PercentCodec(0, False, byteArray0)

        try:
            percentCodec0.decode1(percentCodec0)
            self.fail("Expecting exception: Exception")

        except Exception as e:
            # Objects of type org.apache.commons.codec.net.PercentCodec cannot be Percent decoded
            self.verifyException("org.apache.commons.codec.net.PercentCodec", e)

    def test12(self) -> None:

        byteArray0 = bytearray(8)
        percentCodec0 = PercentCodec(3404, True, byteArray0)
        object0 = percentCodec0.decode1(None)
        self.assertIsNone(object0)

    def test11(self) -> None:

        byteArray0 = bytearray(4)
        byteArray0[0] = -3
        percentCodec0 = None
        try:
            percentCodec0 = PercentCodec(0, True, byteArray0)
            self.fail("Expecting exception: IndexOutOfBoundsException")

        except IndexError as e:
            # bitIndex < 0: -3
            self.verifyException("java.util.BitSet", e)

    def test09(self) -> None:

        byteArray0 = bytearray(2)
        byteArray0[1] = 37
        percentCodec0 = PercentCodec(1067, True, byteArray0)
        try:
            percentCodec0.decode0(byteArray0)
            self.fail("Expecting exception: Exception")

        except Exception as e:
            #
            # Invalid percent decoding:
            #
            self.verifyException("org.apache.commons.codec.net.PercentCodec", e)

    def test06(self) -> None:

        byteArray0 = bytearray(0)
        percentCodec0 = PercentCodec(-547, False, byteArray0)
        byteArray1 = percentCodec0.decode0(byteArray0)
        self.assertEqual(0, len(byteArray1))

    def test03(self) -> None:

        byteArray0 = bytearray(7)
        byteArray0[0] = 17
        percentCodec0 = PercentCodec(0, True, byteArray0)

    def test00(self) -> None:

        byteArray0 = bytearray(1)
        byteArray0[0] = 67
        percentCodec0 = PercentCodec(0, True, byteArray0)
        byteArray1 = percentCodec0.decode0(byteArray0)
        self.assertEqual([67], byteArray1)
