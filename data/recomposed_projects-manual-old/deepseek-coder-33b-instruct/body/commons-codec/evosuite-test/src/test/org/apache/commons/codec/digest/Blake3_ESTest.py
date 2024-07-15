from __future__ import annotations
import time
import re
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.codec.digest.Blake3 import *

# from src.test.org.apache.commons.codec.digest.Blake3_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class Blake3_ESTest(unittest.TestCase):

    def test21(self) -> None:

        blake3_0 = Blake3.initHash()
        blake3_0.reset()

    def test20(self) -> None:

        blake3_0 = Blake3.initHash()
        byteArray0 = blake3_0.doFinalize2(1049)

        try:
            Blake3.keyedHash(byteArray0, byteArray0)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            self.verifyException("org.apache.commons.codec.digest.Blake3", e)

    def test19(self) -> None:

        blake3_0 = Blake3.initHash()
        try:
            blake3_0.doFinalize2((-1411))
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            self.assertEqual(str(e), "Requested bytes must be non-negative")

    def test18(self) -> None:

        byteArray0 = bytearray(5)
        blake3_0 = Blake3.initKeyDerivationFunction(byteArray0)

        try:
            blake3_0.doFinalize1(byteArray0, 891, 891)
            self.fail("Expecting exception: IndexOutOfBoundsException")

        except IndexError as e:
            self.assertEqual(
                str(e), "Offset 891 and length 891 out of bounds with buffer length 5"
            )

    def test17(self) -> None:

        blake3_0 = Blake3.initHash()
        byteArray0 = blake3_0.doFinalize2(3437)
        blake3_0.update0(byteArray0)
        self.assertEqual(3437, len(byteArray0))

    def test16(self) -> None:

        blake3_0 = Blake3.initHash()
        byteArray0 = bytearray(6)
        try:
            blake3_0.update1(byteArray0, 1359893119, -2693)
            self.fail("Expecting exception: IndexOutOfBoundsException")

        except IndexError as e:
            self.assertIsInstance(e, IndexError)

    def test15(self) -> None:

        blake3_0 = Blake3.initHash()
        byteArray0 = bytearray(6)
        blake3_0.doFinalize0(byteArray0)
        #  // Unstable assertion: assertArrayEquals(bytearray([(byte) (-11), (byte) (-113), (byte) (-56), (byte) (-48), (byte) (-94), (byte) (-79)]), byteArray0)

    def test14(self) -> None:

        byteArray0 = bytearray(5)

        try:
            Blake3.initKeyedHash(byteArray0)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            self.assertEqual(str(e), "Blake3 keys must be 32 bytes")

    def test13(self) -> None:

        blake3_0 = Blake3.initHash()
        byteArray0 = bytearray(0)
        # Undeclared exception in Java, but equivalent in Python is IndexError
        try:
            blake3_0.doFinalize1(byteArray0, -997, -997)
            self.fail("Expecting exception: IndexError")

        except IndexError as e:
            # Offset must be non-negative
            self.assertEqual(type(e), IndexError)

    def test12(self) -> None:

        blake3_0 = Blake3.initHash()
        try:
            blake3_0.doFinalize0(None)
            self.fail("Expecting exception: RuntimeError")

        except ValueError as e:
            self.assertEqual(str(e), "out cannot be None")

    def test11(self) -> None:

        blake3_0 = Blake3.initHash()
        try:
            blake3_0.doFinalize1(None, 2534, -1)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.assertEqual(str(e), "")
            self.assertEqual(type(e).__name__, "RuntimeError")

    def test10(self) -> None:

        try:
            Blake3.hash(None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.assertEqual(str(e), "")

    def test09(self) -> None:

        blake3_0 = Blake3.initHash()
        byteArray0 = blake3_0.doFinalize2(3434)
        blake3_0.doFinalize2(1715)
        Blake3.initKeyDerivationFunction(byteArray0)
        # Undeclared exception in Java code, so no equivalent in Python
        Blake3.hash(byteArray0)

    def test08(self) -> None:

        try:
            Blake3.initKeyDerivationFunction(None)
            self.fail("Expecting exception: RuntimeError")

        except ValueError as e:
            self.assertEqual(str(e), "kdfContext cannot be None")

    def test07(self) -> None:

        try:
            Blake3.initKeyedHash(None)
            self.fail("Expecting exception: RuntimeError")

        except ValueError as e:
            self.assertEqual(str(e), "key cannot be None")

    def test06(self) -> None:

        try:
            Blake3.keyedHash(None, None)
            self.fail("Expecting exception: RuntimeError")

        except ValueError as e:
            self.assertEqual(str(e), "Key and data cannot be None")

    def test05(self) -> None:

        blake3_0 = Blake3.initHash()
        try:
            blake3_0.update0(None)
            self.fail("Expecting exception: RuntimeError")

        except ValueError as e:
            self.assertEqual(str(e), "Input cannot be None")

    def test04(self) -> None:

        blake3_0 = Blake3.initHash()
        byteArray0 = blake3_0.doFinalize2(3437)
        Blake3.initKeyDerivationFunction(byteArray0)
        blake3_1 = Blake3.initKeyDerivationFunction(byteArray0)
        blake3_1.update0(byteArray0)

    def test03(self) -> None:

        blake3_0 = Blake3.initHash()
        try:
            blake3_0.update1(None, 2037, -1964)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.assertEqual(str(e), "")
            self.assertEqual(type(e).__name__, "RuntimeError")

    def test02(self) -> None:

        blake3_0 = Blake3.initHash()
        blake3_0.doFinalize2(0)

    def test01(self) -> None:

        byteArray0 = bytearray(5)
        blake3_0 = Blake3.initKeyDerivationFunction(byteArray0)
        blake3_0.doFinalize1(byteArray0, 2, 2)

    def test00(self) -> None:

        byteArray0 = bytearray(9)
        byteArray1 = Blake3.hash(byteArray0)
        blake3_0 = Blake3.initKeyedHash(byteArray1)
        blake3_0.update1(byteArray1, 0, 32)
