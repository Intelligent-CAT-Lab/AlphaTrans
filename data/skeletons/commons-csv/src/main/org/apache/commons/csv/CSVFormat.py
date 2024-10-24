from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.csv.QuoteMode import *
from src.main.org.apache.commons.csv.IOUtils import *
from src.main.org.apache.commons.csv.ExtendedBufferedReader import *
from src.main.org.apache.commons.csv.DuplicateHeaderMode import *
from src.main.org.apache.commons.csv.Constants import *
from src.main.org.apache.commons.csv.CSVPrinter import *
from src.main.org.apache.commons.csv.CSVParser import *
import os
import typing
from typing import *
import io
from io import IOBase
import pathlib

# Imports End


class Builder:

    # Class Fields Begin
    __allowMissingColumnNames: bool = None
    __autoFlush: bool = None
    __commentMarker: str = None
    __delimiter: str = None
    __duplicateHeaderMode: DuplicateHeaderMode = None
    __escapeCharacter: str = None
    __headerComments: typing.List[typing.List[str]] = None
    __headers: typing.List[typing.List[str]] = None
    __ignoreEmptyLines: bool = None
    __ignoreHeaderCase: bool = None
    __ignoreSurroundingSpaces: bool = None
    __nullString: str = None
    __quoteCharacter: str = None
    __quotedNullString: str = None
    __quoteMode: QuoteMode = None
    __recordSeparator: str = None
    __skipHeaderRecord: bool = None
    __trailingDelimiter: bool = None
    __trim: bool = None
    # Class Fields End

    # Class Methods Begin
    def setAllowDuplicateHeaderNames(self, allowDuplicateHeaderNames: bool) -> Builder:
        pass

    def setTrim(self, trim: bool) -> Builder:
        pass

    def setTrailingDelimiter(self, trailingDelimiter: bool) -> Builder:
        pass

    def setSkipHeaderRecord(self, skipHeaderRecord: bool) -> Builder:
        pass

    def setRecordSeparator1(self, recordSeparator: str) -> Builder:
        pass

    def setRecordSeparator0(self, recordSeparator: str) -> Builder:
        pass

    def setQuoteMode(self, quoteMode: QuoteMode) -> Builder:
        pass

    def setQuote1(self, quoteCharacter: str) -> Builder:
        pass

    def setQuote0(self, quoteCharacter: str) -> Builder:
        pass

    def setNullString(self, nullString: str) -> Builder:
        pass

    def setIgnoreSurroundingSpaces(self, ignoreSurroundingSpaces: bool) -> Builder:
        pass

    def setIgnoreHeaderCase(self, ignoreHeaderCase: bool) -> Builder:
        pass

    def setIgnoreEmptyLines(self, ignoreEmptyLines: bool) -> Builder:
        pass

    def setHeaderComments1(
        self, headerComments: typing.List[typing.List[str]]
    ) -> Builder:
        pass

    def setHeaderComments0(self, headerComments: typing.List[typing.Any]) -> Builder:
        pass

    def setEscape1(self, escapeCharacter: str) -> Builder:
        pass

    def setEscape0(self, escapeCharacter: str) -> Builder:
        pass

    def setDuplicateHeaderMode(
        self, duplicateHeaderMode: DuplicateHeaderMode
    ) -> Builder:
        pass

    def setDelimiter1(self, delimiter: str) -> Builder:
        pass

    def setDelimiter0(self, delimiter: str) -> Builder:
        pass

    def setCommentMarker1(self, commentMarker: str) -> Builder:
        pass

    def setCommentMarker0(self, commentMarker: str) -> Builder:
        pass

    def setAutoFlush(self, autoFlush: bool) -> Builder:
        pass

    def setAllowMissingColumnNames(self, allowMissingColumnNames: bool) -> Builder:
        pass

    def build(self) -> CSVFormat:
        pass

    @staticmethod
    def create1(csvFormat: CSVFormat) -> Builder:
        pass

    @staticmethod
    def create0() -> Builder:
        pass

    def __init__(self, csvFormat: CSVFormat) -> None:
        pass

    # Class Methods End


class Predefined:

    # Class Fields Begin
    Default: Predefined = None
    Excel: Predefined = None
    InformixUnload: Predefined = None
    InformixUnloadCsv: Predefined = None
    MongoDBCsv: Predefined = None
    MongoDBTsv: Predefined = None
    MySQL: Predefined = None
    Oracle: Predefined = None
    PostgreSQLCsv: Predefined = None
    PostgreSQLText: Predefined = None
    RFC4180: Predefined = None
    TDF: Predefined = None
    __format: CSVFormat = None
    # Class Fields End

    # Class Methods Begin
    def getFormat(self) -> CSVFormat:
        pass

    def __init__(self, format_: CSVFormat) -> None:
        pass

    # Class Methods End


