from __future__ import annotations
import re
import typing
from typing import *
import numbers
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.csv.Constants import *
from src.main.org.apache.commons.csv.ExtendedBufferedReader import *


class ExtendedBufferedReaderTest(unittest.TestCase):

    def testReadLookahead2(self) -> None:
        ref = ["a", "b", "c", "d", "e"]
        res = ["a", "b", "c", "d", "e"]

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
        with ExtendedBufferedReader(self.__createBufferedReader("1\n2\r3\n")) as br:
            self.assertEqual(0, br.getCurrentLineNumber())
            self.assertEqual("1", br.lookAhead0())
            self.assertEqual(UNDEFINED, br.getLastChar())
            self.assertEqual(0, br.getCurrentLineNumber())
            self.assertEqual("1", br.read0())  # Start line 1
            self.assertEqual("1", br.getLastChar())

            self.assertEqual(1, br.getCurrentLineNumber())
            self.assertEqual("\n", br.lookAhead0())
            self.assertEqual(1, br.getCurrentLineNumber())
            self.assertEqual("1", br.getLastChar())
            self.assertEqual("\n", br.read0())
            self.assertEqual(1, br.getCurrentLineNumber())
            self.assertEqual("\n", br.getLastChar())
            self.assertEqual(1, br.getCurrentLineNumber())

            self.assertEqual("2", br.lookAhead0())
            self.assertEqual(1, br.getCurrentLineNumber())
            self.assertEqual("\n", br.getLastChar())
            self.assertEqual(1, br.getCurrentLineNumber())
            self.assertEqual("2", br.read0())  # Start line 2
            self.assertEqual(2, br.getCurrentLineNumber())
            self.assertEqual("2", br.getLastChar())

            self.assertEqual("\r", br.lookAhead0())
            self.assertEqual(2, br.getCurrentLineNumber())
            self.assertEqual("2", br.getLastChar())
            self.assertEqual("\r", br.read0())
            self.assertEqual("\r", br.getLastChar())
            self.assertEqual(2, br.getCurrentLineNumber())

            self.assertEqual("3", br.lookAhead0())
            self.assertEqual("\r", br.getLastChar())
            self.assertEqual("3", br.read0())  # Start line 3
            self.assertEqual("3", br.getLastChar())
            self.assertEqual(3, br.getCurrentLineNumber())

            self.assertEqual("\n", br.lookAhead0())
            self.assertEqual(3, br.getCurrentLineNumber())
            self.assertEqual("3", br.getLastChar())
            self.assertEqual("\n", br.read0())
            self.assertEqual(3, br.getCurrentLineNumber())
            self.assertEqual("\n", br.getLastChar())
            self.assertEqual(3, br.getCurrentLineNumber())

            self.assertEqual(END_OF_STREAM, br.lookAhead0())
            self.assertEqual("\n", br.getLastChar())
            self.assertEqual(END_OF_STREAM, br.read0())
            self.assertEqual(END_OF_STREAM, br.getLastChar())
            self.assertEqual(END_OF_STREAM, br.read0())
            self.assertEqual(END_OF_STREAM, br.lookAhead0())
            self.assertEqual(3, br.getCurrentLineNumber())

    def testReadLine(self) -> None:

        pass  # LLM could not translate this method

    def testReadingInDifferentBuffer(self) -> None:
        tmp1: typing.List[str] = [""] * 2
        tmp2: typing.List[str] = [""] * 4
        with self.__createBufferedReader("1\r\n2\r\n") as reader:
            reader.read1(tmp1, 0, 2)
            reader.read1(tmp2, 2, 2)
            self.assertEqual(2, reader.getCurrentLineNumber())

    def testReadChar(self) -> None:
        LF = "\n"
        CR = "\r"
        CRLF = CR + LF
        LFCR = LF + CR  # easier to read the string below
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

        with self.__createBufferedReader(test) as br:
            self.assertEqual(0, br.getCurrentLineNumber())
            while br.readLine() != None:
                pass
            self.assertEqual(EOLeolct, br.getCurrentLineNumber())
        with self.__createBufferedReader(test) as br:
            self.assertEqual(0, br.getCurrentLineNumber())
            while br.read0() != -1:
                pass
            self.assertEqual(EOLeolct, br.getCurrentLineNumber())
        with self.__createBufferedReader(test) as br:
            self.assertEqual(0, br.getCurrentLineNumber())
            buff = [None] * 10
            while br.read1(buff, 0, 3) != -1:
                pass
            self.assertEqual(EOLeolct, br.getCurrentLineNumber())

    def testEmptyInput(self) -> None:
        with ExtendedBufferedReader(self.__createBufferedReader("")) as br:
            self.assertEqual(END_OF_STREAM, br.read0())
            self.assertEqual(END_OF_STREAM, br.lookAhead0())
            self.assertEqual(END_OF_STREAM, br.getLastChar())
            self.assertIsNone(br.readLine())
            self.assertEqual(0, br.read1([""] * 10, 0, 0))

    def __createBufferedReader(self, s: str) -> ExtendedBufferedReader:
        return ExtendedBufferedReader(StringReader(s))
