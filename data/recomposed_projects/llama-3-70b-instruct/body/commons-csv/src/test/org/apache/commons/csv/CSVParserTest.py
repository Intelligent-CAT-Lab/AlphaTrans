from __future__ import annotations
import re
from io import StringIO
import unittest
import pytest
import pathlib
import io
import numbers
import typing
from typing import *
import os
import unittest
from src.main.org.apache.commons.csv.CSVFormat import *
from src.main.org.apache.commons.csv.CSVParser import *
from src.main.org.apache.commons.csv.CSVPrinter import *
from src.main.org.apache.commons.csv.CSVRecord import *
from src.main.org.apache.commons.csv.Constants import *
from src.test.org.apache.commons.csv.Utils import *


class CSVParserTest(unittest.TestCase):

    __CSV_INPUT_MULTILINE_HEADER_TRAILER_COMMENT: str = (
        "# multi-line"
        + CRLF
        + "# header comment"
        + CRLF
        + "A,B"
        + CRLF
        + "1,2"
        + CRLF
        + "# multi-line"
        + CRLF
        + "# comment"
    )
    __CSV_INPUT_HEADER_TRAILER_COMMENT: str = (
        "# header comment" + CRLF + "A,B" + CRLF + "1,2" + CRLF + "# comment"
    )
    __CSV_INPUT_HEADER_COMMENT: str = (
        "# header comment" + CRLF + "A,B" + CRLF + "1,2" + CRLF
    )
    __CSV_INPUT_NO_COMMENT: str = "A,B" + CRLF + "1,2" + CRLF
    __RESULT: typing.List[typing.List[str]] = [
        ["a", "b", "c", "d"],
        ["a", "b", "1 2"],
        ["foo baar", "b", ""],
        ['foo\n,,\n",,\n"', "d", "e"],
    ]
    __CSV_INPUT_2: str = "a,b,1 2"
    __CSV_INPUT_1: str = "a,b,c,d"
    __CSV_INPUT: str = (
        "a,b,c,d\n"
        + " a , b , 1 2 \n"
        + '"foo baar", b,\n'
        + '   "foo\n,,\n"",,\n""",d,e\n'
    )
    __UTF_8: str = "UTF_8"
    __UTF_8_NAME: str = __UTF_8.name()

    def testStream(self) -> None:
        in_ = io.StringIO("a,b,c\n1,2,3\nx,y,z")
        with CSVFormat.DEFAULT.parse(in_) as parser:
            list_ = parser.stream().collect(Collectors.toList())
            assertFalse(list_.isEmpty())
            assertArrayEquals(["a", "b", "c"], list_.get(0).values())
            assertArrayEquals(["1", "2", "3"], list_.get(1).values())
            assertArrayEquals(["x", "y", "z"], list_.get(2).values())

    def testStartWithEmptyLinesThenHeaders(self) -> None:
        codes = [
            "\r\n\r\n\r\nhello,\r\n\r\n\r\n",
            "hello,\n\n\n",
            'hello,""\r\n\r\n\r\n',
            'hello,""\n\n\n',
        ]
        res = [["hello", ""], [""], [""]]  # Excel format does not ignore empty lines
        for code in codes:
            with CSVParser.parse4(code, CSVFormat.EXCEL) as parser:
                records = parser.getRecords()
                self.assertEqual(res.length, records.size())
                self.assertFalse(records.isEmpty())
                for i in range(res.length):
                    self.assertArrayEquals(res[i], records.get(i).values())

    def testRoundtrip(self) -> None:
        out = io.StringIO()
        data = "a,b,c\r\n1,2,3\r\nx,y,z\r\n"
        with CSVPrinter(out, CSVFormat.DEFAULT) as printer, CSVParser.parse4(
            data, CSVFormat.DEFAULT
        ) as parse:
            for record in parse:
                printer.printRecord0(record)
            self.assertEqual(data, out.getvalue())

    def testParseWithQuoteWithEscape(self) -> None:
        source: str = "'a?,b?,c?d',xyz"
        csvFormat: CSVFormat = CSVFormat.DEFAULT.withQuote0("'").withEscape0("?")
        with csvFormat.parse(StringReader(source)) as csvParser:
            csvRecord: CSVRecord = csvParser.nextRecord()
            self.assertEqual("a,b,c?d", csvRecord.get1(0))
            self.assertEqual("xyz", csvRecord.get1(1))

    def testParseWithQuoteThrowsException(self) -> None:
        csvFormat = CSVFormat.DEFAULT.withQuote0("'")
        with self.assertRaises(IOException):
            csvFormat.parse(StringReader("'a,b,c','")).nextRecord()
        with self.assertRaises(IOException):
            csvFormat.parse(StringReader("'a,b,c'abc,xyz")).nextRecord()
        with self.assertRaises(IOException):
            csvFormat.parse(StringReader("'abc'a,b,c',xyz")).nextRecord()

    def testParseWithDelimiterWithQuote(self) -> None:
        source: str = "'a,b,c',xyz"
        csvFormat: CSVFormat = CSVFormat.DEFAULT.withQuote0("'")
        with csvFormat.parse(StringReader(source)) as csvParser:
            csvRecord: CSVRecord = csvParser.nextRecord()
            self.assertEqual("a,b,c", csvRecord.get1(0))
            self.assertEqual("xyz", csvRecord.get1(1))

    def testParseWithDelimiterWithEscape(self) -> None:
        source: str = "a!,b!,c,xyz"
        csvFormat: CSVFormat = CSVFormat.DEFAULT.withEscape0("!")
        with csvFormat.parse(StringReader(source)) as csvParser:
            csvRecord: CSVRecord = csvParser.nextRecord()
            self.assertEqual("a,b,c", csvRecord.get1(0))
            self.assertEqual("xyz", csvRecord.get1(1))

    def testParseWithDelimiterStringWithQuote(self) -> None:
        source: str = "'a[|]b[|]c'[|]xyz\r\nabc[abc][|]xyz"
        csvFormat: CSVFormat = (
            CSVFormat.DEFAULT.builder().setDelimiter1("[|]").setQuote0("'").build()
        )
        with csvFormat.parse(StringReader(source)) as csvParser:
            csvRecord: CSVRecord = csvParser.nextRecord()
            self.assertEqual("a[|]b[|]c", csvRecord.get1(0))
            self.assertEqual("xyz", csvRecord.get1(1))
            csvRecord = csvParser.nextRecord()
            self.assertEqual("abc[abc]", csvRecord.get1(0))
            self.assertEqual("xyz", csvRecord.get1(1))

    def testParseWithDelimiterStringWithEscape(self) -> None:
        source: str = "a![!|!]b![|]c[|]xyz\r\nabc[abc][|]xyz"
        csvFormat: CSVFormat = (
            CSVFormat.DEFAULT.builder().setDelimiter1("[|]").setEscape0("!").build()
        )
        with csvFormat.parse(StringReader(source)) as csvParser:
            csvRecord: CSVRecord = csvParser.nextRecord()
            self.assertEqual("a[|]b![|]c", csvRecord.get1(0))
            self.assertEqual("xyz", csvRecord.get1(1))
            csvRecord = csvParser.nextRecord()
            self.assertEqual("abc[abc]", csvRecord.get1(0))
            self.assertEqual("xyz", csvRecord.get1(1))

    def testParseUrlCharsetNullFormat(self) -> None:
        with self.assertRaises(RuntimeError):
            CSVParser.parse5(
                URL("https://commons.apache.org"), Charset.defaultCharset(), None
            )

    def testParseStringNullFormat(self) -> None:
        with self.assertRaises(RuntimeError):
            CSVParser.parse4("csv data", None)

    def testParserUrlNullCharsetFormat(self) -> None:
        with self.assertRaises(RuntimeError):
            CSVParser.parse5(URL("https://commons.apache.org"), None, CSVFormat.DEFAULT)

    def testParseNullUrlCharsetFormat(self) -> None:
        with self.assertRaises(RuntimeError):
            CSVParser.parse5(None, Charset.defaultCharset(), CSVFormat.DEFAULT)

    def testParseNullStringFormat(self) -> None:
        with self.assertRaises(RuntimeError):
            CSVParser.parse4(None, CSVFormat.DEFAULT)

    def testParseNullPathFormat(self) -> None:
        with self.assertRaises(RuntimeError):
            CSVParser.parse2(None, Charset.defaultCharset(), CSVFormat.DEFAULT)

    def testParseNullFileFormat(self) -> None:
        with self.assertRaises(RuntimeError):
            CSVParser.parse0(None, Charset.defaultCharset(), CSVFormat.DEFAULT)

    def testParseFileNullFormat(self) -> None:
        with self.assertRaises(RuntimeError):
            CSVParser.parse0(
                pathlib.Path("CSVFileParser/test.csv"), Charset.defaultCharset(), None
            )

    def testNotValueCSV(self) -> None:
        source: str = "#"
        csvFormat: CSVFormat = CSVFormat.DEFAULT.withCommentMarker0("#")
        with csvFormat.parse(StringReader(source)) as csvParser:
            csvRecord: CSVRecord = csvParser.nextRecord()
            self.assertIsNone(csvRecord)

    def testNoHeaderMap(self) -> None:
        with CSVParser.parse4("a,b,c\n1,2,3\nx,y,z", CSVFormat.DEFAULT) as parser:
            self.assertIsNone(parser.getHeaderMap())

    def testNewCSVParserReaderNullFormat(self) -> None:
        with self.assertRaises(RuntimeError):
            CSVParser.CSVParser1(StringReader(""), None)

    def testNewCSVParserNullReaderFormat(self) -> None:
        with self.assertRaises(RuntimeError):
            CSVParser.CSVParser1(None, CSVFormat.DEFAULT)

    def testMultipleIterators(self) -> None:
        with CSVParser.parse4("a,b,c" + CRLF + "d,e,f", CSVFormat.DEFAULT) as parser:
            itr1 = parser.iterator()

            first = itr1.next()
            self.assertEqual("a", first.get1(0))
            self.assertEqual("b", first.get1(1))
            self.assertEqual("c", first.get1(2))

            second = itr1.next()
            self.assertEqual("d", second.get1(0))
            self.assertEqual("e", second.get1(1))
            self.assertEqual("f", second.get1(2))

    def testMongoDbCsv(self) -> None:
        with CSVParser.parse4(
            '"a a",b,c' + LF + "d,e,f", CSVFormat.MONGODB_CSV
        ) as parser:
            itr1 = parser.iterator()
            itr2 = parser.iterator()

            first = itr1.next()
            self.assertEqual("a a", first.get1(0))
            self.assertEqual("b", first.get1(1))
            self.assertEqual("c", first.get1(2))

            second = itr2.next()
            self.assertEqual("d", second.get1(0))
            self.assertEqual("e", second.get1(1))
            self.assertEqual("f", second.get1(2))

    def testLineFeedEndings(self) -> None:
        code = "foo\nbaar,\nhello,world\n,kanu"
        with CSVParser.parse4(code, CSVFormat.DEFAULT) as parser:
            records = parser.getRecords()
            self.assertEqual(4, len(records))

    def testIteratorSequenceBreaking(self) -> None:
        fiveRows = "1\n2\n3\n4\n5\n"
        with CSVFormat.DEFAULT.parse(io.StringIO(fiveRows)) as parser:
            iter = parser.iterator()
            recordNumber = 0
            while iter.hasNext():
                record = iter.next()
                recordNumber += 1
                self.assertEqual(str(recordNumber), record.get1(0))
                if recordNumber >= 2:
                    break
            iter.hasNext()
            while iter.hasNext():
                record = iter.next()
                recordNumber += 1
                self.assertEqual(str(recordNumber), record.get1(0))
        with CSVFormat.DEFAULT.parse(io.StringIO(fiveRows)) as parser:
            recordNumber = 0
            for record in parser:
                recordNumber += 1
                self.assertEqual(str(recordNumber), record.get1(0))
                if recordNumber >= 2:
                    break
            for record in parser:
                recordNumber += 1
                self.assertEqual(str(recordNumber), record.get1(0))
        with CSVFormat.DEFAULT.parse(io.StringIO(fiveRows)) as parser:
            recordNumber = 0
            for record in parser:
                recordNumber += 1
                self.assertEqual(str(recordNumber), record.get1(0))
                if recordNumber >= 2:
                    break
            parser.iterator().hasNext()
            for record in parser:
                recordNumber += 1
                self.assertEqual(str(recordNumber), record.get1(0))

    def testIterator(self) -> None:
        in_ = io.StringIO("a,b,c\n1,2,3\nx,y,z")
        with CSVFormat.DEFAULT.parse(in_) as parser:
            iterator = parser.iterator()
            self.assertTrue(iterator.hasNext())
            self.assertRaises(NotImplementedError, iterator.remove)
            self.assertArrayEquals(["a", "b", "c"], iterator.next().values())
            self.assertArrayEquals(["1", "2", "3"], iterator.next().values())
            self.assertTrue(iterator.hasNext())
            self.assertTrue(iterator.hasNext())
            self.assertTrue(iterator.hasNext())
            self.assertArrayEquals(["x", "y", "z"], iterator.next().values())
            self.assertFalse(iterator.hasNext())
            self.assertRaises(RuntimeError, iterator.next)

    def testInvalidFormat(self) -> None:
        with self.assertRaises(ValueError):
            CSVFormat.DEFAULT.withDelimiter(CR)

    def testIgnoreEmptyLines(self) -> None:
        code = "\nfoo,baar\n\r\n,\n\n,world\r\n\n"
        with CSVParser.parse4(code, CSVFormat.DEFAULT) as parser:
            records = parser.getRecords()
            self.assertEqual(3, len(records))

    def testGetRecordWithMultiLineValues(self) -> None:
        with CSVParser.parse4(
            '"a\r\n1","a\r\n2"'
            + CRLF
            + '"b\r\n1","b\r\n2"'
            + CRLF
            + '"c\r\n1","c\r\n2"',
            CSVFormat.DEFAULT.withRecordSeparator1(CRLF),
        ) as parser:
            record: CSVRecord
            self.assertEqual(0, parser.getRecordNumber())
            self.assertEqual(0, parser.getCurrentLineNumber())
            self.assertIsNotNone(record=parser.nextRecord())
            self.assertEqual(3, parser.getCurrentLineNumber())
            self.assertEqual(1, record.getRecordNumber())
            self.assertEqual(1, parser.getRecordNumber())
            self.assertIsNotNone(record=parser.nextRecord())
            self.assertEqual(6, parser.getCurrentLineNumber())
            self.assertEqual(2, record.getRecordNumber())
            self.assertEqual(2, parser.getRecordNumber())
            self.assertIsNotNone(record=parser.nextRecord())
            self.assertEqual(9, parser.getCurrentLineNumber())
            self.assertEqual(3, record.getRecordNumber())
            self.assertEqual(3, parser.getRecordNumber())
            self.assertIsNone(record=parser.nextRecord())
            self.assertEqual(9, parser.getCurrentLineNumber())
            self.assertEqual(3, parser.getRecordNumber())

    def testGetRecords(self) -> None:
        with CSVParser.parse4(
            self.__CSV_INPUT, CSVFormat.DEFAULT.withIgnoreSurroundingSpaces0()
        ) as parser:
            records: typing.List[CSVRecord] = parser.getRecords()
            self.assertEqual(len(self.__RESULT), len(records))
            self.assertFalse(records.isEmpty())
            for i in range(len(self.__RESULT)):
                self.assertArrayEquals(self.__RESULT[i], records.get(i).values())

    def testGetRecordPositionWithLF(self) -> None:
        self.__validateRecordPosition(String.valueOf(LF))

    def testGetRecordPositionWithCRLF(self) -> None:
        self.__validateRecordPosition(CRLF)

    def testGetRecordNumberWithLF(self) -> None:
        self.__validateRecordNumbers(str(LF))

    def testGetRecordNumberWithCRLF(self) -> None:
        self.__validateRecordNumbers(CRLF)

    def testGetRecordNumberWithCR(self) -> None:
        self.__validateRecordNumbers(String.valueOf(CR))

    def testGetOneLineOneParser(self) -> None:
        format: CSVFormat = CSVFormat.DEFAULT
        with PipedWriter() as writer, CSVParser.CSVParser1(
            PipedReader(writer), format
        ) as parser:
            writer.append(self.__CSV_INPUT_1)
            writer.append(format.getRecordSeparator())
            record1: CSVRecord = parser.nextRecord()
            self.assertArrayEquals(self.__RESULT[0], record1.values())
            writer.append(self.__CSV_INPUT_2)
            writer.append(format.getRecordSeparator())
            record2: CSVRecord = parser.nextRecord()
            self.assertArrayEquals(self.__RESULT[1], record2.values())

    def testGetOneLine(self) -> None:
        with CSVParser.parse4(self.__CSV_INPUT_1, CSVFormat.DEFAULT) as parser:
            record: CSVRecord = parser.getRecords()[0]
            assertArrayEquals(self.__RESULT[0], record.values())

    def testGetLineNumberWithLF(self) -> None:
        self.__validateLineNumbers(String.valueOf(LF))

    def testGetLineNumberWithCRLF(self) -> None:
        self.__validateLineNumbers(CRLF)

    def testGetLineNumberWithCR(self) -> None:
        self.__validateLineNumbers(String.valueOf(CR))

    def testGetLine(self) -> None:
        with CSVParser.parse4(
            self.__CSV_INPUT, CSVFormat.DEFAULT.withIgnoreSurroundingSpaces0()
        ) as parser:
            for re in self.__RESULT:
                self.assertArrayEquals(re, parser.nextRecord().values())
            self.assertNull(parser.nextRecord())

    def testForEach(self) -> None:
        with io.StringIO("a,b,c\n1,2,3\nx,y,z") as in_:
            with CSVFormat.DEFAULT.parse(in_) as parser:
                records: typing.List[CSVRecord] = []
                for record in parser:
                    records.append(record)
                self.assertEqual(3, len(records))
                self.assertListEqual(["a", "b", "c"], records[0].values())
                self.assertListEqual(["1", "2", "3"], records[1].values())
                self.assertListEqual(["x", "y", "z"], records[2].values())

    def testFirstEndOfLineLf(self) -> None:
        data = "foo\nbaar,\nhello,world\n,kanu"
        with CSVParser.parse4(data, CSVFormat.DEFAULT) as parser:
            records = parser.getRecords()
            self.assertEqual(4, len(records))
            self.assertEqual("\n", parser.getFirstEndOfLine())

    def testFirstEndOfLineCrLf(self) -> None:
        data = "foo\r\nbaar,\r\nhello,world\r\n,kanu"
        with CSVParser.parse4(data, CSVFormat.DEFAULT) as parser:
            records = parser.getRecords()
            self.assertEqual(4, len(records))
            self.assertEqual("\r\n", parser.getFirstEndOfLine())

    def testFirstEndOfLineCr(self) -> None:
        data = "foo\rbaar,\rhello,world\r,kanu"
        with CSVParser.parse4(data, CSVFormat.DEFAULT) as parser:
            records = parser.getRecords()
            self.assertEqual(4, len(records))
            self.assertEqual("\r", parser.getFirstEndOfLine())

    def testExcelFormat2(self) -> None:
        code = "foo,baar\r\n\r\nhello,\r\n\r\nworld,\r\n"
        res = [["foo", "baar"], [""], ["hello", ""], [""], ["world", ""]]
        with CSVParser.parse4(code, CSVFormat.EXCEL) as parser:
            records = parser.getRecords()
            self.assertEqual(len(res), len(records))
            self.assertFalse(records.isEmpty())
            for i in range(len(res)):
                self.assertArrayEquals(res[i], records.get(i).values())

    def testExcelFormat1(self) -> None:
        code = (
            "value1,value2,value3,value4\r\na,b,c,d\r\n  x,,,"
            + '\r\n\r\n"""hello""","  ""world""","abc\ndef",\r\n'
        )
        res = [
            ["value1", "value2", "value3", "value4"],
            ["a", "b", "c", "d"],
            ["  x", "", "", ""],
            [""],
            ['"hello"', '  "world"', "abc\ndef", ""],
        ]
        with CSVParser.parse4(code, CSVFormat.EXCEL) as parser:
            records = parser.getRecords()
            self.assertEqual(res.length, records.size())
            self.assertFalse(records.isEmpty())
            for i in range(res.length):
                self.assertArrayEquals(res[i], records.get(i).values())

    def testEndOfFileBehaviorExcel(self) -> None:
        codes = [
            "hello,\r\n\r\nworld,\r\n",
            "hello,\r\n\r\nworld,",
            'hello,\r\n\r\nworld,""\r\n',
            'hello,\r\n\r\nworld,""',
            "hello,\r\n\r\nworld,\n",
            "hello,\r\n\r\nworld,",
            'hello,\r\n\r\nworld,""\n',
            'hello,\r\n\r\nworld,""',
        ]
        res = [
            ["hello", ""],
            [""],  # Excel format does not ignore empty lines
            ["world", ""],
        ]

        for code in codes:
            with CSVParser.parse4(code, CSVFormat.EXCEL) as parser:
                records = parser.getRecords()
                self.assertEqual(res.length, records.size())
                self.assertFalse(records.isEmpty())
                for i in range(res.length):
                    self.assertArrayEquals(res[i], records.get(i).values())

    def testEndOfFileBehaviorCSV(self) -> None:
        codes = [
            "hello,\r\n\r\nworld,\r\n",
            "hello,\r\n\r\nworld,",
            'hello,\r\n\r\nworld,""\r\n',
            'hello,\r\n\r\nworld,""',
            "hello,\r\n\r\nworld,\n",
            "hello,\r\n\r\nworld,",
            'hello,\r\n\r\nworld,""\n',
            'hello,\r\n\r\nworld,""',
        ]
        res = [["hello", ""], ["world", ""]]  # CSV format ignores empty lines
        for code in codes:
            with CSVParser.parse4(code, CSVFormat.DEFAULT) as parser:
                records = parser.getRecords()
                self.assertEqual(res.length, records.size())
                self.assertFalse(records.isEmpty())
                for i in range(res.length):
                    self.assertArrayEquals(res[i], records.get(i).values())

    def testEmptyString(self) -> None:
        with CSVParser.parse4("", CSVFormat.DEFAULT) as parser:
            self.assertIsNone(parser.nextRecord())

    def testEmptyLineBehaviorExcel(self) -> None:
        codes = [
            "hello,\r\n\r\n\r\n",
            "hello,\n\n\n",
            'hello,""\r\n\r\n\r\n',
            'hello,""\n\n\n',
        ]
        res = [["hello", ""], [""], [""]]
        for code in codes:
            with CSVParser.parse4(code, CSVFormat.EXCEL) as parser:
                records = parser.getRecords()
                self.assertEqual(len(res), len(records))
                self.assertFalse(records.isEmpty())
                for i in range(len(res)):
                    self.assertArrayEquals(res[i], records.get(i).values())

    def testEmptyLineBehaviorCSV(self) -> None:
        codes = [
            "hello,\r\n\r\n\r\n",
            "hello,\n\n\n",
            'hello,""\r\n\r\n\r\n',
            'hello,""\n\n\n',
        ]
        res = [["hello", ""]]
        for code in codes:
            with CSVParser.parse4(code, CSVFormat.DEFAULT) as parser:
                records = parser.getRecords()
                self.assertEqual(res.length, records.size())
                self.assertFalse(records.isEmpty())
                for i in range(res.length):
                    self.assertArrayEquals(res[i], records.get(i).values())

    def testEmptyFile(self) -> None:
        with CSVParser.parse2(
            pathlib.Path("src/test/resources/org/apache/commons/csv/empty.txt"),
            self.__UTF_8,
            CSVFormat.DEFAULT,
        ) as parser:
            self.assertIsNone(parser.nextRecord())

    def testDefaultFormat(self) -> None:
        code = (
            "a,b#\n"  # 1)
            + '"\n"," ",#\n'  # 2)
            + '#,""\n'  # 3)
            + "# Final comment\n"  # 4)
        )
        res = [["a", "b#"], ["\n", " ", "#"], ["#", ""], ["# Final comment"]]

        format = CSVFormat.DEFAULT
        assert not format.isCommentMarkerSet()
        res_comments = [["a", "b#"], ["\n", " ", "#"]]

        with CSVParser.parse4(code, format) as parser:
            records = parser.getRecords()
            assert records
            Utils.compare("Failed to parse without comments", res, records)

            format = CSVFormat.DEFAULT.withCommentMarker0("#")
        with CSVParser.parse4(code, format) as parser:
            records = parser.getRecords()

            Utils.compare("Failed to parse with comments", res_comments, records)

    def testCSV57(self) -> None:
        with CSVParser.parse4("", CSVFormat.DEFAULT) as parser:
            list = parser.getRecords()
            self.assertIsNotNone(list)
            self.assertEqual(0, len(list))

    def testCSV235(self) -> None:
        dqString = '"aaa","b""bb","ccc"'  # "aaa","b""bb","ccc"
        with CSVFormat.RFC4180.parse(io.StringIO(dqString)) as parser:
            records = parser.iterator()
            record = records.next()
            self.assertFalse(records.hasNext())
            self.assertEqual(3, record.size())
            self.assertEqual("aaa", record.get1(0))
            self.assertEqual('b"bb', record.get1(1))
            self.assertEqual("ccc", record.get1(2))

    def testCSV141RFC4180(self) -> None:
        self.__testCSV141Failure(CSVFormat.RFC4180, 3)

    def testCSV141Excel(self) -> None:
        self.__testCSV141Ok(CSVFormat.EXCEL)

    def testCSV141CSVFormat_POSTGRESQL_CSV(self) -> None:
        self.__testCSV141Failure(CSVFormat.POSTGRESQL_CSV, 3)

    def testCSV141CSVFormat_ORACLE(self) -> None:
        self.__testCSV141Failure(CSVFormat.ORACLE, 2)

    def testCSV141CSVFormat_INFORMIX_UNLOAD_CSV(self) -> None:
        self.__testCSV141Failure(CSVFormat.INFORMIX_UNLOAD_CSV, 3)

    def testCSV141CSVFormat_INFORMIX_UNLOAD(self) -> None:
        self.__testCSV141Failure(CSVFormat.INFORMIX_UNLOAD, 1)

    def testCSV141CSVFormat_DEFAULT(self) -> None:
        self.__testCSV141Failure(CSVFormat.DEFAULT, 3)

    def testCarriageReturnLineFeedEndings(self) -> None:
        code = "foo\r\nbaar,\r\nhello,world\r\n,kanu"
        with CSVParser.parse4(code, CSVFormat.DEFAULT) as parser:
            records = parser.getRecords()
            self.assertEqual(4, len(records))

    def testCarriageReturnEndings(self) -> None:
        code = "foo\rbaar,\rhello,world\r,kanu"
        with CSVParser.parse4(code, CSVFormat.DEFAULT) as parser:
            records = parser.getRecords()
            self.assertEqual(4, len(records))

    def testBackslashEscapingOld(self) -> None:
        code = (
            "one,two,three\n"
            + 'on\\"e,two\n'
            + 'on"e,two\n'
            + 'one,"tw\\"o"\n'
            + 'one,"t\\,wo"\n'
            + 'one,two,"th,ree"\n'
            + '"a\\\\"\n'
            + "a\\,b\n"
            + '"a\\\\,b"'
        )
        res = [
            ["one", "two", "three"],
            ['on\\"e', "two"],
            ['on"e', "two"],
            ["one", 'tw"o'],
            ["one", "t\\,wo"],  # backslash in quotes only
            ["one", "two", "th,ree"],
            ["a\\\\"],  # backslash in quotes only escapes a delimiter (",")
            ["a\\", "b"],  # a backslash must be returned
            ["a\\\\,b"],  # backslash in quotes only escapes a delimiter (",")
        ]
        with CSVParser.parse4(code, CSVFormat.DEFAULT) as parser:
            records = parser.getRecords()
            self.assertEqual(len(res), len(records))
            self.assertFalse(records)
            for i in range(len(res)):
                self.assertArrayEquals(res[i], records[i].values())

    def testBackslashEscaping2(self) -> None:
        code = (
            " , , \n"  # 1)
            " \t ,  , \n"  # 2)
            " // , /, , /,\n"  # 3)
        )
        res = [
            [" ", " ", " "],  # 1
            [" \t ", "  ", " "],  # 2
            [" / ", " , ", " ,"],  # 3
        ]

        format = (
            CSVFormat.newFormat(",")
            .withRecordSeparator1(CRLF)
            .withEscape0("/")
            .withIgnoreEmptyLines0()
        )

        with CSVParser.parse4(code, format) as parser:
            records = parser.getRecords()
            self.assertFalse(records)

            Utils.compare("", res, records)

    def testBackslashEscaping(self) -> None:

        pass  # LLM could not translate this method

    def __validateRecordPosition(self, lineSeparator: str) -> None:
        code = (
            "a,b,c"
            + lineSeparator
            + "1,2,3"
            + lineSeparator
            + "'A"
            + lineSeparator
            + "A','B"
            + lineSeparator
            + "B',CC"
            + lineSeparator
            + "\u00c4,\u00d6,\u00dc"
            + lineSeparator
            + "EOF,EOF,EOF"
        )

        format = (
            CSVFormat.newFormat(",").withQuote0("'").withRecordSeparator1(lineSeparator)
        )
        parser = CSVParser.parse4(code, format)

        record = None
        self.assertEqual(0, parser.getRecordNumber())

        record = parser.nextRecord()
        self.assertIsNotNone(record)
        self.assertEqual(1, record.getRecordNumber())
        self.assertEqual(code.index("a"), record.getCharacterPosition())

        record = parser.nextRecord()
        self.assertIsNotNone(record)
        self.assertEqual(2, record.getRecordNumber())
        self.assertEqual(code.index("1"), record.getCharacterPosition())

        record = parser.nextRecord()
        positionRecord3 = record.getCharacterPosition()
        self.assertEqual(3, record.getRecordNumber())
        self.assertEqual(code.index("'A"), record.getCharacterPosition())
        self.assertEqual("A" + lineSeparator + "A", record.get1(0))
        self.assertEqual("B" + lineSeparator + "B", record.get1(1))
        self.assertEqual("CC", record.get1(2))

        record = parser.nextRecord()
        self.assertIsNotNone(record)
        self.assertEqual(4, record.getRecordNumber())
        self.assertEqual(code.index("\u00c4"), record.getCharacterPosition())

        record = parser.nextRecord()
        self.assertIsNotNone(record)
        self.assertEqual(5, record.getRecordNumber())
        self.assertEqual(code.index("EOF"), record.getCharacterPosition())

        parser.close()

        parser = CSVParser(
            StringIO(code[positionRecord3:]),
            format,
            positionRecord3,
            3,
        )

        record = parser.nextRecord()
        self.assertIsNotNone(record)
        self.assertEqual(3, record.getRecordNumber())
        self.assertEqual(code.index("'A"), record.getCharacterPosition())
        self.assertEqual("A" + lineSeparator + "A", record.get1(0))
        self.assertEqual("B" + lineSeparator + "B", record.get1(1))
        self.assertEqual("CC", record.get1(2))

        record = parser.nextRecord()
        self.assertIsNotNone(record)
        self.assertEqual(4, record.getRecordNumber())
        self.assertEqual(code.index("\u00c4"), record.getCharacterPosition())
        self.assertEqual("\u00c4", record.get1(0))

        parser.close()

    def __validateRecordNumbers(self, lineSeparator: str) -> None:
        with CSVParser.parse4(
            "a" + lineSeparator + "b" + lineSeparator + "c",
            CSVFormat.DEFAULT.withRecordSeparator1(lineSeparator),
        ) as parser:
            record: CSVRecord = None
            self.assertEqual(0, parser.getRecordNumber())
            self.assertIsNotNone(record=parser.nextRecord())
            self.assertEqual(1, record.getRecordNumber())
            self.assertEqual(1, parser.getRecordNumber())
            self.assertIsNotNone(record=parser.nextRecord())
            self.assertEqual(2, record.getRecordNumber())
            self.assertEqual(2, parser.getRecordNumber())
            self.assertIsNotNone(record=parser.nextRecord())
            self.assertEqual(3, record.getRecordNumber())
            self.assertEqual(3, parser.getRecordNumber())
            self.assertIsNone(record=parser.nextRecord())
            self.assertEqual(3, parser.getRecordNumber())

    def __validateLineNumbers(self, lineSeparator: str) -> None:
        with CSVParser.parse4(
            "a" + lineSeparator + "b" + lineSeparator + "c",
            CSVFormat.DEFAULT.withRecordSeparator1(lineSeparator),
        ) as parser:
            self.assertEqual(0, parser.getCurrentLineNumber())
            self.assertIsNotNone(parser.nextRecord())
            self.assertEqual(1, parser.getCurrentLineNumber())
            self.assertIsNotNone(parser.nextRecord())
            self.assertEqual(2, parser.getCurrentLineNumber())
            self.assertIsNotNone(parser.nextRecord())
            self.assertEqual(3, parser.getCurrentLineNumber())
            self.assertIsNone(parser.nextRecord())
            self.assertEqual(3, parser.getCurrentLineNumber())

    def __testCSV141Ok(self, format: CSVFormat) -> None:
        path: Path = Paths.get(
            "src/test/resources/org/apache/commons/csv/CSV-141/csv-141.csv"
        )
        with CSVParser.parse2(path, self.__UTF_8, format) as parser:
            record: CSVRecord = parser.nextRecord()
            self.assertEqual("1414770317901", record.get1(0))
            self.assertEqual("android.widget.EditText", record.get1(1))
            self.assertEqual("pass sem1 _84*|*", record.get1(2))
            self.assertEqual("0", record.get1(3))
            self.assertEqual("pass sem1 _8", record.get1(4))
            self.assertEqual(5, record.size())
            record = parser.nextRecord()
            self.assertEqual("1414770318470", record.get1(0))
            self.assertEqual("android.widget.EditText", record.get1(1))
            self.assertEqual("pass sem1 _84:|", record.get1(2))
            self.assertEqual("0", record.get1(3))
            self.assertEqual("pass sem1 _84:\\", record.get1(4))
            self.assertEqual(5, record.size())
            record = parser.nextRecord()
            self.assertEqual("1414770318327", record.get1(0))
            self.assertEqual("android.widget.EditText", record.get1(1))
            self.assertEqual("pass sem1", record.get1(2))
            self.assertEqual(3, record.size())
            record = parser.nextRecord()
            self.assertEqual("1414770318628", record.get1(0))
            self.assertEqual("android.widget.EditText", record.get1(1))
            self.assertEqual("pass sem1 _84*|*", record.get1(2))
            self.assertEqual("0", record.get1(3))
            self.assertEqual("pass sem1", record.get1(4))
            self.assertEqual(5, record.size())

    def __testCSV141Failure(self, format: CSVFormat, failParseRecordNo: int) -> None:
        path = pathlib.Path(
            "src/test/resources/org/apache/commons/csv/CSV-141/csv-141.csv"
        )
        with CSVParser.parse2(path, self.__UTF_8, format) as parser:
            record = self.parse(parser, failParseRecordNo)
            if record is None:
                return  # expected failure
            self.assertEqual("1414770317901", record.get1(0))
            self.assertEqual("android.widget.EditText", record.get1(1))
            self.assertEqual("pass sem1 _84*|*", record.get1(2))
            self.assertEqual("0", record.get1(3))
            self.assertEqual("pass sem1 _8", record.get1(4))
            self.assertEqual(5, record.size())
            record = self.parse(parser, failParseRecordNo)
            if record is None:
                return  # expected failure
            self.assertEqual("1414770318470", record.get1(0))
            self.assertEqual("android.widget.EditText", record.get1(1))
            self.assertEqual("pass sem1 _84:|", record.get1(2))
            self.assertEqual("0", record.get1(3))
            self.assertEqual("pass sem1 _84:\\", record.get1(4))
            self.assertEqual(5, record.size())
            with self.assertRaises(IOException):
                parser.nextRecord()

    def __parseFully(self, parser: CSVParser) -> None:

        pass  # LLM could not translate this method

    def parse(self, parser: CSVParser, failParseRecordNo: int) -> CSVRecord:
        if parser.getRecordNumber() + 1 == failParseRecordNo:
            with self.assertRaises(IOException):
                parser.nextRecord()
            return None
        return parser.nextRecord()
