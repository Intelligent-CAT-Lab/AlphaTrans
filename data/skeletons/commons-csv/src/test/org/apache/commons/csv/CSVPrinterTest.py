# Imports Begin
from src.main.org.apache.commons.csv.Utils import *
from src.main.org.apache.commons.csv.QuoteMode import *
from src.main.org.apache.commons.csv.Constants import *
from src.main.org.apache.commons.csv.CSVRecord import *
from src.main.org.apache.commons.csv.CSVPrinter import *
from src.main.org.apache.commons.csv.CSVParser import *
from src.main.org.apache.commons.csv.CSVFormat import *
import typing
import pathlib

# Imports End


class CSVPrinterTest:

    # Class Fields Begin
    __DQUOTE_CHAR: str = None
    __EURO_CH: str = None
    __ITERATIONS_FOR_RANDOM_TEST: int = None
    __QUOTE_CH: str = None
    __longText2: str = None
    __recordSeparator: str = None
    # Class Fields End

    # Class Methods Begin
    def testTrimOnTwoColumns(self) -> None:
        pass

    def testTrimOnOneColumn(self) -> None:
        pass

    def testTrimOffOneColumn(self) -> None:
        pass

    def testTrailingDelimiterOnTwoColumns(self) -> None:
        pass

    def testSingleQuoteQuoted(self) -> None:
        pass

    def testSingleLineComment(self) -> None:
        pass

    def testRandomTdf(self) -> None:
        pass

    def testRandomRfc4180(self) -> None:
        pass

    def testRandomPostgreSqlText(self) -> None:
        pass

    def testRandomPostgreSqlCsv(self) -> None:
        pass

    def testRandomOracle(self) -> None:
        pass

    def testRandomMySql(self) -> None:
        pass

    def testRandomMongoDbCsv(self) -> None:
        pass

    def testRandomExcel(self) -> None:
        pass

    def testRandomDefault(self) -> None:
        pass

    def testQuoteNonNumeric(self) -> None:
        pass

    def testQuoteCommaFirstChar(self) -> None:
        pass

    def testQuoteAll(self) -> None:
        pass

    def testPrintToPathWithDefaultCharset(self) -> None:
        pass

    def testPrintRecordStream(self) -> None:
        pass

    def testPrintReaderWithoutQuoteToWriter(self) -> None:
        pass

    def testPrintReaderWithoutQuoteToAppendable(self) -> None:
        pass

    def testPrintOnePositiveInteger(self) -> None:
        pass

    def testPrintNullValues(self) -> None:
        pass

    def testPrinter7(self) -> None:
        pass

    def testPrinter6(self) -> None:
        pass

    def testPrinter5(self) -> None:
        pass

    def testPrinter4(self) -> None:
        pass

    def testPrinter3(self) -> None:
        pass

    def testPrinter2(self) -> None:
        pass

    def testPrinter1(self) -> None:
        pass

    def testPrintCustomNullValues(self) -> None:
        pass

    def testPrintCSVRecords(self) -> None:
        pass

    def testPrintCSVRecord(self) -> None:
        pass

    def testPrintCSVParser(self) -> None:
        pass

    def testPrint(self) -> None:
        pass

    def testPostgreSqlNullStringDefaultText(self) -> None:
        pass

    def testPostgreSqlNullStringDefaultCsv(self) -> None:
        pass

    def testPostgreSqlCsvTextOutput(self) -> None:
        pass

    def testPostgreSqlCsvNullOutput(self) -> None:
        pass

    def testPlainQuoted(self) -> None:
        pass

    def testPlainPlain(self) -> None:
        pass

    def testPlainEscaped(self) -> None:
        pass

    def testParseCustomNullValues(self) -> None:
        pass

    def testNotFlushable(self) -> None:
        pass

    def testNewCsvPrinterNullAppendableFormat(self) -> None:
        pass

    def testNewCsvPrinterAppendableNullFormat(self) -> None:
        pass

    def testMySqlNullStringDefault(self) -> None:
        pass

    def testMySqlNullOutput(self) -> None:
        pass

    def testMultiLineComment(self) -> None:
        pass

    def testMongoDbTsvTabInValue(self) -> None:
        pass

    def testMongoDbTsvCommaInValue(self) -> None:
        pass

    def testMongoDbTsvBasic(self) -> None:
        pass

    def testMongoDbCsvTabInValue(self) -> None:
        pass

    def testMongoDbCsvDoubleQuoteInValue(self) -> None:
        pass

    def testMongoDbCsvCommaInValue(self) -> None:
        pass

    def testMongoDbCsvBasic(self) -> None:
        pass

    def testJira135All(self) -> None:
        pass

    def testJira135_part3(self) -> None:
        pass

    def testJira135_part2(self) -> None:
        pass

    def testJira135_part1(self) -> None:
        pass

    def testInvalidFormat(self) -> None:
        pass

    def testHeaderNotSet(self) -> None:
        pass

    def testExcelPrinter2(self) -> None:
        pass

    def testExcelPrinter1(self) -> None:
        pass

    def testExcelPrintAllIterableOfLists(self) -> None:
        pass

    def testExcelPrintAllIterableOfArrays(self) -> None:
        pass

    def testExcelPrintAllArrayOfLists(self) -> None:
        pass

    def testExcelPrintAllArrayOfArrays(self) -> None:
        pass

    def testEscapeNull5(self) -> None:
        pass

    def testEscapeNull4(self) -> None:
        pass

    def testEscapeNull3(self) -> None:
        pass

    def testEscapeNull2(self) -> None:
        pass

    def testEscapeNull1(self) -> None:
        pass

    def testEscapeBackslash5(self) -> None:
        pass

    def testEscapeBackslash4(self) -> None:
        pass

    def testEscapeBackslash3(self) -> None:
        pass

    def testEscapeBackslash2(self) -> None:
        pass

    def testEscapeBackslash1(self) -> None:
        pass

    def testEolQuoted(self) -> None:
        pass

    def testEolPlain(self) -> None:
        pass

    def testEolEscaped(self) -> None:
        pass

    def testDontQuoteEuroFirstChar(self) -> None:
        pass

    def testDisabledComment(self) -> None:
        pass

    def testDelimiterStringEscaped(self) -> None:
        pass

    def testDelimiterPlain(self) -> None:
        pass

    def testDelimiterEscaped(self) -> None:
        pass

    def testDelimeterStringQuoteNone(self) -> None:
        pass

    def testDelimeterStringQuoted(self) -> None:
        pass

    def testDelimeterQuoteNone(self) -> None:
        pass

    def testDelimeterQuoted(self) -> None:
        pass

    def testCSV259(self) -> None:
        pass

    def testCSV135(self) -> None:
        pass

    def testCRComment(self) -> None:
        pass

    def __tryFormat(
        self, list: typing.List[str], quote: str, escape: str, expected: str
    ) -> None:
        pass

    def __toFirstRecordValues(
        self, expected: str, format: CSVFormat
    ) -> typing.List[str]:
        pass

    def __randStr(self) -> str:
        pass

    def __generateLines(self, nLines: int, nCol: int) -> typing.List[typing.List[str]]:
        pass

    def __expectNulls(
        self, original: typing.List[typing.Any], csvFormat: CSVFormat
    ) -> typing.List[typing.Any]:
        pass

    def __doRandom(self, format: CSVFormat, iter: int) -> None:
        pass

    def __doOneRandom(self, format: CSVFormat) -> None:
        pass

    def __createTempPath(self) -> Path:
        pass

    def __createTempFile(self) -> pathlib.Path:
        pass

    @staticmethod
    def __printable(s: str) -> str:
        pass

    # Class Methods End


class Executable:

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def execute(self) -> None:
        pass

    def execute(self) -> None:
        pass

    def execute(self) -> None:
        pass

    # Class Methods End
