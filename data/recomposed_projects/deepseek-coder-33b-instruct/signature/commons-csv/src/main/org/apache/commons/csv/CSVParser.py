from __future__ import annotations
import copy
import re
import pathlib
from io import StringIO
import io
from io import BytesIO
import numbers
import typing
from typing import *
import os
import urllib
from src.main.org.apache.commons.csv.CSVFormat import *
from src.main.org.apache.commons.csv.CSVRecord import *
from src.main.org.apache.commons.csv.Constants import *
from src.main.org.apache.commons.csv.DuplicateHeaderMode import *
from src.main.org.apache.commons.csv.ExtendedBufferedReader import *
from src.main.org.apache.commons.csv.Lexer import *
from src.main.org.apache.commons.csv.QuoteMode import *
from src.main.org.apache.commons.csv.Token import *


class CSVRecordIterator:

    __current: CSVRecord = None

    def remove(self) -> None:
        raise NotImplementedError()

    def next(self) -> CSVRecord:

        if self.isClosed():
            raise RuntimeError("CSVParser has been closed")

        next = self.__current
        self.__current = None

        if next is None:
            next = self.__getNextRecord()
            if next is None:
                raise RuntimeError("No more CSV records available")

        return next

    def hasNext(self) -> bool:

        if self.__csvParser.isClosed():
            return False
        if self.__current is None:
            self.__current = self.__getNextRecord()

        return self.__current is not None

    def __getNextRecord(self) -> CSVRecord:
        try:
            return self.next()
        except IOError as e:
            raise IOError(e.errno, e.strerror + " reading next record: " + str(e))


class Headers:

    headerNames: typing.List[str] = None

    headerMap: typing.Dict[str, int] = None

    def __init__(
        self, headerMap: typing.Dict[str, int], headerNames: typing.List[str]
    ) -> None:
        self.headerMap = headerMap
        self.headerNames = headerNames


