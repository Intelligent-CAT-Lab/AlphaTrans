from __future__ import annotations
import time
import re
import os
import typing
from typing import *
import numbers
from io import StringIO
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.csv.ExtendedBufferedReader import *

# from src.test.org.apache.commons.csv.ExtendedBufferedReader_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class ExtendedBufferedReader_ESTest(unittest.TestCase):

    def test28(self) -> None:

        reader0 = io.StringIO("")
        extendedBufferedReader0 = ExtendedBufferedReader(reader0)
        extendedBufferedReader0.close()
        try:
            extendedBufferedReader0.lookAhead0()
            self.fail("Expecting exception: IOException")

        except IOError as e:
            # Stream closed
            self.verifyException("java.io.BufferedReader", e)

    def test27(self) -> None:
        reader0 = io.StringIO("")
        extendedBufferedReader0 = ExtendedBufferedReader(reader0)
        boolean0 = extendedBufferedReader0.isClosed()
        self.assertFalse(boolean0)

    def test26(self) -> None:

        stringReader0 = io.StringIO("1SQFO+3-8;p^-wG-Cnt")
        extendedBufferedReader0 = ExtendedBufferedReader(stringReader0)
        int0 = extendedBufferedReader0.getLastChar()
        self.assertEqual(-2, int0)

    def test25(self) -> None:
        reader0 = io.StringIO("")
        extendedBufferedReader0 = ExtendedBufferedReader(reader0)
        long0 = extendedBufferedReader0.getPosition()
        self.assertEqual(0, long0)

    def test24(self) -> None:

        stringReader0 = io.StringIO("1SQFO+3-8;p^-wG-Cnt")
        extendedBufferedReader0 = ExtendedBufferedReader(stringReader0)
        string0 = extendedBufferedReader0.readLine()
        self.assertEqual("1SQFO+3-8;p^-wG-Cnt", string0)
        self.assertIsNotNone(string0)

    def test23(self) -> None:

        reader0 = io.StringIO("")  # StringIO is a file-like object in memory
        extendedBufferedReader0 = ExtendedBufferedReader(reader0)
        long0 = extendedBufferedReader0.getCurrentLineNumber()
        self.assertEqual(0, long0)

    def test22(self) -> None:

        reader0 = io.StringIO("")
        extendedBufferedReader0 = ExtendedBufferedReader(reader0)
        int0 = extendedBufferedReader0.read0()
        self.assertEqual(-1, int0)

        long0 = extendedBufferedReader0.getCurrentLineNumber()
        self.assertEqual(1, long0)

    def test21(self) -> None:

        stringReader0 = io.StringIO("q>:2TkH(M")
        extendedBufferedReader0 = ExtendedBufferedReader(stringReader0)
        charArray0 = ["\0"] * 6
        int0 = extendedBufferedReader0.read1(charArray0, 1, 1)
        self.assertEqual(1, int0)
        self.assertListEqual(["\0", "q", "\0", "\0", "\0", "\0"], charArray0)

        long0 = extendedBufferedReader0.getCurrentLineNumber()
        self.assertEqual(1, long0)

    def test20(self) -> None:

        reader0 = io.StringIO("")
        extendedBufferedReader0 = ExtendedBufferedReader(reader0)
        extendedBufferedReader0.read0()
        int0 = extendedBufferedReader0.read0()
        self.assertEqual(-1, int0)

    def test19(self) -> None:

        reader0 = io.StringIO()
        extendedBufferedReader0 = ExtendedBufferedReader(reader0)
        int0 = extendedBufferedReader0.read1(None, 0, 0)
        self.assertEqual(0, int0)

    def test18(self) -> None:

        reader0 = io.StringIO("")
        extendedBufferedReader0 = ExtendedBufferedReader(reader0)
        string0 = extendedBufferedReader0.readLine()
        self.assertIsNone(string0)

    def test17(self) -> None:

        extendedBufferedReader0 = None
        try:
            extendedBufferedReader0 = ExtendedBufferedReader(None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.assertIsInstance(e, RuntimeError)
            # no message in exception (getMessage() returned null)
            # verifyException("java.io.Reader", e)

    def test16(self) -> None:

        reader0 = io.StringIO()
        extendedBufferedReader0 = ExtendedBufferedReader(reader0)
        extendedBufferedReader0.close()
        charArray0 = ["\0"]
        try:
            extendedBufferedReader0.lookAhead1(charArray0)
            self.fail("Expecting exception: IOException")

        except IOError as e:
            # Stream closed
            self.verifyException("java.io.BufferedReader", e)

    def test15(self) -> None:

        reader0 = io.StringIO("")
        extendedBufferedReader0 = ExtendedBufferedReader(reader0)

        with self.assertRaises(TypeError):
            extendedBufferedReader0.lookAhead1(None)

    def test14(self) -> None:

        reader0 = io.StringIO("")
        extendedBufferedReader0 = ExtendedBufferedReader(reader0)
        extendedBufferedReader0.close()
        try:
            extendedBufferedReader0.lookAhead2(212)
            self.fail("Expecting exception: IOException")

        except IOError as e:
            # Stream closed
            self.verifyException("java.io.BufferedReader", e)

    def test13(self) -> None:

        reader0 = io.StringIO("")
        extendedBufferedReader0 = ExtendedBufferedReader(reader0)

        with pytest.raises(NegativeArraySizeException):
            extendedBufferedReader0.lookAhead2(-4253)
            self.fail("Expecting exception: NegativeArraySizeException")

    def test12(self) -> None:

        reader0 = io.StringIO()
        extendedBufferedReader0 = ExtendedBufferedReader(reader0)
        extendedBufferedReader0.close()

        with pytest.raises(IOError):
            extendedBufferedReader0.read0()
            # verifyException("java.io.BufferedReader", e)

    def test11(self) -> None:

        reader0 = io.StringIO()
        extendedBufferedReader0 = ExtendedBufferedReader(reader0)
        charArray0 = ["\0"] * 6
        extendedBufferedReader0.close()
        try:
            extendedBufferedReader0.read1(charArray0, 1, 1)
            self.fail("Expecting exception: IOException")

        except IOError as e:
            # Stream closed
            self.verifyException("java.io.BufferedReader", e)

    def test10(self) -> None:

        reader0 = io.StringIO("")
        extendedBufferedReader0 = ExtendedBufferedReader(reader0)

        with pytest.raises(TypeError):
            extendedBufferedReader0.read1(None, 30, 30)

    def test09(self) -> None:

        reader0 = io.StringIO()
        extendedBufferedReader0 = ExtendedBufferedReader(reader0)
        extendedBufferedReader0.close()

        with pytest.raises(IOError):
            extendedBufferedReader0.readLine()
            assert False, "Expecting exception: IOException"

        # verifyException("java.io.BufferedReader", e)
        # This line is commented out because it's not clear what "verifyException" is supposed to do.
        # If it's a method in the same class, it should be uncommented.

    def test08(self) -> None:

        stringReader0 = io.StringIO("1SQFO+3-8;p^-wG-Cnt")
        extendedBufferedReader0 = ExtendedBufferedReader(stringReader0)
        int0 = extendedBufferedReader0.read0()
        int1 = extendedBufferedReader0.getLastChar()
        self.assertEqual(49, int1)
        self.assertTrue(int1 == int0)

    def test07(self) -> None:

        reader0 = io.StringIO("")
        extendedBufferedReader0 = ExtendedBufferedReader(reader0)
        charArray0 = ["\0", "\0"]
        extendedBufferedReader0.read1(charArray0, 1, 1)
        long0 = extendedBufferedReader0.getPosition()
        self.assertEqual((-1), long0)

    def test06(self) -> None:

        reader0 = io.StringIO("")
        extendedBufferedReader0 = ExtendedBufferedReader(reader0)
        int0 = extendedBufferedReader0.read0()
        self.assertEqual(-1, int0)

        long0 = extendedBufferedReader0.getPosition()
        self.assertEqual(1, long0)

    def test05(self) -> None:
        reader0 = io.StringIO("")
        extendedBufferedReader0 = ExtendedBufferedReader(reader0)
        extendedBufferedReader0.close()
        boolean0 = extendedBufferedReader0.isClosed()
        self.assertTrue(boolean0)

    def test04(self) -> None:

        stringReader0 = io.StringIO("F,2=")
        extendedBufferedReader0 = ExtendedBufferedReader(stringReader0)
        charArray0 = extendedBufferedReader0.lookAhead2(4612)
        int0 = extendedBufferedReader0.read1(charArray0, 1, 32)
        self.assertEqual(4, int0)
        self.assertEqual(4612, len(charArray0))

        int1 = extendedBufferedReader0.lookAhead0()
        self.assertEqual(-1, int1)

    def test03(self) -> None:

        stringReader0 = io.StringIO("zu-4~(,lL9p (")
        extendedBufferedReader0 = ExtendedBufferedReader(stringReader0)
        int0 = extendedBufferedReader0.lookAhead0()
        self.assertEqual(122, int0)

    def test02(self) -> None:

        reader0 = io.StringIO("")
        extendedBufferedReader0 = ExtendedBufferedReader(reader0)
        charArray0 = extendedBufferedReader0.lookAhead2(0)
        charArray1 = extendedBufferedReader0.lookAhead1(charArray0)
        self.assertEqual(0, len(charArray1))

    def test01(self) -> None:

        stringReader0 = io.StringIO("1SQFO+3-8;p^-wG-Cnt")
        extendedBufferedReader0 = ExtendedBufferedReader(stringReader0)
        charArray0 = [""]
        charArray1 = extendedBufferedReader0.lookAhead1(charArray0)
        self.assertEqual(1, len(charArray1))

    def test00(self) -> None:

        reader0 = io.StringIO("")
        extendedBufferedReader0 = ExtendedBufferedReader(reader0)
        charArray0 = extendedBufferedReader0.lookAhead2(1406)

        with pytest.raises(IndexError):
            extendedBufferedReader0.read1(charArray0, 478, -1)
            pytest.fail("Expecting exception: IndexError")
