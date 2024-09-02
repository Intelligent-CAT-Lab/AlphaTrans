from __future__ import annotations
import copy
import re
import collections
import pathlib
from pathlib import Path
from io import StringIO
import io
from io import BytesIO
import numbers
import typing
from typing import *
import os
import urllib.parse
import urllib.request
from src.main.org.apache.commons.csv.CSVFormat import *
from src.main.org.apache.commons.csv.CSVRecord import *
from src.main.org.apache.commons.csv.CSVRecord import *
from src.main.org.apache.commons.csv.Constants import *
from src.main.org.apache.commons.csv.DuplicateHeaderMode import *
from src.main.org.apache.commons.csv.ExtendedBufferedReader import *
from src.main.org.apache.commons.csv.Lexer import *
from src.main.org.apache.commons.csv.QuoteMode import *
from src.main.org.apache.commons.csv.Token import *


class CSVRecordIterator:

    __current: CSVRecord = None

    def __init__(self, parser: CSVParser) -> None:
        self.__csvParser = parser

    def __iter__(self) -> CSVRecordIterator:
        return self
    
    def __next__(self) -> CSVRecord:
        if self.hasNext():
            return self.next_()
        else:
            raise StopIteration

    def remove(self) -> None:
        raise NotImplementedError()

    def next_(self) -> CSVRecord:

        if self.__csvParser.isClosed():
            raise RuntimeError("CSVParser has been closed")

        next_ = self.__current
        self.__current = None

        if next_ is None:
            next_ = self.__getNextRecord()
            if next_ is None:
                raise RuntimeError("No more CSV records available")

        return next_

    def hasNext(self) -> bool:

        if self.__csvParser.isClosed():
            return False
        if self.__current is None:
            self.__current = self.__getNextRecord()

        return self.__current is not None

    def __getNextRecord(self) -> CSVRecord:

        try:
            return self.__csvParser.nextRecord()
        except (IOError, OSError) as e:
            raise IOError(f"{e.__class__.__name__} reading next record: {str(e)}") from e


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
        format_: CSVFormat,
    ) -> CSVParser:

        if url is None or charset is None or format_ is None:
            raise ValueError("None values are not allowed")

        if isinstance(url, str):
            parsed_url = urllib.parse.urlparse(url)
        elif isinstance(url, (urllib.parse.ParseResult, urllib.parse.SplitResult, urllib.parse.DefragResult)):
            parsed_url = url
        else:
            raise TypeError("url must be a string or a valid parsed URL object")

        with urllib.request.urlopen(parsed_url.geturl()) as response:
            reader = io.StringIO(response.read().decode(charset))
        parser = CSVParser.CSVParser1(reader, format_)
        return parser

    @staticmethod
    def parse2(path: Path, charset: str, format_: CSVFormat) -> CSVParser:

        if path is None or format_ is None:
            raise ValueError("path and format cannot be None")

        f = io.StringIO(path.open("r", encoding=charset).read())
        return CSVParser.parse1(f, charset, format_)

    @staticmethod
    def parse1(
        inputStream: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader],
        charset: str,
        format_: CSVFormat,
    ) -> CSVParser:

        if inputStream is None or format_ is None:
            raise ValueError("inputStream and format cannot be None")

        if isinstance(inputStream, io.StringIO):
            return CSVParser.parse3(inputStream, format_)
        else:
            return CSVParser.parse3(io.TextIOWrapper(inputStream, charset), format_)

    def __addRecordValue(self, lastRecord: bool) -> None:
        input_ = self.__format.trim1(self.__reusableToken.content.getvalue())
        if lastRecord and input_ == "" and self.__format.getTrailingDelimiter():
            return
        self.__recordList.append(self.__handleNull(input_))

    def stream(self) -> typing.Iterable[CSVRecord]:
        return iter(self.iterator())

    def isClosed(self) -> bool:
        return self.__lexer.isClosed()

    def hasTrailerComment(self) -> bool:
        return self.__trailerComment != ""

    def hasHeaderComment(self) -> bool:
        return self.__headerComment != ""

    def getTrailerComment(self) -> str:
        return self.__trailerComment

    def getRecords(self) -> typing.List[CSVRecord]:
        return list(self.iterator())

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
        reader: typing.Union[io.TextIOWrapper, io.BufferedReader, io.TextIOBase], format_: CSVFormat
    ) -> CSVParser:

        return CSVParser(reader, format_, 0, 1)

    def __init__(
        self,
        reader: typing.Union[io.TextIOWrapper, io.BufferedReader, io.TextIOBase],
        format_: CSVFormat,
        characterOffset: int,
        recordNumber: int,
    ) -> None:

        self.__format = format_.copy()
        if isinstance(reader, io.StringIO):
            self.__lexer = Lexer(
                format_,
                StringIOWrapper(reader)
            )
        elif isinstance(reader, io.TextIOWrapper):
            if isinstance(reader.buffer, io.StringIO):
                self.__lexer = Lexer(
                    format_,
                    StringIOWrapper(reader.buffer)
                )
            else:
                self.__lexer = Lexer(format_, ExtendedBufferedReader(reader.buffer))
        else:
            self.__lexer = Lexer(format_, ExtendedBufferedReader(reader))
        self.__csvRecordIterator = CSVRecordIterator(self)
        self.__headers = self.__createHeaders()
        self.__characterOffset = characterOffset
        self.__recordNumber = recordNumber - 1

    @staticmethod
    def parse4(string: str, format_: CSVFormat) -> CSVParser:

        if string is None or format_ is None:
            raise ValueError("string and format cannot be None")

        return CSVParser.CSVParser1(StringIO(string), format_)

    @staticmethod
    def parse3(
        reader: typing.Union[io.TextIOWrapper, io.BufferedReader, io.TextIOBase], format_: CSVFormat
    ) -> CSVParser:

        return CSVParser.CSVParser1(reader, format_)

    @staticmethod
    def parse0(file: pathlib.Path, charset: str, format_: CSVFormat) -> CSVParser:

        if file is None or format_ is None:
            raise ValueError("file and format cannot be None")

        return CSVParser.parse2(file, charset, format_)

    def __isStrictQuoteMode(self) -> bool:
        return (
            self.__format.getQuoteMode() == QuoteMode.ALL_NON_NULL
            or self.__format.getQuoteMode() == QuoteMode.NON_NUMERIC
        )

    def __handleNull(self, input_: str) -> str:
        isQuoted = self.__reusableToken.isQuoted
        nullString = self.__format.getNullString()
        strictQuoteMode = self.__isStrictQuoteMode()
        if input_ == nullString:
            return nullString if strictQuoteMode and isQuoted else None
        return (
            None
            if strictQuoteMode and nullString == None and input_ == "" and not isQuoted
            else input_
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
                    blankHeader = CSVFormat.isBlank(header)
                    if blankHeader and not self.__format.getAllowMissingColumnNames():
                        raise ValueError(f"A header name is missing in {headerRecord}")

                    containsHeader = blankHeader or hdrMap.get(header) is not None
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
                            f'The header contains a duplicate name: "{header}" in {headerRecord}. If'
                            " this is valid then use"
                            " CSVFormat.Builder.setDuplicateHeaderMode()."
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
            self.__format.getIgnoreHeaderCase() and dict() or collections.OrderedDict()
        )

    def nextRecord(self) -> CSVRecord:

        result = None
        self.__recordList.clear()
        sb = None
        startCharPosition = self.__lexer.getCharacterPosition() + self.__characterOffset
        while True:
            self.__reusableToken.reset()
            self.__lexer.nextToken(self.__reusableToken)
            if self.__reusableToken.type == Token.Type.TOKEN:
                self.__addRecordValue(False)
            elif self.__reusableToken.type == Token.Type.EORECORD:
                self.__addRecordValue(True)
            elif self.__reusableToken.type == Token.Type.EOF:
                if self.__reusableToken.isReady:
                    self.__addRecordValue(True)
                elif sb is not None:
                    self.trailerComment = sb.getvalue()
            elif self.__reusableToken.type == Token.Type.INVALID:
                raise IOError(
                    f"(line {self.getCurrentLineNumber()}) invalid parse sequence"
                )
            elif self.__reusableToken.type == Token.Type.COMMENT:
                if sb is None:
                    sb = io.StringIO()
                else:
                    sb.write(Constants.LF)
                sb.write(self.__reusableToken.content.getvalue())
                self.__reusableToken.type = Token.Type.TOKEN
            else:
                raise ValueError(f"Unexpected Token type: {self.__reusableToken.type}")
            if not self.__reusableToken.type == Token.Type.TOKEN:
                break

        if self.__recordList:
            self.__recordNumber += 1
            comment = None if sb is None else sb.getvalue()
            result = CSVRecord(
                self, self.__recordList.copy(), comment, self.__recordNumber, startCharPosition
            )

        return result

    def getHeaderMapRaw(self) -> typing.Dict[str, int]:
        return self.__headers.headerMap

    def __iter__(self) -> typing.Iterator[CSVRecord]:
        return self.iterator()
