# Imports Begin
from src.main.org.apache.commons.csv.Utils import *
from src.main.org.apache.commons.csv.Constants import *
from src.main.org.apache.commons.csv.CSVRecord import *
from src.main.org.apache.commons.csv.CSVPrinter import *
from src.main.org.apache.commons.csv.CSVParser import *
from src.main.org.apache.commons.csv.CSVFormat import *
import typing
import numbers
import pathlib

# Imports End


class CSVParserTest:

    # Class Fields Begin
    __UTF_8: str = None
    __UTF_8_NAME: str = None
    __CSV_INPUT: str = None
    __CSV_INPUT_1: str = None
    __CSV_INPUT_2: str = None
    __RESULT: typing.List[typing.List[str]] = None
    __CSV_INPUT_NO_COMMENT: str = None
    __CSV_INPUT_HEADER_COMMENT: str = None
    __CSV_INPUT_HEADER_TRAILER_COMMENT: str = None
    __CSV_INPUT_MULTILINE_HEADER_TRAILER_COMMENT: str = None
    # Class Fields End

    # Class Methods Begin
    def testStream(self) -> None:
        pass

    def testStartWithEmptyLinesThenHeaders(self) -> None:
        pass

    def testRoundtrip(self) -> None:
        pass

    def testParseWithQuoteWithEscape(self) -> None:
        pass

    def testParseWithQuoteThrowsException(self) -> None:
        pass

    def testParseWithDelimiterWithQuote(self) -> None:
        pass

    def testParseWithDelimiterWithEscape(self) -> None:
        pass

    def testParseWithDelimiterStringWithQuote(self) -> None:
        pass

    def testParseWithDelimiterStringWithEscape(self) -> None:
        pass

    def testParseUrlCharsetNullFormat(self) -> None:
        pass

    def testParseStringNullFormat(self) -> None:
        pass

    def testParserUrlNullCharsetFormat(self) -> None:
        pass

    def testParseNullUrlCharsetFormat(self) -> None:
        pass

    def testParseNullStringFormat(self) -> None:
        pass

    def testParseNullPathFormat(self) -> None:
        pass

    def testParseNullFileFormat(self) -> None:
        pass

    def testParseFileNullFormat(self) -> None:
        pass

    def testNotValueCSV(self) -> None:
        pass

    def testNoHeaderMap(self) -> None:
        pass

    def testNewCSVParserReaderNullFormat(self) -> None:
        pass

    def testNewCSVParserNullReaderFormat(self) -> None:
        pass

    def testMultipleIterators(self) -> None:
        pass

    def testMongoDbCsv(self) -> None:
        pass

    def testLineFeedEndings(self) -> None:
        pass

    def testIteratorSequenceBreaking(self) -> None:
        pass

    def testIterator(self) -> None:
        pass

    def testInvalidFormat(self) -> None:
        pass

    def testIgnoreEmptyLines(self) -> None:
        pass

    def testGetRecordWithMultiLineValues(self) -> None:
        pass

    def testGetRecords(self) -> None:
        pass

    def testGetRecordPositionWithLF(self) -> None:
        pass

    def testGetRecordPositionWithCRLF(self) -> None:
        pass

    def testGetRecordNumberWithLF(self) -> None:
        pass

    def testGetRecordNumberWithCRLF(self) -> None:
        pass

    def testGetRecordNumberWithCR(self) -> None:
        pass

    def testGetOneLineOneParser(self) -> None:
        pass

    def testGetOneLine(self) -> None:
        pass

    def testGetLineNumberWithLF(self) -> None:
        pass

    def testGetLineNumberWithCRLF(self) -> None:
        pass

    def testGetLineNumberWithCR(self) -> None:
        pass

    def testGetLine(self) -> None:
        pass

    def testForEach(self) -> None:
        pass

    def testFirstEndOfLineLf(self) -> None:
        pass

    def testFirstEndOfLineCrLf(self) -> None:
        pass

    def testFirstEndOfLineCr(self) -> None:
        pass

    def testExcelFormat2(self) -> None:
        pass

    def testExcelFormat1(self) -> None:
        pass

    def testEndOfFileBehaviorExcel(self) -> None:
        pass

    def testEndOfFileBehaviorCSV(self) -> None:
        pass

    def testEmptyString(self) -> None:
        pass

    def testEmptyLineBehaviorExcel(self) -> None:
        pass

    def testEmptyLineBehaviorCSV(self) -> None:
        pass

    def testEmptyFile(self) -> None:
        pass

    def testDefaultFormat(self) -> None:
        pass

    def testCSV57(self) -> None:
        pass

    def testCSV235(self) -> None:
        pass

    def testCSV141RFC4180(self) -> None:
        pass

    def testCSV141Excel(self) -> None:
        pass

    def testCSV141CSVFormat_POSTGRESQL_CSV(self) -> None:
        pass

    def testCSV141CSVFormat_ORACLE(self) -> None:
        pass

    def testCSV141CSVFormat_INFORMIX_UNLOAD_CSV(self) -> None:
        pass

    def testCSV141CSVFormat_INFORMIX_UNLOAD(self) -> None:
        pass

    def testCSV141CSVFormat_DEFAULT(self) -> None:
        pass

    def testCarriageReturnLineFeedEndings(self) -> None:
        pass

    def testCarriageReturnEndings(self) -> None:
        pass

    def testBackslashEscapingOld(self) -> None:
        pass

    def testBackslashEscaping2(self) -> None:
        pass

    def testBackslashEscaping(self) -> None:
        pass

    def __validateRecordPosition(self, lineSeparator: str) -> None:
        pass

    def __validateRecordNumbers(self, lineSeparator: str) -> None:
        pass

    def __validateLineNumbers(self, lineSeparator: str) -> None:
        pass

    def __testCSV141Ok(self, format: CSVFormat) -> None:
        pass

    def __testCSV141Failure(self, format: CSVFormat, failParseRecordNo: int) -> None:
        pass

    def __parseFully(self, parser: CSVParser) -> None:
        pass

    def parse(self, parser: CSVParser, failParseRecordNo: int) -> CSVRecord:
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

    def execute(self) -> None:
        pass

    def execute(self) -> typing.Any:
        pass

    def execute(self) -> None:
        pass

    def execute(self) -> None:
        pass

    def execute(self) -> None:
        pass

    def execute(self) -> None:
        pass

    def execute(self) -> None:
        pass

    def execute(self) -> None:
        pass

    def execute(self) -> None:
        pass

    def execute(self) -> None:
        pass

    def execute(self) -> None:
        pass

    def execute(self) -> None:
        pass

    def execute(self) -> None:
        pass

    def execute(self) -> None:
        pass

    def execute(self) -> None:
        pass

    # Class Methods End


class Consumer:

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def accept(self, actual: typing.Any) -> None:
        pass

    # Class Methods End
