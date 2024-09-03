import pytest

from src.main.org.apache.commons.csv.ExtendedBufferedReader import *
from src.main.org.apache.commons.csv.Constants import *
import unittest
import io

class ExtendedBufferedReaderTest(unittest.TestCase):

    def __createBufferedReader(self, s) -> ExtendedBufferedReader:
        return ExtendedBufferedReader(io.StringIO(s))


    @pytest.mark.test
    def testEmptyInput(self) -> None:
        try:
            br = self.__createBufferedReader("")
            try:
                self.assertEqual(Constants.END_OF_STREAM, br.read0())
                self.assertEqual(Constants.END_OF_STREAM, br.lookAhead0())
                self.assertEqual(Constants.END_OF_STREAM, br.getLastChar())
                self.assertIsNone(br.readLine())
                self.assertEqual(0, br.read1(['\u0000'] * 10, 0, 0))
            finally:
                br.close()
        except Exception as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testReadChar(self) -> None:
        try:
            LF = "\n"
            CR = "\r"
            CRLF = CR + LF
            LFCR = LF + CR  # easier to read the string below
            test = "a" +\
                LF +\
                "b" +\
                CR +\
                "c" +\
                LF +\
                LF +\
                "d" +\
                CR +\
                CR +\
                "e" +\
                LFCR +\
                "f " +\
                CRLF
            EOLeolct = 9

            br = self.__createBufferedReader(test)
            try:
                self.assertEqual(0, br.getCurrentLineNumber())
                while br.readLine() is not None:
                    pass
                self.assertEqual(EOLeolct, br.getCurrentLineNumber())
            finally:
                br.close()
            br = self.__createBufferedReader(test)
            try:
                self.assertEqual(0, br.getCurrentLineNumber())
                while br.read0() != -1:
                    pass
                self.assertEqual(EOLeolct, br.getCurrentLineNumber())
            finally:
                br.close()
            br = self.__createBufferedReader(test)
            try:
                self.assertEqual(0, br.getCurrentLineNumber())
                buff = ['\u0000'] * 10
                while br.read1(buff, 0, 3) != -1:
                    pass
                self.assertEqual(EOLeolct, br.getCurrentLineNumber())
            finally:
                br.close()
        except Exception as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testReadingInDifferentBuffer(self) -> None:
        try:
            tmp1 = ['\u0000'] * 2
            tmp2 = ['\u0000'] * 4
            reader = self.__createBufferedReader("1\r\n2\r\n")
            try:
                reader.read1(tmp1, 0, 2)
                reader.read1(tmp2, 2, 2)
                self.assertEqual(2, reader.getCurrentLineNumber())
            finally:
                reader.close()
        except Exception as e:
            self.fail(f"An unexpected exception occurred: {e}")
        

    @pytest.mark.test
    def testReadLine(self) -> None:
        try:
            br = self.__createBufferedReader("")
            try:
                self.assertIsNone(br.readLine())
            finally:
                br.close()
            br = self.__createBufferedReader('\n')
            try:
                self.assertEqual("", br.readLine())
                self.assertIsNone(br.readLine())
            finally:
                br.close()
            br = self.__createBufferedReader("foo\n\nhello") 
            try:
                self.assertEqual(0, br.getCurrentLineNumber())
                self.assertEqual("foo", br.readLine())
                self.assertEqual(1, br.getCurrentLineNumber())
                self.assertEqual("", br.readLine())
                self.assertEqual(2, br.getCurrentLineNumber())
                self.assertEqual("hello", br.readLine())
                self.assertEqual(3, br.getCurrentLineNumber())
                self.assertIsNone(br.readLine())
                self.assertEqual(3, br.getCurrentLineNumber())
            finally:
                br.close()
            br = self.__createBufferedReader("foo\n\nhello")
            try:
                self.assertEqual("f", chr(br.read0()))
                self.assertEqual("o",  chr(br.lookAhead0()))
                self.assertEqual("oo", br.readLine())
                self.assertEqual(1, br.getCurrentLineNumber())
                self.assertEqual('\n', chr(br.lookAhead0()))
                self.assertEqual("", br.readLine())
                self.assertEqual(2, br.getCurrentLineNumber())
                self.assertEqual("h", chr(br.lookAhead0()))
                self.assertEqual("hello", br.readLine())
                self.assertIsNone(br.readLine())
                self.assertEqual(3, br.getCurrentLineNumber())
            finally:
                br.close()
            br = self.__createBufferedReader("foo\rbaar\r\nfoo")
            try:
                self.assertEqual("foo", br.readLine())
                self.assertEqual("b", chr(br.lookAhead0()))
                self.assertEqual("baar", br.readLine())
                self.assertEqual("f", chr(br.lookAhead0()))
                self.assertEqual("foo", br.readLine())
                self.assertIsNone(br.readLine())
            finally:
                br.close()
        except Exception as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testReadLookahead1(self) -> None:
        try:
            br = self.__createBufferedReader("1\n2\r3\n")
            try:
                self.assertEqual(0, br.getCurrentLineNumber())
                self.assertEqual('1', chr(br.lookAhead0()))
                self.assertEqual(Constants.UNDEFINED, br.getLastChar())
                self.assertEqual(0, br.getCurrentLineNumber())
                self.assertEqual('1', chr(br.read0()))  # Start line 1
                self.assertEqual('1', chr(br.getLastChar()))

                self.assertEqual(1, br.getCurrentLineNumber())
                self.assertEqual('\n', chr(br.lookAhead0()))
                self.assertEqual(1, br.getCurrentLineNumber())
                self.assertEqual('1', chr(br.getLastChar()))
                self.assertEqual('\n', chr(br.read0()))
                self.assertEqual(1, br.getCurrentLineNumber())
                self.assertEqual('\n', chr(br.getLastChar()))
                self.assertEqual(1, br.getCurrentLineNumber())

                self.assertEqual('2', chr(br.lookAhead0()))
                self.assertEqual(1, br.getCurrentLineNumber())
                self.assertEqual('\n', chr(br.getLastChar()))
                self.assertEqual(1, br.getCurrentLineNumber())
                self.assertEqual('2', chr(br.read0()))  # Start line 2
                self.assertEqual(2, br.getCurrentLineNumber())
                self.assertEqual('2', chr(br.getLastChar()))

                self.assertEqual('\r', chr(br.lookAhead0()))
                self.assertEqual(2, br.getCurrentLineNumber())
                self.assertEqual('2', chr(br.getLastChar()))
                self.assertEqual('\r', chr(br.read0()))
                self.assertEqual('\r', chr(br.getLastChar()))
                self.assertEqual(2, br.getCurrentLineNumber())

                self.assertEqual('3', chr(br.lookAhead0()))
                self.assertEqual('\r', chr(br.getLastChar()))
                self.assertEqual('3', chr(br.read0()))  # Start line 3
                self.assertEqual('3', chr(br.getLastChar()))
                self.assertEqual(3, br.getCurrentLineNumber())

                self.assertEqual('\n', chr(br.lookAhead0()))
                self.assertEqual(3, br.getCurrentLineNumber())
                self.assertEqual('3', chr(br.getLastChar()))
                self.assertEqual('\n', chr(br.read0()))
                self.assertEqual(3, br.getCurrentLineNumber())
                self.assertEqual('\n', chr(br.getLastChar()))
                self.assertEqual(3, br.getCurrentLineNumber())

                self.assertEqual(Constants.END_OF_STREAM, br.lookAhead0())
                self.assertEqual('\n', chr(br.getLastChar()))
                self.assertEqual(Constants.END_OF_STREAM, br.read0())
                self.assertEqual(Constants.END_OF_STREAM, br.getLastChar())
                self.assertEqual(Constants.END_OF_STREAM, br.read0())
                self.assertEqual(Constants.END_OF_STREAM, br.lookAhead0())
                self.assertEqual(3, br.getCurrentLineNumber())
            finally:
                br.close()
        except Exception as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testReadLookahead2(self) -> None:
        try:
            ref = ['\u0000'] * 5
            res = ['\u0000'] * 5
            br = self.__createBufferedReader("abcdefg")
            try:
                ref[0] = 'a'
                ref[1] = 'b'
                ref[2] = 'c'
                self.assertEqual(3, br.read1(res, 0, 3))
                self.assertEqual(ref, res)
                self.assertEqual("c", chr(br.getLastChar()))

                self.assertEqual("d", chr(br.lookAhead0()))
                ref[4] = 'd'
                self.assertEqual(1, br.read1(res, 4, 1))
                self.assertEqual(ref, res)
                self.assertEqual("d", chr(br.getLastChar()))
            finally:
                br.close()
        except Exception as e:
            self.fail(f"An unexpected exception occurred: {e}")
