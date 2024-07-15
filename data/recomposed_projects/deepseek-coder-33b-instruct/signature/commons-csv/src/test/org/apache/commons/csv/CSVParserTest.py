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

    __CSV_INPUT_MULTILINE_HEADER_TRAILER_COMMENT: str = """# multi-line
CRLF
# header comment
CRLF
A,B
CRLF
1,2
CRLF
# multi-line
CRLF
# comment"""
    __CSV_INPUT_HEADER_TRAILER_COMMENT: str = "# header comment\nA,B\n1,2\n# comment"
    __CSV_INPUT_HEADER_COMMENT: str = "# header comment\nA,B\n1,2\n"
    __CSV_INPUT_NO_COMMENT: str = "A,B\n1,2\n"
    __RESULT: typing.List[typing.List[str]] = [
        ["a", "b", "c", "d"],
        ["a", "b", "1 2"],
        ["foo baar", "b", ""],
        ['foo\n,,\n",,\n"', "d", "e"],
    ]
    __CSV_INPUT_2: str = "a,b,1 2"
    __CSV_INPUT_1: str = "a,b,c,d"
    __CSV_INPUT: str = None  # LLM could not translate this field

    __UTF_8_NAME: str = "UTF-8"
    __UTF_8: str = "UTF-8"

    def testStream(self) -> None:

        in_ = io.StringIO("a,b,c\n1,2,3\nx,y,z")
        try:
            parser = CSVFormat.DEFAULT.parse(in_)
            list_ = list(parser.stream())
            assert not list_
            assert list_[0].values() == ["a", "b", "c"]
            assert list_[1].values() == ["1", "2", "3"]
            assert list_[2].values() == ["x", "y", "z"]
        finally:
            in_.close()

    def testStartWithEmptyLinesThenHeaders(self) -> None:

        codes = [
            "\r\n\r\n\r\nhello,\r\n\r\n\r\n",
            "hello,\n\n\n",
            'hello,""\r\n\r\n\r\n',
            'hello,""\n\n\n',
        ]
        res = [["hello", ""], [""], [""]]  # Excel format does not ignore empty lines
        for code in codes:
            parser = CSVParser.parse4(code, CSVFormat.EXCEL)
            records = parser.getRecords()
            self.assertEqual(len(res), len(records))
            self.assertFalse(not records)
            for i in range(len(res)):
                self.assertEqual(res[i], records[i].values())

    def testRoundtrip(self) -> None:

        out = io.StringIO()
        data = "a,b,c\r\n1,2,3\r\nx,y,z\r\n"
        try:
            printer = CSVPrinter(out, CSVFormat.DEFAULT)
            parse = CSVParser.parse4(data, CSVFormat.DEFAULT)
            for record in parse:
                printer.printRecord0(record)
            self.assertEqual(data, out.getvalue())
        finally:
            out.close()

    def testParseWithQuoteWithEscape(self) -> None:

        source = "'a?,b?,c?d',xyz"
        csvFormat = CSVFormat.DEFAULT.withQuote0("'").withEscape0("?")
        csvParser = csvFormat.parse(io.StringIO(source))
        csvRecord = csvParser.nextRecord()
        self.assertEqual("a,b,c?d", csvRecord.get1(0))
        self.assertEqual("xyz", csvRecord.get1(1))

    def testParseWithQuoteThrowsException(self) -> None:

        csv_format = CSVFormat.DEFAULT.withQuote0("'")

        with pytest.raises(IOError):
            csv_format.parse(io.StringIO("'a,b,c','")).nextRecord()

        with pytest.raises(IOError):
            csv_format.parse(io.StringIO("'a,b,c'abc,xyz")).nextRecord()

        with pytest.raises(IOError):
            csv_format.parse(io.StringIO("'abc'a,b,c',xyz")).nextRecord()

    def testParseWithDelimiterWithQuote(self) -> None:

        source = "'a,b,c',xyz"
        csvFormat = CSVFormat.DEFAULT.withQuote0("'")
        csvParser = csvFormat.parse(io.StringIO(source))
        csvRecord = csvParser.nextRecord()
        self.assertEqual("a,b,c", csvRecord.get1(0))
        self.assertEqual("xyz", csvRecord.get1(1))

    def testParseWithDelimiterWithEscape(self) -> None:

        source = "a!!,b!!,c,xyz"
        csv_format = CSVFormat.DEFAULT.withEscape0("!!")
        csv_parser = csv_format.parse(io.StringIO(source))
        csv_record = csv_parser.nextRecord()
        self.assertEqual("a,b,c", csv_record.get1(0))
        self.assertEqual("xyz", csv_record.get1(1))

    def testParseWithDelimiterStringWithQuote(self) -> None:

        source = "'a[|]b[|]c'[|]xyz\r\nabc[abc][|]xyz"
        csvFormat = (
            CSVFormat.DEFAULT.builder().setDelimiter1("[|]").setQuote0("'").build()
        )

        with csvFormat.parse(io.StringIO(source)) as csvParser:
            csvRecord = csvParser.nextRecord()
            self.assertEqual("a[|]b[|]c", csvRecord.get1(0))
            self.assertEqual("xyz", csvRecord.get1(1))
            csvRecord = csvParser.nextRecord()
            self.assertEqual("abc[abc]", csvRecord.get1(0))
            self.assertEqual("xyz", csvRecord.get1(1))

    def testParseWithDelimiterStringWithEscape(self) -> None:

        source = "a![!]b![|]c[|]xyz\r\nabc[abc][|]xyz"
        csvFormat = (
            CSVFormat.DEFAULT.builder().setDelimiter1("[|]").setEscape0("[!]").build()
        )
        csvParser = csvFormat.parse(io.StringIO(source))
        csvRecord = csvParser.nextRecord()
        self.assertEqual("a[|]b![|]c", csvRecord.get1(0))
        self.assertEqual("xyz", csvRecord.get1(1))
        csvRecord = csvParser.nextRecord()
        self.assertEqual("abc[abc]", csvRecord.get1(0))
        self.assertEqual("xyz", csvRecord.get1(1))

    def testParseUrlCharsetNullFormat(self) -> None:

        with pytest.raises(RuntimeError):
            CSVParser.parse5(
                URL("https://commons.apache.org"), Charset.defaultCharset(), None
            )

    def testParseStringNullFormat(self) -> None:

        with pytest.raises(RuntimeError):
            CSVParser.parse4("csv data", None)

    def testParserUrlNullCharsetFormat(self) -> None:

        with pytest.raises(RuntimeError):
            CSVParser.parse5(URL("https://commons.apache.org"), None, CSVFormat.DEFAULT)

    def testParseNullUrlCharsetFormat(self) -> None:

        with pytest.raises(RuntimeError):
            CSVParser.parse5(None, Charset.defaultCharset(), CSVFormat.DEFAULT)

    def testParseNullStringFormat(self) -> None:

        with pytest.raises(TypeError):
            CSVParser.parse(None, CSVFormat.DEFAULT)

    def testParseNullPathFormat(self) -> None:

        with pytest.raises(TypeError):
            CSVParser.parse2(None, Charset.defaultCharset(), CSVFormat.DEFAULT)

    def testParseNullFileFormat(self) -> None:
        with pytest.raises(TypeError):
            CSVParser.parse0(None, Charset.defaultCharset(), CSVFormat.DEFAULT)

    def testParseFileNullFormat(self) -> None:

        with pytest.raises(RuntimeError):
            CSVParser.parse0(pathlib.Path("CSVFileParser/test.csv"), None)

    def testNotValueCSV(self) -> None:

        source = "#"
        csvFormat = CSVFormat.DEFAULT.withCommentMarker0("#")
        csvParser = csvFormat.parse(io.StringIO(source))
        csvRecord = csvParser.nextRecord()
        self.assertIsNone(csvRecord)

    def testNoHeaderMap(self) -> None:

        with CSVParser.parse4("a,b,c\n1,2,3\nx,y,z", CSVFormat.DEFAULT) as parser:
            self.assertIsNone(parser.getHeaderMap())

    def testNewCSVParserReaderNullFormat(self) -> None:

        with pytest.raises(TypeError):
            CSVParser.CSVParser1(io.StringIO(""), None)

    def testNewCSVParserNullReaderFormat(self) -> None:

        with pytest.raises(TypeError):
            CSVParser.CSVParser1(None, CSVFormat.DEFAULT)

    def testMultipleIterators(self) -> None:

        with CSVParser.parse4("a,b,c" + "\r\n" + "d,e,f", CSVFormat.DEFAULT) as parser:
            itr1 = parser.iterator()

            first = next(itr1)
            self.assertEqual("a", first.get1(0))
            self.assertEqual("b", first.get1(1))
            self.assertEqual("c", first.get1(2))

            second = next(itr1)
            self.assertEqual("d", second.get1(0))
            self.assertEqual("e", second.get1(1))
            self.assertEqual("f", second.get1(2))

    def testMongoDbCsv(self) -> None:

        try:
            parser = CSVParser.parse4('"a a",b,c\nd,e,f', CSVFormat.MONGODB_CSV)
            itr1 = parser.iterator()
            itr2 = parser.iterator()

            first = next(itr1)
            self.assertEqual("a a", first.get1(0))
            self.assertEqual("b", first.get1(1))
            self.assertEqual("c", first.get1(2))

            second = next(itr2)
            self.assertEqual("d", second.get1(0))
            self.assertEqual("e", second.get1(1))
            self.assertEqual("f", second.get1(2))
        finally:
            parser.close()

    def testLineFeedEndings(self) -> None:

        code = "foo\nbaar,\nhello,world\n,kanu"
        try:
            parser = CSVParser.parse4(code, CSVFormat.DEFAULT)
            records = parser.getRecords()
            self.assertEqual(len(records), 4)
        finally:
            parser.close()

    def testIteratorSequenceBreaking(self) -> None:

        five_rows = "1\n2\n3\n4\n5\n"

        parser = CSVFormat.DEFAULT.parse(io.StringIO(five_rows))

        iter = parser.iterator()
        record_number = 0
        while iter.hasNext():
            record = iter.next()
            record_number += 1
            self.assertEqual(str(record_number), record.get1(0))
            if record_number >= 2:
                break

        while iter.hasNext():
            record = iter.next()
            record_number += 1
            self.assertEqual(str(record_number), record.get1(0))

        parser = CSVFormat.DEFAULT.parse(io.StringIO(five_rows))
        record_number = 0
        for record in parser:
            record_number += 1
            self.assertEqual(str(record_number), record.get1(0))
            if record_number >= 2:
                break

        for record in parser:
            record_number += 1
            self.assertEqual(str(record_number), record.get1(0))

        parser = CSVFormat.DEFAULT.parse(io.StringIO(five_rows))
        record_number = 0
        for record in parser:
            record_number += 1
            self.assertEqual(str(record_number), record.get1(0))
            if record_number >= 2:
                break

        parser.iterator().hasNext()
        for record in parser:
            record_number += 1
            self.assertEqual(str(record_number), record.get1(0))

    def testIterator(self) -> None:

        in_ = io.StringIO("a,b,c\n1,2,3\nx,y,z")

        try:
            parser = CSVFormat.DEFAULT.parse(in_)
            iterator = parser.iterator()

            assert iterator.hasNext()
            with pytest.raises(NotImplementedError):
                iterator.remove()
            assert iterator.next().values() == ["a", "b", "c"]
            assert iterator.next().values() == ["1", "2", "3"]
            assert iterator.hasNext()
            assert iterator.hasNext()
            assert iterator.hasNext()
            assert iterator.next().values() == ["x", "y", "z"]
            assert not iterator.hasNext()

            with pytest.raises(RuntimeError):
                iterator.next()
        finally:
            in_.close()

    def testInvalidFormat(self) -> None:
        with pytest.raises(ValueError):
            CSVFormat.DEFAULT.withDelimiter(CR)

    def testIgnoreEmptyLines(self) -> None:

        code = "\nfoo,baar\n\r\n,\n\n,world\r\n\n"
        try:
            parser = CSVParser.parse4(code, CSVFormat.DEFAULT)
            records = parser.getRecords()
            self.assertEqual(len(records), 3)
        finally:
            parser.close()

    def testGetRecordWithMultiLineValues(self) -> None:

        try:
            parser = CSVParser.parse4(
                '"a\r\n1","a\r\n2"'
                + CRLF
                + '"b\r\n1","b\r\n2"'
                + CRLF
                + '"c\r\n1","c\r\n2"',
                CSVFormat.DEFAULT.withRecordSeparator1(CRLF),
            )

            record = None
            self.assertEqual(0, parser.getRecordNumber())
            self.assertEqual(0, parser.getCurrentLineNumber())
            self.assertIsNotNone(record := parser.nextRecord())
            self.assertEqual(3, parser.getCurrentLineNumber())
            self.assertEqual(1, record.getRecordNumber())
            self.assertEqual(1, parser.getRecordNumber())
            self.assertIsNotNone(record := parser.nextRecord())
            self.assertEqual(6, parser.getCurrentLineNumber())
            self.assertEqual(2, record.getRecordNumber())
            self.assertEqual(2, parser.getRecordNumber())
            self.assertIsNotNone(record := parser.nextRecord())
            self.assertEqual(9, parser.getCurrentLineNumber())
            self.assertEqual(3, record.getRecordNumber())
            self.assertEqual(3, parser.getRecordNumber())
            self.assertIsNone(record := parser.nextRecord())
            self.assertEqual(9, parser.getCurrentLineNumber())
            self.assertEqual(3, parser.getRecordNumber())
        finally:
            parser.close()

    def testGetRecords(self) -> None:

        CSV_INPUT = (
            "a,b,c,d\n"
            + " a , b , 1 2 \n"
            + '"foo baar", b,\n'
            + '   "foo\n,,\n"",,\n""",d,e\n'
        )

        RESULT = [
            ["a", "b", "c", "d"],
            ["a", "b", "1 2"],
            ["foo baar", "b", ""],
            ['foo\n,,\n",,\n"', "d", "e"],
        ]

        with CSVParser.parse4(
            CSV_INPUT, CSVFormat.DEFAULT.withIgnoreSurroundingSpaces0()
        ) as parser:
            records = parser.getRecords()
            self.assertEqual(len(RESULT), len(records))
            self.assertFalse(not records)
            for i in range(len(RESULT)):
                self.assertListEqual(RESULT[i], records[i].values())

    def testGetRecordPositionWithLF(self) -> None:

        # Call the validateRecordPosition method with LF as line separator
        self.__validateRecordPosition(String.valueOf(LF))

    def testGetRecordPositionWithCRLF(self) -> None:
        self.__validateRecordPosition(CRLF)

    def testGetRecordNumberWithLF(self) -> None:

        # Call the validateRecordNumbers method with LF as the line separator
        self.__validateRecordNumbers(String.valueOf(LF))

    def testGetRecordNumberWithCRLF(self) -> None:
        self.__validateRecordNumbers(CRLF)

    def testGetRecordNumberWithCR(self) -> None:
        self.__validateRecordNumbers(String.valueOf(CR))

    def testGetOneLineOneParser(self) -> None:

        format = CSVFormat.DEFAULT
        with io.PipeWriter() as writer, CSVParser.CSVParser1(
            io.PipedReader(writer), format
        ) as parser:
            writer.write(self.__CSV_INPUT_1)
            writer.write(format.getRecordSeparator())
            record1 = parser.nextRecord()
            self.assertListEqual(self.__RESULT[0], record1.values())
            writer.write(self.__CSV_INPUT_2)
            writer.write(format.getRecordSeparator())
            record2 = parser.nextRecord()
            self.assertListEqual(self.__RESULT[1], record2.values())

    def testGetOneLine(self) -> None:

        # CSV_INPUT_1 is a string, so we can use it directly
        parser = CSVParser.parse4(self.__CSV_INPUT_1, CSVFormat.DEFAULT)

        # getRecords() returns a list of CSVRecord objects, so we need to get the first one
        record = parser.getRecords()[0]

        # values() returns a list of strings, so we can compare it directly with the expected result
        assert self.__RESULT[0] == record.values()

    def testGetLineNumberWithLF(self) -> None:

        # Call the validateLineNumbers method with LF as the line separator
        self.__validateLineNumbers(String.valueOf(LF))

    def testGetLineNumberWithCRLF(self) -> None:
        self.__validateLineNumbers(CRLF)

    def testGetLineNumberWithCR(self) -> None:

        # Call the validateLineNumbers method with the Carriage Return character
        self.__validateLineNumbers("\r")

    def testGetLine(self) -> None:

        with CSVParser.parse4(
            self.__CSV_INPUT, CSVFormat.DEFAULT.withIgnoreSurroundingSpaces0()
        ) as parser:
            for re in self.__RESULT:
                self.assertListEqual(re, parser.nextRecord().values())

            self.assertIsNone(parser.nextRecord())

    def testForEach(self) -> None:

        # Create a StringIO object to simulate a file-like object
        in_ = io.StringIO("a,b,c\n1,2,3\nx,y,z")

        # Create a CSVParser object
        parser = CSVFormat.DEFAULT.parse(in_)

        # Initialize an empty list to store CSVRecords
        records = []

        # Iterate over the CSVParser object
        for record in parser:
            records.append(record)

        # Assert that the number of records is 3
        self.assertEqual(3, len(records))

        # Assert that the values of the first record are ["a", "b", "c"]
        self.assertListEqual(["a", "b", "c"], records[0].values())

        # Assert that the values of the second record are ["1", "2", "3"]
        self.assertListEqual(["1", "2", "3"], records[1].values())

        # Assert that the values of the third record are ["x", "y", "z"]
        self.assertListEqual(["x", "y", "z"], records[2].values())

    def testFirstEndOfLineLf(self) -> None:

        data = "foo\nbaar,\nhello,world\n,kanu"
        try:
            parser = CSVParser.parse4(data, CSVFormat.DEFAULT)
            records = parser.getRecords()
            self.assertEqual(4, len(records))
            self.assertEqual("\n", parser.getFirstEndOfLine())
        finally:
            parser.close()

    def testFirstEndOfLineCrLf(self) -> None:

        data = "foo\r\nbaar,\r\nhello,world\r\n,kanu"
        try:
            parser = CSVParser.parse4(data, CSVFormat.DEFAULT)
            records = parser.getRecords()
            self.assertEqual(4, len(records))
            self.assertEqual("\r\n", parser.getFirstEndOfLine())
        finally:
            parser.close()

    def testFirstEndOfLineCr(self) -> None:

        data = "foo\rbaar,\rhello,world\r,kanu"
        try:
            parser = CSVParser.parse4(data, CSVFormat.DEFAULT)
            records = parser.getRecords()
            self.assertEqual(4, len(records))
            self.assertEqual("\r", parser.getFirstEndOfLine())
        finally:
            parser.close()

    def testExcelFormat2(self) -> None:

        code = "foo,baar\r\n\r\nhello,\r\n\r\nworld,\r\n"
        res = [["foo", "baar"], [""], ["hello", ""], [""], ["world", ""]]

        try:
            parser = CSVParser.parse4(code, CSVFormat.EXCEL)
            records = parser.getRecords()

            self.assertEqual(len(res), len(records))
            self.assertFalse(not records)

            for i in range(len(res)):
                self.assertListEqual(res[i], records[i].values())
        finally:
            parser.close()

    def testExcelFormat1(self) -> None:

        code = 'value1,value2,value3,value4\r\na,b,c,d\r\n  x,,,\r\n\r\n"""hello""","  ""world""","abc\ndef",\r\n'
        res = [
            ["value1", "value2", "value3", "value4"],
            ["a", "b", "c", "d"],
            ["  x", "", "", ""],
            [""],
            ['"hello"', '  "world"', "abc\ndef", ""],
        ]

        with CSVParser.parse4(code, CSVFormat.EXCEL) as parser:
            records = parser.getRecords()
            self.assertEqual(len(res), len(records))
            self.assertFalse(not records)
            for i in range(len(res)):
                self.assertEqual(res[i], records[i].values())

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
        res = [["hello", ""], [""], ["world", ""]]

        for code in codes:
            parser = CSVParser.parse4(code, CSVFormat.EXCEL)
            records = parser.getRecords()
            self.assertEqual(len(res), len(records))
            self.assertFalse(not records)
            for i in range(len(res)):
                self.assertListEqual(res[i], records[i].values())

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
        res = [["hello", ""], ["world", ""]]
        for code in codes:
            parser = CSVParser.parse4(code, CSVFormat.DEFAULT)
            records = parser.getRecords()
            self.assertEqual(len(res), len(records))
            self.assertFalse(not records)
            for i in range(len(res)):
                self.assertEqual(res[i], records[i].values())

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
            parser = CSVParser.parse4(code, CSVFormat.EXCEL)
            records = parser.getRecords()
            self.assertEqual(len(res), len(records))
            self.assertFalse(not records)
            for i in range(len(res)):
                self.assertEqual(res[i], records[i].values())

    def testEmptyLineBehaviorCSV(self) -> None:

        codes = [
            "hello,\r\n\r\n\r\n",
            "hello,\n\n\n",
            'hello,""\r\n\r\n\r\n',
            'hello,""\n\n\n',
        ]
        res = [["hello", ""]]  # CSV format ignores empty lines
        for code in codes:
            parser = CSVParser.parse4(code, CSVFormat.DEFAULT)
            records = parser.getRecords()
            self.assertEqual(len(res), len(records))
            self.assertFalse(not records)
            for i in range(len(res)):
                self.assertEqual(res[i], records[i].values())

    def testEmptyFile(self) -> None:

        try:
            parser = CSVParser.parse2(
                pathlib.Path("src/test/resources/org/apache/commons/csv/empty.txt"),
                "UTF-8",
                CSVFormat.DEFAULT,
            )
            self.assertIsNone(parser.nextRecord())
        finally:
            parser.close()

    def testDefaultFormat(self) -> None:

        code = (
            ""
            + "a,b#\n"  # 1)
            + '"\n"," ",#\n'  # 2)
            + '#,""\n'  # 3)
            + "# Final comment\n"  # 4)
        )
        res = [["a", "b#"], ["\n", " ", "#"], ["#", ""], ["# Final comment"]]

        format = CSVFormat.DEFAULT
        assert not format.isCommentMarkerSet()
        res_comments = [
            ["a", "b#"],
            ["\n", " ", "#"],
        ]

        with CSVParser.parse4(code, format) as parser:
            records = parser.getRecords()
            assert records

            Utils.compare("Failed to parse without comments", res, records)

            format = format.withCommentMarker0("#")

        with CSVParser.parse4(code, format) as parser:
            records = parser.getRecords()

            Utils.compare("Failed to parse with comments", res_comments, records)

    def testCSV57(self) -> None:

        with CSVParser.parse4("", CSVFormat.DEFAULT) as parser:
            list = parser.getRecords()
            assert list is not None
            assert len(list) == 0

    def testCSV235(self) -> None:

        dqString = '"aaa","b""bb","ccc"'  # "aaa","b""bb","ccc"
        parser = CSVFormat.RFC4180.parse(io.StringIO(dqString))
        records = parser.iterator()
        record = next(records)
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
        try:
            parser = CSVParser.parse4(code, CSVFormat.DEFAULT)
            records = parser.getRecords()
            self.assertEqual(len(records), 4)
        except Exception as e:
            self.fail(
                "testCarriageReturnLineFeedEndings failed with exception: " + str(e)
            )

    def testCarriageReturnEndings(self) -> None:

        code = "foo\rbaar,\rhello,world\r,kanu"
        try:
            parser = CSVParser.parse4(code, CSVFormat.DEFAULT)
            records = parser.getRecords()
            self.assertEqual(4, len(records))
        finally:
            parser.close()

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
            ["one", "t\\,wo"],
            ["one", "two", "th,ree"],
            ["a\\\\"],
            ["a\\", "b"],
            ["a\\\\,b"],
        ]
        try:
            parser = CSVParser.parse4(code, CSVFormat.DEFAULT)
            records = parser.getRecords()
            self.assertEqual(len(res), len(records))
            self.assertFalse(not records)
            for i in range(len(res)):
                self.assertListEqual(res[i], records[i].values())
        finally:
            parser.close()

    def testBackslashEscaping2(self) -> None:

        code = "" + " , , \n" + " \t ,  , \n" + " // , /, , /,\n"  # 1)  # 2)  # 3)
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

        parser = CSVParser.parse4(code, format)
        records = parser.getRecords()
        assert not records == []

        Utils.compare("", res, records)

    def testBackslashEscaping(self) -> None:

        code = (
            "one,two,three\n"
            + "''\n"
            + "'/'\n"
            + "'/''\n"
            + "''''\n"
            + "/,,/\n"
            + "//,//\n"
            + "'//','//'\n"
            + '   8   ,   "quoted "" /" // string"   \n'
            + "9,   /\n   \n"
        )

        res = [
            ["one", "two", "three"],
            ["", ""],
            ["'", "'"],
            ["'", "'"],
            ["'", "'"],
            [",", ","],
            ["/", "/"],
            ["/", "/"],
            ["   8   ", '   "quoted "" /" // string"   '],
            ["9", "   \n   "],
        ]

        format = (
            CSVFormat.newFormat(",")
            .withQuote0("'")
            .withRecordSeparator1(CRLF)
            .withEscape0("/")
            .withIgnoreEmptyLines0()
        )

        with CSVParser.parse4(code, format) as parser:
            records = parser.getRecords()
            self.assertFalse(not records)

            Utils.compare("Records do not match expected result", res, records)

    def __validateRecordPosition(self, lineSeparator: str) -> None:

        nl = lineSeparator  # used as linebreak in values for better distinction

        code = (
            "a,b,c"
            + nl
            + "1,2,3"
            + nl
            + "'A"
            + nl
            + "A','B"
            + nl
            + "B',CC"
            + nl
            + "\u00c4,\u00d6,\u00dc"
            + nl
            + "EOF,EOF,EOF"
        )

        format = CSVFormat.newFormat(",").withQuote0("'").withRecordSeparator1(nl)
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
        self.assertIsNotNone(record)
        self.assertEqual(3, record.getRecordNumber())
        self.assertEqual(code.index("'A"), record.getCharacterPosition())
        self.assertEqual("A" + nl + "A", record.get1(0))
        self.assertEqual("B" + nl + "B", record.get1(1))
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
            io.StringIO(code[positionRecord3:]), format, positionRecord3, 3
        )

        record = parser.nextRecord()
        self.assertIsNotNone(record)
        self.assertEqual(3, record.getRecordNumber())
        self.assertEqual(code.index("'A"), record.getCharacterPosition())
        self.assertEqual("A" + nl + "A", record.get1(0))
        self.assertEqual("B" + nl + "B", record.get1(1))
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

            record = None
            self.assertEqual(0, parser.getRecordNumber())
            self.assertIsNotNone(record := parser.nextRecord())
            self.assertEqual(1, record.getRecordNumber())
            self.assertEqual(1, parser.getRecordNumber())
            self.assertIsNotNone(record := parser.nextRecord())
            self.assertEqual(2, record.getRecordNumber())
            self.assertEqual(2, parser.getRecordNumber())
            self.assertIsNotNone(record := parser.nextRecord())
            self.assertEqual(3, record.getRecordNumber())
            self.assertEqual(3, parser.getRecordNumber())
            self.assertIsNone(record := parser.nextRecord())
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

        path = pathlib.Path(
            "src/test/resources/org/apache/commons/csv/CSV-141/csv-141.csv"
        )
        with CSVParser.parse2(path, "UTF-8", format) as parser:
            record = parser.nextRecord()
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
        with CSVParser.parse2(path, "UTF-8", format) as parser:
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
        for record in parser:
            assert record is not None

    def parse(self, parser: CSVParser, failParseRecordNo: int) -> CSVRecord:

        if parser.getRecordNumber() + 1 == failParseRecordNo:
            with pytest.raises(IOError):
                parser.nextRecord()
            return None
        return parser.nextRecord()
