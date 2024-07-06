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
        if CSVParser.this.isClosed():
            raise RuntimeError("CSVParser has been closed")
        next: CSVRecord = self.__current
        self.__current = None

        if next == None:
            next = self.__getNextRecord()
            if next == None:
                raise RuntimeError("No more CSV records available")

        return next

    def hasNext(self) -> bool:
        if CSVParser.this.isClosed():
            return False
        if self.__current == None:
            self.__current = self.__getNextRecord()
        return self.__current != None

    def __getNextRecord(self) -> CSVRecord:

        pass  # LLM could not translate this method


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
        if self.__lexer != None:
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
        return CSVParser.CSVParser1(StringIO(url.open().read()), format)

    @staticmethod
    def parse2(path: Path, charset: str, format: CSVFormat) -> CSVParser:
        return CSVParser.parse1(path.open("rb"), charset, format)

    @staticmethod
    def parse1(
        inputStream: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader],
        charset: str,
        format: CSVFormat,
    ) -> CSVParser:
        return CSVParser.parse3(io.TextIOWrapper(inputStream, charset), format)

    def __addRecordValue(self, lastRecord: bool) -> None:
        input: str = self.__format.trim1(self.__reusableToken.content.toString())
        if lastRecord and input.isEmpty() and self.__format.getTrailingDelimiter():
            return
        self.__recordList.add(self.__handleNull(input))

    def stream(self) -> typing.Iterable[CSVRecord]:
        return self.__csvRecordIterator

    def isClosed(self) -> bool:
        return self.__lexer.isClosed()

    def hasTrailerComment(self) -> bool:
        return self.__trailerComment != None

    def hasHeaderComment(self) -> bool:
        return self.__headerComment != None

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
        if (
            self.__lexer.getCurrentLineNumber() == CR
            or self.__lexer.getCurrentLineNumber() == LF
            or self.__lexer.getCurrentLineNumber() == UNDEFINED
            or self.__lexer.getCurrentLineNumber() == END_OF_STREAM
        ):
            return self.__lexer.getCurrentLineNumber()
        return self.__lexer.getCurrentLineNumber() + 1

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
        Objects.requireNonNull(reader, "reader")
        Objects.requireNonNull(format, "format")

        self.__format = format.copy()
        self.__lexer = Lexer(format, ExtendedBufferedReader(reader))
        self.__csvRecordIterator = CSVRecordIterator()
        self.__headers = self.__createHeaders()
        self.__characterOffset = characterOffset
        self.__recordNumber = recordNumber - 1

    @staticmethod
    def parse4(string: str, format: CSVFormat) -> CSVParser:
        return CSVParser.CSVParser1(StringIO(string), format)

    @staticmethod
    def parse3(
        reader: typing.Union[io.TextIOWrapper, io.BufferedReader], format: CSVFormat
    ) -> CSVParser:
        return CSVParser.CSVParser1(reader, format)

    @staticmethod
    def parse0(file: pathlib.Path, charset: str, format: CSVFormat) -> CSVParser:
        return CSVParser.parse2(file, charset, format)

    def __isStrictQuoteMode(self) -> bool:
        return (
            self.__format.getQuoteMode() == QuoteMode.ALL_NON_NULL
            or self.__format.getQuoteMode() == QuoteMode.NON_NUMERIC
        )

    def __handleNull(self, input: str) -> str:
        isQuoted: bool = self.__reusableToken.isQuoted
        nullString: str = self.__format.getNullString()
        strictQuoteMode: bool = self.__isStrictQuoteMode()
        if input == nullString:
            return strictQuoteMode and isQuoted and input
        return (
            strictQuoteMode
            and nullString == None
            and input == ""
            and not isQuoted
            and None
            or input
        )

    def __createHeaders(self) -> Headers:
        hdrMap: typing.Dict[str, int] = None
        headerNames: typing.List[str] = None
        formatHeader: typing.List[str] = self.__format.getHeader()
        if formatHeader is not None:
            hdrMap = self.__createEmptyHeaderMap()
            headerRecord: typing.List[str] = None
            if len(formatHeader) == 0:
                nextRecord: CSVRecord = self.nextRecord()
                if nextRecord is not None:
                    headerRecord = nextRecord.values()
                    self.__headerComment = nextRecord.getComment()
            else:
                if self.__format.getSkipHeaderRecord():
                    nextRecord: CSVRecord = self.nextRecord()
                    if nextRecord is not None:
                        self.__headerComment = nextRecord.getComment()
                headerRecord = formatHeader
            if headerRecord is not None:
                observedMissing: bool = False
                for i in range(len(headerRecord)):
                    header: str = headerRecord[i]
                    blankHeader: bool = CSVFormat.isBlank(header)
                    if blankHeader and not self.__format.getAllowMissingColumnNames():
                        raise ValueError(
                            "A header name is missing in "
                            + Arrays.toString(headerRecord)
                        )
                    containsHeader: bool = (
                        blankHeader and observedMissing or hdrMap.containsKey(header)
                    )
                    headerMode: DuplicateHeaderMode = (
                        self.__format.getDuplicateHeaderMode()
                    )
                    duplicatesAllowed: bool = (
                        headerMode == DuplicateHeaderMode.ALLOW_ALL
                    )
                    emptyDuplicatesAllowed: bool = (
                        headerMode == DuplicateHeaderMode.ALLOW_EMPTY
                    )
                    if (
                        containsHeader
                        and not duplicatesAllowed
                        and not (blankHeader and emptyDuplicatesAllowed)
                    ):
                        raise ValueError(
                            String.format(
                                'The header contains a duplicate name: "%s" in %s. If'
                                + " this is valid then use"
                                + " CSVFormat.Builder.setDuplicateHeaderMode().",
                                header,
                                Arrays.toString(headerRecord),
                            )
                        )
                    observedMissing |= blankHeader
                    if header is not None:
                        hdrMap.put(header, Integer.valueOf(i))
                        if headerNames is None:
                            headerNames = ArrayList(headerRecord.length)
                        headerNames.add(header)
        if headerNames is None:
            headerNames = Collections.emptyList()  # immutable
        else:
            headerNames = Collections.unmodifiableList(headerNames)
        return Headers(hdrMap, headerNames)

    def __createEmptyHeaderMap(self) -> typing.Dict[str, int]:
        return (
            self.__format.getIgnoreHeaderCase()
            and TreeMap(String.CASE_INSENSITIVE_ORDER)
            or LinkedHashMap()
        )

    def nextRecord(self) -> CSVRecord:
        result: CSVRecord = None
        self.__recordList.clear()
        sb: StringBuilder = None
        startCharPosition: int = (
            self.__lexer.getCharacterPosition() + self.__characterOffset
        )
        while True:
            self.__reusableToken.reset()
            self.__lexer.nextToken(self.__reusableToken)
            if self.__reusableToken.type == Type.TOKEN:
                self.__addRecordValue(False)
            elif self.__reusableToken.type == Type.EORECORD:
                self.__addRecordValue(True)
            elif self.__reusableToken.type == Type.EOF:
                if self.__reusableToken.isReady:
                    self.__addRecordValue(True)
                elif sb is not None:
                    self.__trailerComment = sb.toString()
            elif self.__reusableToken.type == Type.INVALID:
                raise IOException(
                    "(line " + self.getCurrentLineNumber() + ") invalid parse sequence"
                )
            elif self.__reusableToken.type == Type.COMMENT:  # Ignored currently
                if sb is None:  # first comment for this record
                    sb = StringBuilder()
                else:
                    sb.append(Constants.LF)
                sb.append(self.__reusableToken.content)
                self.__reusableToken.type = Type.TOKEN  # Read another token
            else:
                raise RuntimeError(
                    "Unexpected Token type: " + self.__reusableToken.type
                )
            if self.__reusableToken.type != Type.TOKEN:
                break
        if not self.__recordList.isEmpty():
            self.__recordNumber += 1
            comment: str = sb is None and None or sb.toString()
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
