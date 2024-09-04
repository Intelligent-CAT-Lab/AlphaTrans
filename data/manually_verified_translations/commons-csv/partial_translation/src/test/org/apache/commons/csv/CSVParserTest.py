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
        None  # LLM could not translate this field
    )

    __CSV_INPUT_HEADER_TRAILER_COMMENT: str = None  # LLM could not translate this field

    __CSV_INPUT_HEADER_COMMENT: str = None  # LLM could not translate this field

    __CSV_INPUT_NO_COMMENT: str = None  # LLM could not translate this field

    __RESULT: typing.List[typing.List[str]] = [
        ["a", "b", "c", "d"],
        ["a", "b", "1 2"],
        ["foo baar", "b", ""],
        ['foo\n,,\n",,\n"', "d", "e"],
    ]
    __CSV_INPUT_2: str = "a,b,1 2"
    __CSV_INPUT_1: str = "a,b,c,d"
    __CSV_INPUT: str = """a,b,c,d
 a , b , 1 2 
"foo baar", b,
   "foo
,,"
"",,d,e
"""
    __UTF_8_NAME: str = "UTF-8"
    __UTF_8: str = "UTF-8"

    def testStream(self) -> None:

        in_ = io.StringIO("a,b,c\n1,2,3\nx,y,z")
        parser = CSVFormat.DEFAULT.parse(in_)
        list_ = list(parser.stream())
        assert not list_
        assert list_[0].values() == ["a", "b", "c"]
        assert list_[1].values() == ["1", "2", "3"]
        assert list_[2].values() == ["x", "y", "z"]

    def testStartWithEmptyLinesThenHeaders(self) -> None:

        codes = [
            "\r\n\r\n\r\nhello,\r\n\r\n\r\n",
            "hello,\n\n\n",
            'hello,""\r\n\r\n\r\n',
            'hello,""\n\n\n',
        ]
        res = [["hello", ""], [""], [""]]  # Excel format does not ignore empty lines
        for code in codes:
            try:
                parser = CSVParser.parse4(code, CSVFormat.EXCEL)
                records = parser.getRecords()
                self.assertEqual(len(res), len(records))
                self.assertFalse(not records)
                for i in range(len(res)):
                    self.assertEqual(res[i], records[i].values())
            finally:
                parser.close()

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

        csvFormat = CSVFormat.DEFAULT.withQuote0("'")

        with pytest.raises(IOError):
            csvFormat.parse(io.StringIO("'a,b,c','")).nextRecord()
        with pytest.raises(IOError):
            csvFormat.parse(io.StringIO("'a,b,c'abc,xyz")).nextRecord()
        with pytest.raises(IOError):
            csvFormat.parse(io.StringIO("'abc'a,b,c',xyz")).nextRecord()

    def testParseWithDelimiterWithQuote(self) -> None:

        source = "'a,b,c',xyz"
        csvFormat = CSVFormat.DEFAULT.withQuote0("'")
        csvParser = csvFormat.parse(io.StringIO(source))
        csvRecord = csvParser.nextRecord()
        self.assertEqual("a,b,c", csvRecord.get1(0))
        self.assertEqual("xyz", csvRecord.get1(1))

    def testParseWithDelimiterWithEscape(self) -> None:

        source = "a!!,b!!,c,xyz"
        csvFormat = CSVFormat.DEFAULT.withEscape0("!!")
        csvParser = csvFormat.parse(io.StringIO(source))
        csvRecord = csvParser.nextRecord()
        self.assertEqual("a,b,c", csvRecord.get1(0))
        self.assertEqual("xyz", csvRecord.get1(1))

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

    def testParseUrlCharsetNullFormat(self) -> None:

        with pytest.raises(TypeError):
            CSVParser.parse5(
                url=URL("https://commons.apache.org"),
                charset=Charset.defaultCharset(),
                format=None,
            )

    def testParseStringNullFormat(self) -> None:
        with pytest.raises(TypeError):
            CSVParser.parse4("csv data", None)

    def testParserUrlNullCharsetFormat(self) -> None:

        with pytest.raises(RuntimeError):
            CSVParser.parse5(URL("https://commons.apache.org"), None, CSVFormat.DEFAULT)

    def testParseNullUrlCharsetFormat(self) -> None:

        with pytest.raises(TypeError):
            CSVParser.parse(None, Charset.defaultCharset(), CSVFormat.DEFAULT)

    def testParseNullStringFormat(self) -> None:

        with pytest.raises(RuntimeError):
            CSVParser.parse4(None, CSVFormat.DEFAULT)

    def testParseNullPathFormat(self) -> None:

        with pytest.raises(TypeError):
            CSVParser.parse2(None, Charset.defaultCharset(), CSVFormat.DEFAULT)

    def testParseNullFileFormat(self) -> None:

        with pytest.raises(TypeError):
            CSVParser.parse0(None, Charset.defaultCharset(), CSVFormat.DEFAULT)

    def testParseFileNullFormat(self) -> None:

        with pytest.raises(TypeError):
            CSVParser.parse0(pathlib.Path("CSVFileParser/test.csv"), None)

    def testNotValueCSV(self) -> None:

        source = "#"
        csvFormat = CSVFormat.DEFAULT.withCommentMarker0("#")
        csvParser = csvFormat.parse(io.StringIO(source))
        csvRecord = csvParser.nextRecord()
        self.assertIsNone(csvRecord)

    def testNoHeaderMap(self) -> None:

        try:
            parser = CSVParser.parse4("a,b,c\n1,2,3\nx,y,z", CSVFormat.DEFAULT)
            self.assertIsNone(parser.getHeaderMap())
        finally:
            parser.close()

    def testNewCSVParserReaderNullFormat(self) -> None:

        with pytest.raises(TypeError):
            CSVParser.CSVParser1(io.StringIO(""), None)

    def testNewCSVParserNullReaderFormat(self) -> None:

        with pytest.raises(TypeError):
            CSVParser.CSVParser1(None, CSVFormat.DEFAULT)

    def testMultipleIterators(self) -> None:

        with CSVParser.parse4(
            "a,b,c" + Constants.CRLF + "d,e,f", CSVFormat.DEFAULT
        ) as parser:
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
            parser = CSVParser.parse4(
                '"a a",b,c' + Constants.LF + "d,e,f", CSVFormat.MONGODB_CSV
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

    def testLineFeedEndings(self) -> None:

        code = "foo\nbaar,\nhello,world\n,kanu"
        with CSVParser.parse4(code, CSVFormat.DEFAULT) as parser:
            records = parser.getRecords()
            self.assertEqual(len(records), 4)

    def testIteratorSequenceBreaking(self) -> None:

        five_rows = "1\n2\n3\n4\n5\n"

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

        with CSVParser.parse(in_, CSVFormat.DEFAULT) as parser:
            iterator = parser.iterator()

            self.assertTrue(iterator.hasNext())
            with self.assertRaises(NotImplementedError):
                iterator.remove()
            self.assertEqual(["a", "b", "c"], next(iterator).values())
            self.assertEqual(["1", "2", "3"], next(iterator).values())
            self.assertTrue(iterator.hasNext())
            self.assertTrue(iterator.hasNext())
            self.assertTrue(iterator.hasNext())
            self.assertEqual(["x", "y", "z"], next(iterator).values())
            self.assertFalse(iterator.hasNext())

            with self.assertRaises(RuntimeError):
                next(iterator)

    def testInvalidFormat(self) -> None:

        with pytest.raises(ValueError):
            CSVFormat.DEFAULT.withDelimiter(Constants.CR)

    def testIgnoreEmptyLines(self) -> None:

        code = "\nfoo,baar\n\r\n,\n\n,world\r\n\n"
        parser = CSVParser.parse4(code, CSVFormat.DEFAULT)
        records = parser.getRecords()
        self.assertEqual(len(records), 3)

    def testGetRecordWithMultiLineValues(self) -> None:

        try:
            parser = CSVParser.parse4(
                '"a\r\n1","a\r\n2"'
                + Constants.CRLF
                + '"b\r\n1","b\r\n2"'
                + Constants.CRLF
                + '"c\r\n1","c\r\n2"',
                CSVFormat.DEFAULT.withRecordSeparator1(Constants.CRLF),
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

    def testGetRecords(self) -> None:

        with CSVParser.parse4(
            self.__CSV_INPUT, CSVFormat.DEFAULT.withIgnoreSurroundingSpaces0()
        ) as parser:
            records = parser.getRecords()
            self.assertEqual(len(self.__RESULT), len(records))
            self.assertFalse(not records)
            for i in range(len(self.__RESULT)):
                self.assertListEqual(self.__RESULT[i], records[i].values())

    def testGetRecordPositionWithLF(self) -> None:

        self.__validateRecordPosition(Constants.LF)

    def testGetRecordPositionWithCRLF(self) -> None:

        self.__validateRecordPosition(Constants.CRLF)

    def testGetRecordNumberWithLF(self) -> None:

        try:
            self.__validateRecordNumbers(Constants.LF)
        except Exception as e:
            self.fail(f"Unexpected exception: {e}")

    def testGetRecordNumberWithCRLF(self) -> None:

        try:
            self.__validateRecordNumbers(Constants.CRLF)
        except Exception as e:
            self.fail(f"Unexpected exception: {e}")

    def testGetRecordNumberWithCR(self) -> None:

        try:
            self.__validateRecordNumbers(Constants.CR)
        except Exception as e:
            self.fail(f"Unexpected exception: {e}")

    def testGetOneLineOneParser(self) -> None:

        format_ = CSVFormat.DEFAULT
        with io.PipeWriter() as writer, CSVParser.CSVParser1(
            io.PipeReader(writer), format_
        ) as parser:
            writer.write(self.__CSV_INPUT_1.encode())
            writer.write(format_.getRecordSeparator().encode())
            record1 = parser.nextRecord()
            self.assertEqual(self.__RESULT[0], record1.values())
            writer.write(self.__CSV_INPUT_2.encode())
            writer.write(format_.getRecordSeparator().encode())
            record2 = parser.nextRecord()
            self.assertEqual(self.__RESULT[1], record2.values())

    def testGetOneLine(self) -> None:

        with CSVParser.parse4(self.__CSV_INPUT_1, CSVFormat.DEFAULT) as parser:
            record = parser.getRecords()[0]
            self.assertEqual(self.__RESULT[0], record.values())

    def testGetLineNumberWithLF(self) -> None:

        self.__validateLineNumbers(Constants.LF)

    def testGetLineNumberWithCRLF(self) -> None:

        self.__validateLineNumbers(Constants.CRLF)

    def testGetLineNumberWithCR(self) -> None:

        self.__validateLineNumbers(Constants.CR)

    def testGetLine(self) -> None:

        with CSVParser.parse4(
            self.__CSV_INPUT, CSVFormat.DEFAULT.withIgnoreSurroundingSpaces0()
        ) as parser:
            for re in self.__RESULT:
                self.assertListEqual(re, parser.nextRecord().values())

            self.assertIsNone(parser.nextRecord())

    def testForEach(self) -> None:

        try:
            in_ = io.StringIO("a,b,c\n1,2,3\nx,y,z")
            parser = CSVFormat.DEFAULT.parse(in_)
            records = []
            for record in parser:
                records.append(record)
            self.assertEqual(3, len(records))
            self.assertListEqual(["a", "b", "c"], records[0].values())
            self.assertListEqual(["1", "2", "3"], records[1].values())
            self.assertListEqual(["x", "y", "z"], records[2].values())
        finally:
            in_.close()

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
            self.assertFalse(not records)
            for i in range(len(res)):
                self.assertEqual(res[i], records[i].values())

    def testExcelFormat1(self) -> None:

        code = 'value1,value2,value3,value4\r\na,b,c,d\r\n  x,,,\r\n\r\n"""hello""","  ""world""","abc\ndef",\r\n'
        res = [
            ["value1", "value2", "value3", "value4"],
            ["a", "b", "c", "d"],
            ["  x", "", "", ""],
            [""],
            ['"hello"', '  "world"', "abc\ndef", ""],
        ]

        parser = CSVParser.parse4(code, CSVFormat.EXCEL)
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
                for i in range(len(res)):
                    self.assertEqual(res[i], records[i].values())

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
                self.assertEqual(len(res), len(records))
                self.assertFalse(not records)
                for i in range(len(res)):
                    self.assertListEqual(res[i], records[i].values())

    def testEmptyString(self) -> None:

        try:
            parser = CSVParser.parse4("", CSVFormat.DEFAULT)
            self.assertIsNone(parser.nextRecord())
        except Exception as e:
            self.fail(f"testEmptyString raised exception {e}")

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
        res = [["hello", ""]]
        for code in codes:
            with CSVParser.parse4(code, CSVFormat.DEFAULT) as parser:
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
            assert parser.nextRecord() is None
        except Exception as e:
            pytest.fail(f"Unexpected exception: {e}")

    def testDefaultFormat(self) -> None:

        code = "" + "a,b#\n" + '"\n"," ",#\n' + '#,""\n' + "# Final comment\n"
        res = [["a", "b#"], ["\n", " ", "#"], ["#", ""], ["# Final comment"]]

        format_ = CSVFormat.DEFAULT
        assert not format_.isCommentMarkerSet()
        res_comments = [
            ["a", "b#"],
            ["\n", " ", "#"],
        ]

        with CSVParser.parse4(code, format_) as parser:
            records = parser.getRecords()
            assert records

            Utils.compare("Failed to parse without comments", res, records)

            format_ = format_.withCommentMarker0("#")

        with CSVParser.parse4(code, format_) as parser:
            records = parser.getRecords()

            Utils.compare("Failed to parse with comments", res_comments, records)

    def testCSV57(self) -> None:

        try:
            parser = CSVParser.parse4("", CSVFormat.DEFAULT)
            list_ = parser.getRecords()
            self.assertIsNotNone(list_)
            self.assertEqual(0, len(list_))
        except Exception as e:
            self.fail("testCSV57 raised Exception unexpectedly: " + str(e))

    def testCSV235(self) -> None:

        dqString = '"aaa","b""bb","ccc"'  # "aaa","b""bb","ccc"
        with CSVParser.parse(io.StringIO(dqString), CSVFormat.RFC4180) as parser:
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

        path = pathlib.Path(
            "src/test/resources/org/apache/commons/csv/CSV-141/csv-141.csv"
        )
        with CSVParser.parse2(path, self.__UTF_8, CSVFormat.ORACLE) as parser:
            record = self.parse(parser, 2)
            if record is None:
                return  # expected failure
            self.assertEqual("1414770317901", record.get1(0))
            self.assertEqual("android.widget.EditText", record.get1(1))
            self.assertEqual("pass sem1 _84*|*", record.get1(2))
            self.assertEqual("0", record.get1(3))
            self.assertEqual("pass sem1 _8", record.get1(4))
            self.assertEqual(5, record.size())
            record = self.parse(parser, 2)
            if record is None:
                return  # expected failure
            self.assertEqual("1414770318470", record.get1(0))
            self.assertEqual("android.widget.EditText", record.get1(1))
            self.assertEqual("pass sem1 _84:|", record.get1(2))
            self.assertEqual("0", record.get1(3))
            self.assertEqual("pass sem1 _84:\\", record.get1(4))
            self.assertEqual(5, record.size())
            with pytest.raises(IOError):
                parser.nextRecord()

    def testCSV141CSVFormat_INFORMIX_UNLOAD_CSV(self) -> None:

        self.__testCSV141Failure(CSVFormat.INFORMIX_UNLOAD_CSV, 3)

    def testCSV141CSVFormat_INFORMIX_UNLOAD(self) -> None:

        self.__testCSV141Failure(CSVFormat.INFORMIX_UNLOAD, 1)

    def testCSV141CSVFormat_DEFAULT(self) -> None:

        self.__testCSV141Failure(CSVFormat.DEFAULT, 3)

    def testCarriageReturnLineFeedEndings(self) -> None:

        code = "foo\r\nbaar,\r\nhello,world\r\n,kanu"
        parser = CSVParser.parse4(code, CSVFormat.DEFAULT)
        records = parser.getRecords()
        self.assertEqual(len(records), 4)

    def testCarriageReturnEndings(self) -> None:

        code = "foo\rbaar,\rhello,world\r,kanu"
        try:
            parser = CSVParser.parse4(code, CSVFormat.DEFAULT)
            records = parser.getRecords()
            self.assertEqual(4, len(records))
        except Exception as e:
            self.fail("testCarriageReturnEndings failed with exception: " + str(e))

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
        parser = CSVParser.parse4(code, CSVFormat.DEFAULT)
        records = parser.getRecords()
        self.assertEqual(len(res), len(records))
        self.assertFalse(not records)
        for i in range(len(res)):
            self.assertEqual(res[i], records[i].values())

    def testBackslashEscaping2(self) -> None:

        code = "" + " , , \n" + " \t ,  , \n" + " // , /, , /,\n"  # 1)  # 2)  # 3)
        res = [
            [" ", " ", " "],  # 1
            [" \t ", "  ", " "],  # 2
            [" / ", " , ", " ,"],  # 3
        ]

        format_ = (
            CSVFormat.newFormat(",")
            .withRecordSeparator1(Constants.CRLF)
            .withEscape0("/")
            .withIgnoreEmptyLines0()
        )

        with CSVParser.parse4(code, format_) as parser:
            records = parser.getRecords()
            assert not records, "records should not be empty"

            Utils.compare("", res, records)

    def testBackslashEscaping(self) -> None:

        code = (
            "one,two,three\n"
            + "''\n"
            + "'/'\n"
            + "'/',''\n"
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
            ["   8   ", '   "quoted "" /" / string"   '],
            ["9", "   \n   "],
        ]

        format_ = (
            CSVFormat.newFormat(",")
            .withQuote0("'")
            .withRecordSeparator1(Constants.CRLF)
            .withEscape0("/")
            .withIgnoreEmptyLines0()
        )

        with CSVParser.parse4(code, format_) as parser:
            records = parser.getRecords()
            assert records, "Records are empty"

            Utils.compare("Records do not match expected result", res, records)

    def __validateRecordPosition(self, lineSeparator: str) -> None:

        nl = lineSeparator

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

        format_ = (
            CSVFormat.newFormat(",").withQuote0("'").withRecordSeparator1(lineSeparator)
        )
        parser = CSVParser.parse4(code, format_)

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
            io.StringIO(code[positionRecord3:]), format_, positionRecord3, 3
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

        try:
            parser = CSVParser.parse4(
                "a" + lineSeparator + "b" + lineSeparator + "c",
                CSVFormat.DEFAULT.withRecordSeparator1(lineSeparator),
            )
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
        except Exception as e:
            self.fail(f"Unexpected exception: {e}")

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

    def __testCSV141Ok(self, format_: CSVFormat) -> None:

        path = pathlib.Path(
            "src/test/resources/org/apache/commons/csv/CSV-141/csv-141.csv"
        )
        with CSVParser.parse2(path, self.__UTF_8, format_) as parser:
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

    def __testCSV141Failure(self, format_: CSVFormat, failParseRecordNo: int) -> None:

        path = pathlib.Path(
            "src/test/resources/org/apache/commons/csv/CSV-141/csv-141.csv"
        )
        with CSVParser.parse2(path, self.__UTF_8, format_) as parser:
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
            with pytest.raises(IOError):
                parser.nextRecord()

    def __parseFully(self, parser: CSVParser) -> None:
        parser.forEach(lambda x: self.assertIsNotNone(x))

    def parse(self, parser: CSVParser, failParseRecordNo: int) -> CSVRecord:

        try:
            if parser.getRecordNumber() + 1 == failParseRecordNo:
                with pytest.raises(IOError):
                    parser.nextRecord()
                return None
            else:
                return parser.nextRecord()
        except ValueError as ve:
            print(f"Unexpected Token type: {ve}")
            return None