class CSVParser:

    __reusableToken: Token = Token()
    __characterOffset: int = 0

    __recordNumber: int = 0

    __recordList: typing.List[str] = []

    __csvRecordIterator: CSVRecordIterator = None
    __lexer: Lexer = None

    __headers: Headers = None
    __format: CSVFormat = None

    __trailerComment: str = ""

    __headerComment: str = ""

    @staticmethod
    def initialize_fields() -> None:
        CSVParser.__csvRecordIterator: CSVRecordIterator = None
        CSVParser.__headers: Headers = None

    def iterator(self) -> typing.Iterator[CSVRecord]:
        return self.__csvRecordIterator

    def close(self) -> None:
        if self.__lexer is not None:
            self.__lexer.close()

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
    ) -> CSVParser:

        if url is None or charset is None or format is None:
            raise ValueError("None values are not allowed")

        return CSVParser.CSVParser1(
            io.TextIOWrapper(urllib.request.urlopen(url), encoding=charset), format
        )

    @staticmethod
    def parse2(path: Path, charset: str, format: CSVFormat) -> CSVParser:

        if path is None or format is None:
            raise ValueError("path and format cannot be None")

        with path.open("r", encoding=charset) as f:
            return CSVParser.parse1(f, charset, format)

    @staticmethod
    def parse1(
        inputStream: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader],
        charset: str,
        format: CSVFormat,
    ) -> CSVParser:

        if not inputStream or not format:
            raise ValueError("inputStream and format cannot be None")

        if isinstance(inputStream, io.BytesIO):
            reader = io.TextIOWrapper(inputStream, encoding=charset)
        elif isinstance(inputStream, io.StringIO):
            reader = io.BufferedReader(inputStream)
        else:
            reader = inputStream

        return CSVParser.parse3(reader, format)

    def __addRecordValue(self, lastRecord: bool) -> None:

        input = self.__format.trim1(self.__reusableToken.content.toString())

        if lastRecord and input.isEmpty() and self.__format.getTrailingDelimiter():
            return

        self.__recordList.append(self.__handleNull(input))

    def stream(self) -> typing.Iterable[CSVRecord]:
        return iter(self.iterator(), None)

    def isClosed(self) -> bool:
        return self.__lexer.isClosed()

    def hasTrailerComment(self) -> bool:
        return self.__trailerComment != ""

    def hasHeaderComment(self) -> bool:
        return self.__headerComment != ""

    def getTrailerComment(self) -> str:
        return self.__trailerComment

    def getRecords(self) -> typing.List[CSVRecord]:
        return list(self.stream())

    def getRecordNumber(self) -> int:
        return self.__recordNumber

    def getHeaderNames(self) -> typing.List[str]:
        return self.__headers.headerNames

    def getHeaderMap(self) -> typing.Dict[str, int]:
        if self.__headers.headerMap is None:
            return None
        map = self.__createEmptyHeaderMap()
        map.update(self.__headers.headerMap)
        return map

    def getHeaderComment(self) -> str:
        return self.__headerComment

    def getFirstEndOfLine(self) -> str:
        return self.__lexer.getFirstEol()

    def getCurrentLineNumber(self) -> int:
        return self.__lexer.getCurrentLineNumber()

    @staticmethod
    def CSVParser1(
        reader: typing.Union[io.TextIOWrapper, io.BufferedReader], format: CSVFormat
    ) -> CSVParser:
        return CSVParser(reader, format, 0, 1)

    def __init__(
        self,
        reader: typing.Union[io.TextIOWrapper, io.BufferedReader],
        format: CSVFormat,
        characterOffset: int,
        recordNumber: int,
    ) -> None:

        if reader is None or format is None:
            raise ValueError("reader and format cannot be None")

        self.__format = format.copy()
        self.__lexer = Lexer(format, ExtendedBufferedReader(reader))
        self.__csvRecordIterator = CSVRecordIterator()
        self.__headers = self.__createHeaders()
        self.__characterOffset = characterOffset
        self.__recordNumber = recordNumber - 1

    @staticmethod
    def parse4(string: str, format: CSVFormat) -> CSVParser:

        if string is None or format is None:
            raise ValueError("string and format cannot be None")

        return CSVParser.CSVParser1(io.StringIO(string), format)

    @staticmethod
    def parse3(
        reader: typing.Union[io.TextIOWrapper, io.BufferedReader], format: CSVFormat
    ) -> CSVParser:
        return CSVParser.CSVParser1(reader, format)

    @staticmethod
    def parse0(file: pathlib.Path, charset: str, format: CSVFormat) -> CSVParser:

        if file is None:
            raise ValueError("file cannot be null")

        return CSVParser.parse2(file.to_path(), charset, format)

    def __isStrictQuoteMode(self) -> bool:
        return (
            self.__format.getQuoteMode() == QuoteMode.ALL_NON_NULL
            or self.__format.getQuoteMode() == QuoteMode.NON_NUMERIC
        )

    def __handleNull(self, input: str) -> str:

        isQuoted = self.__reusableToken.isQuoted
        nullString = self.__format.getNullString()
        strictQuoteMode = self.__isStrictQuoteMode()

        if input == nullString:
            return strictQuoteMode and isQuoted and input or None

        return (
            strictQuoteMode
            and nullString == None
            and input == ""
            and not isQuoted
            and None
            or input
        )

    def __createHeaders(self) -> Headers:

        hdrMap = None
        headerNames = None
        formatHeader = self.format.getHeader()

        if formatHeader is not None:
            hdrMap = self.__createEmptyHeaderMap()
            headerRecord = None

            if len(formatHeader) == 0:
                nextRecord = self.nextRecord()
                if nextRecord is not None:
                    headerRecord = nextRecord.values()
                    self.headerComment = nextRecord.getComment()
            else:
                if self.format.getSkipHeaderRecord():
                    nextRecord = self.nextRecord()
                    if nextRecord is not None:
                        self.headerComment = nextRecord.getComment()
                headerRecord = formatHeader

            if headerRecord is not None:
                observedMissing = False
                for i in range(len(headerRecord)):
                    header = headerRecord[i]
                    blankHeader = CSVFormat.isBlank(header)
                    if blankHeader and not self.format.getAllowMissingColumnNames():
                        raise ValueError(
                            "A header name is missing in " + str(headerRecord)
                        )

                    containsHeader = (
                        observedMissing if blankHeader else header in hdrMap
                    )
                    headerMode = self.format.getDuplicateHeaderMode()
                    duplicatesAllowed = headerMode == DuplicateHeaderMode.ALLOW_ALL
                    emptyDuplicatesAllowed = (
                        headerMode == DuplicateHeaderMode.ALLOW_EMPTY
                    )

                    if (
                        containsHeader
                        and not duplicatesAllowed
                        and not (blankHeader and emptyDuplicatesAllowed)
                    ):
                        raise ValueError(
                            'The header contains a duplicate name: "{}" in {}. If this is valid then use CSVFormat.Builder.setDuplicateHeaderMode().'.format(
                                header, str(headerRecord)
                            )
                        )
                    observedMissing |= blankHeader
                    if header is not None:
                        hdrMap[header] = i
                        if headerNames is None:
                            headerNames = []
                        headerNames.append(header)

        if headerNames is None:
            headerNames = []  # immutable
        else:
            headerNames = tuple(headerNames)  # immutable

        return Headers(hdrMap, headerNames)

    def __createEmptyHeaderMap(self) -> typing.Dict[str, int]:
        return (
            self.__format.getIgnoreHeaderCase()
            and dict(String.CASE_INSENSITIVE_ORDER)
            or dict()
        )

    def nextRecord(self) -> CSVRecord:

        result = None
        self.recordList.clear()
        sb = None
        startCharPosition = self.lexer.getCharacterPosition() + self.characterOffset

        while True:
            self.reusableToken.reset()
            self.lexer.nextToken(self.reusableToken)

            if self.reusableToken.type == TOKEN:
                self.__addRecordValue(False)
            elif self.reusableToken.type == EORECORD:
                self.__addRecordValue(True)
            elif self.reusableToken.type == EOF:
                if self.reusableToken.isReady:
                    self.__addRecordValue(True)
                elif sb is not None:
                    self.trailerComment = sb.getvalue()
                break
            elif self.reusableToken.type == INVALID:
                raise IOError(
                    f"(line {self.getCurrentLineNumber()}) invalid parse sequence"
                )
            elif self.reusableToken.type == COMMENT:
                if sb is None:
                    sb = StringIO()
                else:
                    sb.write(Constants.LF)
                sb.write(self.reusableToken.content)
                self.reusableToken.type = TOKEN
            else:
                raise ValueError(f"Unexpected Token type: {self.reusableToken.type}")

        if self.recordList:
            self.recordNumber += 1
            comment = sb.getvalue() if sb is not None else None
            result = CSVRecord(
                self, self.recordList, comment, self.recordNumber, startCharPosition
            )

        return result

    def getHeaderMapRaw(self) -> typing.Dict[str, int]:
        return self.__headers.headerMap


CSVParser.initialize_fields()
