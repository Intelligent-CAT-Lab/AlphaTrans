# Imports Begin
from src.main.org.apache.commons.csv.ExtendedBufferedReader import *
from src.main.org.apache.commons.csv.Constants import *
import unittest
import typing
from typing import *
import numbers

# Imports End


class ExtendedBufferedReaderTest(unittest.TestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def testReadLookahead2(self) -> None:

        ref = ["a", "b", "c"]
        res = ["a", "b", "c"]
        with self.__createBufferedReader("abcdefg") as br:
            self.assertEqual(3, br.read1(res, 0, 3))
            assertArrayEquals(ref, res)
            self.assertEqual("c", br.getLastChar())
            self.assertEqual("d", br.lookAhead0())
            ref.append("d")
            self.assertEqual(1, br.read1(res, 4, 1))
            assertArrayEquals(ref, res)
            self.assertEqual("d", br.getLastChar())

    def testReadLookahead1(self) -> None:

        with self.assertRaises(Exception):
            br = self.__createBufferedReader("1\n2\r3\n")
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

    def testReadingInDifferentBuffer(self) -> None:

        tmp1 = [0] * 2
        tmp2 = [0] * 4
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
            while br.readLine() is not None:
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

        with self.__createBufferedReader("") as br:
            self.assertEqual(br.read0(), END_OF_STREAM)
            self.assertEqual(br.lookAhead0(), END_OF_STREAM)
            self.assertEqual(br.getLastChar(), END_OF_STREAM)
            self.assertIsNone(br.readLine())
            self.assertEqual(br.read1(typing.List[str], 0, 0), 0)

    def __createBufferedReader(self, s: str) -> ExtendedBufferedReader:

        return ExtendedBufferedReader(StringReader(s))

    # Class Methods End
