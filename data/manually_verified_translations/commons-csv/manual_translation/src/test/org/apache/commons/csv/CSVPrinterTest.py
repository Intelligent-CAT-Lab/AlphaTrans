from __future__ import annotations
import copy
import re
import random
import tempfile
from io import StringIO
import unittest
import pytest
import pathlib
import io
import typing
from typing import *
import os
import unittest
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

    def testTrimOnTwoColumns(self) -> None:

        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.DEFAULT.withTrim0()) as printer:
            printer.print_(" A ")
            printer.print_(" B ")
            self.assertEqual("A,B", sw.getvalue().strip())

    def testTrimOnOneColumn(self) -> None:

        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.DEFAULT.withTrim0()) as printer:
            printer.print_(" A ")
            self.assertEqual("A", sw.getvalue())

    def testTrimOffOneColumn(self) -> None:

        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.DEFAULT.withTrim1(False)) as printer:
            printer.print_(" A ")
            self.assertEqual('" A "', sw.getvalue())

    def testTrailingDelimiterOnTwoColumns(self) -> None:

        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.DEFAULT.withTrailingDelimiter0()) as printer:
            printer.printRecord1(["A", "B"])
            self.assertEqual("A,B,\r\n", sw.getvalue())

    def testSingleQuoteQuoted(self) -> None:

        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.DEFAULT.withQuote0("'")) as printer:
            printer.print_("a'b'c")
            printer.print_("xyz")
            self.assertEqual("'a''b''c',xyz", sw.getvalue())

    def testSingleLineComment(self) -> None:

        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.DEFAULT.withCommentMarker0("#")) as printer:
            printer.printComment("This is a comment")
            self.assertEqual(
                "# This is a comment" + self.__recordSeparator, sw.getvalue()
            )

    def testRandomTdf(self) -> None:

        self.__doRandom(CSVFormat.TDF, self.__ITERATIONS_FOR_RANDOM_TEST)

    def testRandomRfc4180(self) -> None:

        self.__doRandom(CSVFormat.RFC4180, CSVPrinterTest.__ITERATIONS_FOR_RANDOM_TEST)

    def testRandomPostgreSqlText(self) -> None:

        self.__doRandom(
            CSVFormat.POSTGRESQL_TEXT, CSVPrinterTest.__ITERATIONS_FOR_RANDOM_TEST
        )

    @unittest.skip("Disabled")
    def testRandomPostgreSqlCsv(self) -> None:

        self.__doRandom(
            CSVFormat.POSTGRESQL_CSV, CSVPrinterTest.__ITERATIONS_FOR_RANDOM_TEST
        )

    @unittest.skip("Disabled")
    def testRandomOracle(self) -> None:

        self.__doRandom(CSVFormat.ORACLE, CSVPrinterTest.__ITERATIONS_FOR_RANDOM_TEST)

    def testRandomMySql(self) -> None:

        self.__doRandom(CSVFormat.MYSQL, CSVPrinterTest.__ITERATIONS_FOR_RANDOM_TEST)

    @unittest.skip("Disabled")
    def testRandomMongoDbCsv(self) -> None:

        self.__doRandom(
            CSVFormat.MONGODB_CSV, CSVPrinterTest.__ITERATIONS_FOR_RANDOM_TEST
        )

    def testRandomExcel(self) -> None:

        self.__doRandom(CSVFormat.EXCEL, self.__ITERATIONS_FOR_RANDOM_TEST)

    def testRandomDefault(self) -> None:

        self.__doRandom(CSVFormat.DEFAULT, self.__ITERATIONS_FOR_RANDOM_TEST)

    def testQuoteNonNumeric(self) -> None:

        sw = io.StringIO()
        with CSVPrinter(
            sw, CSVFormat.DEFAULT.withQuoteMode(QuoteMode.NON_NUMERIC)
        ) as printer:
            printer.printRecord1(["a", "b\nc", 1])
            self.assertEqual('"a","b\nc",1' + self.__recordSeparator, sw.getvalue())

    def testQuoteCommaFirstChar(self) -> None:

        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.RFC4180) as printer:
            printer.printRecord1([","])
            self.assertEqual('","' + self.__recordSeparator, sw.getvalue())

    def testQuoteAll(self) -> None:

        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.DEFAULT.withQuoteMode(QuoteMode.ALL)) as printer:
            printer.printRecord1(["a", "b\nc", "d"])
            self.assertEqual('"a","b\nc","d"' + self.__recordSeparator, sw.getvalue())

    def testPrintToPathWithDefaultCharset(self) -> None:

        file = self.__createTempPath()
        with CSVFormat.DEFAULT.print4(file, "utf-8") as printer:
            printer.printRecord1(["a", "b\\c"])

        with open(file, "r", encoding="utf-8", newline='') as f:
            self.assertEqual("a,b\\c" + self.__recordSeparator, f.read())

    def testPrintRecordStream(self) -> None:

        code = "a1,b1\n" + "a2,b2\n" + "a3,b3\n" + "a4,b4\n"
        res = [["a1", "b1"], ["a2", "b2"], ["a3", "b3"], ["a4", "b4"]]
        format_ = CSVFormat.DEFAULT
        sw = io.StringIO()
        printer = format_.print0(sw)
        parser = CSVParser.parse4(code, format_)
        try:
            for record in parser:
                printer.printRecord2(record.stream())
                parser2 = CSVParser.parse4(sw.getvalue(), format_)
            try:
                records = parser2.getRecords()
                assert records, "Fail - records should not be empty"
                Utils.compare("Fail", res, records)
            finally:
                parser2.close()
        finally:
            printer.close()
            parser.close()

    def testPrintReaderWithoutQuoteToWriter(self) -> None:

        sw = io.StringIO()
        content = "testValue"
        try:
            format_ = CSVFormat.DEFAULT.withQuote1(None)
            printer = CSVPrinter(sw, format_)
            value = io.StringIO(content)
            printer.print_(value)
            self.assertEqual(content, sw.getvalue())
        finally:
            printer.close()
         
    def testPrintReaderWithoutQuoteToAppendable(self) -> None:

        sb = io.StringIO()
        content = "testValue"
        try:
            printer = CSVPrinter(sb, CSVFormat.DEFAULT.withQuote1(None))
            value = io.StringIO(content)
            printer.print_(value)
            self.assertEqual(content, sb.getvalue())
        finally:
            printer.close()

    def testPrintOnePositiveInteger(self) -> None:

        sw = io.StringIO()
        with CSVPrinter(
            sw, CSVFormat.DEFAULT.withQuoteMode(QuoteMode.MINIMAL)
        ) as printer:
            printer.print_(2147483647)
            self.assertEqual(str(2147483647), sw.getvalue())

    def testPrintNullValues(self) -> None:

        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.DEFAULT) as printer:
            printer.printRecord1(["a", None, "b"])
            self.assertEqual("a,,b" + self.__recordSeparator, sw.getvalue())

    def testPrinter7(self) -> None:

        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.DEFAULT) as printer:
            printer.printRecord1(["a", "b\\c"])
            self.assertEqual("a,b\\c" + self.__recordSeparator, sw.getvalue())

    def testPrinter6(self) -> None:

        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.DEFAULT) as printer:
            printer.printRecord1(["a", "b\r\nc"])
            self.assertEqual('a,"b\r\nc"' + self.__recordSeparator, sw.getvalue())

    def testPrinter5(self) -> None:

        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.DEFAULT) as printer:
            printer.printRecord1(["a", "b\nc"])
            self.assertEqual('a,"b\nc"' + self.__recordSeparator, sw.getvalue())

    def testPrinter4(self) -> None:

        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.DEFAULT) as printer:
            printer.printRecord1(["a", 'b"c'])
            self.assertEqual('a,"b""c"' + self.__recordSeparator, sw.getvalue())

    def testPrinter3(self) -> None:

        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.DEFAULT) as printer:
            printer.printRecord1(["a, b", "b "])
            self.assertEqual('"a, b","b "' + self.__recordSeparator, sw.getvalue())

    def testPrinter2(self) -> None:

        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.DEFAULT) as printer:
            printer.printRecord1(["a,b", "b"])
            self.assertEqual('"a,b",b' + self.__recordSeparator, sw.getvalue())

    def testPrinter1(self) -> None:

        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.DEFAULT) as printer:
            printer.printRecord1(["a", "b"])
            self.assertEqual("a,b" + self.__recordSeparator, sw.getvalue())

    def testPrintCustomNullValues(self) -> None:

        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.DEFAULT.withNullString("NULL")) as printer:
            printer.printRecord1(["a", None, "b"])
            self.assertEqual("a,NULL,b" + self.__recordSeparator, sw.getvalue())

    def testPrintCSVRecords(self) -> None:

        code = "a1,b1\n" + "a2,b2\n" + "a3,b3\n" + "a4,b4\n"
        res = [["a1", "b1"], ["a2", "b2"], ["a3", "b3"], ["a4", "b4"]]
        format_ = CSVFormat.DEFAULT
        sw = io.StringIO()
        printer = format_.print0(sw)
        parser = CSVParser.parse4(code, format_)
        try:
            printer.printRecords0(parser.getRecords())
            parser2 = CSVParser.parse4(sw.getvalue(), format_)
            try:
                records = parser2.getRecords()
                assert len(records) > 0
                Utils.compare("Fail", res, records)
            finally:
                parser2.close()
        finally:
            printer.close()
            parser.close()

    def testPrintCSVRecord(self) -> None:

        code = "a1,b1\n" + "a2,b2\n" + "a3,b3\n" + "a4,b4\n"
        res = [["a1", "b1"], ["a2", "b2"], ["a3", "b3"], ["a4", "b4"]]
        format_ = CSVFormat.DEFAULT
        sw = io.StringIO()
        printer = format_.print0(sw)
        parser = CSVParser.parse4(code, format_)
        try:
            for record in parser:
                printer.printRecord0(record.values())
            parser2 = CSVParser.parse4(sw.getvalue(), format_)
            try:
                records = parser2.getRecords()
                assert len(records) > 0
                Utils.compare("Fail", res, records)
            finally:
                parser2.close()
        finally:
            printer.close()
            parser.close()

    def testPrintCSVParser(self) -> None:

        code = "a1,b1\n" + "a2,b2\n" + "a3,b3\n" + "a4,b4\n"
        res = [["a1", "b1"], ["a2", "b2"], ["a3", "b3"], ["a4", "b4"]]
        format_ = CSVFormat.DEFAULT
        sw = io.StringIO()
        printer = CSVPrinter(sw, format_)
        parser =  CSVParser.parse4(code, format_)
        try:
            printer.printRecords0(parser.getRecords())
            parser2 = CSVParser.parse4(sw.getvalue(), format_)
            try:
                records = parser2.getRecords()
                assert records, "Fail - records should not be empty"
                Utils.compare("Fail", res, records)
            finally:
                parser2.close()
        finally:
            printer.close()
            parser.close()

    def testPrint(self) -> None:

        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.DEFAULT) as printer:
            printer.printRecord1(["a", "b\\c"])
            self.assertEqual("a,b\\c" + self.__recordSeparator, sw.getvalue())

    def testPostgreSqlNullStringDefaultText(self) -> None:

        # The Python equivalent of the Java assert statement is the unittest.TestCase.assertEqual() method.
        self.assertEqual("\\N", CSVFormat.POSTGRESQL_TEXT.getNullString())

    def testPostgreSqlNullStringDefaultCsv(self) -> None:

        self.assertEqual("", CSVFormat.POSTGRESQL_CSV.getNullString())

    @unittest.skip("Disabled")
    def testPostgreSqlCsvTextOutput(self) -> None:

        s = ["NULL", None]
        format_ = (
            CSVFormat.POSTGRESQL_TEXT.withQuote0(self.__DQUOTE_CHAR)
            .withNullString("NULL")
            .withQuoteMode(QuoteMode.ALL_NON_NULL)
        )
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
            expected = '"NULL"\tNULL\n'
            self.assertEqual(expected, writer.getvalue())
            record0 = self.__toFirstRecordValues(expected, format_)
            self.assertListEqual([None, None], record0)

        s = ["\\N", None]
        format_ = CSVFormat.POSTGRESQL_TEXT.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\\\N\t\\N\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["\\N", "A"]
        format_ = CSVFormat.POSTGRESQL_TEXT.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\\\N\tA\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["\n", "A"]
        format_ = CSVFormat.POSTGRESQL_TEXT.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\n\tA\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["", None]
        format_ = CSVFormat.POSTGRESQL_TEXT.withNullString("NULL")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\tNULL\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["", None]
        format_ = CSVFormat.POSTGRESQL_TEXT
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\t\\N\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["\\N", "", "\u000e,\\\r"]
        format_ = CSVFormat.POSTGRESQL_TEXT
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\\\N\t\t\u000e,\\\\\\r\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["NULL", "\\\r"]
        format_ = CSVFormat.POSTGRESQL_TEXT
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "NULL\t\\\\\\r\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["\\\r"]
        format_ = CSVFormat.POSTGRESQL_TEXT
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\\\\\r\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

    @unittest.skip("Disabled")
    def testPostgreSqlCsvNullOutput(self) -> None:

        s = ["NULL", None]
        format_ = (
            CSVFormat.POSTGRESQL_CSV.withQuote0(self.__DQUOTE_CHAR)
            .withNullString("NULL")
            .withQuoteMode(QuoteMode.ALL_NON_NULL)
        )
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
            expected = '"NULL",NULL\n'
            self.assertEqual(expected, writer.getvalue())
            record0 = self.__toFirstRecordValues(expected, format_)
            self.assertListEqual([None, None], record0)

        s = ["\\N", None]
        format_ = CSVFormat.POSTGRESQL_CSV.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
            expected = "\\\\N\t\\N\n"
            self.assertEqual(expected, writer.getvalue())
            record0 = self.__toFirstRecordValues(expected, format_)
            self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["\\N", "A"]
        format_ = CSVFormat.POSTGRESQL_CSV.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
            expected = "\\\\N\tA\n"
            self.assertEqual(expected, writer.getvalue())
            record0 = self.__toFirstRecordValues(expected, format_)
            self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["\n", "A"]
        format_ = CSVFormat.POSTGRESQL_CSV.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
            expected = "\\n\tA\n"
            self.assertEqual(expected, writer.getvalue())
            record0 = self.__toFirstRecordValues(expected, format_)
            self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["", None]
        format_ = CSVFormat.POSTGRESQL_CSV.withNullString("NULL")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
            expected = "\tNULL\n"
            self.assertEqual(expected, writer.getvalue())
            record0 = self.__toFirstRecordValues(expected, format_)
            self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["", None]
        format_ = CSVFormat.POSTGRESQL_CSV
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
            expected = "\t\\N\n"
            self.assertEqual(expected, writer.getvalue())
            record0 = self.__toFirstRecordValues(expected, format_)
            self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["\\N", "", "\u000e,\\\r"]
        format_ = CSVFormat.POSTGRESQL_CSV
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
            expected = "\\\\N\t\t\u000e,\\\\\\r\n"
            self.assertEqual(expected, writer.getvalue())
            record0 = self.__toFirstRecordValues(expected, format_)
            self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["NULL", "\\\r"]
        format_ = CSVFormat.POSTGRESQL_CSV
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
            expected = "NULL\t\\\\\\r\n"
            self.assertEqual(expected, writer.getvalue())
            record0 = self.__toFirstRecordValues(expected, format_)
            self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["\\\r"]
        format_ = CSVFormat.POSTGRESQL_CSV
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
            expected = "\\\\\\r\n"
            self.assertEqual(expected, writer.getvalue())
            record0 = self.__toFirstRecordValues(expected, format_)
            self.assertListEqual(self.__expectNulls(s, format_), record0)

    def testPlainQuoted(self) -> None:

        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.DEFAULT.withQuote0("'")) as printer:
            printer.print_("abc")
            self.assertEqual("abc", sw.getvalue())

    def testPlainPlain(self) -> None:

        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.DEFAULT.withQuote1(None)) as printer:
            printer.print_("abc")
            printer.print_("xyz")
            self.assertEqual("abc,xyz", sw.getvalue())

    def testPlainEscaped(self) -> None:

        sw = io.StringIO()
        with CSVPrinter(
            sw, CSVFormat.DEFAULT.withQuote1(None).withEscape0("!")
        ) as printer:
            printer.print_("abc")
            printer.print_("xyz")
            self.assertEqual("abc,xyz", sw.getvalue())

    def testParseCustomNullValues(self) -> None:

        sw = io.StringIO()
        format = CSVFormat.DEFAULT.withNullString("NULL")
        with CSVPrinter(sw, format) as printer:
            printer.printRecord1(["a", None, "b"])
            csvString = sw.getvalue()
            self.assertEqual("a,NULL,b" + self.__recordSeparator, csvString)
        iterable = format.parse(io.StringIO(csvString))
        try:
            iterator = iterable.iterator()
            record = next(iterator)
            self.assertEqual("a", record.get1(0))
            self.assertIsNone(record.get1(1))
            self.assertEqual("b", record.get1(2))
            self.assertFalse(iterator.hasNext())
        finally:
            iterable.close()

    def testNotFlushable(self) -> None:

        out = io.StringIO()
        with CSVPrinter(out, CSVFormat.DEFAULT) as printer:
            printer.printRecord1(["a", "b", "c"])
            self.assertEqual("a,b,c" + self.__recordSeparator, out.getvalue())
            printer.flush()

    def testNewCsvPrinterNullAppendableFormat(self) -> None:

        with pytest.raises(Exception):
            CSVPrinter(None, CSVFormat.DEFAULT)

    def testNewCsvPrinterAppendableNullFormat(self) -> None:

        with pytest.raises((TypeError, ValueError, AttributeError)):
            CSVPrinter(io.StringIO(), None)

    def testMySqlNullStringDefault(self) -> None:
        self.assertEqual("\\N", CSVFormat.MYSQL.getNullString())

    def testMySqlNullOutput(self) -> None:

        s = ["NULL", None]
        format_ = (
            CSVFormat.MYSQL.withQuote0(self.__DQUOTE_CHAR)
            .withNullString("NULL")
            .withQuoteMode(QuoteMode.NON_NUMERIC)
        )
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
            expected = '"NULL"\tNULL\n'
            self.assertEqual(expected, writer.getvalue())
            record0 = self.__toFirstRecordValues(expected, format_)
            self.assertListEqual(s, record0)

        s = ["\\N", None]
        format_ = CSVFormat.MYSQL.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
            expected = "\\\\N\t\\N\n"
            self.assertEqual(expected, writer.getvalue())
            record0 = self.__toFirstRecordValues(expected, format_)
            self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["\\N", "A"]
        format_ = CSVFormat.MYSQL.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
            expected = "\\\\N\tA\n"
            self.assertEqual(expected, writer.getvalue())
            record0 = self.__toFirstRecordValues(expected, format_)
            self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["\n", "A"]
        format_ = CSVFormat.MYSQL.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
            expected = "\\n\tA\n"
            self.assertEqual(expected, writer.getvalue())
            record0 = self.__toFirstRecordValues(expected, format_)
            self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["", None]
        format_ = CSVFormat.MYSQL.withNullString("NULL")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
            expected = "\tNULL\n"
            self.assertEqual(expected, writer.getvalue())
            record0 = self.__toFirstRecordValues(expected, format_)
            self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["", None]
        format_ = CSVFormat.MYSQL
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
            expected = "\t\\N\n"
            self.assertEqual(expected, writer.getvalue())
            record0 = self.__toFirstRecordValues(expected, format_)
            self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["\\N", "", "\u000e,\\\r"]
        format_ = CSVFormat.MYSQL
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
            expected = "\\\\N\t\t\u000e,\\\\\\r\n"
            self.assertEqual(expected, writer.getvalue())
            record0 = self.__toFirstRecordValues(expected, format_)
            self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["NULL", "\\\r"]
        format_ = CSVFormat.MYSQL
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
            expected = "NULL\t\\\\\\r\n"
            self.assertEqual(expected, writer.getvalue())
            record0 = self.__toFirstRecordValues(expected, format_)
            self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["\\\r"]
        format_ = CSVFormat.MYSQL
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
            expected = "\\\\\\r\n"
            self.assertEqual(expected, writer.getvalue())
            record0 = self.__toFirstRecordValues(expected, format_)
            self.assertListEqual(self.__expectNulls(s, format_), record0)

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

    def testMongoDbTsvTabInValue(self) -> None:

        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.MONGODB_TSV) as printer:
            printer.printRecord1(["a\tb", "c"])
            self.assertEqual('"a\tb"\tc' + self.__recordSeparator, sw.getvalue())

    def testMongoDbTsvCommaInValue(self) -> None:

        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.MONGODB_TSV) as printer:
            printer.printRecord1(["a,b", "c"])
            self.assertEqual("a,b\tc" + self.__recordSeparator, sw.getvalue())

    def testMongoDbTsvBasic(self) -> None:

        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.MONGODB_TSV) as printer:
            printer.printRecord1(["a", "b"])
            self.assertEqual("a\tb" + self.__recordSeparator, sw.getvalue())

    def testMongoDbCsvTabInValue(self) -> None:

        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.MONGODB_CSV) as printer:
            printer.printRecord1(["a\tb", "c"])
            self.assertEqual("a\tb,c" + self.__recordSeparator, sw.getvalue())

    def testMongoDbCsvDoubleQuoteInValue(self) -> None:

        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.MONGODB_CSV) as printer:
            printer.printRecord1(['a "c" b', "d"])
            self.assertEqual('"a ""c"" b",d\r\n', sw.getvalue())

    def testMongoDbCsvCommaInValue(self) -> None:

        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.MONGODB_CSV) as printer:
            printer.printRecord1(["a,b", "c"])
            self.assertEqual('"a,b",c' + self.__recordSeparator, sw.getvalue())

    def testMongoDbCsvBasic(self) -> None:

        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.MONGODB_CSV) as printer:
            printer.printRecord1(["a", "b"])
            self.assertEqual("a,b" + self.__recordSeparator, sw.getvalue())

    @unittest.skip("Disabled")
    def testJira135All(self) -> None:

        format_ = (
            CSVFormat.DEFAULT.withRecordSeparator0("\n")
            .withQuote0(self.__DQUOTE_CHAR)
            .withEscape0(Constants.BACKSLASH)
        )
        sw = io.StringIO()
        list_ = ['"', "\n", "\\"]
        with CSVPrinter(sw, format_) as printer:
            printer.printRecord0(list_)

            expected = "\"\\\"\",\"\\n\",\"\\\"" + format_.getRecordSeparator()
            self.assertEqual(expected, sw.getvalue())
            record0 = self.__toFirstRecordValues(expected, format_)
            self.assertListEqual(self.__expectNulls(list_, format_), record0)

    def testJira135_part3(self) -> None:

        format_ = (
            CSVFormat.DEFAULT.withRecordSeparator0("\n")
            .withQuote0(self.__DQUOTE_CHAR)
            .withEscape0(Constants.BACKSLASH)
        )
        sw = io.StringIO()
        list_ = ["\\"]
        with CSVPrinter(sw, format_) as printer:
            printer.printRecord0(list_)

            expected = '"\\\\"' + format_.getRecordSeparator()
            self.assertEqual(expected, sw.getvalue())
            record0 = self.__toFirstRecordValues(expected, format_)
            self.assertListEqual(self.__expectNulls(list_, format_), record0)

    @unittest.skip("Disabled")
    def testJira135_part2(self) -> None:

        format_ = (
            CSVFormat.DEFAULT.withRecordSeparator0("\n")
            .withQuote0(self.__DQUOTE_CHAR)
            .withEscape0(Constants.BACKSLASH)
        )
        sw = io.StringIO()
        list_ = ["\n"]
        with CSVPrinter(sw, format_) as printer:
            printer.printRecord0(list_)

            expected = '"\\n"' + format_.getRecordSeparator()
            self.assertEqual(expected, sw.getvalue())
            record0 = self.__toFirstRecordValues(expected, format_)
            self.assertListEqual(self.__expectNulls(list_, format_), record0)

    def testJira135_part1(self) -> None:

        format_ = (
            CSVFormat.DEFAULT.withRecordSeparator0("\n")
            .withQuote0(self.__DQUOTE_CHAR)
            .withEscape0(Constants.BACKSLASH)
        )
        sw = io.StringIO()
        list_ = ['"']
        with CSVPrinter(sw, format_) as printer:
            printer.printRecord0(list_)

            expected = '"\\""' + format_.getRecordSeparator()
            self.assertEqual(expected, sw.getvalue())
            record0 = self.__toFirstRecordValues(expected, format_)
            self.assertListEqual(self.__expectNulls(list_, format_), record0)

    def testInvalidFormat(self) -> None:

        with pytest.raises(ValueError):
            CSVFormat.DEFAULT.withDelimiter(Constants.CR)

    def testHeaderNotSet(self) -> None:

        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.DEFAULT.withQuote1(None)) as printer:
            printer.printRecord1(["a", "b", "c"])
            printer.printRecord1(["x", "y", "z"])
            self.assertEqual("a,b,c\r\nx,y,z\r\n", sw.getvalue())

    def testExcelPrinter2(self) -> None:

        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.EXCEL) as printer:
            printer.printRecord1(["a,b", "b"])
            self.assertEqual('"a,b",b' + self.__recordSeparator, sw.getvalue())

    def testExcelPrinter1(self) -> None:

        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.EXCEL) as printer:
            printer.printRecord1(["a", "b"])
            self.assertEqual("a,b" + self.__recordSeparator, sw.getvalue())

    def testExcelPrintAllIterableOfLists(self) -> None:

        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.EXCEL) as printer:
            printer.printRecords0([["r1c1", "r1c2"], ["r2c1", "r2c2"]])
            self.assertEqual(
                "r1c1,r1c2"
                + self.__recordSeparator
                + "r2c1,r2c2"
                + self.__recordSeparator,
                sw.getvalue(),
            )

    def testExcelPrintAllIterableOfArrays(self) -> None:

        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.EXCEL) as printer:
            printer.printRecords0([["r1c1", "r1c2"], ["r2c1", "r2c2"]])
            self.assertEqual(
                "r1c1,r1c2"
                + self.__recordSeparator
                + "r2c1,r2c2"
                + self.__recordSeparator,
                sw.getvalue(),
            )

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

    def testEscapeNull5(self) -> None:

        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.DEFAULT.withEscape1(None)) as printer:
            printer.print_("\\\\")

            self.assertEqual("\\\\", sw.getvalue())

    def testEscapeNull4(self) -> None:

        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.DEFAULT.withEscape1(None)) as printer:
            printer.print_("\\\\")

            self.assertEqual("\\\\", sw.getvalue())

    def testEscapeNull3(self) -> None:

        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.DEFAULT.withEscape1(None)) as printer:
            printer.print_("X\\\r")

            self.assertEqual('"X\\\r"', sw.getvalue())

    def testEscapeNull2(self) -> None:

        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.DEFAULT.withEscape1(None)) as printer:
            printer.print_("\\\r")

            self.assertEqual('"\\\r"', sw.getvalue())

    def testEscapeNull1(self) -> None:

        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.DEFAULT.withEscape1(None)) as printer:
            printer.print_("\\")

            self.assertEqual("\\", sw.getvalue())

    def testEscapeBackslash5(self) -> None:

        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.DEFAULT.withQuote0(self.__QUOTE_CH)) as printer:
            printer.print_("\\\\")

            self.assertEqual("\\\\", sw.getvalue())

    def testEscapeBackslash4(self) -> None:

        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.DEFAULT.withQuote0(self.__QUOTE_CH)) as printer:
            printer.print_("\\\\")

            self.assertEqual("\\\\", sw.getvalue())

    def testEscapeBackslash3(self) -> None:

        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.DEFAULT.withQuote0(self.__QUOTE_CH)) as printer:
            printer.print_("X\\\r")

            self.assertEqual("'X\\\r'", sw.getvalue())

    def testEscapeBackslash2(self) -> None:

        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.DEFAULT.withQuote0(self.__QUOTE_CH)) as printer:
            printer.print_("\\\r")

            self.assertEqual("'\\\r'", sw.getvalue())

    def testEscapeBackslash1(self) -> None:

        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.DEFAULT.withQuote0(self.__QUOTE_CH)) as printer:
            printer.print_("\\")

            self.assertEqual("\\", sw.getvalue())

    def testEolQuoted(self) -> None:

        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.DEFAULT.withQuote0("'")) as printer:
            printer.print_("a\rb\nc")
            printer.print_("x\by\fz")
            self.assertEqual("'a\rb\nc',x\by\fz", sw.getvalue())

    def testEolPlain(self) -> None:

        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.DEFAULT.withQuote1(None)) as printer:
            printer.print_("a\rb\nc")
            printer.print_("x\fy\bz")
            self.assertEqual("a\rb\nc,x\fy\bz", sw.getvalue())

    def testEolEscaped(self) -> None:

        sw = io.StringIO()
        with CSVPrinter(
            sw, CSVFormat.DEFAULT.withQuote1(None).withEscape0("!")
        ) as printer:
            printer.print_("a\rb\nc")
            printer.print_("x\fy\bz")
            self.assertEqual("a!rb!nc,x\fy\bz", sw.getvalue())

    def testDontQuoteEuroFirstChar(self) -> None:

        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.RFC4180) as printer:
            printer.printRecord1([self.__EURO_CH, "Deux"])
            self.assertEqual(
                self.__EURO_CH + ",Deux" + self.__recordSeparator, sw.getvalue()
            )

    def testDisabledComment(self) -> None:

        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.DEFAULT) as printer:
            printer.printComment("This is a comment")
            self.assertEqual("", sw.getvalue())

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
            printer.print_("a|||b|||c")
            printer.print_("xyz")
            self.assertEqual("a1|1|1|b1|1|1|c|||xyz", sw.getvalue())

    def testDelimiterPlain(self) -> None:

        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.DEFAULT.withQuote1(None)) as printer:
            printer.print_("a,b,c")
            printer.print_("xyz")
            self.assertEqual("a,b,c,xyz", sw.getvalue())

    def testDelimiterEscaped(self) -> None:

        sw = io.StringIO()
        with CSVPrinter(
            sw, CSVFormat.DEFAULT.withEscape0("0").withQuote1(None)
        ) as printer:
            printer.print_("a,b,c")
            printer.print_("xyz")
            self.assertEqual("a0,b0,c,xyz", sw.getvalue())

    def testDelimeterStringQuoteNone(self) -> None:

        sw = io.StringIO()
        format = (
            CSVFormat.DEFAULT.builder()
            .setDelimiter1("[|]")
            .setEscape0("!")
            .setQuoteMode(QuoteMode.NONE)
            .build()
        )
        with CSVPrinter(sw, format) as printer:
            printer.print_("a[|]b[|]c")
            printer.print_("xyz")
            printer.print_("a[xy]bc[]")
            self.assertEqual("a![!|!]b![!|!]c[|]xyz[|]a[xy]bc[]", sw.getvalue())

    def testDelimeterStringQuoted(self) -> None:

        sw = io.StringIO()
        format_ = (
            CSVFormat.DEFAULT.builder().setDelimiter1("[|]").setQuote0("'").build()
        )
        printer = CSVPrinter(sw, format_)
        printer.print_("a[|]b[|]c")
        printer.print_("xyz")
        self.assertEqual("'a[|]b[|]c'[|]xyz", sw.getvalue())

    def testDelimeterQuoteNone(self) -> None:

        sw = io.StringIO()
        format_ = CSVFormat.DEFAULT.withEscape0("0").withQuoteMode(QuoteMode.NONE)
        with CSVPrinter(sw, format_) as printer:
            printer.print_("a,b,c")
            printer.print_("xyz")
            self.assertEqual("a0,b0,c,xyz", sw.getvalue())

    def testDelimeterQuoted(self) -> None:

        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.DEFAULT.withQuote0("'")) as printer:
            printer.print_("a,b,c")
            printer.print_("xyz")
            self.assertEqual("'a,b,c',xyz", sw.getvalue())

    def testCSV259(self) -> None:

        sw = io.StringIO()
        reader = open(
            "src/test/resources/org/apache/commons/csv/CSV-259/sample.txt", "r"
        )
        printer = CSVPrinter(sw, CSVFormat.DEFAULT.withEscape0("0").withQuote1(None))
        printer.print_(reader)
        self.assertEqual("x0,y0,z", sw.getvalue())
        reader.close()

    def testCSV135(self) -> None:

        list_ = ["\"\"", "\\\\", "\\\"\\"]
        self.__tryFormat(list_, None, None, "\"\",\\\\,\\\"\\")
        self.__tryFormat(
            list_, '"', None, "\"\"\"\"\"\",\\\\,\"\\\"\"\\\""
        )
        self.__tryFormat(list_, None, "\\", "\"\",\\\\\\\\,\\\\\"\\\\")
        self.__tryFormat(
            list_,
            '"',
            '\\',
            "\"\\\"\\\"\",\"\\\\\\\\\",\"\\\\\\\"\\\\\"",
        )
        self.__tryFormat(
            list_,
            '"',
            '"',
            "\"\"\"\"\"\",\\\\,\"\\\"\"\\\"",
        )

    def testCRComment(self) -> None:

        sw = io.StringIO()
        value = "abc"
        try:
            printer = CSVPrinter(sw, CSVFormat.DEFAULT.withCommentMarker0("#"))
            printer.print_(value)
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
        finally:
            printer.close()

    def __tryFormat(
        self, list_: typing.List[str], quote: str, escape: str, expected: str
    ) -> None:

        format_ = (
            CSVFormat.DEFAULT.withQuote1(quote)
            .withEscape1(escape)
            .withRecordSeparator1(None)
        )
        out = io.StringIO()
        try:
            printer = CSVPrinter(out, format_)
            printer.printRecord0(list_)
        finally:
            self.assertEqual(expected, out.getvalue())

    def __toFirstRecordValues(
        self, expected: str, format_: CSVFormat
    ) -> typing.List[typing.List[str]]:

        parser = CSVParser.parse4(expected, format_)
        try:
            return parser.getRecords()[0].values()
        finally:
            parser.close()

    def __randStr(self) -> str:

        r = random.Random()

        sz = r.randint(0, 19)
        buf = [None] * sz
        for i in range(sz):
            what = r.randint(0, 19)
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
                ch = Constants.BACKSLASH
            else:
                ch = chr(r.randint(0, 299))
                if ch == '\xa0':
                    ch = " "
                elif ch == '\x85':
                    ch = "\n"
            buf[i] = ch
        return "".join(buf)

    def __generateLines(self, nLines: int, nCol: int) -> typing.List[typing.List[str]]:

        lines = []
        for i in range(nLines):
            line = []
            for j in range(nCol):
                line.append(self.__randStr())
            lines.append(line)
        return lines

    def __expectNulls(
        self, original: typing.List[typing.Any], csvFormat: CSVFormat
    ) -> typing.List[typing.Any]:

        fixed = original.copy()
        for i in range(len(fixed)):
            if fixed[i] == csvFormat.getNullString():
                fixed[i] = None
        return fixed

    def __doRandom(self, format_: CSVFormat, iter_: int) -> None:

        for _ in range(iter_):
            self.__doOneRandom(format_)

    def __doOneRandom(self, format_: CSVFormat) -> None:

        r = random.Random()

        nLines = r.randint(1, 4)
        nCol = r.randint(1, 3)
        lines = self.__generateLines(nLines, nCol)

        sw = io.StringIO()
        printer = CSVPrinter(sw, format_)
        try:
            for i in range(nLines):
                printer.printRecord1(lines[i])
            printer.flush()
            result = sw.getvalue()
            parser = CSVParser.parse4(result, format_)
            try:
                parseResult = parser.getRecords()

                expected = lines.copy()
                for i in range(len(expected)):
                    expected[i] = self.__expectNulls(expected[i], format_)
                Utils.compare(
                    "Printer output :" + self.__printable(result), expected, parseResult
                )
            finally:
                parser.close()
        finally:
            printer.close()

    def __createTempPath(self) -> Path:
        return Path(tempfile.mktemp(suffix=".csv"))

    def __createTempFile(self) -> pathlib.Path:
        return self.__createTempPath()

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
