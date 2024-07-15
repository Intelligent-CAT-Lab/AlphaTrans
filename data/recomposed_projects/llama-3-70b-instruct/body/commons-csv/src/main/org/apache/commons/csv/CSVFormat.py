from __future__ import annotations
import copy
import re
import sys
import enum
import numbers
from io import StringIO
import pathlib
from io import IOBase
import io
import typing
from typing import *
import os
from src.main.org.apache.commons.csv.CSVParser import *
from src.main.org.apache.commons.csv.CSVPrinter import *
from src.main.org.apache.commons.csv.Constants import *
from src.main.org.apache.commons.csv.DuplicateHeaderMode import *
from src.main.org.apache.commons.csv.ExtendedBufferedReader import *
from src.main.org.apache.commons.csv.IOUtils import *
from src.main.org.apache.commons.csv.QuoteMode import *


class Builder:

    __trim: bool = False

    __trailingDelimiter: bool = False

    __skipHeaderRecord: bool = False

    __recordSeparator: str = ""

    __quoteMode: QuoteMode = None

    __quotedNullString: str = ""

    __quoteCharacter: str = ""

    __nullString: str = ""

    __ignoreSurroundingSpaces: bool = False

    __ignoreHeaderCase: bool = False

    __ignoreEmptyLines: bool = False

    __headers: typing.List[str] = None

    __headerComments: typing.List[str] = None

    __escapeCharacter: str = ""

    __duplicateHeaderMode: DuplicateHeaderMode = None

    __delimiter: str = ""

    __commentMarker: str = ""

    __autoFlush: bool = False

    __allowMissingColumnNames: bool = False

    def setAllowDuplicateHeaderNames(self, allowDuplicateHeaderNames: bool) -> Builder:
        self.setDuplicateHeaderMode(
            DuplicateHeaderMode.ALLOW_ALL
            if allowDuplicateHeaderNames
            else DuplicateHeaderMode.ALLOW_EMPTY
        )
        return self

    def setTrim(self, trim: bool) -> Builder:
        self.__trim = trim
        return self

    def setTrailingDelimiter(self, trailingDelimiter: bool) -> Builder:
        self.__trailingDelimiter = trailingDelimiter
        return self

    def setSkipHeaderRecord(self, skipHeaderRecord: bool) -> Builder:
        self.__skipHeaderRecord = skipHeaderRecord
        return self

    def setRecordSeparator1(self, recordSeparator: str) -> Builder:
        self.__recordSeparator = recordSeparator
        return self

    def setRecordSeparator0(self, recordSeparator: str) -> Builder:
        self.__recordSeparator = recordSeparator
        return self

    def setQuoteMode(self, quoteMode: QuoteMode) -> Builder:
        self.__quoteMode = quoteMode
        return self

    def setQuote1(self, quoteCharacter: str) -> Builder:
        if CSVFormat.__isLineBreak1(quoteCharacter):
            raise ValueError("The quoteChar cannot be a line break")
        self.__quoteCharacter = quoteCharacter
        return self

    def setQuote0(self, quoteCharacter: str) -> Builder:
        self.setQuote1(chr(quoteCharacter))
        return self

    def setNullString(self, nullString: str) -> Builder:
        self.__nullString = nullString
        self.__quotedNullString = (
            self.__quoteCharacter + nullString + self.__quoteCharacter
        )
        return self

    def setIgnoreSurroundingSpaces(self, ignoreSurroundingSpaces: bool) -> Builder:
        self.__ignoreSurroundingSpaces = ignoreSurroundingSpaces
        return self

    def setIgnoreHeaderCase(self, ignoreHeaderCase: bool) -> Builder:
        self.__ignoreHeaderCase = ignoreHeaderCase
        return self

    def setIgnoreEmptyLines(self, ignoreEmptyLines: bool) -> Builder:
        self.__ignoreEmptyLines = ignoreEmptyLines
        return self

    def setHeaderComments1(self, headerComments: typing.List[str]) -> Builder:
        self.__headerComments = CSVFormat.clone(headerComments)
        return self

    def setHeaderComments0(self, headerComments: typing.List[typing.Any]) -> Builder:
        self.__headerComments = CSVFormat.clone(
            [str(value) if value is not None else "" for value in headerComments]
        )
        return self

    def setEscape1(self, escapeCharacter: str) -> Builder:
        if CSVFormat.__isLineBreak1(escapeCharacter):
            raise ValueError("The escape character cannot be a line break")
        self.__escapeCharacter = escapeCharacter
        return self

    def setEscape0(self, escapeCharacter: str) -> Builder:
        self.setEscape1(chr(escapeCharacter))
        return self

    def setDuplicateHeaderMode(
        self, duplicateHeaderMode: DuplicateHeaderMode
    ) -> Builder:
        if duplicateHeaderMode is None:
            raise ValueError("duplicateHeaderMode cannot be null")
        self.__duplicateHeaderMode = duplicateHeaderMode
        return self

    def setDelimiter1(self, delimiter: str) -> Builder:
        if CSVFormat.__containsLineBreak(delimiter):
            raise ValueError("The delimiter cannot be a line break")
        if delimiter == "":
            raise ValueError("The delimiter cannot be empty")
        self.__delimiter = delimiter
        return self

    def setDelimiter0(self, delimiter: str) -> Builder:
        return self.setDelimiter1(str(delimiter))

    def setCommentMarker1(self, commentMarker: str) -> Builder:
        if CSVFormat.__isLineBreak1(commentMarker):
            raise ValueError(
                "The comment start marker character cannot be a line break"
            )
        self.__commentMarker = commentMarker
        return self

    def setCommentMarker0(self, commentMarker: str) -> Builder:
        self.setCommentMarker1(chr(commentMarker))
        return self

    def setAutoFlush(self, autoFlush: bool) -> Builder:
        self.__autoFlush = autoFlush
        return self

    def setAllowMissingColumnNames(self, allowMissingColumnNames: bool) -> Builder:
        self.__allowMissingColumnNames = allowMissingColumnNames
        return self

    def build(self) -> CSVFormat:
        return CSVFormat(
            1,
            False,
            False,
            None,
            None,
            None,
            False,
            False,
            self,
            None,
            False,
            None,
            None,
            False,
            None,
            None,
            False,
            False,
            None,
            None,
        )

    @staticmethod
    def create1(csvFormat: CSVFormat) -> Builder:
        return Builder(csvFormat)

    @staticmethod
    def create0() -> Builder:
        return Builder(CSVFormat.DEFAULT)

    def __init__(self, csvFormat: CSVFormat) -> None:
        self.__delimiter = csvFormat.delimiter
        self.__quoteCharacter = csvFormat.quoteCharacter
        self.__quoteMode = csvFormat.quoteMode
        self.__commentMarker = csvFormat.commentMarker
        self.__escapeCharacter = csvFormat.escapeCharacter
        self.__ignoreSurroundingSpaces = csvFormat.ignoreSurroundingSpaces
        self.__allowMissingColumnNames = csvFormat.allowMissingColumnNames
        self.__ignoreEmptyLines = csvFormat.ignoreEmptyLines
        self.__recordSeparator = csvFormat.recordSeparator
        self.__nullString = csvFormat.nullString
        self.__headerComments = csvFormat.headerComments
        self.__headers = csvFormat.headers
        self.__skipHeaderRecord = csvFormat.skipHeaderRecord
        self.__ignoreHeaderCase = csvFormat.ignoreHeaderCase
        self.__trailingDelimiter = csvFormat.trailingDelimiter
        self.__trim = csvFormat.trim
        self.__autoFlush = csvFormat.autoFlush
        self.__quotedNullString = csvFormat.quotedNullString
        self.__duplicateHeaderMode = csvFormat.duplicateHeaderMode


