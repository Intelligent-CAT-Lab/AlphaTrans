from __future__ import annotations
import time
import re
import os
import numbers
from io import StringIO
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.csv.CSVFormat import *
from src.main.org.apache.commons.csv.ExtendedBufferedReader import *
from src.main.org.apache.commons.csv.Lexer import *

# from src.test.org.apache.commons.csv.Lexer_ESTest_scaffolding import *
from src.main.org.apache.commons.csv.Token import *

# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class Lexer_ESTest(unittest.TestCase):

    def test44(self) -> None:

        cSVFormat0 = CSVFormat.INFORMIX_UNLOAD
        stringReader0 = io.StringIO(")\r\n")
        extendedBufferedReader0 = ExtendedBufferedReader(stringReader0)
        lexer0 = Lexer(cSVFormat0, extendedBufferedReader0)
        long0 = lexer0.getCharacterPosition()
        self.assertEqual(0, long0)

    def test43(self) -> None:

        cSVFormat0 = CSVFormat.MONGODB_TSV
        stringReader0 = io.StringIO(")\r\n")
        extendedBufferedReader0 = ExtendedBufferedReader(stringReader0)
        lexer0 = Lexer(cSVFormat0, extendedBufferedReader0)
        string0 = lexer0.getFirstEol()
        self.assertIsNone(string0)

    def test42(self) -> None:

        cSVFormat0 = CSVFormat.MONGODB_TSV
        stringReader0 = io.StringIO("The delimiter cannot be a line break")
        extendedBufferedReader0 = ExtendedBufferedReader(stringReader0)
        lexer0 = Lexer(cSVFormat0, extendedBufferedReader0)
        long0 = lexer0.getCurrentLineNumber()
        self.assertEqual(0, long0)

    def test41(self) -> None:

        cSVFormat0 = CSVFormat.INFORMIX_UNLOAD
        stringReader0 = io.StringIO("")
        extendedBufferedReader0 = ExtendedBufferedReader(stringReader0)
        lexer0 = Lexer(cSVFormat0, extendedBufferedReader0)
        boolean0 = lexer0.isClosed()
        self.assertFalse(boolean0)

    def test40(self) -> None:

        csv_format0 = CSVFormat.DEFAULT
        string_reader0 = io.StringIO("The delimiter cannot be a line break")
        extended_buffered_reader0 = ExtendedBufferedReader(string_reader0)
        token0 = Token()
        lexer0 = Lexer(csv_format0, extended_buffered_reader0)
        lexer0.nextToken(token0)
        try:
            lexer0.readEscape()
            self.fail("Expecting exception: IOException")

        except IOError as e:
            # EOF whilst processing escape sequence
            self.verifyException("org.apache.commons.csv.Lexer", e)

    def test39(self) -> None:

        csv_format0 = CSVFormat.INFORMIX_UNLOAD
        reader0 = ExtendedBufferedReader(io.StringIO(""))
        lexer0 = Lexer(csv_format0, reader0)
        boolean0 = lexer0.isCommentStart(65534)
        self.assertTrue(boolean0)

    def test38(self) -> None:

        csv_format0 = CSVFormat.MONGODB_TSV
        reader0 = ExtendedBufferedReader(io.StringIO(""))
        lexer0 = Lexer(csv_format0, reader0)
        boolean0 = lexer0.isDelimiter(9)
        self.assertTrue(boolean0)

    def test37(self) -> None:

        csv_format0 = CSVFormat.DEFAULT
        string_reader0 = io.StringIO("The delimiter cannot be a line break")
        extended_buffered_reader0 = ExtendedBufferedReader(string_reader0)
        lexer0 = Lexer(csv_format0, extended_buffered_reader0)
        boolean0 = lexer0.isEscapeDelimiter()
        self.assertFalse(boolean0)

    def test36(self) -> None:

        csv_format0 = CSVFormat.INFORMIX_UNLOAD
        string_reader0 = io.StringIO(")\r\n")
        extended_buffered_reader0 = ExtendedBufferedReader(string_reader0)
        lexer0 = Lexer(csv_format0, extended_buffered_reader0)
        lexer0.readEscape()
        token0 = Token()
        token1 = lexer0.nextToken(token0)
        self.assertIs(token1, token0)

    def test35(self) -> None:

        cSVFormat0 = CSVFormat.TDF
        stringReader0 = io.StringIO('2"jd5*jbNaI)QKi')
        extendedBufferedReader0 = ExtendedBufferedReader(stringReader0)
        lexer0 = Lexer(cSVFormat0, extendedBufferedReader0)
        int0 = lexer0.readEscape()
        self.assertEqual((-1), int0)

        int1 = lexer0.readEscape()
        self.assertEqual(34, int1)

    def test34(self) -> None:

        csv_format0 = CSVFormat.MONGODB_TSV
        string_reader0 = io.StringIO("The delimiter cannot be a line break")
        extended_buffered_reader0 = ExtendedBufferedReader(string_reader0)
        lexer0 = Lexer(csv_format0, extended_buffered_reader0)
        boolean0 = lexer0.isStartOfLine(10)
        self.assertTrue(boolean0)

    def test33(self) -> None:

        csv_format0 = CSVFormat.MONGODB_TSV
        string_reader0 = io.StringIO(")\r\n")
        extended_buffered_reader0 = ExtendedBufferedReader(string_reader0)
        lexer0 = Lexer(csv_format0, extended_buffered_reader0)
        token0 = Token()
        lexer0.readEscape()
        lexer0.readEscape()
        token1 = lexer0.nextToken(token0)
        self.assertIs(token0, token1)

    def test32(self) -> None:

        stringReader0 = io.StringIO("khe delimiter canno. be a line break")
        extendedBufferedReader0 = ExtendedBufferedReader(stringReader0)
        cSVFormat0 = CSVFormat.POSTGRESQL_TEXT
        lexer0 = Lexer(cSVFormat0, extendedBufferedReader0)
        token0 = Token()
        token1 = lexer0.nextToken(token0)
        token2 = lexer0.nextToken(token1)
        self.assertIs(token1, token2)

    def test31(self) -> None:

        csv_format0 = CSVFormat.INFORMIX_UNLOAD
        string_reader0 = io.StringIO(")\r\n")
        extended_buffered_reader0 = ExtendedBufferedReader(string_reader0)
        lexer0 = Lexer(csv_format0, extended_buffered_reader0)
        token0 = Token()
        token1 = lexer0.nextToken(token0)
        token2 = lexer0.nextToken(token1)
        self.assertIs(token2, token0)

    def test30(self) -> None:

        csv_format0 = CSVFormat.TDF
        string_reader0 = io.StringIO("The delimiter cannot be a line break")
        extended_buffered_reader0 = ExtendedBufferedReader(string_reader0)
        token0 = Token()
        lexer0 = Lexer(csv_format0, extended_buffered_reader0)
        token1 = lexer0.nextToken(token0)
        self.assertIs(token1, token0)

    def test29(self) -> None:

        cSVFormat0 = CSVFormat.TDF
        stringReader0 = io.StringIO("The delimiter cannot be a line break")
        extendedBufferedReader0 = ExtendedBufferedReader(stringReader0)
        lexer0 = Lexer(cSVFormat0, extendedBufferedReader0)
        boolean0 = lexer0.readEndOfLine(13)
        self.assertTrue(boolean0)

    def test28(self) -> None:

        csv_format0 = CSVFormat.MONGODB_TSV
        string_reader0 = io.StringIO(")\r\n")
        extended_buffered_reader0 = ExtendedBufferedReader(string_reader0)
        lexer0 = Lexer(csv_format0, extended_buffered_reader0)
        int0 = lexer0.readEscape()
        self.assertEqual(-1, int0)

        lexer0.readEscape()
        int1 = lexer0.readEscape()
        self.assertEqual(10, int1)

    def test27(self) -> None:

        cSVFormat0 = CSVFormat.MONGODB_TSV
        stringReader0 = io.StringIO("bZFFw_G;")
        extendedBufferedReader0 = ExtendedBufferedReader(stringReader0)
        lexer0 = Lexer(cSVFormat0, extendedBufferedReader0)
        int0 = lexer0.readEscape()
        self.assertEqual(8, int0)

    def test26(self) -> None:

        csv_format0 = CSVFormat.MONGODB_TSV
        string_reader0 = io.StringIO("org.apache.commons.csv.Lexer")
        extended_buffered_reader0 = ExtendedBufferedReader(string_reader0)
        lexer0 = Lexer(csv_format0, extended_buffered_reader0)
        int0 = lexer0.readEscape()
        self.assertEqual(-1, int0)

        int1 = lexer0.readEscape()
        self.assertEqual(13, int1)

    def test25(self) -> None:

        stringReader0 = io.StringIO("t# EauyH91")
        extendedBufferedReader0 = ExtendedBufferedReader(stringReader0)
        cSVFormat0 = CSVFormat.POSTGRESQL_TEXT
        lexer0 = Lexer(cSVFormat0, extendedBufferedReader0)
        int0 = lexer0.readEscape()
        self.assertEqual(9, int0)

        int1 = lexer0.readEscape()
        self.assertEqual(-1, int1)

    def test24(self) -> None:

        cSVFormat0 = CSVFormat.INFORMIX_UNLOAD
        reader0 = ExtendedBufferedReader(io.StringIO(""))
        lexer0 = Lexer(cSVFormat0, reader0)
        stringBuilder0 = io.StringIO()
        lexer0.trimTrailingSpaces(stringBuilder0)
        self.assertEqual("", stringBuilder0.getvalue())

    def test23(self) -> None:

        reader0 = io.StringIO("")
        extendedBufferedReader0 = ExtendedBufferedReader(reader0)
        lexer0 = None
        try:
            lexer0 = Lexer(None, extendedBufferedReader0)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.assertEqual(str(e.__class__), "<class 'org.apache.commons.csv.Lexer'>")

    def test22(self) -> None:

        pipedReader0 = io.PipeReader()
        extendedBufferedReader0 = ExtendedBufferedReader(pipedReader0)
        cSVFormat0 = CSVFormat.ORACLE
        lexer0 = Lexer(cSVFormat0, extendedBufferedReader0)

        try:
            lexer0.isEscapeDelimiter()
            self.fail("Expecting exception: IOException")

        except IOError as e:
            # Pipe not connected
            self.verifyException("java.io.PipedReader", e)

    def test21(self) -> None:

        cSVFormat0 = CSVFormat.MYSQL
        lexer0 = Lexer(cSVFormat0, None)

        try:
            lexer0.isEscapeDelimiter()
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.verifyException("org.apache.commons.csv.Lexer", e)

    def test20(self) -> None:

        csv_format0 = CSVFormat.POSTGRESQL_CSV
        piped_reader0 = io.PipedReader()
        extended_buffered_reader0 = ExtendedBufferedReader(piped_reader0)
        lexer0 = Lexer(csv_format0, extended_buffered_reader0)
        token0 = Token()
        try:
            lexer0.nextToken(token0)
            self.fail("Expecting exception: IOException")

        except IOError as e:
            # Pipe not connected
            self.verifyException("java.io.PipedReader", e)

    def test19(self) -> None:

        csv_format0 = CSVFormat.RFC4180
        lexer0 = Lexer(csv_format0, None)

        try:
            lexer0.nextToken(None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.verifyException("org.apache.commons.csv.Lexer", e)

    def test18(self) -> None:

        csv_format0 = CSVFormat.MONGODB_TSV
        lexer0 = Lexer(csv_format0, None)

        try:
            lexer0.readEscape()
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.verifyException("org.apache.commons.csv.Lexer", e)

    def test17(self) -> None:

        cSVFormat0 = CSVFormat.INFORMIX_UNLOAD
        stringReader0 = io.StringIO("")
        extendedBufferedReader0 = ExtendedBufferedReader(stringReader0)
        lexer0 = Lexer(cSVFormat0, extendedBufferedReader0)

        with pytest.raises(RuntimeError):
            lexer0.trimTrailingSpaces(None)
            self.fail("Expecting exception: RuntimeError")

    def test16(self) -> None:

        cSVFormat0 = CSVFormat.INFORMIX_UNLOAD
        stringReader0 = io.StringIO(")\r\n")
        extendedBufferedReader0 = ExtendedBufferedReader(stringReader0)
        lexer0 = Lexer(cSVFormat0, extendedBufferedReader0)
        lexer0.readEscape()
        long0 = lexer0.getCharacterPosition()
        self.assertEqual(1, long0)

    def test15(self) -> None:

        csv_format0 = CSVFormat.MONGODB_TSV
        string_reader0 = io.StringIO("The delimiter cannot be a line break")
        extended_buffered_reader0 = ExtendedBufferedReader(string_reader0)
        lexer0 = Lexer(csv_format0, extended_buffered_reader0)
        lexer0.readEscape()
        long0 = lexer0.getCurrentLineNumber()
        self.assertEqual(1, long0)

    def test14(self) -> None:

        csv_format0 = CSVFormat.MONGODB_TSV
        string_reader0 = io.StringIO(")\r\n")
        extended_buffered_reader0 = ExtendedBufferedReader(string_reader0)
        lexer0 = Lexer(csv_format0, extended_buffered_reader0)
        token0 = Token()
        lexer0.nextToken(token0)
        string0 = lexer0.getFirstEol()
        self.assertEqual("\r\n", string0)
        self.assertIsNotNone(string0)

    def test13(self) -> None:

        cSVFormat0 = CSVFormat.INFORMIX_UNLOAD
        stringReader0 = io.StringIO("")
        extendedBufferedReader0 = ExtendedBufferedReader(stringReader0)
        lexer0 = Lexer(cSVFormat0, extendedBufferedReader0)
        lexer0.close()
        boolean0 = lexer0.isClosed()
        self.assertTrue(boolean0)

    def test12(self) -> None:

        cSVFormat0 = CSVFormat.INFORMIX_UNLOAD
        stringReader0 = io.StringIO("")
        extendedBufferedReader0 = ExtendedBufferedReader(stringReader0)
        lexer0 = Lexer(cSVFormat0, extendedBufferedReader0)
        boolean0 = lexer0.isCommentStart(0)
        self.assertFalse(boolean0)

    def test11(self) -> None:

        cSVFormat0 = CSVFormat.newFormat("y")
        reader0 = Reader.nullReader()
        extendedBufferedReader0 = ExtendedBufferedReader(reader0)
        lexer0 = Lexer(cSVFormat0, extendedBufferedReader0)
        boolean0 = lexer0.isDelimiter(-992)
        self.assertFalse(boolean0)

    def test10(self) -> None:
        cSVFormat0 = CSVFormat.MYSQL
        lexer0 = Lexer(cSVFormat0, None)
        boolean0 = lexer0.isEndOfFile(0)
        self.assertFalse(boolean0)

    def test09(self) -> None:

        cSVFormat0 = CSVFormat.MONGODB_TSV
        stringReader0 = io.StringIO(")\r\n")
        extendedBufferedReader0 = ExtendedBufferedReader(stringReader0)
        lexer0 = Lexer(cSVFormat0, extendedBufferedReader0)
        boolean0 = lexer0.isEndOfFile(-1)
        self.assertTrue(boolean0)

    def test08(self) -> None:

        cSVFormat0 = CSVFormat.INFORMIX_UNLOAD
        stringReader0 = io.StringIO("")
        extendedBufferedReader0 = ExtendedBufferedReader(stringReader0)
        lexer0 = Lexer(cSVFormat0, extendedBufferedReader0)
        boolean0 = lexer0.isEscape(0)
        self.assertFalse(boolean0)

    def test07(self) -> None:

        csv_format0 = CSVFormat.MONGODB_TSV
        lexer0 = Lexer(csv_format0, None)
        boolean0 = lexer0.isQuoteChar(-3398)
        self.assertFalse(boolean0)

    def test06(self) -> None:

        reader0 = ExtendedBufferedReader(io.StringIO(""))
        cSVFormat0 = CSVFormat.POSTGRESQL_TEXT
        lexer0 = Lexer(cSVFormat0, reader0)
        boolean0 = lexer0.isStartOfLine(549)
        self.assertFalse(boolean0)

    def test05(self) -> None:

        cSVFormat0 = CSVFormat.INFORMIX_UNLOAD
        stringReader0 = io.StringIO("")
        extendedBufferedReader0 = ExtendedBufferedReader(stringReader0)
        lexer0 = Lexer(cSVFormat0, extendedBufferedReader0)
        boolean0 = lexer0.readEndOfLine(0)
        self.assertFalse(boolean0)

    def test04(self) -> None:
        reader0 = ExtendedBufferedReader(io.StringIO(""))
        cSVFormat_Builder0 = Builder.create0()
        cSVFormat_Builder0.setDelimiter1("?N0<'")
        cSVFormat0 = cSVFormat_Builder0.build()
        lexer0 = Lexer(cSVFormat0, reader0)

    def test03(self) -> None:
        cSVFormat_Builder0 = Builder.create0()
        cSVFormat_Builder0.setCommentMarker0("s")
        cSVFormat0 = cSVFormat_Builder0.build()
        reader0 = ExtendedBufferedReader(Reader.nullReader())
        lexer0 = Lexer(cSVFormat0, reader0)
        boolean0 = lexer0.isCommentStart(65534)
        self.assertFalse(boolean0)

    def test02(self) -> None:

        cSVFormat0 = CSVFormat.newFormat("\u008A")
        reader0 = Reader.nullReader()
        extendedBufferedReader0 = ExtendedBufferedReader(reader0)
        lexer0 = Lexer(cSVFormat0, extendedBufferedReader0)
        boolean0 = lexer0.isEscapeDelimiter()
        self.assertFalse(boolean0)

    def test01(self) -> None:

        csv_format0 = CSVFormat.MONGODB_TSV
        string_reader0 = io.StringIO("KQ$O+cyb{;")
        extended_buffered_reader0 = ExtendedBufferedReader(string_reader0)
        lexer0 = Lexer(csv_format0, extended_buffered_reader0)
        boolean0 = lexer0.isStartOfLine(-2588)
        self.assertFalse(boolean0)

    def test00(self) -> None:

        cSVFormat0 = CSVFormat.INFORMIX_UNLOAD
        reader0 = ExtendedBufferedReader(io.StringIO(""))
        lexer0 = Lexer(cSVFormat0, reader0)
        boolean0 = lexer0.readEndOfLine(13)
        self.assertTrue(boolean0)
