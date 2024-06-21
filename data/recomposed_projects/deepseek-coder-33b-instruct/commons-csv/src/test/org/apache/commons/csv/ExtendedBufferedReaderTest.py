from __future__ import annotations
import re
import unittest
import pytest
import io
from src.main.org.apache.commons.csv.Constants import *
from src.main.org.apache.commons.csv.ExtendedBufferedReader import *


class ExtendedBufferedReaderTest(unittest.TestCase):

    @pytest.mark.test
    def testReadLookahead2(self) -> None:

        ref = ["a", "b", "c", "", "d"]
        res = ["", "", "", "", ""]

        with self.__createBufferedReader("abcdefg") as br:
            self.assertEqual(3, br.read1(res, 0, 3))
            self.assertEqual(ref, res)
            self.assertEqual("c", br.getLastChar())

            self.assertEqual("d", br.lookAhead0())
            self.assertEqual(1, br.read1(res, 4, 1))
            self.assertEqual(ref, res)
            self.assertEqual("d", br.getLastChar())

    @pytest.mark.test
    def testReadLookahead1(self) -> None:

        with self.__createBufferedReader("1\n2\r3\n") as br:
            self.assertEqual(0, br.getCurrentLineNumber())
            self.assertEqual("1", chr(br.lookAhead0()))
            self.assertEqual(UNDEFINED, br.getLastChar())
            self.assertEqual(0, br.getCurrentLineNumber())
            self.assertEqual("1", chr(br.read0()))  # Start line 1
            self.assertEqual("1", chr(br.getLastChar()))

            self.assertEqual(1, br.getCurrentLineNumber())
            self.assertEqual("\n", chr(br.lookAhead0()))
            self.assertEqual(1, br.getCurrentLineNumber())
            self.assertEqual("1", chr(br.getLastChar()))
            self.assertEqual("\n", chr(br.read0()))
            self.assertEqual(1, br.getCurrentLineNumber())
            self.assertEqual("\n", chr(br.getLastChar()))
            self.assertEqual(1, br.getCurrentLineNumber())

            self.assertEqual("2", chr(br.lookAhead0()))
            self.assertEqual(1, br.getCurrentLineNumber())
            self.assertEqual("\n", chr(br.getLastChar()))
            self.assertEqual(1, br.getCurrentLineNumber())
            self.assertEqual("2", chr(br.read0()))  # Start line 2
            self.assertEqual(2, br.getCurrentLineNumber())
            self.assertEqual("2", chr(br.getLastChar()))

            self.assertEqual("\r", chr(br.lookAhead0()))
            self.assertEqual(2, br.getCurrentLineNumber())
            self.assertEqual("2", chr(br.getLastChar()))
            self.assertEqual("\r", chr(br.read0()))
            self.assertEqual("\r", chr(br.getLastChar()))
            self.assertEqual(2, br.getCurrentLineNumber())

            self.assertEqual("3", chr(br.lookAhead0()))
            self.assertEqual("\r", chr(br.getLastChar()))
            self.assertEqual("3", chr(br.read0()))  # Start line 3
            self.assertEqual("3", chr(br.getLastChar()))
            self.assertEqual(3, br.getCurrentLineNumber())

            self.assertEqual("\n", chr(br.lookAhead0()))
            self.assertEqual(3, br.getCurrentLineNumber())
            self.assertEqual("3", chr(br.getLastChar()))
            self.assertEqual("\n", chr(br.read0()))
            self.assertEqual(3, br.getCurrentLineNumber())
            self.assertEqual("\n", chr(br.getLastChar()))
            self.assertEqual(3, br.getCurrentLineNumber())

            self.assertEqual(END_OF_STREAM, br.lookAhead0())
            self.assertEqual("\n", chr(br.getLastChar()))
            self.assertEqual(END_OF_STREAM, br.read0())
            self.assertEqual(END_OF_STREAM, br.getLastChar())
            self.assertEqual(END_OF_STREAM, br.read0())
            self.assertEqual(END_OF_STREAM, br.lookAhead0())
            self.assertEqual(3, br.getCurrentLineNumber())

    @pytest.mark.test
    def testReadLine(self) -> None:

        with self.__createBufferedReader("") as br:
            self.assertIsNone(br.readLine())

        with self.__createBufferedReader("\n") as br:
            self.assertEqual("", br.readLine())
            self.assertIsNone(br.readLine())

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

        with self.__createBufferedReader("foo\rbaar\r\nfoo") as br:
            self.assertEqual("foo", br.readLine())
            self.assertEqual("b", br.lookAhead0())
            self.assertEqual("baar", br.readLine())
            self.assertEqual("f", br.lookAhead0())
            self.assertEqual("foo", br.readLine())
            self.assertIsNone(br.readLine())

    @pytest.mark.test
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

    @pytest.mark.test
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

        br = self.__createBufferedReader(test)
        self.assertEqual(0, br.getCurrentLineNumber())
        while br.readLine() is not None:
            pass
        self.assertEqual(EOLeolct, br.getCurrentLineNumber())

        br = self.__createBufferedReader(test)
        self.assertEqual(0, br.getCurrentLineNumber())
        while br.read0() != -1:
            pass
        self.assertEqual(EOLeolct, br.getCurrentLineNumber())

        br = self.__createBufferedReader(test)
        self.assertEqual(0, br.getCurrentLineNumber())
        buff = [""] * 10
        while br.read1(buff, 0, 3) != -1:
            pass
        self.assertEqual(EOLeolct, br.getCurrentLineNumber())

    @pytest.mark.test
    def testEmptyInput(self) -> None:

        with self.__createBufferedReader("") as br:
            self.assertEqual(END_OF_STREAM, br.read0())
            self.assertEqual(END_OF_STREAM, br.lookAhead0())
            self.assertEqual(END_OF_STREAM, br.getLastChar())
            self.assertIsNone(br.readLine())
            self.assertEqual(0, br.read1([None] * 10, 0, 0))

    def __createBufferedReader(self, s: str) -> ExtendedBufferedReader:

        return ExtendedBufferedReader(io.StringIO(s))
