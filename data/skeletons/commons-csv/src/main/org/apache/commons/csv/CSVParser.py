# Imports Begin
from src.main.org.apache.commons.csv.Token import *
from src.main.org.apache.commons.csv.QuoteMode import *
from src.main.org.apache.commons.csv.Lexer import *
from src.main.org.apache.commons.csv.ExtendedBufferedReader import *
from src.main.org.apache.commons.csv.DuplicateHeaderMode import *
from src.main.org.apache.commons.csv.Constants import *
from src.main.org.apache.commons.csv.CSVRecord import *
from src.main.org.apache.commons.csv.CSVFormat import *
import typing
import numbers
import io
import pathlib

# Imports End


class CSVParser(Closeable, Iterable):

    # Class Fields Begin
    __headerComment: str = None
    __trailerComment: str = None
    __format: CSVFormat = None
    __headers: Headers = None
    __lexer: Lexer = None
    __csvRecordIterator: CSVRecordIterator = None
    __recordList: typing.List[str] = None
    __recordNumber: int = None
    __characterOffset: int = None
    __reusableToken: Token = None
    # Class Fields End

    # Class Methods Begin
    def iterator(self) -> typing.Iterator[CSVRecord]:
        pass

    def close(self) -> None:
        pass

    @staticmethod
    def parse5(
        url: typing.Union[
            urllib.parse.ParseResult,
            urllib.parse.SplitResult,
            urllib.parse.DefragResult,
            str,
        ],
        charset: str,
        format: CSVFormat,
    ) -> "CSVParser":
        pass

    @staticmethod
    def parse2(path: Path, charset: str, format: CSVFormat) -> "CSVParser":
        pass

    @staticmethod
    def parse1(
        inputStream: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader],
        charset: str,
        format: CSVFormat,
    ) -> "CSVParser":
        pass

    def __addRecordValue(self, lastRecord: bool) -> None:
        pass

    def stream(self) -> typing.Iterable[CSVRecord]:
        pass

    def isClosed(self) -> bool:
        pass

    def hasTrailerComment(self) -> bool:
        pass

    def hasHeaderComment(self) -> bool:
        pass

    def getTrailerComment(self) -> str:
        pass

    def getRecords(self) -> typing.List[CSVRecord]:
        pass

    def getRecordNumber(self) -> int:
        pass

    def getHeaderNames(self) -> typing.List[str]:
        pass

    def getHeaderMap(self) -> typing.Dict[str, int]:
        pass

    def getHeaderComment(self) -> str:
        pass

    def getFirstEndOfLine(self) -> str:
        pass

    def getCurrentLineNumber(self) -> int:
        pass

    @staticmethod
    def CSVParser1(
        reader: typing.Union[io.TextIOWrapper, io.BufferedReader], format: CSVFormat
    ) -> "CSVParser":
        pass

    def __init__(
        self,
        reader: typing.Union[io.TextIOWrapper, io.BufferedReader],
        format: CSVFormat,
        characterOffset: int,
        recordNumber: int,
    ) -> None:
        pass

    @staticmethod
    def parse4(string: str, format: CSVFormat) -> "CSVParser":
        pass

    @staticmethod
    def parse3(
        reader: typing.Union[io.TextIOWrapper, io.BufferedReader], format: CSVFormat
    ) -> "CSVParser":
        pass

    @staticmethod
    def parse0(file: pathlib.Path, charset: str, format: CSVFormat) -> "CSVParser":
        pass

    def __isStrictQuoteMode(self) -> bool:
        pass

    def __handleNull(self, input: str) -> str:
        pass

    def __createHeaders(self) -> Headers:
        pass

    def __createEmptyHeaderMap(self) -> typing.Dict[str, int]:
        pass

    def nextRecord(self) -> CSVRecord:
        pass

    def getHeaderMapRaw(self) -> typing.Dict[str, int]:
        pass

    # Class Methods End


class CSVRecordIterator(Iterator):

    # Class Fields Begin
    __current: CSVRecord = None
    # Class Fields End

    # Class Methods Begin
    def remove(self) -> None:
        pass

    def next(self) -> CSVRecord:
        pass

    def hasNext(self) -> bool:
        pass

    def __getNextRecord(self) -> CSVRecord:
        pass

    # Class Methods End


class Headers:

    # Class Fields Begin
    headerMap: typing.Dict[str, int] = None
    headerNames: typing.List[str] = None
    # Class Fields End

    # Class Methods Begin
    def __init__(
        self, headerMap: typing.Dict[str, int], headerNames: typing.List[str]
    ) -> None:
        pass

    # Class Methods End
