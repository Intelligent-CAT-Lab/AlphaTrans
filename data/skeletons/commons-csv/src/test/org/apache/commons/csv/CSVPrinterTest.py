from __future__ import annotations

# Imports Begin
from src.test.org.apache.commons.csv.Utils import *
from src.main.org.apache.commons.csv.QuoteMode import *
from src.main.org.apache.commons.csv.Constants import *
from src.main.org.apache.commons.csv.CSVRecord import *
from src.main.org.apache.commons.csv.CSVPrinter import *
from src.main.org.apache.commons.csv.CSVParser import *
from src.main.org.apache.commons.csv.CSVFormat import *
import unittest
import os
import typing
from typing import *
import io
import pathlib

# Imports End


class CSVPrinterTest(unittest.TestCase):

    # Class Fields Begin
    __DQUOTE_CHAR: str = None
    __EURO_CH: str = None
    __ITERATIONS_FOR_RANDOM_TEST: int = None
    __QUOTE_CH: str = None
    __longText2: str = None
    __recordSeparator: str = None
    # Class Fields End

    # Class Methods Begin
    def testTrimOnTwoColumns_test0_decomposed(self) -> None:
        pass

    def testTrimOnOneColumn_test0_decomposed(self) -> None:
        pass

    def testTrimOffOneColumn_test0_decomposed(self) -> None:
        pass

    def testTrailingDelimiterOnTwoColumns_test0_decomposed(self) -> None:
        pass

    def testSingleQuoteQuoted_test0_decomposed(self) -> None:
        pass

    def testSingleLineComment_test0_decomposed(self) -> None:
        pass

    def testRandomTdf_test0_decomposed(self) -> None:
        pass

    def testRandomRfc4180_test0_decomposed(self) -> None:
        pass

    def testRandomPostgreSqlText_test0_decomposed(self) -> None:
        pass

    def testRandomMySql_test0_decomposed(self) -> None:
        pass

    def testRandomExcel_test0_decomposed(self) -> None:
        pass

    def testRandomDefault_test0_decomposed(self) -> None:
        pass

    def testQuoteNonNumeric_test0_decomposed(self) -> None:
        pass

    def testQuoteCommaFirstChar_test0_decomposed(self) -> None:
        pass

    def testQuoteAll_test0_decomposed(self) -> None:
        pass

    def testPrintToPathWithDefaultCharset_test2_decomposed(self) -> None:
        pass

    def testPrintToPathWithDefaultCharset_test1_decomposed(self) -> None:
        pass

    def testPrintToPathWithDefaultCharset_test0_decomposed(self) -> None:
        pass

    def testPrintRecordStream_test1_decomposed(self) -> None:
        pass

    def testPrintRecordStream_test0_decomposed(self) -> None:
        pass

    def testPrintReaderWithoutQuoteToWriter_test1_decomposed(self) -> None:
        pass

    def testPrintReaderWithoutQuoteToWriter_test0_decomposed(self) -> None:
        pass

    def testPrintReaderWithoutQuoteToAppendable_test1_decomposed(self) -> None:
        pass

    def testPrintReaderWithoutQuoteToAppendable_test0_decomposed(self) -> None:
        pass

    def testPrintOnePositiveInteger_test0_decomposed(self) -> None:
        pass

    def testPrintNullValues_test0_decomposed(self) -> None:
        pass

    def testPrinter7_test0_decomposed(self) -> None:
        pass

    def testPrinter6_test0_decomposed(self) -> None:
        pass

    def testPrinter5_test0_decomposed(self) -> None:
        pass

    def testPrinter4_test0_decomposed(self) -> None:
        pass

    def testPrinter3_test0_decomposed(self) -> None:
        pass

    def testPrinter2_test0_decomposed(self) -> None:
        pass

    def testPrinter1_test0_decomposed(self) -> None:
        pass

    def testPrintCustomNullValues_test0_decomposed(self) -> None:
        pass

    def testPrintCSVRecords_test1_decomposed(self) -> None:
        pass

    def testPrintCSVRecords_test0_decomposed(self) -> None:
        pass

    def testPrintCSVRecord_test1_decomposed(self) -> None:
        pass

    def testPrintCSVRecord_test0_decomposed(self) -> None:
        pass

    def testPrintCSVParser_test1_decomposed(self) -> None:
        pass

    def testPrintCSVParser_test0_decomposed(self) -> None:
        pass

    def testPrint_test0_decomposed(self) -> None:
        pass

    def testPostgreSqlNullStringDefaultText_test0_decomposed(self) -> None:
        pass

    def testPostgreSqlNullStringDefaultCsv_test0_decomposed(self) -> None:
        pass

    def testPlainQuoted_test0_decomposed(self) -> None:
        pass

    def testPlainPlain_test0_decomposed(self) -> None:
        pass

    def testPlainEscaped_test0_decomposed(self) -> None:
        pass

    def testParseCustomNullValues_test3_decomposed(self) -> None:
        pass

    def testParseCustomNullValues_test2_decomposed(self) -> None:
        pass

    def testParseCustomNullValues_test1_decomposed(self) -> None:
        pass

    def testParseCustomNullValues_test0_decomposed(self) -> None:
        pass

    def testNotFlushable_test0_decomposed(self) -> None:
        pass

    def testNewCsvPrinterNullAppendableFormat_test0_decomposed(self) -> None:
        pass

    def testNewCsvPrinterAppendableNullFormat_test0_decomposed(self) -> None:
        pass

    def testMySqlNullStringDefault_test0_decomposed(self) -> None:
        pass

    def testMySqlNullOutput_test41_decomposed(self) -> None:
        pass

    def testMySqlNullOutput_test40_decomposed(self) -> None:
        pass

    def testMySqlNullOutput_test39_decomposed(self) -> None:
        pass

    def testMySqlNullOutput_test38_decomposed(self) -> None:
        pass

    def testMySqlNullOutput_test37_decomposed(self) -> None:
        pass

    def testMySqlNullOutput_test36_decomposed(self) -> None:
        pass

    def testMySqlNullOutput_test35_decomposed(self) -> None:
        pass

    def testMySqlNullOutput_test34_decomposed(self) -> None:
        pass

    def testMySqlNullOutput_test33_decomposed(self) -> None:
        pass

    def testMySqlNullOutput_test32_decomposed(self) -> None:
        pass

    def testMySqlNullOutput_test31_decomposed(self) -> None:
        pass

    def testMySqlNullOutput_test30_decomposed(self) -> None:
        pass

    def testMySqlNullOutput_test29_decomposed(self) -> None:
        pass

    def testMySqlNullOutput_test28_decomposed(self) -> None:
        pass

    def testMySqlNullOutput_test27_decomposed(self) -> None:
        pass

    def testMySqlNullOutput_test26_decomposed(self) -> None:
        pass

    def testMySqlNullOutput_test25_decomposed(self) -> None:
        pass

    def testMySqlNullOutput_test24_decomposed(self) -> None:
        pass

    def testMySqlNullOutput_test23_decomposed(self) -> None:
        pass

    def testMySqlNullOutput_test22_decomposed(self) -> None:
        pass

    def testMySqlNullOutput_test21_decomposed(self) -> None:
        pass

    def testMySqlNullOutput_test20_decomposed(self) -> None:
        pass

    def testMySqlNullOutput_test19_decomposed(self) -> None:
        pass

    def testMySqlNullOutput_test18_decomposed(self) -> None:
        pass

    def testMySqlNullOutput_test17_decomposed(self) -> None:
        pass

    def testMySqlNullOutput_test16_decomposed(self) -> None:
        pass

    def testMySqlNullOutput_test15_decomposed(self) -> None:
        pass

    def testMySqlNullOutput_test14_decomposed(self) -> None:
        pass

    def testMySqlNullOutput_test13_decomposed(self) -> None:
        pass

    def testMySqlNullOutput_test12_decomposed(self) -> None:
        pass

    def testMySqlNullOutput_test11_decomposed(self) -> None:
        pass

    def testMySqlNullOutput_test10_decomposed(self) -> None:
        pass

    def testMySqlNullOutput_test9_decomposed(self) -> None:
        pass

    def testMySqlNullOutput_test8_decomposed(self) -> None:
        pass

    def testMySqlNullOutput_test7_decomposed(self) -> None:
        pass

    def testMySqlNullOutput_test6_decomposed(self) -> None:
        pass

    def testMySqlNullOutput_test5_decomposed(self) -> None:
        pass

    def testMySqlNullOutput_test4_decomposed(self) -> None:
        pass

    def testMySqlNullOutput_test3_decomposed(self) -> None:
        pass

    def testMySqlNullOutput_test2_decomposed(self) -> None:
        pass

    def testMySqlNullOutput_test1_decomposed(self) -> None:
        pass

    def testMySqlNullOutput_test0_decomposed(self) -> None:
        pass

    def testMultiLineComment_test0_decomposed(self) -> None:
        pass

    def testMongoDbTsvTabInValue_test0_decomposed(self) -> None:
        pass

    def testMongoDbTsvCommaInValue_test0_decomposed(self) -> None:
        pass

    def testMongoDbTsvBasic_test0_decomposed(self) -> None:
        pass

    def testMongoDbCsvTabInValue_test0_decomposed(self) -> None:
        pass

    def testMongoDbCsvDoubleQuoteInValue_test0_decomposed(self) -> None:
        pass

    def testMongoDbCsvCommaInValue_test0_decomposed(self) -> None:
        pass

    def testMongoDbCsvBasic_test0_decomposed(self) -> None:
        pass

    def testJira135_part3_test7_decomposed(self) -> None:
        pass

    def testJira135_part3_test6_decomposed(self) -> None:
        pass

    def testJira135_part3_test5_decomposed(self) -> None:
        pass

    def testJira135_part3_test4_decomposed(self) -> None:
        pass

    def testJira135_part3_test3_decomposed(self) -> None:
        pass

    def testJira135_part3_test2_decomposed(self) -> None:
        pass

    def testJira135_part3_test1_decomposed(self) -> None:
        pass

    def testJira135_part3_test0_decomposed(self) -> None:
        pass

    def testJira135_part1_test7_decomposed(self) -> None:
        pass

    def testJira135_part1_test6_decomposed(self) -> None:
        pass

    def testJira135_part1_test5_decomposed(self) -> None:
        pass

    def testJira135_part1_test4_decomposed(self) -> None:
        pass

    def testJira135_part1_test3_decomposed(self) -> None:
        pass

    def testJira135_part1_test2_decomposed(self) -> None:
        pass

    def testJira135_part1_test1_decomposed(self) -> None:
        pass

    def testJira135_part1_test0_decomposed(self) -> None:
        pass

    def testInvalidFormat_test0_decomposed(self) -> None:
        pass

    def testHeaderNotSet_test0_decomposed(self) -> None:
        pass

    def testExcelPrinter2_test0_decomposed(self) -> None:
        pass

    def testExcelPrinter1_test0_decomposed(self) -> None:
        pass

    def testExcelPrintAllIterableOfLists_test0_decomposed(self) -> None:
        pass

    def testExcelPrintAllIterableOfArrays_test0_decomposed(self) -> None:
        pass

    def testExcelPrintAllArrayOfLists_test0_decomposed(self) -> None:
        pass

    def testExcelPrintAllArrayOfArrays_test0_decomposed(self) -> None:
        pass

    def testEscapeNull5_test1_decomposed(self) -> None:
        pass

    def testEscapeNull5_test0_decomposed(self) -> None:
        pass

    def testEscapeNull4_test1_decomposed(self) -> None:
        pass

    def testEscapeNull4_test0_decomposed(self) -> None:
        pass

    def testEscapeNull3_test1_decomposed(self) -> None:
        pass

    def testEscapeNull3_test0_decomposed(self) -> None:
        pass

    def testEscapeNull2_test1_decomposed(self) -> None:
        pass

    def testEscapeNull2_test0_decomposed(self) -> None:
        pass

    def testEscapeNull1_test1_decomposed(self) -> None:
        pass

    def testEscapeNull1_test0_decomposed(self) -> None:
        pass

    def testEscapeBackslash5_test1_decomposed(self) -> None:
        pass

    def testEscapeBackslash5_test0_decomposed(self) -> None:
        pass

    def testEscapeBackslash4_test1_decomposed(self) -> None:
        pass

    def testEscapeBackslash4_test0_decomposed(self) -> None:
        pass

    def testEscapeBackslash3_test1_decomposed(self) -> None:
        pass

    def testEscapeBackslash3_test0_decomposed(self) -> None:
        pass

    def testEscapeBackslash2_test1_decomposed(self) -> None:
        pass

    def testEscapeBackslash2_test0_decomposed(self) -> None:
        pass

    def testEscapeBackslash1_test1_decomposed(self) -> None:
        pass

    def testEscapeBackslash1_test0_decomposed(self) -> None:
        pass

    def testEolQuoted_test0_decomposed(self) -> None:
        pass

    def testEolPlain_test0_decomposed(self) -> None:
        pass

    def testEolEscaped_test0_decomposed(self) -> None:
        pass

    def testDontQuoteEuroFirstChar_test0_decomposed(self) -> None:
        pass

    def testDisabledComment_test0_decomposed(self) -> None:
        pass

    def testDelimiterStringEscaped_test0_decomposed(self) -> None:
        pass

    def testDelimiterPlain_test0_decomposed(self) -> None:
        pass

    def testDelimiterEscaped_test0_decomposed(self) -> None:
        pass

    def testDelimeterStringQuoteNone_test5_decomposed(self) -> None:
        pass

    def testDelimeterStringQuoteNone_test4_decomposed(self) -> None:
        pass

    def testDelimeterStringQuoteNone_test3_decomposed(self) -> None:
        pass

    def testDelimeterStringQuoteNone_test2_decomposed(self) -> None:
        pass

    def testDelimeterStringQuoteNone_test1_decomposed(self) -> None:
        pass

    def testDelimeterStringQuoteNone_test0_decomposed(self) -> None:
        pass

    def testDelimeterStringQuoted_test0_decomposed(self) -> None:
        pass

    def testDelimeterQuoteNone_test2_decomposed(self) -> None:
        pass

    def testDelimeterQuoteNone_test1_decomposed(self) -> None:
        pass

    def testDelimeterQuoteNone_test0_decomposed(self) -> None:
        pass

    def testDelimeterQuoted_test0_decomposed(self) -> None:
        pass

    def testCSV259_test0_decomposed(self) -> None:
        pass

    def testCSV135_test1_decomposed(self) -> None:
        pass

    def testCSV135_test0_decomposed(self) -> None:
        pass

    def testCRComment_test0_decomposed(self) -> None:
        pass

    def testRandomPostgreSqlCsv(self) -> None:
        pass

    def testRandomOracle(self) -> None:
        pass

    def testRandomMongoDbCsv(self) -> None:
        pass

    def testPostgreSqlCsvTextOutput(self) -> None:
        pass

    def testPostgreSqlCsvNullOutput(self) -> None:
        pass

    def testJira135All(self) -> None:
        pass

    def testJira135_part2(self) -> None:
        pass

    def __tryFormat(
        self, list_: typing.List[str], quote: str, escape: str, expected: str
    ) -> None:
        pass

    def __toFirstRecordValues(
        self, expected: str, format_: CSVFormat
    ) -> typing.List[typing.List[str]]:
        pass

    def __randStr(self) -> str:
        pass

    def __generateLines(self, nLines: int, nCol: int) -> typing.List[typing.List[str]]:
        pass

    def __expectNulls(
        self, original: typing.List[typing.Any], csvFormat: CSVFormat
    ) -> typing.List[typing.Any]:
        pass

    def __doRandom(self, format_: CSVFormat, iter_: int) -> None:
        pass

    def __doOneRandom(self, format_: CSVFormat) -> None:
        pass

    def __createTempPath(self) -> Path:
        pass

    def __createTempFile(self) -> pathlib.Path:
        pass

    @staticmethod
    def __printable(s: str) -> str:
        pass

    # Class Methods End
