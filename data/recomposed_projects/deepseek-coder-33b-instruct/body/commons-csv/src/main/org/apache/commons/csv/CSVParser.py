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

        if self.__csvRecordIterator.isClosed():
            raise RuntimeError("CSVParser has been closed")

        next = self.__current
        self.__current = None

        if next is None:
            next = self.__getNextRecord()
            if next is None:
                raise RuntimeError("No more CSV records available")

        return next

    def hasNext(self) -> bool:

        if self.__csvRecordIterator.isClosed():
            return False
        if self.__current is None:
            self.__current = self.__getNextRecord()

        return self.__current is not None

    def __getNextRecord(self) -> CSVRecord:

        try:
            return self.next()
        except IOError as e:
            raise IOError(e.__class__.__name__ + " reading next record: " + str(e))


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

        with path.open("r", encoding=charset) as file:
            return CSVParser.parse1(file, charset, format)

    @staticmethod
    def parse1(
        inputStream: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader],
        charset: str,
        format: CSVFormat,
    ) -> CSVParser:

        if inputStream is None or format is None:
            raise ValueError("inputStream and format cannot be None")

        if isinstance(inputStream, io.BytesIO):
            reader = io.TextIOWrapper(inputStream, encoding=charset)
        elif isinstance(inputStream, io.StringIO):
            reader = io.TextIOWrapper(inputStream.detach(), encoding=charset)
        else:
            reader = inputStream

        return CSVParser.parse3(reader, format)

    def __addRecordValue(self, lastRecord: bool) -> None:

        input = self.__format.trim1(self.__reusableToken.content.toString())

        if lastRecord and input.isEmpty() and self.__format.getTrailingDelimiter():
            return

        self.__recordList.append(self.__handleNull(input))

    def stream(self) -> typing.Iterable[CSVRecord]:
        return iter(self.iterator())

    def isClosed(self) -> bool:
        return self.__lexer.isClosed()

    def hasTrailerComment(self) -> bool:
        return self.__trailerComment is not None

    def hasHeaderComment(self) -> bool:
        return self.__headerComment is not None

    def getTrailerComment(self) -> str:
        return self.__trailerComment

    def getRecords(self) -> typing.List[CSVRecord]:
        return list(self.stream())

    def getRecordNumber(self) -> int:
        return self.__recordNumber

    def getHeaderNames(self) -> typing.List[str]:
        return typing.cast(typing.List[str], self.__headers.headerNames)

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
            raise ValueError("file cannot be None")

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
        formatHeader = self.__format.getHeader()

        if formatHeader is not None:
            hdrMap = self.__createEmptyHeaderMap()
            headerRecord = None

            if len(formatHeader) == 0:
                nextRecord = self.nextRecord()
                if nextRecord is not None:
                    headerRecord = nextRecord.values()
                    self.__headerComment = nextRecord.getComment()
            else:
                if self.__format.getSkipHeaderRecord():
                    nextRecord = self.nextRecord()
                    if nextRecord is not None:
                        self.__headerComment = nextRecord.getComment()
                headerRecord = formatHeader

            if headerRecord is not None:
                observedMissing = False
                for i in range(len(headerRecord)):
                    header = headerRecord[i]
                    blankHeader = CSVRecord.isBlank(header)
                    if blankHeader and not self.__format.getAllowMissingColumnNames():
                        raise ValueError(
                            "A header name is missing in " + str(headerRecord)
                        )

                    containsHeader = blankHeader or header in hdrMap
                    headerMode = self.__format.getDuplicateHeaderMode()
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
            headerNames = tuple(headerNames)

        return Headers(hdrMap, headerNames)

    def __createEmptyHeaderMap(self) -> typing.Dict[str, int]:
        return (
            self.__format.getIgnoreHeaderCase()
            and dict(TreeMap(String.CASE_INSENSITIVE_ORDER))
            or dict(LinkedHashMap())
        )

    def nextRecord(self) -> CSVRecord:

        result = None
        self.__recordList.clear()
        sb = None
        startCharPosition = self.__lexer.getCharacterPosition() + self.__characterOffset

        while True:
            self.__reusableToken.reset()
            self.__lexer.nextToken(self.__reusableToken)

            if self.__reusableToken.type == TOKEN:
                self.__addRecordValue(False)
            elif self.__reusableToken.type == EORECORD:
                self.__addRecordValue(True)
            elif self.__reusableToken.type == EOF:
                if self.__reusableToken.isReady:
                    self.__addRecordValue(True)
                elif sb is not None:
                    self.__trailerComment = sb.toString()
            elif self.__reusableToken.type == INVALID:
                raise IOException(
                    "(line " + self.getCurrentLineNumber() + ") invalid parse sequence"
                )
            elif self.__reusableToken.type == COMMENT:
                if sb is None:
                    sb = StringBuilder()
                else:
                    sb.append(Constants.LF)
                sb.append(self.__reusableToken.content)
                self.__reusableToken.type = TOKEN
            else:
                raise RuntimeError(
                    "Unexpected Token type: " + self.__reusableToken.type
                )

            if self.__reusableToken.type != TOKEN:
                break

        if self.__recordList:
            self.__recordNumber += 1
            comment = None if sb is None else sb.toString()
            result = CSVRecord(
                self,
                self.__recordList.toArray(Constants.EMPTY_STRING_ARRAY),
                comment,
                self.__recordNumber,
                startCharPosition,
            )

        return result

    def getHeaderMapRaw(self) -> typing.Dict[str, int]:
        return self.__headers.headerMap


CSVParser.initialize_fields()
