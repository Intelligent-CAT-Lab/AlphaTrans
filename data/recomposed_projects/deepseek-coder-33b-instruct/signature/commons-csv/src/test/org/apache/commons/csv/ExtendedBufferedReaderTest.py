from __future__ import annotations
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
from src.main.org.apache.commons.csv.Constants import *
from src.main.org.apache.commons.csv.ExtendedBufferedReader import *


class ExtendedBufferedReaderTest(unittest.TestCase):

    def testReadLookahead2(self) -> None:

        ref = [""] * 5
        res = [""] * 5

        with self.__createBufferedReader("abcdefg") as br:
            ref[0] = "a"
            ref[1] = "b"
            ref[2] = "c"
            self.assertEqual(3, br.read1(res, 0, 3))
            self.assertListEqual(ref, res)
            self.assertEqual("c", br.getLastChar())

            self.assertEqual("d", br.lookAhead0())
            ref[4] = "d"
            self.assertEqual(1, br.read1(res, 4, 1))
            self.assertListEqual(ref, res)
            self.assertEqual("d", br.getLastChar())

    def testReadLookahead1(self) -> None:

        with self.__createBufferedReader("1\n2\r3\n") as br:
            self.assertEqual(0, br.getCurrentLineNumber())
            self.assertEqual(ord("1"), br.lookAhead0())
            self.assertEqual(UNDEFINED, br.getLastChar())
            self.assertEqual(0, br.getCurrentLineNumber())
            self.assertEqual(ord("1"), br.read0())  # Start line 1
            self.assertEqual(ord("1"), br.getLastChar())

            self.assertEqual(1, br.getCurrentLineNumber())
            self.assertEqual(ord("\n"), br.lookAhead0())
            self.assertEqual(1, br.getCurrentLineNumber())
            self.assertEqual(ord("1"), br.getLastChar())
            self.assertEqual(ord("\n"), br.read0())
            self.assertEqual(1, br.getCurrentLineNumber())
            self.assertEqual(ord("\n"), br.getLastChar())
            self.assertEqual(1, br.getCurrentLineNumber())

            self.assertEqual(ord("2"), br.lookAhead0())
            self.assertEqual(1, br.getCurrentLineNumber())
            self.assertEqual(ord("\n"), br.getLastChar())
            self.assertEqual(1, br.getCurrentLineNumber())
            self.assertEqual(ord("2"), br.read0())  # Start line 2
            self.assertEqual(2, br.getCurrentLineNumber())
            self.assertEqual(ord("2"), br.getLastChar())

            self.assertEqual(ord("\r"), br.lookAhead0())
            self.assertEqual(2, br.getCurrentLineNumber())
            self.assertEqual(ord("2"), br.getLastChar())
            self.assertEqual(ord("\r"), br.read0())
            self.assertEqual(ord("\r"), br.getLastChar())
            self.assertEqual(2, br.getCurrentLineNumber())

            self.assertEqual(ord("3"), br.lookAhead0())
            self.assertEqual(ord("\r"), br.getLastChar())
            self.assertEqual(ord("3"), br.read0())  # Start line 3
            self.assertEqual(ord("3"), br.getLastChar())
            self.assertEqual(3, br.getCurrentLineNumber())

            self.assertEqual(ord("\n"), br.lookAhead0())
            self.assertEqual(3, br.getCurrentLineNumber())
            self.assertEqual(ord("3"), br.getLastChar())
            self.assertEqual(ord("\n"), br.read0())
            self.assertEqual(3, br.getCurrentLineNumber())
            self.assertEqual(ord("\n"), br.getLastChar())
            self.assertEqual(3, br.getCurrentLineNumber())

            self.assertEqual(END_OF_STREAM, br.lookAhead0())
            self.assertEqual(ord("\n"), br.getLastChar())
            self.assertEqual(END_OF_STREAM, br.read0())
            self.assertEqual(END_OF_STREAM, br.getLastChar())
            self.assertEqual(END_OF_STREAM, br.read0())
            self.assertEqual(END_OF_STREAM, br.lookAhead0())
            self.assertEqual(3, br.getCurrentLineNumber())

    def testReadLine(self) -> None:

        # Test 1
        with self.__createBufferedReader("") as br:
            self.assertIsNone(br.readLine())

        # Test 2
        with self.__createBufferedReader("\n") as br:
            self.assertEqual("", br.readLine())
            self.assertIsNone(br.readLine())

        # Test 3
        with self.__createBufferedReader("foo\n\nhello") as br:
            self.assertEqual(0, br.getCurrentLineNumber())
            self.assertEqual("foo", br.readLine())
            self.assertEqual(1, br.getCurrentLineNumber())
            self.assertEqual("", br.readLine())
            self.assertEqual(2, br.getCurrentLineNumber())
            self.assertEqual("hello", br.readLine())
            self.assertEqual(3, br.getCurrentLineNumber())
            self.assertIsNone(br.readLine())
            self.assertEqual(3, br.getCurrentLineNumber())

        # Test 4
        with self.__createBufferedReader("foo\n\nhello") as br:
            self.assertEqual("f", br.read0())
            self.assertEqual("o", br.lookAhead0())
            self.assertEqual("oo", br.readLine())
            self.assertEqual(1, br.getCurrentLineNumber())
            self.assertEqual("\n", br.lookAhead0())
            self.assertEqual("", br.readLine())
            self.assertEqual(2, br.getCurrentLineNumber())
            self.assertEqual("h", br.lookAhead0())
            self.assertEqual("hello", br.readLine())
            self.assertIsNone(br.readLine())
            self.assertEqual(3, br.getCurrentLineNumber())

        # Test 5
        with self.__createBufferedReader("foo\rbaar\r\nfoo") as br:
            self.assertEqual("foo", br.readLine())
            self.assertEqual("b", br.lookAhead0())
            self.assertEqual("baar", br.readLine())
            self.assertEqual("f", br.lookAhead0())
            self.assertEqual("foo", br.readLine())
            self.assertIsNone(br.readLine())

    def testReadingInDifferentBuffer(self) -> None:

        tmp1 = ["\0"] * 2
        tmp2 = ["\0"] * 4
        try:
            reader = self.__createBufferedReader("1\r\n2\r\n")
            reader.read1(tmp1, 0, 2)
            reader.read1(tmp2, 2, 2)
            self.assertEqual(2, reader.getCurrentLineNumber())
        finally:
            reader.close()

    def testReadChar(self) -> None:

        LF = "\n"
        CR = "\r"
        CRLF = CR + LF
        LFCR = LF + CR
        test = (
            "a"
            + LF
            + "b"
            + CR
            + "c"
            + LF
            + LF
            + "d"
            + CR
            + CR
            + "e"
            + LFCR
            + "f "
            + CRLF
        )
        EOLeolct = 9

        try:
            br = self.__createBufferedReader(test)
            self.assertEqual(0, br.getCurrentLineNumber())
            while br.readLine() != None:
                pass
            self.assertEqual(EOLeolct, br.getCurrentLineNumber())
        finally:
            br.close()

        try:
            br = self.__createBufferedReader(test)
            self.assertEqual(0, br.getCurrentLineNumber())
            while br.read0() != -1:
                pass
            self.assertEqual(EOLeolct, br.getCurrentLineNumber())
        finally:
            br.close()

        try:
            br = self.__createBufferedReader(test)
            self.assertEqual(0, br.getCurrentLineNumber())
            buff = ["\0"] * 10
            while br.read1(buff, 0, 3) != -1:
                pass
            self.assertEqual(EOLeolct, br.getCurrentLineNumber())
        finally:
            br.close()

    def testEmptyInput(self) -> None:

        with self.__createBufferedReader("") as br:
            self.assertEqual(END_OF_STREAM, br.read0())
            self.assertEqual(END_OF_STREAM, br.lookAhead0())
            self.assertEqual(END_OF_STREAM, br.getLastChar())
            self.assertIsNone(br.readLine())
            self.assertEqual(0, br.read1([None] * 10, 0, 0))

    def __createBufferedReader(self, s: str) -> ExtendedBufferedReader:
        return ExtendedBufferedReader(io.StringIO(s))
