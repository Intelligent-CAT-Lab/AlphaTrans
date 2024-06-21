from __future__ import annotations
import re
import random
import unittest
import pytest
import pathlib
import io
import typing
from typing import *
import os
from src.main.org.apache.commons.csv.CSVFormat import *
from src.main.org.apache.commons.csv.CSVParser import *
from src.main.org.apache.commons.csv.CSVPrinter import *
from src.main.org.apache.commons.csv.CSVRecord import *
from src.main.org.apache.commons.csv.Constants import *
from src.main.org.apache.commons.csv.QuoteMode import *
from src.test.org.apache.commons.csv.Utils import *


class CSVPrinterTest(unittest.TestCase):

    __recordSeparator: str = CSVFormat.DEFAULT.getRecordSeparator()
    __longText2: str = ""

    __QUOTE_CH: str = "'"
    __ITERATIONS_FOR_RANDOM_TEST: int = 50000
    __EURO_CH: str = "\u20AC"
    __DQUOTE_CHAR: str = '"'

    @pytest.mark.test
    def testTrimOnTwoColumns(self) -> None:

        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.DEFAULT.withTrim0()) as printer:
            printer.print(" A ")
            printer.print(" B ")
            self.assertEqual("A,B", sw.getvalue())

    @pytest.mark.test
    def testTrimOnOneColumn(self) -> None:

        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.DEFAULT.withTrim0()) as printer:
            printer.print(" A ")
            self.assertEqual("A", sw.getvalue())

    @pytest.mark.test
    def testTrimOffOneColumn(self) -> None:

        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.DEFAULT.withTrim1(False)) as printer:
            printer.print(" A ")
            self.assertEqual('" A "', sw.getvalue())

    @pytest.mark.test
    def testTrailingDelimiterOnTwoColumns(self) -> None:

        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.DEFAULT.withTrailingDelimiter0()) as printer:
            printer.printRecord1(["A", "B"])
            self.assertEqual("A,B,\r\n", sw.getvalue())

    @pytest.mark.test
    def testSingleQuoteQuoted(self) -> None:

        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.DEFAULT.withQuote0("'")) as printer:
            printer.print("a'b'c")
            printer.print("xyz")
            self.assertEqual("'a''b''c',xyz", sw.getvalue())

    @pytest.mark.test
    def testSingleLineComment(self) -> None:

        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.DEFAULT.withCommentMarker0("#")) as printer:
            printer.printComment("This is a comment")
            self.assertEqual(
                "# This is a comment" + self.__recordSeparator, sw.getvalue()
            )

    @pytest.mark.test
    def testRandomTdf(self) -> None:

        self.__doRandom(CSVFormat.TDF, self.__ITERATIONS_FOR_RANDOM_TEST)

    @pytest.mark.test
    def testRandomRfc4180(self) -> None:

        self.__doRandom(CSVFormat.RFC4180, self.__ITERATIONS_FOR_RANDOM_TEST)

    @pytest.mark.test
    def testRandomPostgreSqlText(self) -> None:

        self.__doRandom(CSVFormat.POSTGRESQL_TEXT, self.__ITERATIONS_FOR_RANDOM_TEST)

    @pytest.mark.test
    def testRandomPostgreSqlCsv(self) -> None:

        self.__doRandom(CSVFormat.POSTGRESQL_CSV, self.__ITERATIONS_FOR_RANDOM_TEST)

    @pytest.mark.test
    def testRandomOracle(self) -> None:

        self.__doRandom(CSVFormat.ORACLE, self.__ITERATIONS_FOR_RANDOM_TEST)

    @pytest.mark.test
    def testRandomMySql(self) -> None:

        self.__doRandom(CSVFormat.MYSQL, self.__ITERATIONS_FOR_RANDOM_TEST)

    @pytest.mark.test
    def testRandomMongoDbCsv(self) -> None:

        self.__doRandom(CSVFormat.MONGODB_CSV, self.__ITERATIONS_FOR_RANDOM_TEST)

    @pytest.mark.test
    def testRandomExcel(self) -> None:

        self.__doRandom(CSVFormat.EXCEL, self.__ITERATIONS_FOR_RANDOM_TEST)

    @pytest.mark.test
    def testRandomDefault(self) -> None:

        self.__doRandom(CSVFormat.DEFAULT, self.__ITERATIONS_FOR_RANDOM_TEST)

    @pytest.mark.test
    def testQuoteNonNumeric(self) -> None:

        sw = io.StringIO()
        with CSVPrinter(
            sw, CSVFormat.DEFAULT.withQuoteMode(QuoteMode.NON_NUMERIC)
        ) as printer:
            printer.printRecord1(["a", "b\nc", 1])
            self.assertEqual('"a","b\nc",1' + self.__recordSeparator, sw.getvalue())

    @pytest.mark.test
    def testQuoteCommaFirstChar(self) -> None:

        sw = io.StringIO()
        try:
            printer = CSVPrinter(sw, CSVFormat.RFC4180)
            printer.printRecord1([","])
            self.assertEqual('","\n', sw.getvalue())
        finally:
            sw.close()

    @pytest.mark.test
    def testQuoteAll(self) -> None:

        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.DEFAULT.withQuoteMode(QuoteMode.ALL)) as printer:
            printer.printRecord1(["a", "b\nc", "d"])
            self.assertEqual('"a","b\nc","d"' + self.__recordSeparator, sw.getvalue())

    @pytest.mark.test
    def testPrintToPathWithDefaultCharset(self) -> None:

        file = self.__createTempPath()
        with CSVFormat.DEFAULT.print4(file, "utf-8") as printer:
            printer.printRecord1("a", "b\\c")

        with open(file, "r", encoding="utf-8") as f:
            self.assertEqual("a,b\\c" + self.__recordSeparator, f.read())

    @pytest.mark.test
    def testPrintRecordStream(self) -> None:

        code = "a1,b1\n" + "a2,b2\n" + "a3,b3\n" + "a4,b4\n"
        res = [["a1", "b1"], ["a2", "b2"], ["a3", "b3"], ["a4", "b4"]]
        format = CSVFormat.DEFAULT
        sw = io.StringIO()
        try:
            printer = format.print0(sw)
            parser = CSVParser.parse4(code, format)
            for record in parser:
                printer.printRecord2(record.stream())
        finally:
            parser.close()
            printer.close()

        try:
            parser = CSVParser.parse4(sw.getvalue(), format)
            records = parser.getRecords()
            assert not records == [], "Fail"
            Utils.compare("Fail", res, records)
        finally:
            parser.close()

    @pytest.mark.test
    def testPrintReaderWithoutQuoteToWriter(self) -> None:

        sw = io.StringIO()
        content = "testValue"
        with CSVPrinter(sw, CSVFormat.DEFAULT.withQuote1(None)) as printer:
            value = io.StringIO(content)
            printer.print(value)
        self.assertEqual(content, sw.getvalue())

    @pytest.mark.test
    def testPrintReaderWithoutQuoteToAppendable(self) -> None:

        sb = io.StringIO()
        content = "testValue"
        with CSVPrinter(sb, CSVFormat.DEFAULT.withQuote1(None)) as printer:
            value = io.StringIO(content)
            printer.print(value)

        self.assertEqual(content, sb.getvalue())

    @pytest.mark.test
    def testPrintOnePositiveInteger(self) -> None:

        sw = io.StringIO()
        with CSVPrinter(
            sw, CSVFormat.DEFAULT.withQuoteMode(QuoteMode.MINIMAL)
        ) as printer:
            printer.print(Integer.MAX_VALUE)
            self.assertEqual(str(Integer.MAX_VALUE), sw.getvalue())

    @pytest.mark.test
    def testPrintNullValues(self) -> None:

        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.DEFAULT) as printer:
            printer.printRecord1(["a", None, "b"])
            self.assertEqual("a,,b" + self.__recordSeparator, sw.getvalue())

    @pytest.mark.test
    def testPrinter7(self) -> None:

        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.DEFAULT) as printer:
            printer.printRecord1(["a", "b\\c"])
            self.assertEqual("a,b\\c" + self.__recordSeparator, sw.getvalue())

    @pytest.mark.test
    def testPrinter6(self) -> None:

        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.DEFAULT) as printer:
            printer.printRecord1(["a", "b\r\nc"])
            self.assertEqual('a,"b\r\nc"' + self.__recordSeparator, sw.getvalue())

    @pytest.mark.test
    def testPrinter5(self) -> None:

        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.DEFAULT) as printer:
            printer.printRecord1(["a", "b\nc"])
            self.assertEqual('a,"b\nc"' + self.__recordSeparator, sw.getvalue())

    @pytest.mark.test
    def testPrinter4(self) -> None:

        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.DEFAULT) as printer:
            printer.printRecord1(["a", 'b"c'])
            self.assertEqual('a,"b""c"' + self.__recordSeparator, sw.getvalue())

    @pytest.mark.test
    def testPrinter3(self) -> None:

        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.DEFAULT) as printer:
            printer.printRecord1(["a, b", "b "])
            self.assertEqual('"a, b","b "\n', sw.getvalue())

    @pytest.mark.test
    def testPrinter2(self) -> None:

        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.DEFAULT) as printer:
            printer.printRecord1(["a,b", "b"])
            self.assertEqual('"a,b",b' + self.__recordSeparator, sw.getvalue())

    @pytest.mark.test
    def testPrinter1(self) -> None:

        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.DEFAULT) as printer:
            printer.printRecord1(["a", "b"])
            self.assertEqual("a,b" + self.__recordSeparator, sw.getvalue())

    @pytest.mark.test
    def testPrintCustomNullValues(self) -> None:

        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.DEFAULT.withNullString("NULL")) as printer:
            printer.printRecord1(["a", None, "b"])
            self.assertEqual("a,NULL,b" + self.__recordSeparator, sw.getvalue())

    @pytest.mark.test
    def testPrintCSVRecords(self) -> None:

        code = "a1,b1\n" + "a2,b2\n" + "a3,b3\n" + "a4,b4\n"
        res = [["a1", "b1"], ["a2", "b2"], ["a3", "b3"], ["a4", "b4"]]
        format = CSVFormat.DEFAULT
        sw = io.StringIO()
        try:
            printer = format.print0(sw)
            parser = CSVParser.parse4(code, format)
            printer.printRecords0(parser.getRecords())
        finally:
            parser = CSVParser.parse4(sw.getvalue(), format)
            records = parser.getRecords()
            self.assertFalse(records)
            Utils.compare("Fail", res, records)

    @pytest.mark.test
    def testPrintCSVRecord(self) -> None:

        code = "a1,b1\n" + "a2,b2\n" + "a3,b3\n" + "a4,b4\n"
        res = [["a1", "b1"], ["a2", "b2"], ["a3", "b3"], ["a4", "b4"]]
        format = CSVFormat.DEFAULT
        sw = io.StringIO()
        try:
            printer = format.print0(sw)
            parser = CSVParser.parse4(code, format)
            for record in parser:
                printer.printRecord0(record)
        finally:
            sw.seek(0)
            parser = CSVParser.parse4(sw.getvalue(), format)
            records = parser.getRecords()
            assert not records == [], "Fail"
            Utils.compare("Fail", res, records)

    @pytest.mark.test
    def testPrintCSVParser(self) -> None:

        code = "a1,b1\n" + "a2,b2\n" + "a3,b3\n" + "a4,b4\n"
        res = [["a1", "b1"], ["a2", "b2"], ["a3", "b3"], ["a4", "b4"]]
        format = CSVFormat.DEFAULT
        sw = io.StringIO()
        try:
            printer = format.print0(sw)
            parser = CSVParser.parse4(code, format)
            printer.printRecords0(parser)
        finally:
            sw.seek(0)
            parser = CSVParser.parse4(sw.getvalue(), format)
            records = parser.getRecords()
            self.assertFalse(records == [], "Fail")
            Utils.compare("Fail", res, records)

    @pytest.mark.test
    def testPrint(self) -> None:

        sw = io.StringIO()
        with CSVFormat.DEFAULT.print0(sw) as printer:
            printer.printRecord1("a", "b\\c")
            self.assertEqual(
                "a,b\\c" + CSVFormat.DEFAULT.getRecordSeparator(), sw.getvalue()
            )

    @pytest.mark.test
    def testPostgreSqlNullStringDefaultText(self) -> None:
        self.assertEqual("\\N", CSVFormat.POSTGRESQL_TEXT.getNullString())

    @pytest.mark.test
    def testPostgreSqlNullStringDefaultCsv(self) -> None:
        self.assertEqual("", CSVFormat.POSTGRESQL_CSV.getNullString())

    @pytest.mark.test
    def testPostgreSqlCsvTextOutput(self) -> None:

        s = ["NULL", None]
        format = (
            CSVFormat.POSTGRESQL_TEXT.withQuote0(self.__DQUOTE_CHAR)
            .withNullString("NULL")
            .withQuoteMode(QuoteMode.ALL_NON_NULL)
        )
        writer = io.StringIO()
        with CSVPrinter(writer, format) as printer:
            printer.printRecord1(s)
        expected = '"NULL"\tNULL\n'
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format)
        self.assertListEqual([None, None], record0)

        s = ["\\N", None]
        format = CSVFormat.POSTGRESQL_TEXT.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format) as printer:
            printer.printRecord1(s)
        expected = "\\\\N\t\\N\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format)
        self.assertListEqual(self.__expectNulls(s, format), record0)

        s = ["\\N", "A"]
        format = CSVFormat.POSTGRESQL_TEXT.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format) as printer:
            printer.printRecord1(s)
        expected = "\\\\N\tA\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format)
        self.assertListEqual(self.__expectNulls(s, format), record0)

        s = ["\n", "A"]
        format = CSVFormat.POSTGRESQL_TEXT.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format) as printer:
            printer.printRecord1(s)
        expected = "\\n\tA\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format)
        self.assertListEqual(self.__expectNulls(s, format), record0)

        s = ["", None]
        format = CSVFormat.POSTGRESQL_TEXT.withNullString("NULL")
        writer = io.StringIO()
        with CSVPrinter(writer, format) as printer:
            printer.printRecord1(s)
        expected = "\tNULL\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format)
        self.assertListEqual(self.__expectNulls(s, format), record0)

        s = ["", None]
        format = CSVFormat.POSTGRESQL_TEXT
        writer = io.StringIO()
        with CSVPrinter(writer, format) as printer:
            printer.printRecord1(s)
        expected = "\t\\N\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format)
        self.assertListEqual(self.__expectNulls(s, format), record0)

        s = ["\\N", "", "\u000e,\\\r"]
        format = CSVFormat.POSTGRESQL_TEXT
        writer = io.StringIO()
        with CSVPrinter(writer, format) as printer:
            printer.printRecord1(s)
        expected = "\\\\N\t\t\u000e,\\\\\\r\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format)
        self.assertListEqual(self.__expectNulls(s, format), record0)

        s = ["NULL", "\\\r"]
        format = CSVFormat.POSTGRESQL_TEXT
        writer = io.StringIO()
        with CSVPrinter(writer, format) as printer:
            printer.printRecord1(s)
        expected = "NULL\t\\\\\\r\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format)
        self.assertListEqual(self.__expectNulls(s, format), record0)

        s = ["\\\r"]
        format = CSVFormat.POSTGRESQL_TEXT
        writer = io.StringIO()
        with CSVPrinter(writer, format) as printer:
            printer.printRecord1(s)
        expected = "\\\\\\r\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format)
        self.assertListEqual(self.__expectNulls(s, format), record0)

    @pytest.mark.test
    def testPostgreSqlCsvNullOutput(self) -> None:

        s = ["NULL", None]
        format = (
            CSVFormat.POSTGRESQL_CSV.withQuote0(self.__DQUOTE_CHAR)
            .withNullString("NULL")
            .withQuoteMode(QuoteMode.ALL_NON_NULL)
        )
        writer = io.StringIO()
        with CSVPrinter(writer, format) as printer:
            printer.printRecord1(s)
        expected = '"NULL",NULL\n'
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format)
        self.assertListEqual([None, None], record0)

        s = ["\\N", None]
        format = CSVFormat.POSTGRESQL_CSV.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format) as printer:
            printer.printRecord1(s)
        expected = "\\\\N\t\\N\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format)
        self.assertListEqual(self.__expectNulls(s, format), record0)

        s = ["\\N", "A"]
        format = CSVFormat.POSTGRESQL_CSV.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format) as printer:
            printer.printRecord1(s)
        expected = "\\\\N\tA\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format)
        self.assertListEqual(self.__expectNulls(s, format), record0)

        s = ["\n", "A"]
        format = CSVFormat.POSTGRESQL_CSV.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format) as printer:
            printer.printRecord1(s)
        expected = "\\n\tA\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format)
        self.assertListEqual(self.__expectNulls(s, format), record0)

        s = ["", None]
        format = CSVFormat.POSTGRESQL_CSV.withNullString("NULL")
        writer = io.StringIO()
        with CSVPrinter(writer, format) as printer:
            printer.printRecord1(s)
        expected = "\tNULL\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format)
        self.assertListEqual(self.__expectNulls(s, format), record0)

        s = ["", None]
        format = CSVFormat.POSTGRESQL_CSV
        writer = io.StringIO()
        with CSVPrinter(writer, format) as printer:
            printer.printRecord1(s)
        expected = "\t\\N\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format)
        self.assertListEqual(self.__expectNulls(s, format), record0)

        s = ["\\N", "", "\u000e,\\\r"]
        format = CSVFormat.POSTGRESQL_CSV
        writer = io.StringIO()
        with CSVPrinter(writer, format) as printer:
            printer.printRecord1(s)
        expected = "\\\\N\t\t\u000e,\\\\\\r\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format)
        self.assertListEqual(self.__expectNulls(s, format), record0)

        s = ["NULL", "\\\r"]
        format = CSVFormat.POSTGRESQL_CSV
        writer = io.StringIO()
        with CSVPrinter(writer, format) as printer:
            printer.printRecord1(s)
        expected = "NULL\t\\\\\\r\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format)
        self.assertListEqual(self.__expectNulls(s, format), record0)

        s = ["\\\r"]
        format = CSVFormat.POSTGRESQL_CSV
        writer = io.StringIO()
        with CSVPrinter(writer, format) as printer:
            printer.printRecord1(s)
        expected = "\\\\\\r\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format)
        self.assertListEqual(self.__expectNulls(s, format), record0)

    @pytest.mark.test
    def testPlainQuoted(self) -> None:

        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.DEFAULT.withQuote0("'")) as printer:
            printer.print("abc")
            self.assertEqual("abc", sw.getvalue())

    @pytest.mark.test
    def testPlainPlain(self) -> None:

        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.DEFAULT.withQuote1(None)) as printer:
            printer.print("abc")
            printer.print("xyz")
            self.assertEqual("abc,xyz", sw.getvalue())

    @pytest.mark.test
    def testPlainEscaped(self) -> None:

        sw = io.StringIO()
        with CSVPrinter(
            sw, CSVFormat.DEFAULT.withQuote1(None).withEscape0("!")
        ) as printer:
            printer.print("abc")
            printer.print("xyz")
            self.assertEqual("abc,xyz", sw.getvalue())

    @pytest.mark.test
    def testParseCustomNullValues(self) -> None:

        sw = io.StringIO()
        format = CSVFormat.DEFAULT.withNullString("NULL")
        try:
            printer = CSVPrinter(sw, format)
            printer.printRecord1(["a", None, "b"])
        finally:
            csvString = sw.getvalue()
            self.assertEqual("a,NULL,b" + format.getRecordSeparator(), csvString)
            try:
                iterable = format.parse(io.StringIO(csvString))
                iterator = iter(iterable)
                record = next(iterator)
                self.assertEqual("a", record.get1(0))
                self.assertIsNone(record.get1(1))
                self.assertEqual("b", record.get1(2))
                self.assertFalse(iterator.hasNext())
            finally:
                iterable.close()

    @pytest.mark.test
    def testNotFlushable(self) -> None:

        out = io.StringIO()
        with CSVPrinter(out, CSVFormat.DEFAULT) as printer:
            printer.printRecord1(["a", "b", "c"])
            self.assertEqual("a,b,c" + self.__recordSeparator, out.getvalue())
            printer.flush()

    @pytest.mark.test
    def testNewCsvPrinterNullAppendableFormat(self) -> None:
        with pytest.raises(NullPointerException):
            CSVPrinter(None, CSVFormat.DEFAULT)

    @pytest.mark.test
    def testNewCsvPrinterAppendableNullFormat(self) -> None:

        with pytest.raises(TypeError):
            CSVPrinter(io.StringIO(), None)

    @pytest.mark.test
    def testMySqlNullStringDefault(self) -> None:
        self.assertEqual("\\N", CSVFormat.MYSQL.getNullString())

    @pytest.mark.test
    def testMySqlNullOutput(self) -> None:

        s = ["NULL", None]
        format = (
            CSVFormat.MYSQL.withQuote0(self.__DQUOTE_CHAR)
            .withNullString("NULL")
            .withQuoteMode(QuoteMode.NON_NUMERIC)
        )
        writer = io.StringIO()
        with CSVPrinter(writer, format) as printer:
            printer.printRecord1(s)
        expected = '"NULL"\tNULL\n'
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format)
        self.assertListEqual(s, record0)

        s = ["\\N", None]
        format = CSVFormat.MYSQL.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format) as printer:
            printer.printRecord1(s)
        expected = "\\\\N\t\\N\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format)
        self.assertListEqual(self.__expectNulls(s, format), record0)

        s = ["\\N", "A"]
        format = CSVFormat.MYSQL.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format) as printer:
            printer.printRecord1(s)
        expected = "\\\\N\tA\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format)
        self.assertListEqual(self.__expectNulls(s, format), record0)

        s = ["\n", "A"]
        format = CSVFormat.MYSQL.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format) as printer:
            printer.printRecord1(s)
        expected = "\\n\tA\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format)
        self.assertListEqual(self.__expectNulls(s, format), record0)

        s = ["", None]
        format = CSVFormat.MYSQL.withNullString("NULL")
        writer = io.StringIO()
        with CSVPrinter(writer, format) as printer:
            printer.printRecord1(s)
        expected = "\tNULL\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format)
        self.assertListEqual(self.__expectNulls(s, format), record0)

        s = ["", None]
        format = CSVFormat.MYSQL
        writer = io.StringIO()
        with CSVPrinter(writer, format) as printer:
            printer.printRecord1(s)
        expected = "\t\\N\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format)
        self.assertListEqual(self.__expectNulls(s, format), record0)

        s = ["\\N", "", "\u000e,\\\r"]
        format = CSVFormat.MYSQL
        writer = io.StringIO()
        with CSVPrinter(writer, format) as printer:
            printer.printRecord1(s)
        expected = "\\\\N\t\t\u000e,\\\\\\r\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format)
        self.assertListEqual(self.__expectNulls(s, format), record0)

        s = ["NULL", "\\\r"]
        format = CSVFormat.MYSQL
        writer = io.StringIO()
        with CSVPrinter(writer, format) as printer:
            printer.printRecord1(s)
        expected = "NULL\t\\\\\\r\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format)
        self.assertListEqual(self.__expectNulls(s, format), record0)

        s = ["\\\r"]
        format = CSVFormat.MYSQL
        writer = io.StringIO()
        with CSVPrinter(writer, format) as printer:
            printer.printRecord1(s)
        expected = "\\\\\\r\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format)
        self.assertListEqual(self.__expectNulls(s, format), record0)

    @pytest.mark.test
    def testMultiLineComment(self) -> None:

        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.DEFAULT.withCommentMarker0("#")) as printer:
            printer.printComment("This is a comment\non multiple lines")

            self.assertEqual(
                "# This is a comment"
                + self.__recordSeparator
                + "# on multiple lines"
                + self.__recordSeparator,
                sw.getvalue(),
            )

    @pytest.mark.test
    def testMongoDbTsvTabInValue(self) -> None:

        sw = io.StringIO()
        try:
            printer = CSVPrinter(sw, CSVFormat.MONGODB_TSV)
            printer.printRecord1(["a\tb", "c"])
            self.assertEqual('"a\tb"\tc' + self.__recordSeparator, sw.getvalue())
        finally:
            sw.close()

    @pytest.mark.test
    def testMongoDbTsvCommaInValue(self) -> None:

        sw = io.StringIO()
        try:
            printer = CSVPrinter(sw, CSVFormat.MONGODB_TSV)
            printer.printRecord1(["a,b", "c"])
            self.assertEqual("a,b\tc" + self.__recordSeparator, sw.getvalue())
        finally:
            sw.close()

    @pytest.mark.test
    def testMongoDbTsvBasic(self) -> None:

        sw = io.StringIO()
        try:
            printer = CSVPrinter(sw, CSVFormat.MONGODB_TSV)
            printer.printRecord1(["a", "b"])
            self.assertEqual("a\tb" + self.__recordSeparator, sw.getvalue())
        finally:
            sw.close()

    @pytest.mark.test
    def testMongoDbCsvTabInValue(self) -> None:

        sw = io.StringIO()
        try:
            printer = CSVPrinter(sw, CSVFormat.MONGODB_CSV)
            printer.printRecord1(["a\tb", "c"])
            self.assertEqual("a\tb,c" + self.__recordSeparator, sw.getvalue())
        finally:
            sw.close()

    @pytest.mark.test
    def testMongoDbCsvDoubleQuoteInValue(self) -> None:

        sw = io.StringIO()
        try:
            printer = CSVPrinter(sw, CSVFormat.MONGODB_CSV)
            printer.printRecord1(['a "c" b', "d"])
            self.assertEqual('"a ""c"" b",d' + self.__recordSeparator, sw.getvalue())
        finally:
            sw.close()

    @pytest.mark.test
    def testMongoDbCsvCommaInValue(self) -> None:

        sw = io.StringIO()
        try:
            printer = CSVPrinter(sw, CSVFormat.MONGODB_CSV)
            printer.printRecord1(["a,b", "c"])
            self.assertEqual('"a,b",c' + self.__recordSeparator, sw.getvalue())
        finally:
            sw.close()

    @pytest.mark.test
    def testMongoDbCsvBasic(self) -> None:

        sw = io.StringIO()
        try:
            printer = CSVPrinter(sw, CSVFormat.MONGODB_CSV)
            printer.printRecord1(["a", "b"])
            self.assertEqual("a,b" + self.__recordSeparator, sw.getvalue())
        finally:
            sw.close()

    @pytest.mark.test
    def testJira135All(self) -> None:

        format = (
            CSVFormat.DEFAULT.withRecordSeparator0("\n")
            .withQuote0(self.__DQUOTE_CHAR)
            .withEscape0(BACKSLASH)
        )
        sw = io.StringIO()
        list = []
        try:
            printer = CSVPrinter(sw, format)
            list.append('"')
            list.append("\n")
            list.append("\\")
            printer.printRecord0(list)
        except Exception as e:
            print(f"An error occurred: {e}")

        expected = '"\\"","\\n","\\"' + format.getRecordSeparator()
        self.assertEqual(expected, sw.getvalue())
        record0 = self.__toFirstRecordValues(expected, format)
        self.assertListEqual(self.__expectNulls(list, format), record0)

    @pytest.mark.test
    def testJira135_part3(self) -> None:

        format = (
            CSVFormat.DEFAULT.withRecordSeparator0("\n")
            .withQuote0(self.__DQUOTE_CHAR)
            .withEscape0(BACKSLASH)
        )
        sw = io.StringIO()
        list = []
        try:
            printer = CSVPrinter(sw, format)
            list.append("\\")
            printer.printRecord0(list)
        finally:
            expected = '"\\\\"' + format.getRecordSeparator()
            self.assertEqual(expected, sw.getvalue())
            record0 = self.__toFirstRecordValues(expected, format)
            self.assertListEqual(self.__expectNulls(list, format), record0)

    @pytest.mark.test
    def testJira135_part2(self) -> None:

        format = (
            CSVFormat.DEFAULT.withRecordSeparator0("\n")
            .withQuote0(self.__DQUOTE_CHAR)
            .withEscape0(BACKSLASH)
        )
        sw = io.StringIO()
        list = []
        try:
            printer = CSVPrinter(sw, format)
            list.append("\n")
            printer.printRecord0(list)
        finally:
            expected = '"\\n"' + format.getRecordSeparator()
            self.assertEqual(expected, sw.getvalue())
            record0 = self.__toFirstRecordValues(expected, format)
            self.assertListEqual(self.__expectNulls(list, format), record0)

    @pytest.mark.test
    def testJira135_part1(self) -> None:

        format = (
            CSVFormat.DEFAULT.withRecordSeparator0("\n")
            .withQuote0(self.__DQUOTE_CHAR)
            .withEscape0(BACKSLASH)
        )
        sw = io.StringIO()
        list = []
        try:
            printer = CSVPrinter(sw, format)
            list.append('"')
            printer.printRecord0(list)
        finally:
            expected = '"\\""' + format.getRecordSeparator()
            self.assertEqual(expected, sw.getvalue())
            record0 = self.__toFirstRecordValues(expected, format)
            self.assertListEqual(self.__expectNulls(list, format), record0)

    @pytest.mark.test
    def testInvalidFormat(self) -> None:
        with pytest.raises(ValueError):
            CSVFormat.DEFAULT.withDelimiter(CR)

    @pytest.mark.test
    def testHeaderNotSet(self) -> None:

        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.DEFAULT.withQuote1(None)) as printer:
            printer.printRecord1(["a", "b", "c"])
            printer.printRecord1(["x", "y", "z"])
            self.assertEqual("a,b,c\r\nx,y,z\r\n", sw.getvalue())

    @pytest.mark.test
    def testExcelPrinter2(self) -> None:

        sw = io.StringIO()
        try:
            printer = CSVPrinter(sw, CSVFormat.EXCEL)
            printer.printRecord1(["a,b", "b"])
            self.assertEqual('"a,b",b' + self.__recordSeparator, sw.getvalue())
        finally:
            sw.close()

    @pytest.mark.test
    def testExcelPrinter1(self) -> None:

        sw = io.StringIO()
        try:
            printer = CSVPrinter(sw, CSVFormat.EXCEL)
            printer.printRecord1(["a", "b"])
            self.assertEqual("a,b" + self.__recordSeparator, sw.getvalue())
        finally:
            sw.close()

    @pytest.mark.test
    def testExcelPrintAllIterableOfLists(self) -> None:

        sw = io.StringIO()
        try:
            printer = CSVPrinter(sw, CSVFormat.EXCEL)
            printer.printRecords0([["r1c1", "r1c2"], ["r2c1", "r2c2"]])
            self.assertEqual(
                "r1c1,r1c2"
                + self.__recordSeparator
                + "r2c1,r2c2"
                + self.__recordSeparator,
                sw.getvalue(),
            )
        finally:
            sw.close()

    @pytest.mark.test
    def testExcelPrintAllIterableOfArrays(self) -> None:

        sw = io.StringIO()
        try:
            printer = CSVPrinter(sw, CSVFormat.EXCEL)
            printer.printRecords0([["r1c1", "r1c2"], ["r2c1", "r2c2"]])
            self.assertEqual(
                "r1c1,r1c2"
                + self.__recordSeparator
                + "r2c1,r2c2"
                + self.__recordSeparator,
                sw.getvalue(),
            )
        finally:
            sw.close()

    @pytest.mark.test
    def testExcelPrintAllArrayOfLists(self) -> None:

        sw = io.StringIO()
        try:
            printer = CSVPrinter(sw, CSVFormat.EXCEL)
            printer.printRecords1([["r1c1", "r1c2"], ["r2c1", "r2c2"]])
            self.assertEqual(
                "r1c1,r1c2"
                + self.__recordSeparator
                + "r2c1,r2c2"
                + self.__recordSeparator,
                sw.getvalue(),
            )
        finally:
            sw.close()

    @pytest.mark.test
    def testExcelPrintAllArrayOfArrays(self) -> None:

        sw = io.StringIO()
        try:
            printer = CSVPrinter(sw, CSVFormat.EXCEL)
            printer.printRecords1([["r1c1", "r1c2"], ["r2c1", "r2c2"]])
            self.assertEqual(
                "r1c1,r1c2"
                + self.__recordSeparator
                + "r2c1,r2c2"
                + self.__recordSeparator,
                sw.getvalue(),
            )
        finally:
            sw.close()

    @pytest.mark.test
    def testEscapeNull5(self) -> None:

        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.DEFAULT.withEscape1(None)) as printer:
            printer.print("\\\\")

        self.assertEqual("\\\\", sw.getvalue())

    @pytest.mark.test
    def testEscapeNull4(self) -> None:

        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.DEFAULT.withEscape1(None)) as printer:
            printer.print("\\\\")

        self.assertEqual("\\\\", sw.getvalue())

    @pytest.mark.test
    def testEscapeNull3(self) -> None:

        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.DEFAULT.withEscape1(None)) as printer:
            printer.print("X\\\r")

        self.assertEqual('"X\\\r"', sw.getvalue())

    @pytest.mark.test
    def testEscapeNull2(self) -> None:

        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.DEFAULT.withEscape1(None)) as printer:
            printer.print("\\\r")

        self.assertEqual('"\\\r"', sw.getvalue())

    @pytest.mark.test
    def testEscapeNull1(self) -> None:

        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.DEFAULT.withEscape1(None)) as printer:
            printer.print("\\")

        self.assertEqual("\\", sw.getvalue())

    @pytest.mark.test
    def testEscapeBackslash5(self) -> None:

        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.DEFAULT.withQuote0(self.__QUOTE_CH)) as printer:
            printer.print("\\\\")

        self.assertEqual("\\\\", sw.getvalue())

    @pytest.mark.test
    def testEscapeBackslash4(self) -> None:

        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.DEFAULT.withQuote0(self.__QUOTE_CH)) as printer:
            printer.print("\\\\")

        self.assertEqual("\\\\", sw.getvalue())

    @pytest.mark.test
    def testEscapeBackslash3(self) -> None:

        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.DEFAULT.withQuote0(self.__QUOTE_CH)) as printer:
            printer.print("X\\\r")

        self.assertEqual("'X\\\r'", sw.getvalue())

    @pytest.mark.test
    def testEscapeBackslash2(self) -> None:

        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.DEFAULT.withQuote0(self.__QUOTE_CH)) as printer:
            printer.print("\\\r")

        self.assertEqual("'\\\r'", sw.getvalue())

    @pytest.mark.test
    def testEscapeBackslash1(self) -> None:

        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.DEFAULT.withQuote0(self.__QUOTE_CH)) as printer:
            printer.print("\\")

        self.assertEqual("\\", sw.getvalue())

    @pytest.mark.test
    def testEolQuoted(self) -> None:

        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.DEFAULT.withQuote0("'")) as printer:
            printer.print("a\rb\nc")
            printer.print("x\by\fz")
            self.assertEqual("'a\rb\nc',x\by\fz", sw.getvalue())

    @pytest.mark.test
    def testEolPlain(self) -> None:

        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.DEFAULT.withQuote1(None)) as printer:
            printer.print("a\rb\nc")
            printer.print("x\fy\bz")
            self.assertEqual("a\rb\nc,x\fy\bz", sw.getvalue())

    @pytest.mark.test
    def testEolEscaped(self) -> None:

        sw = io.StringIO()
        with CSVPrinter(
            sw, CSVFormat.DEFAULT.withQuote1(None).withEscape0("!")
        ) as printer:
            printer.print("a\rb\nc")
            printer.print("x\fy\bz")
            self.assertEqual("a\rb\nc,x\fy\bz", sw.getvalue())

    @pytest.mark.test
    def testDontQuoteEuroFirstChar(self) -> None:

        sw = io.StringIO()
        try:
            printer = CSVPrinter(sw, CSVFormat.RFC4180)
            printer.printRecord1([self.__EURO_CH, "Deux"])
            self.assertEqual(
                self.__EURO_CH + ",Deux" + self.__recordSeparator, sw.getvalue()
            )
        finally:
            sw.close()

    @pytest.mark.test
    def testDisabledComment(self) -> None:

        sw = io.StringIO()
        try:
            printer = CSVPrinter(sw, CSVFormat.DEFAULT)
            printer.printComment("This is a comment")
            self.assertEqual("", sw.getvalue())
        finally:
            sw.close()

    @pytest.mark.test
    def testDelimiterStringEscaped(self) -> None:

        sw = io.StringIO()
        with CSVPrinter(
            sw,
            CSVFormat.DEFAULT.builder()
            .setDelimiter1("|||")
            .setEscape0("1")
            .setQuote1(None)
            .build(),
        ) as printer:
            printer.print("a|||b|||c")
            printer.print("xyz")
            self.assertEqual("a1|1|1|b1|1|1|c|||xyz", sw.getvalue())

    @pytest.mark.test
    def testDelimiterPlain(self) -> None:

        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.DEFAULT.withQuote1(None)) as printer:
            printer.print("a,b,c")
            printer.print("xyz")
            self.assertEqual("a,b,c,xyz", sw.getvalue())

    @pytest.mark.test
    def testDelimiterEscaped(self) -> None:

        sw = io.StringIO()
        with CSVPrinter(
            sw, CSVFormat.DEFAULT.withEscape0("0").withQuote1(None)
        ) as printer:
            printer.print("a,b,c")
            printer.print("xyz")
            self.assertEqual("a0,b0,c,xyz", sw.getvalue())

    @pytest.mark.test
    def testDelimeterStringQuoteNone(self) -> None:

        sw = io.StringIO()
        format = (
            CSVFormat.DEFAULT.builder()
            .setDelimiter1("[|]")
            .setEscape0("[!]")
            .setQuoteMode(QuoteMode.NONE)
            .build()
        )
        with CSVPrinter(sw, format) as printer:
            printer.print("a[|]b[|]c")
            printer.print("xyz")
            printer.print("a[xy]bc[]")
        self.assertEqual("a[!]![|!]b[!]![|!]c[|]xyz[|]a[xy]bc[]", sw.getvalue())

    @pytest.mark.test
    def testDelimeterStringQuoted(self) -> None:

        sw = io.StringIO()
        with CSVPrinter(
            sw, CSVFormat.DEFAULT.builder().setDelimiter1("[|]").setQuote0("'").build()
        ) as printer:
            printer.print("a[|]b[|]c")
            printer.print("xyz")
            self.assertEqual("'a[|]b[|]c'[|]xyz", sw.getvalue())

    @pytest.mark.test
    def testDelimeterQuoteNone(self) -> None:

        sw = io.StringIO()
        format = CSVFormat.DEFAULT.withEscape0("0").withQuoteMode(QuoteMode.NONE)
        with CSVPrinter(sw, format) as printer:
            printer.print("a,b,c")
            printer.print("xyz")
        self.assertEqual("a0,b0,c,xyz", sw.getvalue())

    @pytest.mark.test
    def testDelimeterQuoted(self) -> None:

        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.DEFAULT.withQuote0("'")) as printer:
            printer.print("a,b,c")
            printer.print("xyz")
            self.assertEqual("'a,b,c',xyz", sw.getvalue())

    @pytest.mark.test
    def testCSV259(self) -> None:

        sw = io.StringIO()
        try:
            reader = open(
                "src/test/resources/org/apache/commons/csv/CSV-259/sample.txt", "r"
            )
            format = CSVFormat.DEFAULT.withEscape0("0").withQuote1(None)
            printer = CSVPrinter(sw, format)
            printer.print(reader)
            self.assertEqual("x0,y0,z", sw.getvalue())
        finally:
            reader.close()

    @pytest.mark.test
    def testCSV135(self) -> None:

        list = ['""', "\\\\", '\\"\\']
        self.__tryFormat(list, None, None, '"""",\\\\,\\"\\"')
        self.__tryFormat(list, '"', None, '"""""",\\\\,"\\""\\"')
        self.__tryFormat(list, None, "\\", '"",\\\\\\\\,\\\\"\\\\"')
        self.__tryFormat(
            list, '"', "\\", '"\\"\\"\\"",\\\\\\\\\\\\","\\\\\\"\\\\\\"\\"'
        )
        self.__tryFormat(list, '"', '"', '""""""",\\\\,"\\""\\"')

    @pytest.mark.test
    def testCRComment(self) -> None:

        sw = io.StringIO()
        value = "abc"
        with CSVPrinter(sw, CSVFormat.DEFAULT.withCommentMarker0("#")) as printer:
            printer.print(value)
            printer.printComment(
                "This is a comment\r\non multiple lines\rthis is next comment\r"
            )
            self.assertEqual(
                "abc"
                + self.__recordSeparator
                + "# This is a comment"
                + self.__recordSeparator
                + "# on multiple lines"
                + self.__recordSeparator
                + "# this is next comment"
                + self.__recordSeparator
                + "# "
                + self.__recordSeparator,
                sw.getvalue(),
            )

    def __tryFormat(
        self, list: typing.List[str], quote: str, escape: str, expected: str
    ) -> None:

        format = (
            CSVFormat.DEFAULT.withQuote1(quote)
            .withEscape1(escape)
            .withRecordSeparator1(None)
        )
        out = StringIO()
        try:
            printer = CSVPrinter(out, format)
            printer.printRecord0(list)
        finally:
            self.assertEqual(expected, out.getvalue())

    def __toFirstRecordValues(
        self, expected: str, format: CSVFormat
    ) -> typing.List[str]:

        try:
            parser = CSVParser.parse4(expected, format)
            return parser.getRecords()[0].values()
        except Exception as e:
            print(f"An error occurred: {e}")
            return []

    def __randStr(self) -> str:

        r = random.Random()

        sz = r.randint(0, 20)
        buf = [None] * sz
        for i in range(sz):
            what = r.randint(0, 20)
            if what == 0:
                ch = "\r"
            elif what == 1:
                ch = "\n"
            elif what == 2:
                ch = "\t"
            elif what == 3:
                ch = "\f"
            elif what == 4:
                ch = " "
            elif what == 5:
                ch = ","
            elif what == 6:
                ch = self.__DQUOTE_CHAR
            elif what == 7:
                ch = self.__QUOTE_CH
            elif what == 8:
                ch = "\\"
            else:
                ch = chr(r.randint(0, 300))
            buf[i] = ch
        return "".join(buf)

    def __generateLines(self, nLines: int, nCol: int) -> typing.List[typing.List[str]]:

        lines = [[None] * nCol for _ in range(nLines)]
        for i in range(nLines):
            for j in range(nCol):
                lines[i][j] = self.__randStr()
        return lines

    def __expectNulls(
        self, original: typing.List[typing.Any], csvFormat: CSVFormat
    ) -> typing.List[typing.Any]:
        fixed = original.copy()
        for i in range(len(fixed)):
            if fixed[i] == csvFormat.getNullString():
                fixed[i] = None
        return fixed

    def __doRandom(self, format: CSVFormat, iter: int) -> None:

        for _ in range(iter):
            self.__doOneRandom(format)

    def __doOneRandom(self, format: CSVFormat) -> None:

        r = random.Random()

        nLines = r.randint(1, 4)
        nCol = r.randint(1, 3)
        lines = self.__generateLines(nLines, nCol)

        sw = io.StringIO()
        with CSVPrinter(sw, format) as printer:

            for i in range(nLines):
                printer.printRecord1(lines[i])

            printer.flush()
        result = sw.getvalue()

        with CSVParser.parse4(result, format) as parser:
            parseResult = parser.getRecords()

            expected = [self.__expectNulls(line, format) for line in lines]
            Utils.compare(
                "Printer output :" + self.__printable(result), expected, parseResult
            )

    def __createTempPath(self) -> Path:
        return pathlib.Path(
            tempfile.mktemp(prefix=self.__class__.__name__, suffix=".csv")
        )

    def __createTempFile(self) -> pathlib.Path:
        return self.__createTempPath().toFile()

    @staticmethod
    def __printable(s: str) -> str:

        sb = []
        for i in range(len(s)):
            ch = s[i]
            if ord(ch) <= 32 or ord(ch) >= 128:
                sb.append("(" + str(ord(ch)) + ")")
            else:
                sb.append(ch)
        return "".join(sb)