class Predefined:

    TDF: Predefined = None

    RFC4180: Predefined = None

    PostgreSQLText: Predefined = None

    PostgreSQLCsv: Predefined = None

    Oracle: Predefined = None

    MySQL: Predefined = None

    MongoDBTsv: Predefined = None

    MongoDBCsv: Predefined = None

    InformixUnloadCsv: Predefined = None

    InformixUnload: Predefined = None

    Excel: Predefined = None

    Default: Predefined = None

    __format: CSVFormat = None

    def getFormat(self) -> CSVFormat:
        return self.__format

    def __init__(self, format: CSVFormat) -> None:
        self.__format = format


class CSVFormat:

    TDF: CSVFormat = None
    RFC4180: CSVFormat = None
    POSTGRESQL_TEXT: CSVFormat = None
    POSTGRESQL_CSV: CSVFormat = None
    ORACLE: CSVFormat = None
    MYSQL: CSVFormat = None
    MONGODB_TSV: CSVFormat = None
    MONGODB_CSV: CSVFormat = None
    INFORMIX_UNLOAD_CSV: CSVFormat = None
    INFORMIX_UNLOAD: CSVFormat = None
    EXCEL: CSVFormat = None
    DEFAULT: CSVFormat = None
    __trim: bool = False

    __trailingDelimiter: bool = False

    __skipHeaderRecord: bool = False

    __recordSeparator: str = ""

    __quoteMode: QuoteMode = None

    __quotedNullString: str = ""

    __quoteCharacter: str = ""

    __nullString: str = ""

    __ignoreSurroundingSpaces: bool = False

    __ignoreHeaderCase: bool = False

    __ignoreEmptyLines: bool = False

    __headerComments: typing.List[str] = None

    __headers: typing.List[str] = None

    __escapeCharacter: str = ""

    __delimiter: str = ""

    __commentMarker: str = ""

    __autoFlush: bool = False

    __allowMissingColumnNames: bool = False

    __duplicateHeaderMode: DuplicateHeaderMode = None

    __serialVersionUID: int = 2

    @staticmethod
    def initialize_fields() -> None:
        DEFAULT: CSVFormat = CSVFormat(
            0,
            False,
            False,
            Constants.COMMA,
            None,
            None,
            False,
            False,
            None,
            None,
            False,
            Constants.DOUBLE_QUOTE_CHAR,
            None,
            True,
            DuplicateHeaderMode.ALLOW_ALL,
            None,
            False,
            False,
            None,
            Constants.CRLF,
        )

        TDF: CSVFormat = (
            CSVFormat.DEFAULT.builder()
            .setDelimiter0(Constants.TAB)
            .setIgnoreSurroundingSpaces(True)
            .build()
        )

        RFC4180: CSVFormat = (
            CSVFormat.DEFAULT.builder().setIgnoreEmptyLines(False).build()
        )

        POSTGRESQL_TEXT: CSVFormat = (
            CSVFormat.DEFAULT.builder()
            .setDelimiter0(Constants.TAB)
            .setEscape0(Constants.BACKSLASH)
            .setIgnoreEmptyLines(False)
            .setQuote1(None)
            .setRecordSeparator0(Constants.LF)
            .setNullString(Constants.SQL_NULL_STRING)
            .setQuoteMode(QuoteMode.ALL_NON_NULL)
            .build()
        )

        POSTGRESQL_CSV: CSVFormat = (
            CSVFormat.DEFAULT.builder()
            .setDelimiter1(Constants.COMMA)
            .setEscape1(None)
            .setIgnoreEmptyLines(False)
            .setQuote1(Constants.DOUBLE_QUOTE_CHAR)
            .setRecordSeparator0(Constants.LF)
            .setNullString(Constants.EMPTY)
            .setQuoteMode(QuoteMode.ALL_NON_NULL)
            .build()
        )

        ORACLE: CSVFormat = (
            CSVFormat.DEFAULT.builder()
            .setDelimiter1(Constants.COMMA)
            .setEscape0(Constants.BACKSLASH)
            .setIgnoreEmptyLines(False)
            .setQuote1(Constants.DOUBLE_QUOTE_CHAR)
            .setNullString(Constants.SQL_NULL_STRING)
            .setTrim(True)
            .setRecordSeparator1(os.linesep)
            .setQuoteMode(QuoteMode.MINIMAL)
            .build()
        )

        MYSQL: CSVFormat = (
            CSVFormat.DEFAULT.builder()
            .setDelimiter0(Constants.TAB)
            .setEscape0(Constants.BACKSLASH)
            .setIgnoreEmptyLines(False)
            .setQuote1(None)
            .setRecordSeparator0(Constants.LF)
            .setNullString(Constants.SQL_NULL_STRING)
            .setQuoteMode(QuoteMode.ALL_NON_NULL)
            .build()
        )

        MONGODB_TSV: CSVFormat = (
            CSVFormat.DEFAULT.builder()
            .setDelimiter0(Constants.TAB)
            .setEscape1(Constants.DOUBLE_QUOTE_CHAR)
            .setQuote1(Constants.DOUBLE_QUOTE_CHAR)
            .setQuoteMode(QuoteMode.MINIMAL)
            .setSkipHeaderRecord(False)
            .build()
        )

        MONGODB_CSV: CSVFormat = (
            CSVFormat.DEFAULT.builder()
            .setDelimiter1(Constants.COMMA)
            .setEscape1(Constants.DOUBLE_QUOTE_CHAR)
            .setQuote1(Constants.DOUBLE_QUOTE_CHAR)
            .setQuoteMode(QuoteMode.MINIMAL)
            .setSkipHeaderRecord(False)
            .build()
        )

        INFORMIX_UNLOAD_CSV: CSVFormat = (
            CSVFormat.DEFAULT.builder()
            .setDelimiter1(Constants.COMMA)
            .setQuote1(Constants.DOUBLE_QUOTE_CHAR)
            .setRecordSeparator0(Constants.LF)
            .build()
        )

        INFORMIX_UNLOAD: CSVFormat = (
            CSVFormat.DEFAULT.builder()
            .setDelimiter0(Constants.PIPE)
            .setEscape0(Constants.BACKSLASH)
            .setQuote1(Constants.DOUBLE_QUOTE_CHAR)
            .setRecordSeparator0(Constants.LF)
            .build()
        )

        EXCEL: CSVFormat = (
            CSVFormat.DEFAULT.builder()
            .set_ignore_empty_lines(False)
            .set_allow_missing_column_names(True)
            .build()
        )

    def withTrim1(self, trim: bool) -> CSVFormat:
        return self.builder().setTrim(trim).build()

    def withTrim0(self) -> CSVFormat:
        return self.builder().setTrim(True).build()

    def withTrailingDelimiter1(self, trailingDelimiter: bool) -> CSVFormat:
        return self.builder().setTrailingDelimiter(trailingDelimiter).build()

    def withTrailingDelimiter0(self) -> CSVFormat:
        return self.builder().setTrailingDelimiter(True).build()

    def withSystemRecordSeparator(self) -> CSVFormat:
        return self.builder().setRecordSeparator1(os.linesep).build()

    def withSkipHeaderRecord1(self, skipHeaderRecord: bool) -> CSVFormat:
        return self.builder().setSkipHeaderRecord(skipHeaderRecord).build()

    def withSkipHeaderRecord0(self) -> CSVFormat:
        return self.builder().setSkipHeaderRecord(True).build()

    def withRecordSeparator1(self, recordSeparator: str) -> CSVFormat:
        return self.builder().setRecordSeparator1(recordSeparator).build()

    def withRecordSeparator0(self, recordSeparator: str) -> CSVFormat:
        return self.builder().setRecordSeparator0(recordSeparator).build()

    def withQuoteMode(self, quoteMode: QuoteMode) -> CSVFormat:
        return self.builder().setQuoteMode(quoteMode).build()

    def withQuote1(self, quoteChar: str) -> CSVFormat:
        return self.builder().setQuote1(quoteChar).build()

    def withQuote0(self, quoteChar: str) -> CSVFormat:
        return self.builder().setQuote0(quoteChar).build()

    def withNullString(self, nullString: str) -> CSVFormat:
        return self.builder().setNullString(nullString).build()

    def withIgnoreSurroundingSpaces1(self, ignoreSurroundingSpaces: bool) -> CSVFormat:
        return (
            self.builder().setIgnoreSurroundingSpaces(ignoreSurroundingSpaces).build()
        )

    def withIgnoreSurroundingSpaces0(self) -> CSVFormat:
        return self.builder().setIgnoreSurroundingSpaces(True).build()

    def withIgnoreHeaderCase1(self, ignoreHeaderCase: bool) -> CSVFormat:
        return self.builder().setIgnoreHeaderCase(ignoreHeaderCase).build()

    def withIgnoreHeaderCase0(self) -> CSVFormat:
        return self.builder().setIgnoreHeaderCase(True).build()

    def withIgnoreEmptyLines1(self, ignoreEmptyLines: bool) -> CSVFormat:
        return self.builder().setIgnoreEmptyLines(ignoreEmptyLines).build()

    def withIgnoreEmptyLines0(self) -> CSVFormat:
        return self.builder().setIgnoreEmptyLines(True).build()

    def withHeaderComments(self, headerComments: typing.List[typing.Any]) -> CSVFormat:
        return self.builder().setHeaderComments0(headerComments).build()

    def withEscape1(self, escape: str) -> CSVFormat:
        return self.builder().setEscape1(escape).build()

    def withEscape0(self, escape: str) -> CSVFormat:
        return self.builder().setEscape0(escape).build()

    def withDelimiter(self, delimiter: str) -> CSVFormat:
        return self.builder().setDelimiter0(delimiter).build()

    def withCommentMarker1(self, commentMarker: str) -> CSVFormat:
        return self.builder().setCommentMarker1(commentMarker).build()

    def withCommentMarker0(self, commentMarker: str) -> CSVFormat:
        return self.builder().setCommentMarker0(commentMarker).build()

    def withAutoFlush(self, autoFlush: bool) -> CSVFormat:
        return self.builder().setAutoFlush(autoFlush).build()

    def withAllowMissingColumnNames1(self, allowMissingColumnNames: bool) -> CSVFormat:
        return (
            self.builder().setAllowMissingColumnNames(allowMissingColumnNames).build()
        )

    def withAllowMissingColumnNames0(self) -> CSVFormat:
        return self.builder().setAllowMissingColumnNames(True).build()

    def withAllowDuplicateHeaderNames1(
        self, allowDuplicateHeaderNames: bool
    ) -> CSVFormat:
        mode = (
            DuplicateHeaderMode.ALLOW_ALL
            if allowDuplicateHeaderNames
            else DuplicateHeaderMode.ALLOW_EMPTY
        )
        return self.builder().setDuplicateHeaderMode(mode).build()

    def withAllowDuplicateHeaderNames0(self) -> CSVFormat:
        return (
            self.builder().setDuplicateHeaderMode(DuplicateHeaderMode.ALLOW_ALL).build()
        )

    def toString(self) -> str:
        sb = StringBuilder()
        sb.append("Delimiter=<").append(self.__delimiter).append(">")
        if self.isEscapeCharacterSet():
            sb.append(" ")
            sb.append("Escape=<").append(self.__escapeCharacter).append(">")
        if self.isQuoteCharacterSet():
            sb.append(" ")
            sb.append("QuoteChar=<").append(self.__quoteCharacter).append(">")
        if self.__quoteMode is not None:
            sb.append(" ")
            sb.append("QuoteMode=<").append(self.__quoteMode).append(">")
        if self.isCommentMarkerSet():
            sb.append(" ")
            sb.append("CommentStart=<").append(self.__commentMarker).append(">")
        if self.isNullStringSet():
            sb.append(" ")
            sb.append("NullString=<").append(self.__nullString).append(">")
        if self.__recordSeparator is not None:
            sb.append(" ")
            sb.append("RecordSeparator=<").append(self.__recordSeparator).append(">")
        if self.getIgnoreEmptyLines():
            sb.append(" EmptyLines:ignored")
        if self.getIgnoreSurroundingSpaces():
            sb.append(" SurroundingSpaces:ignored")
        if self.getIgnoreHeaderCase():
            sb.append(" IgnoreHeaderCase:ignored")
        sb.append(" SkipHeaderRecord:").append(str(self.__skipHeaderRecord))
        if self.__headerComments is not None:
            sb.append(" ")
            sb.append("HeaderComments:").append(str(self.__headerComments))
        if self.__headers is not None:
            sb.append(" ")
            sb.append("Header:").append(str(self.__headers))
        return str(sb)

    def print4(self, out: Path, charset: str) -> CSVPrinter:
        return self.print0(io.TextIOWrapper(io.FileIO(out, "w"), charset))

    def print1(self, out: pathlib.Path, charset: str) -> CSVPrinter:
        return CSVPrinter(
            io.TextIOWrapper(io.FileIO(out, mode="w"), encoding=charset), self
        )

    def hashCode(self) -> int:
        prime = 31
        result = 1
        result = prime * result + hash(tuple(self.__headers))
        result = prime * result + hash(tuple(self.__headerComments))
        return prime * result + hash(
            (
                self.__duplicateHeaderMode,
                self.__allowMissingColumnNames,
                self.__autoFlush,
                self.__commentMarker,
                self.__delimiter,
                self.__escapeCharacter,
                self.__ignoreEmptyLines,
                self.__ignoreHeaderCase,
                self.__ignoreSurroundingSpaces,
                self.__nullString,
                self.__quoteCharacter,
                self.__quoteMode,
                self.__quotedNullString,
                self.__recordSeparator,
                self.__skipHeaderRecord,
                self.__trailingDelimiter,
                self.__trim,
            )
        )

    def getDelimiter(self) -> str:
        return self.__delimiter[0]

    def getAllowDuplicateHeaderNames(self) -> bool:
        return self.__duplicateHeaderMode == DuplicateHeaderMode.ALLOW_ALL

    def equals(self, obj: typing.Any) -> bool:
        if self is obj:
            return True
        if obj is None or type(self) != type(obj):
            return False
        other: CSVFormat = obj
        return (
            self.__duplicateHeaderMode == other.__duplicateHeaderMode
            and self.__allowMissingColumnNames == other.__allowMissingColumnNames
            and self.__autoFlush == other.__autoFlush
            and self.__commentMarker == other.__commentMarker
            and self.__delimiter == other.__delimiter
            and self.__escapeCharacter == other.__escapeCharacter
            and self.__headers == other.__headers
            and self.__headerComments == other.__headerComments
            and self.__ignoreEmptyLines == other.__ignoreEmptyLines
            and self.__ignoreHeaderCase == other.__ignoreHeaderCase
            and self.__ignoreSurroundingSpaces == other.__ignoreSurroundingSpaces
            and self.__nullString == other.__nullString
            and self.__quoteCharacter == other.__quoteCharacter
            and self.__quoteMode == other.__quoteMode
            and self.__quotedNullString == other.__quotedNullString
            and self.__recordSeparator == other.__recordSeparator
            and self.__skipHeaderRecord == other.__skipHeaderRecord
            and self.__trailingDelimiter == other.__trailingDelimiter
            and self.__trim == other.__trim
        )

    @staticmethod
    def clone(values: typing.List[typing.Any]) -> typing.List[typing.Any]:
        return values.copy() if values is not None else None

    def printRecord(
        self,
        appendable: typing.Union[typing.List, io.TextIOBase],
        values: typing.List[typing.Any],
    ) -> None:
        for i, value in enumerate(values):
            self.print2(value, appendable, i == 0)
        self.println(appendable)

    def println(self, appendable: typing.Union[typing.List, io.TextIOBase]) -> None:
        if self.getTrailingDelimiter():
            self.__append1(self.getDelimiterString(), appendable)
        if self.__recordSeparator != "":
            self.__append1(self.__recordSeparator, appendable)

    def printer(self) -> CSVPrinter:
        return CSVPrinter(io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8"), self)

    def print2(
        self,
        value: typing.Any,
        out: typing.Union[typing.List, io.TextIOBase],
        newRecord: bool,
    ) -> None:
        char_sequence: str
        if value is None:
            if self.__nullString is None:
                char_sequence = Constants.EMPTY
            elif self.__quoteMode == QuoteMode.ALL:
                char_sequence = self.__quotedNullString
            else:
                char_sequence = self.__nullString
        elif isinstance(value, str):
            char_sequence = value
        elif isinstance(value, io.TextIOWrapper):
            self.__print5(value, out, newRecord)
            return
        else:
            char_sequence = str(value)
        char_sequence = (
            self.getTrim() and CSVFormat.trim0(char_sequence) or char_sequence
        )
        self.__print3(value, char_sequence, out, newRecord)

    def print0(self, out: typing.Union[typing.List, io.TextIOBase]) -> CSVPrinter:
        return CSVPrinter(out, self)

    def parse(
        self, reader: typing.Union[io.TextIOWrapper, io.BufferedReader]
    ) -> CSVParser:
        return CSVParser.CSVParser1(reader, self)

    def isQuoteCharacterSet(self) -> bool:
        return self.__quoteCharacter != ""

    def isNullStringSet(self) -> bool:
        return self.__nullString is not None

    def isEscapeCharacterSet(self) -> bool:
        return self.__escapeCharacter != ""

    def isCommentMarkerSet(self) -> bool:
        return self.__commentMarker != ""

    def getTrim(self) -> bool:
        return self.__trim

    def getTrailingDelimiter(self) -> bool:
        return self.__trailingDelimiter

    def getSkipHeaderRecord(self) -> bool:
        return self.__skipHeaderRecord

    def getRecordSeparator(self) -> str:
        return self.__recordSeparator

    def getQuoteMode(self) -> QuoteMode:
        return self.__quoteMode

    def getQuoteCharacter(self) -> str:
        return self.__quoteCharacter

    def getNullString(self) -> str:
        return self.__nullString

    def getIgnoreSurroundingSpaces(self) -> bool:
        return self.__ignoreSurroundingSpaces

    def getIgnoreHeaderCase(self) -> bool:
        return self.__ignoreHeaderCase

    def getIgnoreEmptyLines(self) -> bool:
        return self.__ignoreEmptyLines

    def getHeaderComments(self) -> typing.List[str]:
        return (
            self.__headerComments.copy() if self.__headerComments is not None else None
        )

    def getHeader(self) -> typing.List[str]:
        return self.__headers.copy() if self.__headers is not None else None

    def getEscapeCharacter(self) -> str:
        return self.__escapeCharacter

    def getDuplicateHeaderMode(self) -> DuplicateHeaderMode:
        return self.__duplicateHeaderMode

    def getDelimiterString(self) -> str:
        return self.__delimiter

    def getCommentMarker(self) -> str:
        return self.__commentMarker

    def getAutoFlush(self) -> bool:
        return self.__autoFlush

    def getAllowMissingColumnNames(self) -> bool:
        return self.__allowMissingColumnNames

    def format(self, values: typing.List[typing.Any]) -> str:
        out = io.StringIO()
        try:
            csv_printer = CSVPrinter(out, self)
            csv_printer.printRecord1(values)
            res = out.getvalue()
            len = (
                len(res) - len(self.__recordSeparator)
                if self.__recordSeparator
                else len(res)
            )
            return res[:len]
        except io.IOError as e:
            raise Exception(e)

    def builder(self) -> Builder:
        return Builder.create1(self)

    def __init__(
        self,
        constructorId: int,
        autoFlush: bool,
        skipHeaderRecord: bool,
        delimiter: str,
        nullString: str,
        escape: str,
        ignoreSurroundingSpaces: bool,
        trim: bool,
        builder: Builder,
        commentStart: str,
        ignoreHeaderCase: bool,
        quoteChar: str,
        quoteMode: QuoteMode,
        ignoreEmptyLines: bool,
        duplicateHeaderMode: DuplicateHeaderMode,
        header: typing.List[str],
        allowMissingColumnNames: bool,
        trailingDelimiter: bool,
        headerComments: typing.List[typing.Any],
        recordSeparator: str,
    ) -> None:
        if constructorId == 0:
            self.__delimiter = delimiter
            self.__quoteCharacter = quoteChar
            self.__quoteMode = quoteMode
            self.__commentMarker = commentStart
            self.__escapeCharacter = escape
            self.__ignoreSurroundingSpaces = ignoreSurroundingSpaces
            self.__allowMissingColumnNames = allowMissingColumnNames
            self.__ignoreEmptyLines = ignoreEmptyLines
            self.__recordSeparator = recordSeparator
            self.__nullString = nullString
            self.__headerComments = CSVFormat.toStringArray(headerComments)
            self.__headers = CSVFormat.clone(header)
            self.__skipHeaderRecord = skipHeaderRecord
            self.__ignoreHeaderCase = ignoreHeaderCase
            self.__trailingDelimiter = trailingDelimiter
            self.__trim = trim
            self.__autoFlush = autoFlush
            self.__quotedNullString = quoteChar + nullString + quoteChar
            self.__duplicateHeaderMode = duplicateHeaderMode
            self.__validate()
        else:
            self.__delimiter = builder.__delimiter
            self.__quoteCharacter = builder.__quoteCharacter
            self.__quoteMode = builder.__quoteMode
            self.__commentMarker = builder.__commentMarker
            self.__escapeCharacter = builder.__escapeCharacter
            self.__ignoreSurroundingSpaces = builder.__ignoreSurroundingSpaces
            self.__allowMissingColumnNames = builder.__allowMissingColumnNames
            self.__ignoreEmptyLines = builder.__ignoreEmptyLines
            self.__recordSeparator = builder.__recordSeparator
            self.__nullString = builder.__nullString
            self.__headerComments = builder.__headerComments
            self.__headers = builder.__headers
            self.__skipHeaderRecord = builder.__skipHeaderRecord
            self.__ignoreHeaderCase = builder.__ignoreHeaderCase
            self.__trailingDelimiter = builder.__trailingDelimiter
            self.__trim = builder.__trim
            self.__autoFlush = builder.__autoFlush
            self.__quotedNullString = builder.__quotedNullString
            self.__duplicateHeaderMode = builder.__duplicateHeaderMode
            self.__validate()

    @staticmethod
    def valueOf(format: str) -> CSVFormat:
        return Predefined.valueOf(format).getFormat()

    @staticmethod
    def trim0(charSequence: str) -> str:
        if isinstance(charSequence, str):
            return charSequence.strip()
        count = len(charSequence)
        len_trim = count
        pos = 0

        while pos < len_trim and CSVFormat.__isTrimChar1(charSequence, pos):
            pos += 1
        while pos < len_trim and CSVFormat.__isTrimChar1(charSequence, len_trim - 1):
            len_trim -= 1
        return (
            charSequence[pos:len_trim] if pos > 0 or len_trim < count else charSequence
        )

    @staticmethod
    def toStringArray(values: typing.List[typing.Any]) -> typing.List[str]:
        if values is None:
            return None
        strings = [str(value) if value is not None else "" for value in values]
        return strings

    @staticmethod
    def newFormat(delimiter: str) -> CSVFormat:
        return CSVFormat(
            0,
            False,
            False,
            delimiter,
            None,
            None,
            False,
            False,
            None,
            None,
            False,
            None,
            None,
            False,
            DuplicateHeaderMode.ALLOW_ALL,
            None,
            False,
            False,
            None,
            None,
        )

    @staticmethod
    def isBlank(value: str) -> bool:
        return value is None or value.strip() == ""

    def __validate(self) -> None:
        if CSVFormat.__containsLineBreak(self.__delimiter):
            raise ValueError("The delimiter cannot be a line break")

        if self.__quoteCharacter is not None and CSVFormat.__contains(
            self.__delimiter, self.__quoteCharacter
        ):
            raise ValueError(
                f"The quoteChar character and the delimiter cannot be the same ('{self.__quoteCharacter}')"
            )

        if self.__escapeCharacter is not None and CSVFormat.__contains(
            self.__delimiter, self.__escapeCharacter
        ):
            raise ValueError(
                f"The escape character and the delimiter cannot be the same ('{self.__escapeCharacter}')"
            )

        if self.__commentMarker is not None and CSVFormat.__contains(
            self.__delimiter, self.__commentMarker
        ):
            raise ValueError(
                f"The comment start character and the delimiter cannot be the same ('{self.__commentMarker}')"
            )

        if (
            self.__quoteCharacter is not None
            and self.__quoteCharacter == self.__commentMarker
        ):
            raise ValueError(
                f"The comment start character and the quoteChar cannot be the same ('{self.__commentMarker}')"
            )

        if (
            self.__escapeCharacter is not None
            and self.__escapeCharacter == self.__commentMarker
        ):
            raise ValueError(
                f"The comment start and the escape character cannot be the same ('{self.__commentMarker}')"
            )

        if self.__escapeCharacter is None and self.__quoteMode == QuoteMode.NONE:
            raise ValueError("No quotes mode set but no escape character is set")

        if (
            self.__headers is not None
            and self.__duplicateHeaderMode != DuplicateHeaderMode.ALLOW_ALL
        ):
            dupCheckSet = set()
            emptyDuplicatesAllowed = (
                self.__duplicateHeaderMode == DuplicateHeaderMode.ALLOW_EMPTY
            )
            for header in self.__headers:
                blank = CSVFormat.isBlank(header)
                containsHeader = not dupCheckSet.add(header if not blank else "")
                if containsHeader and not (blank and emptyDuplicatesAllowed):
                    raise ValueError(
                        f'The header contains a duplicate name: "{header}" in {self.__headers}. If this is valid then use CSVFormat.Builder.setDuplicateHeaderMode().'
                    )

    def __printWithQuotes1(
        self,
        reader: typing.Union[io.TextIOWrapper, io.BufferedReader],
        appendable: typing.Union[typing.List, io.TextIOBase],
    ) -> None:
        if self.getQuoteMode() == QuoteMode.NONE:
            self.__printWithEscapes1(reader, appendable)
            return

        pos = 0

        quote = self.getQuoteCharacter()
        builder = io.StringIO()

        self.__append0(quote, appendable)

        c = reader.read(1)
        while c:
            builder.write(c)
            if c == quote:
                if pos > 0:
                    self.__append1(builder.getvalue()[:pos], appendable)
                    self.__append0(quote, appendable)
                    builder.seek(0)
                    builder.truncate(0)
                    pos = -1

                self.__append0(c, appendable)
            pos += 1

        if pos > 0:
            self.__append1(builder.getvalue()[:pos], appendable)

        self.__append0(quote, appendable)

    def __printWithQuotes0(
        self,
        object: typing.Any,
        charSeq: str,
        out: typing.Union[typing.List, io.TextIOBase],
        newRecord: bool,
    ) -> None:
        quote = False
        start = 0
        pos = 0
        len_charSeq = len(charSeq)

        delim = list(self.getDelimiterString())
        delimLength = len(delim)
        quoteChar = self.getQuoteCharacter()
        escapeChar = (
            self.getEscapeCharacter() if self.isEscapeCharacterSet() else quoteChar
        )

        quoteModePolicy = self.getQuoteMode()
        if quoteModePolicy is None:
            quoteModePolicy = QuoteMode.MINIMAL

        if (
            quoteModePolicy == QuoteMode.ALL
            or quoteModePolicy == QuoteMode.ALL_NON_NULL
        ):
            quote = True
        elif quoteModePolicy == QuoteMode.NON_NUMERIC:
            quote = not isinstance(object, numbers.Number)
        elif quoteModePolicy == QuoteMode.NONE:
            self.__printWithEscapes0(charSeq, out)
            return
        elif quoteModePolicy == QuoteMode.MINIMAL:
            if len_charSeq <= 0:
                if newRecord:
                    quote = True
            else:
                c = charSeq[pos]

                if c <= Constants.COMMENT:
                    quote = True
                else:
                    while pos < len_charSeq:
                        c = charSeq[pos]
                        if (
                            c == Constants.LF
                            or c == Constants.CR
                            or c == quoteChar
                            or c == escapeChar
                            or self.__isDelimiter(c, charSeq, pos, delim, delimLength)
                        ):
                            quote = True
                            break
                        pos += 1

                    if not quote:
                        pos = len_charSeq - 1
                        c = charSeq[pos]
                        if self.__isTrimChar0(c):
                            quote = True

            if not quote:
                out.append(charSeq[start:len_charSeq])
                return
        else:
            raise RuntimeError("Unexpected Quote value: " + quoteModePolicy)

        if not quote:
            out.append(charSeq[start:len_charSeq])
            return

        out.append(quoteChar)

        while pos < len_charSeq:
            c = charSeq[pos]
            if c == quoteChar or c == escapeChar:
                out.append(charSeq[start:pos])
                out.append(escapeChar)  # now output the escape
                start = pos  # and restart with the matched char
            pos += 1

        out.append(charSeq[start:pos])
        out.append(quoteChar)

    def __printWithEscapes1(
        self,
        reader: typing.Union[io.TextIOWrapper, io.BufferedReader],
        appendable: typing.Union[typing.List, io.TextIOBase],
    ) -> None:

        pass  # LLM could not translate this method

    def __printWithEscapes0(
        self, charSeq: str, appendable: typing.Union[typing.List, io.TextIOBase]
    ) -> None:
        start = 0
        pos = 0
        end = len(charSeq)

        delim = list(self.getDelimiterString())
        delimLength = len(delim)
        escape = self.getEscapeCharacter()

        while pos < end:
            c = charSeq[pos]
            isDelimiterStart = self.__isDelimiter(c, charSeq, pos, delim, delimLength)
            if c in [Constants.CR, Constants.LF, escape] or isDelimiterStart:
                if pos > start:
                    appendable.append(charSeq[start:pos])
                if c == Constants.LF:
                    c = "n"
                elif c == Constants.CR:
                    c = "r"

                appendable.append(escape)
                appendable.append(c)

                if isDelimiterStart:
                    for i in range(1, delimLength):
                        pos += 1
                        c = charSeq[pos]
                        appendable.append(escape)
                        appendable.append(c)

                start = pos + 1  # start on the current char after this one
            pos += 1

        if pos > start:
            appendable.append(charSeq[start:pos])

    def __print5(
        self,
        reader: typing.Union[io.TextIOWrapper, io.BufferedReader],
        out: typing.Union[typing.List, io.TextIOBase],
        newRecord: bool,
    ) -> None:
        if not newRecord:
            self.__append1(self.getDelimiterString(), out)
        if self.isQuoteCharacterSet():
            self.__printWithQuotes1(reader, out)
        elif self.isEscapeCharacterSet():
            self.__printWithEscapes1(reader, out)
        elif isinstance(out, io.TextIOWrapper):
            IOUtils.copyLarge0(reader, out)
        else:
            IOUtils.copy0(reader, out)

    def __print3(
        self,
        object: typing.Any,
        value: str,
        out: typing.Union[typing.List, io.TextIOBase],
        newRecord: bool,
    ) -> None:
        offset = 0
        length = len(value)
        if not newRecord:
            out.append(self.getDelimiterString())
        if object is None:
            out.append(value)
        elif self.isQuoteCharacterSet():
            self.__printWithQuotes0(object, value, out, newRecord)
        elif self.isEscapeCharacterSet():
            self.__printWithEscapes0(value, out)
        else:
            out.append(value[offset:length])

    def __isDelimiter(
        self,
        ch: str,
        charSeq: str,
        startIndex: int,
        delimiter: typing.List[str],
        delimiterLength: int,
    ) -> bool:
        if ch != delimiter[0]:
            return False
        len_charSeq = len(charSeq)
        if startIndex + delimiterLength > len_charSeq:
            return False
        for i in range(1, delimiterLength):
            if charSeq[startIndex + i] != delimiter[i]:
                return False
        return True

    def __append1(
        self, csq: str, appendable: typing.Union[typing.List, io.TextIOBase]
    ) -> None:
        appendable.append(csq)

    def __append0(
        self, c: str, appendable: typing.Union[typing.List, io.TextIOBase]
    ) -> None:
        appendable.append(c)

    @staticmethod
    def __isTrimChar1(charSequence: str, pos: int) -> bool:
        return CSVFormat.__isTrimChar0(charSequence[pos])

    @staticmethod
    def __isTrimChar0(ch: str) -> bool:
        return ch <= Constants.SP

    @staticmethod
    def __isLineBreak1(c: str) -> bool:
        return c is not None and CSVFormat.__isLineBreak0(c)

    @staticmethod
    def __isLineBreak0(c: str) -> bool:
        return c == Constants.LF or c == Constants.CR

    @staticmethod
    def __containsLineBreak(source: str) -> bool:
        return CSVFormat.__contains(source, Constants.CR) or CSVFormat.__contains(
            source, Constants.LF
        )

    @staticmethod
    def __contains(source: str, searchCh: str) -> bool:
        return source is not None and source.find(searchCh) >= 0

    def trim1(self, value: str) -> str:
        return value.strip() if self.getTrim() else value

    def copy(self) -> CSVFormat:
        return self.builder().build()


CSVFormat.initialize_fields()