class CSVFormat:

    # Class Fields Begin
    ORACLE: CSVFormat = None
    POSTGRESQL_CSV: CSVFormat = None
    POSTGRESQL_TEXT: CSVFormat = None
    RFC4180: CSVFormat = None
    __serialVersionUID: int = None
    TDF: CSVFormat = None
    __duplicateHeaderMode: DuplicateHeaderMode = None
    __allowMissingColumnNames: bool = None
    __autoFlush: bool = None
    __commentMarker: str = None
    __delimiter: str = None
    __escapeCharacter: str = None
    __headers: typing.List[typing.List[str]] = None
    __headerComments: typing.List[typing.List[str]] = None
    __ignoreEmptyLines: bool = None
    __ignoreHeaderCase: bool = None
    __ignoreSurroundingSpaces: bool = None
    __nullString: str = None
    __quoteCharacter: str = None
    __quotedNullString: str = None
    __quoteMode: QuoteMode = None
    __recordSeparator: str = None
    __skipHeaderRecord: bool = None
    __trailingDelimiter: bool = None
    __trim: bool = None
    DEFAULT: CSVFormat = None
    EXCEL: CSVFormat = None
    INFORMIX_UNLOAD: CSVFormat = None
    INFORMIX_UNLOAD_CSV: CSVFormat = None
    MONGODB_CSV: CSVFormat = None
    MONGODB_TSV: CSVFormat = None
    MYSQL: CSVFormat = None
    # Class Fields End

    # Class Methods Begin
    def withTrim1(self, trim: bool) -> CSVFormat:
        pass

    def withTrim0(self) -> CSVFormat:
        pass

    def withTrailingDelimiter1(self, trailingDelimiter: bool) -> CSVFormat:
        pass

    def withTrailingDelimiter0(self) -> CSVFormat:
        pass

    def withSystemRecordSeparator(self) -> CSVFormat:
        pass

    def withSkipHeaderRecord1(self, skipHeaderRecord: bool) -> CSVFormat:
        pass

    def withSkipHeaderRecord0(self) -> CSVFormat:
        pass

    def withRecordSeparator1(self, recordSeparator: str) -> CSVFormat:
        pass

    def withRecordSeparator0(self, recordSeparator: str) -> CSVFormat:
        pass

    def withQuoteMode(self, quoteMode: QuoteMode) -> CSVFormat:
        pass

    def withQuote1(self, quoteChar: str) -> CSVFormat:
        pass

    def withQuote0(self, quoteChar: str) -> CSVFormat:
        pass

    def withNullString(self, nullString: str) -> CSVFormat:
        pass

    def withIgnoreSurroundingSpaces1(self, ignoreSurroundingSpaces: bool) -> CSVFormat:
        pass

    def withIgnoreSurroundingSpaces0(self) -> CSVFormat:
        pass

    def withIgnoreHeaderCase1(self, ignoreHeaderCase: bool) -> CSVFormat:
        pass

    def withIgnoreHeaderCase0(self) -> CSVFormat:
        pass

    def withIgnoreEmptyLines1(self, ignoreEmptyLines: bool) -> CSVFormat:
        pass

    def withIgnoreEmptyLines0(self) -> CSVFormat:
        pass

    def withHeaderComments(self, headerComments: typing.List[typing.Any]) -> CSVFormat:
        pass

    def withEscape1(self, escape: str) -> CSVFormat:
        pass

    def withEscape0(self, escape: str) -> CSVFormat:
        pass

    def withDelimiter(self, delimiter: str) -> CSVFormat:
        pass

    def withCommentMarker1(self, commentMarker: str) -> CSVFormat:
        pass

    def withCommentMarker0(self, commentMarker: str) -> CSVFormat:
        pass

    def withAutoFlush(self, autoFlush: bool) -> CSVFormat:
        pass

    def withAllowMissingColumnNames1(self, allowMissingColumnNames: bool) -> CSVFormat:
        pass

    def withAllowMissingColumnNames0(self) -> CSVFormat:
        pass

    def withAllowDuplicateHeaderNames1(
        self, allowDuplicateHeaderNames: bool
    ) -> CSVFormat:
        pass

    def withAllowDuplicateHeaderNames0(self) -> CSVFormat:
        pass

    def toString(self) -> str:
        pass

    def print4(self, out: Path, charset: str) -> CSVPrinter:
        pass

    def print1(self, out: pathlib.Path, charset: str) -> CSVPrinter:
        pass

    def hashCode(self) -> int:
        pass

    def getDelimiter(self) -> str:
        pass

    def getAllowDuplicateHeaderNames(self) -> bool:
        pass

    def equals(self, obj: typing.Any) -> bool:
        pass

    @staticmethod
    def clone(values: typing.List[typing.Any]) -> typing.List[typing.Any]:
        pass

    def printRecord(
        self,
        appendable: typing.Union[typing.List, io.TextIOBase],
        values: typing.List[typing.Any],
    ) -> None:
        pass

    def println(self, appendable: typing.Union[typing.List, io.TextIOBase]) -> None:
        pass

    def printer(self) -> CSVPrinter:
        pass

    def print2(
        self,
        value: typing.Any,
        out: typing.Union[typing.List, io.TextIOBase],
        newRecord: bool,
    ) -> None:
        pass

    def print0(self, out: typing.Union[typing.List, io.TextIOBase]) -> CSVPrinter:
        pass

    def parse(
        self, reader: typing.Union[io.TextIOWrapper, io.BufferedReader, io.TextIOBase]
    ) -> CSVParser:
        pass

    def isQuoteCharacterSet(self) -> bool:
        pass

    def isNullStringSet(self) -> bool:
        pass

    def isEscapeCharacterSet(self) -> bool:
        pass

    def isCommentMarkerSet(self) -> bool:
        pass

    def getTrim(self) -> bool:
        pass

    def getTrailingDelimiter(self) -> bool:
        pass

    def getSkipHeaderRecord(self) -> bool:
        pass

    def getRecordSeparator(self) -> str:
        pass

    def getQuoteMode(self) -> QuoteMode:
        pass

    def getQuoteCharacter(self) -> str:
        pass

    def getNullString(self) -> str:
        pass

    def getIgnoreSurroundingSpaces(self) -> bool:
        pass

    def getIgnoreHeaderCase(self) -> bool:
        pass

    def getIgnoreEmptyLines(self) -> bool:
        pass

    def getHeaderComments(self) -> typing.List[typing.List[str]]:
        pass

    def getHeader(self) -> typing.List[typing.List[str]]:
        pass

    def getEscapeCharacter(self) -> str:
        pass

    def getDuplicateHeaderMode(self) -> DuplicateHeaderMode:
        pass

    def getDelimiterString(self) -> str:
        pass

    def getCommentMarker(self) -> str:
        pass

    def getAutoFlush(self) -> bool:
        pass

    def getAllowMissingColumnNames(self) -> bool:
        pass

    def format_(self, values: typing.List[typing.Any]) -> str:
        pass

    def builder(self) -> Builder:
        pass

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
        header: typing.List[typing.List[str]],
        allowMissingColumnNames: bool,
        trailingDelimiter: bool,
        headerComments: typing.List[typing.Any],
        recordSeparator: str,
    ) -> None:
        pass

    @staticmethod
    def valueOf(format_: str) -> CSVFormat:
        pass

    @staticmethod
    def trim0(charSequence: str) -> str:
        pass

    @staticmethod
    def toStringArray(values: typing.List[typing.Any]) -> typing.List[typing.List[str]]:
        pass

    @staticmethod
    def newFormat(delimiter: str) -> CSVFormat:
        pass

    @staticmethod
    def isBlank(value: str) -> bool:
        pass

    def __validate(self) -> None:
        pass

    def __printWithQuotes1(
        self,
        reader: typing.Union[io.TextIOWrapper, io.BufferedReader, io.TextIOBase],
        appendable: typing.Union[typing.List, io.TextIOBase],
    ) -> None:
        pass

    def __printWithQuotes0(
        self,
        object_: typing.Any,
        charSeq: str,
        out: typing.Union[typing.List, io.TextIOBase],
        newRecord: bool,
    ) -> None:
        pass

    def __printWithEscapes1(
        self,
        reader: typing.Union[io.TextIOWrapper, io.BufferedReader, io.TextIOBase],
        appendable: typing.Union[typing.List, io.TextIOBase],
    ) -> None:
        pass

    def __printWithEscapes0(
        self, charSeq: str, appendable: typing.Union[typing.List, io.TextIOBase]
    ) -> None:
        pass

    def __print5(
        self,
        reader: typing.Union[io.TextIOWrapper, io.BufferedReader, io.TextIOBase],
        out: typing.Union[typing.List, io.TextIOBase],
        newRecord: bool,
    ) -> None:
        pass

    def __print3(
        self,
        object_: typing.Any,
        value: str,
        out: typing.Union[typing.List, io.TextIOBase],
        newRecord: bool,
    ) -> None:
        pass

    def __isDelimiter(
        self,
        ch: str,
        charSeq: str,
        startIndex: int,
        delimiter: typing.List[str],
        delimiterLength: int,
    ) -> bool:
        pass

    def __append1(
        self, csq: str, appendable: typing.Union[typing.List, io.TextIOBase]
    ) -> None:
        pass

    def __append0(
        self, c: str, appendable: typing.Union[typing.List, io.TextIOBase]
    ) -> None:
        pass

    @staticmethod
    def __isTrimChar1(charSequence: str, pos: int) -> bool:
        pass

    @staticmethod
    def __isTrimChar0(ch: str) -> bool:
        pass

    @staticmethod
    def __isLineBreak1(c: str) -> bool:
        pass

    @staticmethod
    def __isLineBreak0(c: str) -> bool:
        pass

    @staticmethod
    def __containsLineBreak(source: str) -> bool:
        pass

    @staticmethod
    def __contains(source: str, searchCh: str) -> bool:
        pass

    def trim1(self, value: str) -> str:
        pass

    def copy(self) -> CSVFormat:
        pass

    # Class Methods End
