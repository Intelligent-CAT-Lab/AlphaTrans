from __future__ import annotations
import time
import re
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.codec.binary.BinaryCodec import *

# from src.test.org.apache.commons.codec.binary.BinaryCodec_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class BinaryCodec_ESTest(unittest.TestCase):

    def test22(self) -> None:

        byteArray0 = [0] * 7
        byteArray0[4] = 115
        byteArray1 = BinaryCodec.toAsciiBytes(byteArray0)
        byteArray2 = BinaryCodec.fromAscii0(byteArray1)
        self.assertEqual(byteArray2, [0, 0, 0, 0, 115, 0, 0])
        self.assertEqual(len(byteArray2), 7)

    def test21(self) -> None:

        byteArray0 = BinaryCodec.fromAscii1(None)
        self.assertEqual(0, len(byteArray0))

    def test20(self) -> None:

        charArray0 = ["\0"] * 8
        charArray0[6] = "1"
        byteArray0 = BinaryCodec.fromAscii1(charArray0)
        self.assertEqual([2], byteArray0)

    def test19(self) -> None:

        byteArray0 = bytearray()
        byteArray1 = BinaryCodec.toAsciiBytes(byteArray0)
        self.assertEqual(0, len(byteArray1))

    def test18(self) -> None:

        string0 = BinaryCodec.toAsciiString(None)
        self.assertEqual("", string0)

    def test17(self) -> None:

        binaryCodec0 = BinaryCodec()
        object0 = binaryCodec0.decode1(None)
        self.assertIsNotNone(object0)

    def test16(self) -> None:

        binaryCodec0 = BinaryCodec()
        object0 = binaryCodec0.decode1("")
        object1 = binaryCodec0.decode1(object0)
        self.assertIs(object1, object0)

    def test14(self) -> None:

        binaryCodec0 = BinaryCodec()
        try:
            binaryCodec0.encode1("PK")
            self.fail("Expecting exception: Exception")

        except Exception as e:
            # argument not a byte array
            self.verifyException("org.apache.commons.codec.binary.BinaryCodec", e)

    def test13(self) -> None:

        binaryCodec0 = BinaryCodec()
        byteArray0 = binaryCodec0.toByteArray(None)
        self.assertEqual(byteArray0, [])

    def test12(self) -> None:

        byteArray0 = [0]
        binaryCodec0 = BinaryCodec()
        byteArray1 = binaryCodec0.encode0(byteArray0)
        self.assertEqual(byteArray1, [48, 48, 48, 48, 48, 48, 48, 48])
        self.assertEqual(len(byteArray1), 8)

    def test11(self) -> None:

        byteArray0 = BinaryCodec.fromAscii0(None)
        self.assertEqual(0, len(byteArray0))

    def test10(self) -> None:

        charArray0 = []
        byteArray0 = BinaryCodec.fromAscii1(charArray0)
        self.assertEqual(0, len(byteArray0))

    def test09(self) -> None:

        binaryCodec0 = BinaryCodec()
        byteArray0 = [0] * 2
        byteArray1 = binaryCodec0.decode0(byteArray0)
        charArray0 = BinaryCodec.toAsciiChars(byteArray1)
        self.assertEqual(0, len(charArray0))

    def test08(self) -> None:

        byteArray0 = [0] * 9
        byteArray0[0] = -35
        charArray0 = BinaryCodec.toAsciiChars(byteArray0)
        self.assertEqual(72, len(charArray0))

    def test07(self) -> None:

        binaryCodec0 = BinaryCodec()

        try:
            binaryCodec0.decode1(binaryCodec0)
            self.fail("Expecting exception: Exception")

        except Exception as e:
            # argument not a byte array
            self.verifyException("org.apache.commons.codec.binary.BinaryCodec", e)

    def test06(self) -> None:

        binaryCodec0 = BinaryCodec()
        object0 = binaryCodec0.decode1("t0c@y}~Q}/qQP1TVc")
        object1 = binaryCodec0.encode1(object0)
        self.assertNotEqual(object1, object0)

    def test04(self) -> None:

        byteArray0 = [0] * 7
        byteArray1 = BinaryCodec.toAsciiBytes(byteArray0)
        byteArray2 = BinaryCodec.toAsciiBytes(byteArray1)
        BinaryCodec.toAsciiString(byteArray2)
        BinaryCodec.toAsciiString(byteArray2)
        # Undeclared exception is not present in Python
        BinaryCodec.toAsciiString(byteArray2)

    def test02(self) -> None:

        binaryCodec0 = BinaryCodec()
        byteArray0 = binaryCodec0.toByteArray("7")
        byteArray1 = binaryCodec0.encode0(byteArray0)
        self.assertNotEqual(byteArray1, byteArray0)

    def test01(self) -> None:

        binaryCodec0 = BinaryCodec()
        byteArray0 = binaryCodec0.toByteArray("Aq,Ogv;*Qm<[(~z{")
        self.assertEqual(byteArray0, [0, 0])

    def test00(self) -> None:

        binaryCodec0 = BinaryCodec()
        byteArray0 = bytearray(9)
        byteArray0[2] = 84
        byteArray1 = binaryCodec0.decode0(byteArray0)
        self.assertEqual(bytearray([0]), byteArray1)
