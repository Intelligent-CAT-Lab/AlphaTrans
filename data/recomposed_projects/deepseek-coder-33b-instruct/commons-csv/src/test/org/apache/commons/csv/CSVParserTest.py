from __future__ import annotations
import re
import unittest
import pytest
import pathlib
import io
import numbers
import typing
from typing import *
import os
from src.main.org.apache.commons.csv.CSVFormat import *
from src.main.org.apache.commons.csv.CSVParser import *
from src.main.org.apache.commons.csv.CSVPrinter import *
from src.main.org.apache.commons.csv.CSVRecord import *
from src.main.org.apache.commons.csv.Constants import *
from src.test.org.apache.commons.csv.Utils import *


class CSVParserTest(unittest.TestCase):

    __CSV_INPUT_MULTILINE_HEADER_TRAILER_COMMENT: str = (
        "# multi-line"
        + "\n"
        + "# header comment"
        + "\n"
        + "A,B"
        + "\n"
        + "1,2"
        + "\n"
        + "# multi-line"
        + "\n"
        + "# comment"
    )
    __CSV_INPUT_HEADER_TRAILER_COMMENT: str = (
        "# header comment" + "\n" + "A,B" + "\n" + "1,2" + "\n" + "# comment"
    )
    __CSV_INPUT_HEADER_COMMENT: str = (
        "# header comment" + "\n" + "A,B" + "\n" + "1,2" + "\n"
    )
    __CSV_INPUT_NO_COMMENT: str = "A,B" + "\n" + "1,2" + "\n"
    __RESULT: typing.List[typing.List[str]] = []

    __CSV_INPUT_2: str = "a,b,1 2"
    __CSV_INPUT_1: str = "a,b,c,d"
    __CSV_INPUT: str = (
        "a,b,c,d\n"
        + " a , b , 1 2 \n"
        + '"foo baar", b,\n'
        + '   "foo\n,,\n"",,\n""",d,e\n'
    )
    __UTF_8_NAME: str = StandardCharsets.UTF_8.name
    __UTF_8: str = StandardCharsets.UTF_8.name

    @pytest.mark.test
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

    @pytest.mark.test
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
                self.assertEqual(len(res), len(records))
                self.assertFalse(not records)
                for i, record in enumerate(records):
                    self.assertEqual(res[i], record.values())

    @pytest.mark.test
    def testRoundtrip(self) -> None:

        out = io.StringIO()
        data = "a,b,c\r\n1,2,3\r\nx,y,z\r\n"
        try:
            with CSVPrinter(out, CSVFormat.DEFAULT) as printer, CSVParser.parse4(
                data, CSVFormat.DEFAULT
            ) as parse:
                for record in parse:
                    printer.printRecord0(record)
                self.assertEqual(data, out.getvalue())
        finally:
            out.close()

    @pytest.mark.test
    def testParseWithQuoteWithEscape(self) -> None:

        source = "'a?,b?,c?d',xyz"
        csvFormat = CSVFormat.DEFAULT.withQuote0("'").withEscape0("?")
        with csvFormat.parse(io.StringIO(source)) as csvParser:
            csvRecord = csvParser.nextRecord()
            self.assertEqual("a,b,c?d", csvRecord.get1(0))
            self.assertEqual("xyz", csvRecord.get1(1))

    @pytest.mark.test
    def testParseWithQuoteThrowsException(self) -> None:

        csv_format = CSVFormat.DEFAULT.withQuote0("'")

        with pytest.raises(IOException):
            csv_format.parse(io.StringIO("'a,b,c','")).nextRecord()

        with pytest.raises(IOException):
            csv_format.parse(io.StringIO("'a,b,c'abc,xyz")).nextRecord()

        with pytest.raises(IOException):
            csv_format.parse(io.StringIO("'abc'a,b,c',xyz")).nextRecord()

    @pytest.mark.test
    def testParseWithDelimiterWithQuote(self) -> None:

        source = "'a,b,c',xyz"
        csvFormat = CSVFormat.DEFAULT.withQuote0("'")
        csvParser = csvFormat.parse(io.StringIO(source))
        csvRecord = csvParser.nextRecord()
        self.assertEqual("a,b,c", csvRecord.get1(0))
        self.assertEqual("xyz", csvRecord.get1(1))

    @pytest.mark.test
    def testParseWithDelimiterWithEscape(self) -> None:

        source = "a,b,c,xyz"
        csv_format = CSVFormat.DEFAULT.withEscape0("0")
        with csv_format.parse(io.StringIO(source)) as csv_parser:
            csv_record = csv_parser.nextRecord()
            self.assertEqual("a,b,c", csv_record.get1(0))
            self.assertEqual("xyz", csv_record.get1(1))

    @pytest.mark.test
    def testParseWithDelimiterStringWithQuote(self) -> None:

        source = "'a[|]b[|]c'[|]xyz\r\nabc[abc][|]xyz"
        csvFormat = (
            CSVFormat.DEFAULT.builder().setDelimiter1("[|]").setQuote0("'").build()
        )
        csvParser = csvFormat.parse(io.StringIO(source))
        csvRecord = csvParser.nextRecord()
        self.assertEqual("a[|]b[|]c", csvRecord.get1(0))
        self.assertEqual("xyz", csvRecord.get1(1))
        csvRecord = csvParser.nextRecord()
        self.assertEqual("abc[abc]", csvRecord.get1(0))
        self.assertEqual("xyz", csvRecord.get1(1))

    @pytest.mark.test
    def testParseWithDelimiterStringWithEscape(self) -> None:

        source = "a![|!]b![|]c[|]xyz\r\nabc[abc][|]xyz"
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

    @pytest.mark.test
    def testParseUrlCharsetNullFormat(self) -> None:
        with pytest.raises(NullPointerException):
            CSVParser.parse5(
                URL("https://commons.apache.org"), Charset.defaultCharset(), None
            )

    @pytest.mark.test
    def testParseStringNullFormat(self) -> None:
        with pytest.raises(NullPointerException):
            CSVParser.parse4("csv data", None)

    @pytest.mark.test
    def testParserUrlNullCharsetFormat(self) -> None:
        with pytest.raises(NullPointerException):
            CSVParser.parse5(URL("https://commons.apache.org"), None, CSVFormat.DEFAULT)

    @pytest.mark.test
    def testParseNullUrlCharsetFormat(self) -> None:
        with pytest.raises(NullPointerException):
            CSVParser.parse5(None, Charset.defaultCharset(), CSVFormat.DEFAULT)

    @pytest.mark.test
    def testParseNullStringFormat(self) -> None:
        with pytest.raises(NullPointerException):
            CSVParser.parse4(None, CSVFormat.DEFAULT)

    @pytest.mark.test
    def testParseNullPathFormat(self) -> None:
        with pytest.raises(NullPointerException):
            CSVParser.parse2(None, Charset.defaultCharset(), CSVFormat.DEFAULT)

    @pytest.mark.test
    def testParseNullFileFormat(self) -> None:
        with pytest.raises(TypeError):
            CSVParser.parse0(None, StandardCharsets.UTF_8, CSVFormat.DEFAULT)

    @pytest.mark.test
    def testParseFileNullFormat(self) -> None:

        with pytest.raises(NullPointerException):
            CSVParser.parse0(
                pathlib.Path("CSVFileParser/test.csv"), StandardCharsets.UTF_8, None
            )

    @pytest.mark.test
    def testNotValueCSV(self) -> None:

        source = "#"
        csv_format = CSVFormat.DEFAULT.withCommentMarker0("#")
        with csv_format.parse(io.StringIO(source)) as csv_parser:
            csv_record = csv_parser.nextRecord()
            self.assertIsNone(csv_record)

    @pytest.mark.test
    def testNoHeaderMap(self) -> None:

        with CSVParser.parse4("a,b,c\n1,2,3\nx,y,z", CSVFormat.DEFAULT) as parser:
            assert parser.getHeaderMap() is None

    @pytest.mark.test
    def testNewCSVParserReaderNullFormat(self) -> None:
        with pytest.raises(TypeError):
            CSVParser.CSVParser1(io.StringIO(""), None)

    @pytest.mark.test
    def testNewCSVParserNullReaderFormat(self) -> None:
        with pytest.raises(NullPointerException):
            CSVParser.CSVParser1(None, CSVFormat.DEFAULT)

    @pytest.mark.test
    def testMultipleIterators(self) -> None:

        with CSVParser.parse4("a,b,c" + "\n" + "d,e,f", CSVFormat.DEFAULT) as parser:
            itr1 = parser.iterator()

            first = next(itr1)
            self.assertEqual("a", first.get1(0))
            self.assertEqual("b", first.get1(1))
            self.assertEqual("c", first.get1(2))

            second = next(itr1)
            self.assertEqual("d", second.get1(0))
            self.assertEqual("e", second.get1(1))
            self.assertEqual("f", second.get1(2))

    @pytest.mark.test
    def testMongoDbCsv(self) -> None:

        try:
            parser = CSVParser.parse4(
                '"a a",b,c' + "\n" + "d,e,f", CSVFormat.MONGODB_CSV
            )
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
        except Exception as e:
            self.fail("testMongoDbCsv failed with exception: " + str(e))

    @pytest.mark.test
    def testLineFeedEndings(self) -> None:

        code = "foo\nbaar,\nhello,world\n,kanu"
        try:
            parser = CSVParser.parse4(code, CSVFormat.DEFAULT)
            records = parser.getRecords()
            self.assertEqual(4, len(records))
        finally:
            parser.close()

    @pytest.mark.test
    def testIteratorSequenceBreaking(self) -> None:

        five_rows = "1\n2\n3\n4\n5\n"

        with CSVFormat.DEFAULT.parse(io.StringIO(five_rows)) as parser:
            record_number = 0
            iter_ = parser.iterator()
            while iter_.hasNext():
                record = iter_.next()
                record_number += 1
                self.assertEqual(str(record_number), record.get1(0))
                if record_number >= 2:
                    break

            while iter_.hasNext():
                record = iter_.next()
                record_number += 1
                self.assertEqual(str(record_number), record.get1(0))

        with CSVFormat.DEFAULT.parse(io.StringIO(five_rows)) as parser:
            record_number = 0
            for record in parser:
                record_number += 1
                self.assertEqual(str(record_number), record.get1(0))
                if record_number >= 2:
                    break

            for record in parser:
                record_number += 1
                self.assertEqual(str(record_number), record.get1(0))

        with CSVFormat.DEFAULT.parse(io.StringIO(five_rows)) as parser:
            record_number = 0
            for record in parser:
                record_number += 1
                self.assertEqual(str(record_number), record.get1(0))
                if record_number >= 2:
                    break

            iter_ = parser.iterator()
            iter_.hasNext()
            for record in parser:
                record_number += 1
                self.assertEqual(str(record_number), record.get1(0))

    @pytest.mark.test
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

            with pytest.raises(NoSuchElementException):
                iterator.next()
        finally:
            in_.close()

    @pytest.mark.test
    def testInvalidFormat(self) -> None:
        with pytest.raises(ValueError):
            CSVFormat.DEFAULT.withDelimiter(CR)

    @pytest.mark.test
    def testIgnoreEmptyLines(self) -> None:

        code = "\nfoo,baar\n\r\n,\n\n,world\r\n\n"

        with CSVParser.parse4(code, CSVFormat.DEFAULT) as parser:
            records = parser.getRecords()
            self.assertEqual(len(records), 3)

    @pytest.mark.test
    def testGetRecordWithMultiLineValues(self) -> None:

        try:
            parser = CSVParser.parse4(
                '"a\r\n1","a\r\n2"'
                + "\n"
                + '"b\r\n1","b\r\n2"'
                + "\n"
                + '"c\r\n1","c\r\n2"',
                CSVFormat.DEFAULT.withRecordSeparator1("\n"),
            )

            record = None
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
        finally:
            parser.close()

    @pytest.mark.test
    def testGetRecords(self) -> None:

        try:
            parser = CSVParser.parse4(
                self.__CSV_INPUT, CSVFormat.DEFAULT.withIgnoreSurroundingSpaces0()
            )
            records = parser.getRecords()
            self.assertEqual(len(self.__RESULT), len(records))
            self.assertFalse(not records)
            for i in range(len(self.__RESULT)):
                self.assertListEqual(self.__RESULT[i], records[i].values())
        except Exception as e:
            self.fail("testGetRecords failed with exception: " + str(e))

    @pytest.mark.test
    def testGetRecordPositionWithLF(self) -> None:

        self.__validateRecordPosition(os.linesep)

    @pytest.mark.test
    def testGetRecordPositionWithCRLF(self) -> None:

        lineSeparator = "\r\n"  # CRLF in Python
        self.__validateRecordPosition(lineSeparator)

    @pytest.mark.test
    def testGetRecordNumberWithLF(self) -> None:

        self.__validateRecordNumbers("\n")

    @pytest.mark.test
    def testGetRecordNumberWithCRLF(self) -> None:

        self.__validateRecordNumbers("\r\n")

    @pytest.mark.test
    def testGetRecordNumberWithCR(self) -> None:

        self.__validateRecordNumbers(os.linesep)

    @pytest.mark.test
    def testGetOneLineOneParser(self) -> None:

        format = CSVFormat.DEFAULT
        with io.Pipe() as (reader, writer):
            parser = CSVParser.CSVParser1(io.BufferedReader(reader), format)
            writer.write(self.__CSV_INPUT_1.encode())
            writer.write(format.getRecordSeparator().encode())
            record1 = parser.nextRecord()
            self.assertListEqual(self.__RESULT[0], record1.values())
            writer.write(self.__CSV_INPUT_2.encode())
            writer.write(format.getRecordSeparator().encode())
            record2 = parser.nextRecord()
            self.assertListEqual(self.__RESULT[1], record2.values())

    @pytest.mark.test
    def testGetOneLine(self) -> None:

        try:
            parser = CSVParser.parse4(self.__CSV_INPUT_1, CSVFormat.DEFAULT)
            record = parser.getRecords()[0]
            self.assertListEqual(self.__RESULT[0], record.values())
        except Exception as e:
            self.fail(f"testGetOneLine failed with exception: {str(e)}")

    @pytest.mark.test
    def testGetLineNumberWithLF(self) -> None:

        self.__validateLineNumbers("\n")

    @pytest.mark.test
    def testGetLineNumberWithCRLF(self) -> None:

        self.__validateLineNumbers("\r\n")

    @pytest.mark.test
    def testGetLineNumberWithCR(self) -> None:

        self.__validateLineNumbers(os.linesep)

    @pytest.mark.test
    def testGetLine(self) -> None:

        with CSVParser.parse4(
            self.__CSV_INPUT, CSVFormat.DEFAULT.withIgnoreSurroundingSpaces0()
        ) as parser:
            for re in self.__RESULT:
                self.assertListEqual(re, parser.nextRecord().values())

            self.assertIsNone(parser.nextRecord())

    @pytest.mark.test
    def testForEach(self) -> None:

        with io.StringIO("a,b,c\n1,2,3\nx,y,z") as in_file:
            parser = CSVFormat.DEFAULT.parse(in_file)
            records = []
            for record in parser:
                records.append(record)
            self.assertEqual(3, len(records))
            self.assertListEqual(["a", "b", "c"], records[0].values())
            self.assertListEqual(["1", "2", "3"], records[1].values())
            self.assertListEqual(["x", "y", "z"], records[2].values())

    @pytest.mark.test
    def testFirstEndOfLineLf(self) -> None:

        data = "foo\nbaar,\nhello,world\n,kanu"

        with CSVParser.parse4(data, CSVFormat.DEFAULT) as parser:
            records = parser.getRecords()
            self.assertEqual(4, len(records))
            self.assertEqual("\n", parser.getFirstEndOfLine())

    @pytest.mark.test
    def testFirstEndOfLineCrLf(self) -> None:

        data = "foo\r\nbaar,\r\nhello,world\r\n,kanu"

        with CSVParser.parse4(data, CSVFormat.DEFAULT) as parser:
            records = parser.getRecords()
            self.assertEqual(4, len(records))
            self.assertEqual("\r\n", parser.getFirstEndOfLine())

    @pytest.mark.test
    def testFirstEndOfLineCr(self) -> None:

        data = "foo\rbaar,\rhello,world\r,kanu"
        try:
            parser = CSVParser.parse4(data, CSVFormat.DEFAULT)
            records = parser.getRecords()
            self.assertEqual(4, len(records))
            self.assertEqual("\r", parser.getFirstEndOfLine())
        finally:
            parser.close()

    @pytest.mark.test
    def testExcelFormat2(self) -> None:

        code = "foo,baar\r\n\r\nhello,\r\n\r\nworld,\r\n"
        res = [["foo", "baar"], [""], ["hello", ""], [""], ["world", ""]]

        with CSVParser.parse4(code, CSVFormat.EXCEL) as parser:
            records = parser.getRecords()

            self.assertEqual(len(res), len(records))
            self.assertFalse(not records)

            for i in range(len(res)):
                self.assertListEqual(res[i], records[i].values())

    @pytest.mark.test
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
                self.assertListEqual(res[i], records[i].values())

    @pytest.mark.test
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
                self.assertEqual(len(res), len(records))
                self.assertFalse(not records)
                for i, record in enumerate(records):
                    self.assertEqual(res[i], record.values())

    @pytest.mark.test
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
            with CSVParser.parse4(code, CSVFormat.DEFAULT) as parser:
                records = parser.getRecords()
                self.assertEqual(len(res), len(records))
                self.assertFalse(not records)
                for i, record in enumerate(records):
                    self.assertEqual(res[i], record.values())

    @pytest.mark.test
    def testEmptyString(self) -> None:

        try:
            parser = CSVParser.parse4("", CSVFormat.DEFAULT)
            assert parser.nextRecord() is None
        finally:
            parser.close()

    @pytest.mark.test
    def testEmptyLineBehaviorExcel(self) -> None:

        codes = [
            "hello,\r\n\r\n\r\n",
            "hello,\n\n\n",
            'hello,""\r\n\r\n\r\n',
            'hello,""\n\n\n',
        ]
        res = [["hello", ""], [""], [""]]  # Excel format does not ignore empty lines
        for code in codes:
            with CSVParser.parse4(code, CSVFormat.EXCEL) as parser:
                records = parser.getRecords()
                self.assertEqual(len(res), len(records))
                self.assertFalse(not records)
                for i, record in enumerate(records):
                    self.assertListEqual(res[i], record.values())

    @pytest.mark.test
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
                self.assertEqual(len(res), len(records))
                self.assertFalse(not records)
                for i, record in enumerate(records):
                    self.assertListEqual(res[i], record.values())

    @pytest.mark.test
    def testEmptyFile(self) -> None:

        try:
            with CSVParser.parse2(
                pathlib.Path("src/test/resources/org/apache/commons/csv/empty.txt"),
                StandardCharsets.UTF_8.name,
                CSVFormat.DEFAULT,
            ) as parser:
                assert parser.nextRecord() is None
        except Exception as e:
            pytest.fail("Unexpected exception: {}".format(e))

    @pytest.mark.test
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
            assert len(records) != 0

            Utils.compare("Failed to parse without comments", res, records)

            format = format.withCommentMarker0("#")

        with CSVParser.parse4(code, format) as parser:
            records = parser.getRecords()

            Utils.compare("Failed to parse with comments", res_comments, records)

    @pytest.mark.test
    def testCSV57(self) -> None:

        try:
            parser = CSVParser.parse4("", CSVFormat.DEFAULT)
            list = parser.getRecords()
            assert list is not None
            assert len(list) == 0
        finally:
            parser.close()

    @pytest.mark.test
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

    @pytest.mark.test
    def testCSV141RFC4180(self) -> None:

        self.__testCSV141Failure(CSVFormat.RFC4180, 3)

    @pytest.mark.test
    def testCSV141Excel(self) -> None:

        self.__testCSV141Ok(CSVFormat.EXCEL)

    @pytest.mark.test
    def testCSV141CSVFormat_POSTGRESQL_CSV(self) -> None:

        self.__testCSV141Failure(CSVFormat.POSTGRESQL_CSV, 3)

    @pytest.mark.test
    def testCSV141CSVFormat_ORACLE(self) -> None:

        self.__testCSV141Failure(CSVFormat.ORACLE, 2)

    @pytest.mark.test
    def testCSV141CSVFormat_INFORMIX_UNLOAD_CSV(self) -> None:

        self.__testCSV141Failure(CSVFormat.INFORMIX_UNLOAD_CSV, 3)

    @pytest.mark.test
    def testCSV141CSVFormat_INFORMIX_UNLOAD(self) -> None:

        self.__testCSV141Failure(CSVFormat.INFORMIX_UNLOAD, 1)

    @pytest.mark.test
    def testCSV141CSVFormat_DEFAULT(self) -> None:

        self.__testCSV141Failure(CSVFormat.DEFAULT, 3)

    @pytest.mark.test
    def testCarriageReturnLineFeedEndings(self) -> None:

        code = "foo\r\nbaar,\r\nhello,world\r\n,kanu"

        with CSVParser.parse4(code, CSVFormat.DEFAULT) as parser:
            records = parser.getRecords()
            self.assertEqual(len(records), 4)

    @pytest.mark.test
    def testCarriageReturnEndings(self) -> None:

        code = "foo\rbaar,\rhello,world\r,kanu"
        try:
            parser = CSVParser.parse4(code, CSVFormat.DEFAULT)
            records = parser.getRecords()
            self.assertEqual(4, len(records))
        finally:
            parser.close()

    @pytest.mark.test
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
        except Exception as e:
            self.fail(f"Unexpected exception raised: {str(e)}")

    @pytest.mark.test
    def testBackslashEscaping2(self) -> None:

        code = "" + " , , \n" + " \t ,  , \n" + " // , /, , /,\n"  # 1)  # 2)  # 3)
        res = [
            [" ", " ", " "],  # 1
            [" \t ", "  ", " "],  # 2
            [" / ", " , ", " ,"],  # 3
        ]

        format = (
            CSVFormat.newFormat(",")
            .withRecordSeparator1("\n")
            .withEscape0("/")
            .withIgnoreEmptyLines0()
        )

        with CSVParser.parse4(code, format) as parser:
            records = parser.getRecords()
            assert not records, "Records list should not be empty"

            Utils.compare("", res, records)

    @pytest.mark.test
    def testBackslashEscaping(self) -> None:

        code = (
            "one,two,three\n"  # 0
            + "'',''\n"  # 1) empty encapsulators
            + "/',/'\n"  # 2) single encapsulators
            + "'/'','/''\n"  # 3) single encapsulators encapsulated via escape
            + "'''',''''\n"  # 4) single encapsulators encapsulated via doubling
            + "/,,/,\n"  # 5) separator escaped
            + "//,//\n"  # 6) escape escaped
            + "'//','//'\n"  # 7) escape escaped in encapsulation
            + '   8   ,   "quoted "" /" // string"   \n'  # don't eat spaces
            + "9,   /\n   \n"  # escaped newline
            + ""
        )
        res = [
            ["one", "two", "three"],  # 0
            ["", ""],  # 1
            ["'", "'"],  # 2
            ["'", "'"],  # 3
            ["'", "'"],  # 4
            [",", ","],  # 5
            ["/", "/"],  # 6
            ["/", "/"],  # 7
            ["   8   ", '   "quoted "" /" / string"   '],
            ["9", "   \n   "],
        ]

        format = (
            CSVFormat.newFormat(",")
            .withQuote0("'")
            .withRecordSeparator1("\n")
            .withEscape0("/")
            .withIgnoreEmptyLines0()
        )

        with CSVParser.parse4(code, format) as parser:
            records = parser.getRecords()
            assert not records, "Records do not match expected result"

            Utils.compare("Records do not match expected result", res, records)

    def __validateRecordPosition(self, lineSeparator: str) -> None:

        nl = lineSeparator  # used as linebreak in values for better distinction

        code = (
            "a,b,c"
            + lineSeparator
            + "1,2,3"
            + lineSeparator
            + "'A"
            + nl
            + "A','B"
            + nl
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
        assert parser.getRecordNumber() == 0

        record = parser.nextRecord()
        assert record is not None
        assert record.getRecordNumber() == 1
        assert code.index("a") == record.getCharacterPosition()

        record = parser.nextRecord()
        assert record is not None
        assert record.getRecordNumber() == 2
        assert code.index("1") == record.getCharacterPosition()

        record = parser.nextRecord()
        positionRecord3 = record.getCharacterPosition()
        assert record is not None
        assert record.getRecordNumber() == 3
        assert code.index("'A") == record.getCharacterPosition()
        assert record.get1(0) == "A" + lineSeparator + "A"
        assert record.get1(1) == "B" + lineSeparator + "B"
        assert record.get1(2) == "CC"

        record = parser.nextRecord()
        assert record is not None
        assert record.getRecordNumber() == 4
        assert code.index("\u00c4") == record.getCharacterPosition()

        record = parser.nextRecord()
        assert record is not None
        assert record.getRecordNumber() == 5
        assert code.index("EOF") == record.getCharacterPosition()

        parser.close()

        parser = CSVParser(
            io.StringIO(code[positionRecord3:]), format, positionRecord3, 3
        )

        record = parser.nextRecord()
        assert record is not None
        assert record.getRecordNumber() == 3
        assert code.index("'A") == record.getCharacterPosition()
        assert record.get1(0) == "A" + lineSeparator + "A"
        assert record.get1(1) == "B" + lineSeparator + "B"
        assert record.get1(2) == "CC"

        record = parser.nextRecord()
        assert record is not None
        assert record.getRecordNumber() == 4
        assert code.index("\u00c4") == record.getCharacterPosition()
        assert record.get1(0) == "\u00c4"

        parser.close()

    def __validateRecordNumbers(self, lineSeparator: str) -> None:

        with CSVParser.parse4(
            "a" + lineSeparator + "b" + lineSeparator + "c",
            CSVFormat.DEFAULT.withRecordSeparator1(lineSeparator),
        ) as parser:

            record = None
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

            assert parser.getCurrentLineNumber() == 0
            assert parser.nextRecord() is not None
            assert parser.getCurrentLineNumber() == 1
            assert parser.nextRecord() is not None
            assert parser.getCurrentLineNumber() == 2
            assert parser.nextRecord() is not None
            assert parser.getCurrentLineNumber() == 3
            assert parser.nextRecord() is None
            assert parser.getCurrentLineNumber() == 3

    def __testCSV141Ok(self, format: CSVFormat) -> None:

        path = pathlib.Path(
            "src/test/resources/org/apache/commons/csv/CSV-141/csv-141.csv"
        )

        with path.open("r", encoding=StandardCharsets.UTF_8.name) as f:
            parser = CSVParser.parse2(path, StandardCharsets.UTF_8.name, format)

            record = parser.nextRecord()
            assert record.get1(0) == "1414770317901"
            assert record.get1(1) == "android.widget.EditText"
            assert record.get1(2) == "pass sem1 _84*|*"
            assert record.get1(3) == "0"
            assert record.get1(4) == "pass sem1 _8"
            assert record.size() == 5

            record = parser.nextRecord()
            assert record.get1(0) == "1414770318470"
            assert record.get1(1) == "android.widget.EditText"
            assert record.get1(2) == "pass sem1 _84:|"
            assert record.get1(3) == "0"
            assert record.get1(4) == "pass sem1 _84:\\"
            assert record.size() == 5

            record = parser.nextRecord()
            assert record.get1(0) == "1414770318327"
            assert record.get1(1) == "android.widget.EditText"
            assert record.get1(2) == "pass sem1"
            assert record.size() == 3

            record = parser.nextRecord()
            assert record.get1(0) == "1414770318628"
            assert record.get1(1) == "android.widget.EditText"
            assert record.get1(2) == "pass sem1 _84*|*"
            assert record.get1(3) == "0"
            assert record.get1(4) == "pass sem1"
            assert record.size() == 5

    def __testCSV141Failure(self, format: CSVFormat, failParseRecordNo: int) -> None:

        path = pathlib.Path(
            "src/test/resources/org/apache/commons/csv/CSV-141/csv-141.csv"
        )
        with path.open("r", encoding=StandardCharsets.UTF_8.name) as f:
            parser = CSVParser.parse2(path, StandardCharsets.UTF_8.name, format)
            record = self.parse(parser, failParseRecordNo)
            if record is None:
                return  # expected failure
            assert record.get1(0) == "1414770317901"
            assert record.get1(1) == "android.widget.EditText"
            assert record.get1(2) == "pass sem1 _84*|*"
            assert record.get1(3) == "0"
            assert record.get1(4) == "pass sem1 _8"
            assert record.size() == 5
            record = self.parse(parser, failParseRecordNo)
            if record is None:
                return  # expected failure
            assert record.get1(0) == "1414770318470"
            assert record.get1(1) == "android.widget.EditText"
            assert record.get1(2) == "pass sem1 _84:|"
            assert record.get1(3) == "0"
            assert record.get1(4) == "pass sem1 _84:\\"
            assert record.size() == 5
            with pytest.raises(IOException):
                parser.nextRecord()

    def __parseFully(self, parser: CSVParser) -> None:
        for record in parser:
            assert record is not None

    def parse(self, parser: CSVParser, failParseRecordNo: int) -> CSVRecord:

        result = None
        parser._CSVParser__recordList.clear()
        sb = None
        startCharPosition = (
            parser._CSVParser__lexer.getCharacterPosition()
            + parser._CSVParser__characterOffset
        )

        while True:
            parser._CSVParser__reusableToken.reset()
            parser._CSVParser__lexer.nextToken(parser._CSVParser__reusableToken)

            if parser._CSVParser__reusableToken.type == TOKEN:
                self.__addRecordValue(parser, False)
            elif parser._CSVParser__reusableToken.type == EORECORD:
                self.__addRecordValue(parser, True)
            elif parser._CSVParser__reusableToken.type == EOF:
                if parser._CSVParser__reusableToken.isReady:
                    self.__addRecordValue(parser, True)
                elif sb is not None:
                    parser._CSVParser__trailerComment = sb.toString()
            elif parser._CSVParser__reusableToken.type == INVALID:
                raise IOException(
                    "(line "
                    + parser.getCurrentLineNumber()
                    + ") invalid parse sequence"
                )
            elif parser._CSVParser__reusableToken.type == COMMENT:
                if sb is None:
                    sb = StringBuilder()
                else:
                    sb.append(Constants.LF)
                sb.append(parser._CSVParser__reusableToken.content)
                parser._CSVParser__reusableToken.type = TOKEN
            else:
                raise RuntimeError(
                    "Unexpected Token type: " + parser._CSVParser__reusableToken.type
                )

            if parser._CSVParser__reusableToken.type != TOKEN:
                break

        if parser._CSVParser__recordList:
            parser._CSVParser__recordNumber += 1
            comment = None if sb is None else sb.toString()
            result = CSVRecord(
                parser,
                parser._CSVParser__recordList.toArray(Constants.EMPTY_STRING_ARRAY),
                comment,
                parser._CSVParser__recordNumber,
                startCharPosition,
            )

        return result
