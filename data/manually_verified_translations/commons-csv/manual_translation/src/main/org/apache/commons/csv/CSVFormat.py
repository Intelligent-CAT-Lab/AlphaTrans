from __future__ import annotations
import copy
import re
import sys
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

    __headers: typing.List[typing.List[str]] = None

    __headerComments: typing.List[typing.List[str]] = None

    __escapeCharacter: str = ""

    __duplicateHeaderMode: DuplicateHeaderMode = None

    __delimiter: str = ""

    __commentMarker: str = ""

    __autoFlush: bool = False

    __allowMissingColumnNames: bool = False

    def setAllowDuplicateHeaderNames(self, allowDuplicateHeaderNames: bool) -> Builder:

        if allowDuplicateHeaderNames:
            self.setDuplicateHeaderMode(DuplicateHeaderMode.ALLOW_ALL)
        else:
            self.setDuplicateHeaderMode(DuplicateHeaderMode.ALLOW_EMPTY)

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
        if CSVFormat._CSVFormat__isLineBreak1(quoteCharacter):
            raise ValueError("The quoteChar cannot be a line break")
        self.__quoteCharacter = quoteCharacter
        return self

    def setQuote0(self, quoteCharacter: str) -> Builder:
        if CSVFormat._CSVFormat__isLineBreak1(quoteCharacter):
            raise ValueError("The quoteChar cannot be a line break")
        self.__quoteCharacter = quoteCharacter
        return self

    def setNullString(self, nullString: str) -> Builder:
        self.__nullString = nullString
        self.__quotedNullString = (
            str(self.__quoteCharacter) + str(nullString) + str(self.__quoteCharacter)
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

    def setHeaderComments1(
        self, headerComments: typing.List[typing.List[str]]
    ) -> Builder:
        self.__headerComments = CSVFormat.clone(headerComments)
        return self

    def setHeaderComments0(self, headerComments: typing.List[typing.Any]) -> Builder:

        self.__headerComments = CSVFormat.clone(CSVFormat.toStringArray(headerComments))
        return self

    def setEscape1(self, escapeCharacter: str) -> Builder:
        if CSVFormat._CSVFormat__isLineBreak1(escapeCharacter):
            raise ValueError("The escape character cannot be a line break")
        self.__escapeCharacter = escapeCharacter
        return self

    def setEscape0(self, escapeCharacter: str) -> Builder:
        if CSVFormat._CSVFormat__isLineBreak1(escapeCharacter):
            raise ValueError("The escape character cannot be a line break")
        self.__escapeCharacter = escapeCharacter
        return self

    def setDuplicateHeaderMode(
        self, duplicateHeaderMode: DuplicateHeaderMode
    ) -> Builder:

        if duplicateHeaderMode is None:
            raise ValueError("duplicateHeaderMode cannot be None")

        self.__duplicateHeaderMode = duplicateHeaderMode
        return self

    def setDelimiter1(self, delimiter: str) -> Builder:
        if CSVFormat._CSVFormat__containsLineBreak(delimiter):
            raise ValueError("The delimiter cannot be a line break")
        if not delimiter:
            raise ValueError("The delimiter cannot be empty")
        self.__delimiter = delimiter
        return self

    def setDelimiter0(self, delimiter: str) -> Builder:
        if CSVFormat._CSVFormat__containsLineBreak(delimiter):
            raise ValueError("The delimiter cannot be a line break")
        if not delimiter:
            raise ValueError("The delimiter cannot be empty")
        self.__delimiter = delimiter
        return self

    def setCommentMarker1(self, commentMarker: str) -> Builder:
        if CSVFormat._CSVFormat__isLineBreak1(commentMarker):
            raise ValueError(
                "The comment start marker character cannot be a line break"
            )
        self.__commentMarker = commentMarker
        return self

    def setCommentMarker0(self, commentMarker: str) -> Builder:
        if CSVFormat._CSVFormat__isLineBreak1(commentMarker):
            raise ValueError(
                "The comment start marker character cannot be a line break"
            )
        self.__commentMarker = commentMarker
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

        self.__trim = csvFormat.getTrim()
        self.__trailingDelimiter = csvFormat.getTrailingDelimiter()
        self.__skipHeaderRecord = csvFormat.getSkipHeaderRecord()
        self.__recordSeparator = csvFormat.getRecordSeparator()
        self.__quoteMode = csvFormat.getQuoteMode()
        self.__quotedNullString = csvFormat.getQuotedNullString()
        self.__quoteCharacter = csvFormat.getQuoteCharacter()
        self.__nullString = csvFormat.getNullString()
        self.__ignoreSurroundingSpaces = csvFormat.getIgnoreSurroundingSpaces()
        self.__ignoreHeaderCase = csvFormat.getIgnoreHeaderCase()
        self.__ignoreEmptyLines = csvFormat.getIgnoreEmptyLines()
        self.__headers = csvFormat.getHeader()
        self.__headerComments = csvFormat.getHeaderComments()
        self.__escapeCharacter = csvFormat.getEscapeCharacter()
        self.__duplicateHeaderMode = csvFormat.getDuplicateHeaderMode()
        self.__delimiter = csvFormat.getDelimiter()
        self.__commentMarker = csvFormat.getCommentMarker()
        self.__autoFlush = csvFormat.getAutoFlush()
        self.__allowMissingColumnNames = csvFormat.getAllowMissingColumnNames()


class Predefined:

    TDF = None

    RFC4180 = None

    PostgreSQLText = None

    PostgreSQLCsv = None

    Oracle = None

    MySQL = None

    MongoDBTsv = None

    MongoDBCsv = None

    InformixUnloadCsv = None

    InformixUnload = None

    Excel = None

    Default = None

    __format: CSVFormat = None

    def getFormat(self) -> CSVFormat:
        return self.__format

    def __init__(self, format_: CSVFormat) -> None:
        self.__format = format_


class CSVFormat:

    RFC4180: CSVFormat = None

    ORACLE: CSVFormat = None

    MONGODB_CSV: CSVFormat = None
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

    __headerComments: typing.List[typing.List[str]] = None

    __headers: typing.List[typing.List[str]] = None

    __escapeCharacter: str = ""

    __delimiter: str = ""

    __commentMarker: str = ""

    __autoFlush: bool = False

    __allowMissingColumnNames: bool = False

    __duplicateHeaderMode: DuplicateHeaderMode = None

    __serialVersionUID: int = 2

    TDF: CSVFormat = None

    POSTGRESQL_TEXT: CSVFormat = None

    POSTGRESQL_CSV: CSVFormat = None

    MYSQL: CSVFormat = None

    MONGODB_TSV: CSVFormat = None

    INFORMIX_UNLOAD_CSV: CSVFormat = None

    INFORMIX_UNLOAD: CSVFormat = None

    EXCEL: CSVFormat = None

    @staticmethod
    def initialize_fields() -> None:
        CSVFormat.DEFAULT: CSVFormat = CSVFormat(
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

        CSVFormat.RFC4180: CSVFormat = CSVFormat.DEFAULT\
            .builder()\
            .setIgnoreEmptyLines(False)\
            .build()
        
        CSVFormat.ORACLE: CSVFormat = CSVFormat.DEFAULT\
            .builder()\
            .setDelimiter1(Constants.COMMA)\
            .setEscape0(Constants.BACKSLASH)\
            .setIgnoreEmptyLines(False)\
            .setQuote1(Constants.DOUBLE_QUOTE_CHAR)\
            .setNullString(Constants.SQL_NULL_STRING)\
            .setTrim(True)\
            .setRecordSeparator1(os.linesep)\
            .setQuoteMode(QuoteMode.MINIMAL)\
            .build()

        CSVFormat.MONGODB_CSV: CSVFormat = CSVFormat.DEFAULT\
            .builder()\
            .setDelimiter1(Constants.COMMA)\
            .setEscape1(Constants.DOUBLE_QUOTE_CHAR)\
            .setQuote1(Constants.DOUBLE_QUOTE_CHAR)\
            .setQuoteMode(QuoteMode.MINIMAL)\
            .setSkipHeaderRecord(False)\
            .build()

        CSVFormat.MONGODB_TSV: CSVFormat = CSVFormat.DEFAULT\
            .builder()\
            .setDelimiter0(Constants.TAB)\
            .setEscape1(Constants.DOUBLE_QUOTE_CHAR)\
            .setQuote1(Constants.DOUBLE_QUOTE_CHAR)\
            .setQuoteMode(QuoteMode.MINIMAL)\
            .setSkipHeaderRecord(False)\
            .build()
        
        CSVFormat.MYSQL: CSVFormat = CSVFormat.DEFAULT\
            .builder()\
            .setDelimiter0(Constants.TAB)\
            .setEscape0(Constants.BACKSLASH)\
            .setIgnoreEmptyLines(False)\
            .setQuote1(None)\
            .setRecordSeparator0(Constants.LF)\
            .setNullString(Constants.SQL_NULL_STRING)\
            .setQuoteMode(QuoteMode.ALL_NON_NULL)\
            .build()
        
        CSVFormat.POSTGRESQL_CSV: CSVFormat = CSVFormat.DEFAULT\
            .builder()\
            .setDelimiter1(Constants.COMMA)\
            .setEscape1(None)\
            .setIgnoreEmptyLines(False)\
            .setQuote1(Constants.DOUBLE_QUOTE_CHAR)\
            .setRecordSeparator0(Constants.LF)\
            .setNullString(Constants.EMPTY)\
            .setQuoteMode(QuoteMode.ALL_NON_NULL)\
            .build()
        
        CSVFormat.POSTGRESQL_TEXT: CSVFormat = CSVFormat.DEFAULT\
            .builder()\
            .setDelimiter0(Constants.TAB)\
            .setEscape0(Constants.BACKSLASH)\
            .setIgnoreEmptyLines(False)\
            .setQuote1(None)\
            .setRecordSeparator0(Constants.LF)\
            .setNullString(Constants.SQL_NULL_STRING)\
            .setQuoteMode(QuoteMode.ALL_NON_NULL)\
            .build()
        
        CSVFormat.TDF = CSVFormat.DEFAULT\
            .builder()\
            .setDelimiter0(Constants.TAB)\
            .setIgnoreSurroundingSpaces(True)\
            .build()
        
        CSVFormat.INFORMIX_UNLOAD_CSV = CSVFormat.DEFAULT\
            .builder()\
            .setDelimiter1(Constants.COMMA)\
            .setQuote1(Constants.DOUBLE_QUOTE_CHAR)\
            .setRecordSeparator0(Constants.LF)\
            .build()
        
        CSVFormat.INFORMIX_UNLOAD = CSVFormat.DEFAULT\
            .builder()\
            .setDelimiter0(Constants.PIPE)\
            .setEscape0(Constants.BACKSLASH)\
            .setQuote1(Constants.DOUBLE_QUOTE_CHAR)\
            .setRecordSeparator0(Constants.LF)\
            .build()
        
        CSVFormat.EXCEL = CSVFormat.DEFAULT\
            .builder()\
            .setIgnoreEmptyLines(False)\
            .setAllowMissingColumnNames(True)\
            .build()

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

        if allowDuplicateHeaderNames:
            mode = DuplicateHeaderMode.ALLOW_ALL
        else:
            mode = DuplicateHeaderMode.ALLOW_EMPTY

        return self.builder().setDuplicateHeaderMode(mode).build()

    def withAllowDuplicateHeaderNames0(self) -> CSVFormat:

        return (
            self.builder().setDuplicateHeaderMode(DuplicateHeaderMode.ALLOW_ALL).build()
        )

    def toString(self) -> str:

        sb = "Delimiter=<" + self.__delimiter + ">"

        if self.isEscapeCharacterSet():
            sb += " Escape=<" + self.__escapeCharacter + ">"

        if self.isQuoteCharacterSet():
            sb += " QuoteChar=<" + self.__quoteCharacter + ">"

        if self.__quoteMode is not None:
            sb += " QuoteMode=<" + str(self.__quoteMode) + ">"

        if self.isCommentMarkerSet():
            sb += " CommentStart=<" + self.__commentMarker + ">"

        if self.isNullStringSet():
            sb += " NullString=<" + self.__nullString + ">"

        if self.__recordSeparator != None:
            sb += " RecordSeparator=<" + self.__recordSeparator + ">"

        if self.getIgnoreEmptyLines():
            sb += " EmptyLines:ignored"

        if self.getIgnoreSurroundingSpaces():
            sb += " SurroundingSpaces:ignored"

        if self.getIgnoreHeaderCase():
            sb += " IgnoreHeaderCase:ignored"

        sb += (" SkipHeaderRecord:" + "true") if self.__skipHeaderRecord\
            else (" SkipHeaderRecord:" + "false")

        if self.__headerComments is not None:
            sb += " HeaderComments:" + str(self.__headerComments)

        if self.__headers is not None:
            sb += " Header:" + str(self.__headers)

        return sb

    def print4(self, out: Path, charset: str) -> CSVPrinter:

        if out is None:
            raise ValueError("out cannot be None")

        return self.print0(io.open(out, "w", encoding=charset, newline=''))

    def print1(self, out: pathlib.Path, charset: str) -> CSVPrinter:

        if out is None or charset is None:
            raise ValueError("out and charset cannot be None")

        return CSVPrinter(open(out, "w", encoding=charset), self)

    def __hash__(self) -> int:
        return self.hashCode()
    
    def hashCode(self) -> int:

        prime = 31
        result = 1
        if self.__headers is not None:
            result = prime * result + hash(tuple(self.__headers))
        else:
            result = prime * result
        if self.__headerComments is not None:
            result = prime * result + hash(tuple(self.__headerComments))
        else:
            result = prime * result
        result = prime * result + hash(
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
        return result

    def getDelimiter(self) -> str:
        return self.__delimiter

    def getAllowDuplicateHeaderNames(self) -> bool:
        return self.__duplicateHeaderMode == DuplicateHeaderMode.ALLOW_ALL

    def __eq__(self, other: CSVFormat) -> bool:
        return self.equals(other)
    
    def equals(self, obj: typing.Any) -> bool:

        if self is obj:
            return True
        if obj is None or type(self) != type(obj):
            return False
        other: CSVFormat = typing.cast(CSVFormat, obj)
        return (
            self.__duplicateHeaderMode == other._CSVFormat__duplicateHeaderMode
            and self.__allowMissingColumnNames == other._CSVFormat__allowMissingColumnNames
            and self.__autoFlush == other._CSVFormat__autoFlush
            and self.__commentMarker == other._CSVFormat__commentMarker
            and self.__delimiter == other._CSVFormat__delimiter
            and self.__escapeCharacter == other._CSVFormat__escapeCharacter
            and self.__headers == other._CSVFormat__headers
            and self.__headerComments == other._CSVFormat__headerComments
            and self.__ignoreEmptyLines == other._CSVFormat__ignoreEmptyLines
            and self.__ignoreHeaderCase == other._CSVFormat__ignoreHeaderCase
            and self.__ignoreSurroundingSpaces == other._CSVFormat__ignoreSurroundingSpaces
            and self.__nullString == other._CSVFormat__nullString
            and self.__quoteCharacter == other._CSVFormat__quoteCharacter
            and self.__quoteMode == other._CSVFormat__quoteMode
            and self.__quotedNullString == other._CSVFormat__quotedNullString
            and self.__recordSeparator == other._CSVFormat__recordSeparator
            and self.__skipHeaderRecord == other._CSVFormat__skipHeaderRecord
            and self.__trailingDelimiter == other._CSVFormat__trailingDelimiter
            and self.__trim == other._CSVFormat__trim
        )

    @staticmethod
    def clone(values: typing.List[typing.Any]) -> typing.List[typing.Any]:
        return values.copy() if values is not None else None

    def printRecord(
        self,
        appendable: typing.Union[typing.List, io.TextIOBase],
        values: typing.List[typing.Any],
    ) -> None:

        for i in range(len(values)):
            self.print2(values[i], appendable, i == 0)
        self.println(appendable)

    def println(self, appendable: typing.Union[typing.List, io.TextIOBase]) -> None:

        if self.getTrailingDelimiter():
            self.__append1(self.getDelimiterString(), appendable)
        if self.__recordSeparator is not None:
            self.__append1(self.__recordSeparator, appendable)

    def printer(self) -> CSVPrinter:

        # Assuming that CSVPrinter is a class that takes an appendable and a format as arguments
        # and returns a CSVPrinter object.
        # Assuming that sys.stdout is the equivalent of Java's System.out
        # Assuming that self is the instance of CSVFormat

        return CSVPrinter(sys.stdout, self)

    def print2(
        self,
        value: typing.Any,
        out: typing.Union[typing.List, io.TextIOBase],
        newRecord: bool,
    ) -> None:

        charSequence: str
        if value is None:
            if self.__nullString is None:
                charSequence = Constants.EMPTY
            elif self.__quoteMode == QuoteMode.ALL:
                charSequence = self.__quotedNullString
            else:
                charSequence = self.__nullString
        elif isinstance(value, str):
            charSequence = value
        elif isinstance(value, io.TextIOWrapper) or isinstance(
            value, io.BufferedReader
        ) or isinstance(value, io.TextIOBase):
            self.__print5(value, out, newRecord)
            return
        else:
            charSequence = str(value)

        charSequence = self.trim0(charSequence) if self.__trim else charSequence
        self.__print3(value, charSequence, out, newRecord)

    def print0(self, out: typing.Union[typing.List, io.TextIOBase]) -> CSVPrinter:

        if out is None:
            raise ValueError("out cannot be None")

        return CSVPrinter(out, self)

    def parse(
        self, reader: typing.Union[io.TextIOWrapper, io.BufferedReader, io.TextIOBase]
    ) -> CSVParser:

        return CSVParser.CSVParser1(reader, self)

    def isQuoteCharacterSet(self) -> bool:
        return self.__quoteCharacter != None

    def isNullStringSet(self) -> bool:
        return self.__nullString != None

    def isEscapeCharacterSet(self) -> bool:
        return self.__escapeCharacter != None

    def isCommentMarkerSet(self) -> bool:
        return self.__commentMarker != None

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
    
    def getQuotedNullString(self) -> str:
        return self.__quotedNullString

    def getNullString(self) -> str:
        return self.__nullString

    def getIgnoreSurroundingSpaces(self) -> bool:
        return self.__ignoreSurroundingSpaces

    def getIgnoreHeaderCase(self) -> bool:
        return self.__ignoreHeaderCase

    def getIgnoreEmptyLines(self) -> bool:
        return self.__ignoreEmptyLines

    def getHeaderComments(self) -> typing.List[typing.List[str]]:
        return (
            self.__headerComments.copy() if self.__headerComments is not None else None
        )

    def getHeader(self) -> typing.List[typing.List[str]]:
        return self.__headers.clone() if self.__headers is not None else None

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

    def format_(self, values: typing.List[typing.Any]) -> str:

        out = io.StringIO()
        try:
            csvPrinter = CSVPrinter(out, self)
            csvPrinter.printRecord1(values)
            res = out.getvalue()
            len_ = (
                len(res) - len(self.__recordSeparator)
                if self.__recordSeparator
                else len(res)
            )
            return res[:len_]
        except IOError as e:
            raise ValueError(e)

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
        header: typing.List[typing.List[str]],
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
            self.__headerComments = self.toStringArray(headerComments)
            self.__headers = self.clone(header)
            self.__skipHeaderRecord = skipHeaderRecord
            self.__ignoreHeaderCase = ignoreHeaderCase
            self.__trailingDelimiter = trailingDelimiter
            self.__trim = trim
            self.__autoFlush = autoFlush
            self.__quotedNullString = (
                str(self.__quoteCharacter) + str(self.__nullString) + str(self.__quoteCharacter)
            )
            self.__duplicateHeaderMode = duplicateHeaderMode
            self.__validate()
        else:
            self.__delimiter = builder._Builder__delimiter
            self.__quoteCharacter = builder._Builder__quoteCharacter
            self.__quoteMode = builder._Builder__quoteMode
            self.__commentMarker = builder._Builder__commentMarker
            self.__escapeCharacter = builder._Builder__escapeCharacter
            self.__ignoreSurroundingSpaces = builder._Builder__ignoreSurroundingSpaces
            self.__allowMissingColumnNames = builder._Builder__allowMissingColumnNames
            self.__ignoreEmptyLines = builder._Builder__ignoreEmptyLines
            self.__recordSeparator = builder._Builder__recordSeparator
            self.__nullString = builder._Builder__nullString
            self.__headerComments = builder._Builder__headerComments
            self.__headers = builder._Builder__headers
            self.__skipHeaderRecord = builder._Builder__skipHeaderRecord
            self.__ignoreHeaderCase = builder._Builder__ignoreHeaderCase
            self.__trailingDelimiter = builder._Builder__trailingDelimiter
            self.__trim = builder._Builder__trim
            self.__autoFlush = builder._Builder__autoFlush
            self.__quotedNullString = builder._Builder__quotedNullString
            self.__duplicateHeaderMode = builder._Builder__duplicateHeaderMode
            self.__validate()

    @staticmethod
    def valueOf(format_: str) -> CSVFormat:
        return getattr(Predefined, format_).getFormat()

    @staticmethod
    def trim0(charSequence: str) -> str:

        if isinstance(charSequence, str):
            return charSequence.strip()

        count = len(charSequence)
        len_ = count
        pos = 0

        while pos < len_ and CSVFormat.__isTrimChar1(charSequence, pos):
            pos += 1

        while pos < len_ and CSVFormat.__isTrimChar1(charSequence, len_ - 1):
            len_ -= 1

        return charSequence[pos:len_] if pos > 0 or len_ < count else charSequence

    @staticmethod
    def toStringArray(values: typing.List[typing.Any]) -> typing.List[typing.List[str]]:

        if values is None:
            return None

        strings = [None] * len(values)
        for i in range(len(values)):
            strings[i] = str(values[i]) if values[i] is not None else None

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

        if CSVFormat._CSVFormat__containsLineBreak(self.__delimiter):
            raise ValueError("The delimiter cannot be a line break")

        if self.__quoteCharacter is not None and self.__contains(
            self.__delimiter, self.__quoteCharacter
        ):
            raise ValueError(
                "The quoteChar character and the delimiter cannot be the same ('"
                + self.__quoteCharacter
                + "')"
            )

        if self.__escapeCharacter is not None and self.__contains(
            self.__delimiter, self.__escapeCharacter
        ):
            raise ValueError(
                "The escape character and the delimiter cannot be the same ('"
                + self.__escapeCharacter
                + "')"
            )

        if self.__commentMarker is not None and self.__contains(
            self.__delimiter, self.__commentMarker
        ):
            raise ValueError(
                "The comment start character and the delimiter cannot be the same ('"
                + self.__commentMarker
                + "')"
            )

        if (
            self.__quoteCharacter is not None
            and self.__quoteCharacter == self.__commentMarker
        ):
            raise ValueError(
                "The comment start character and the quoteChar cannot be the same ('"
                + self.__commentMarker
                + "')"
            )

        if (
            self.__escapeCharacter is not None
            and self.__escapeCharacter == self.__commentMarker
        ):
            raise ValueError(
                "The comment start and the escape character cannot be the same ('"
                + self.__commentMarker
                + "')"
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
                blank = self.isBlank(header)
                containsHeader = not dupCheckSet.add(blank if "" else header)
                if containsHeader and not (blank and emptyDuplicatesAllowed):
                    raise ValueError(
                        'The header contains a duplicate name: "{}" in {}. If this is'
                        " valid then use"
                        " CSVFormat.Builder.setDuplicateHeaderMode().".format(
                            header, str(self.__headers)
                        )
                    )

    def __printWithQuotes1(
        self,
        reader: typing.Union[io.TextIOWrapper, io.BufferedReader, io.TextIOBase],
        appendable: typing.Union[typing.List, io.TextIOBase],
    ) -> None:

        if self.getQuoteMode() == QuoteMode.NONE:
            self.__printWithEscapes1(reader, appendable)
            return

        pos = 0

        quote = self.getQuoteCharacter()
        builder = ""

        self.__append0(quote, appendable)

        c = reader.read(1)
        while c != "":
            builder += c
            if c == quote:
                if pos > 0:
                    self.__append1(builder[0:pos], appendable)
                    self.__append0(quote, appendable)
                    builder = ""
                    pos = -1

                self.__append0(c, appendable)
            pos += 1
            c = reader.read(1)

        if pos > 0:
            self.__append1(builder[0:pos], appendable)

        self.__append0(quote, appendable)

    def __printWithQuotes0(
        self,
        object_: typing.Any,
        charSeq: str,
        out: typing.Union[typing.List, io.TextIOBase],
        newRecord: bool,
    ) -> None:

        quote = False
        start = 0
        pos = 0
        len_ = len(charSeq)

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
            quote = not isinstance(object_, (int, float, numbers.Number))
        elif quoteModePolicy == QuoteMode.NONE:
            self.__printWithEscapes0(charSeq, out)
            return
        elif quoteModePolicy == QuoteMode.MINIMAL:
            if len_ <= 0:
                if newRecord:
                    quote = True
            else:
                c = charSeq[pos]

                if c <= Constants.COMMENT:
                    quote = True
                else:
                    while pos < len_:
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
                        pos = len_ - 1
                        c = charSeq[pos]
                        if self.__isTrimChar0(c):
                            quote = True

                if not quote:
                    if isinstance(out, list):
                        out.append(charSeq[start:len_])
                    else:
                        out.write(charSeq[start:len_])
                    return
        else:
            raise RuntimeError("Unexpected Quote value: " + quoteModePolicy)

        if not quote:
            if isinstance(out, list):
                out.append(charSeq[start:len_])
            else:
                out.write(charSeq[start:len_])
            return

        if isinstance(out, list):
            out.append(quoteChar)
        else:
            out.write(quoteChar)
        while pos < len_:
            c = charSeq[pos]
            if c == quoteChar or c == escapeChar:
                if isinstance(out, list):
                    out.append(charSeq[start:pos])
                    out.append(escapeChar)
                else:
                    out.write(charSeq[start:pos])
                    out.write(escapeChar)
                start = pos
            pos += 1

        if isinstance(out, list):
            out.append(charSeq[start:pos])
            out.append(quoteChar)
        else:
            out.write(charSeq[start:pos])
            out.write(quoteChar)

    def __printWithEscapes1(
        self,
        reader: typing.Union[io.TextIOWrapper, io.BufferedReader, io.TextIOBase],
        appendable: typing.Union[typing.List, io.TextIOBase],
    ) -> None:

        start = 0
        pos = 0

        if isinstance(reader, io.StringIO):
            bufferedReader = StringIOWrapper(reader)
        elif isinstance(reader, io.TextIOWrapper):
            bufferedReader = StringIOWrapper(reader.buffer)
        else:
            bufferedReader = ExtendedBufferedReader(reader)
        delim = list(self.getDelimiterString())
        delimLength = len(delim)
        escape = self.getEscapeCharacter()
        builder = ""

        c = bufferedReader.read0()
        while c != -1:
            builder += (chr(c))
            isDelimiterStart = self.__isDelimiter(
                chr(c),
                builder
                + "".join(bufferedReader.lookAhead2(delimLength - 1)),
                pos,
                delim,
                delimLength,
            )
            if (
                c == ord(Constants.CR)
                or c == ord(Constants.LF)
                or c == ord(escape)
                or isDelimiterStart
            ):
                if pos > start:
                    self.__append1(builder[start:pos], appendable)
                    builder = ""
                    pos = -1
                if c == ord(Constants.LF):
                    c = ord("n")
                elif c == ord(Constants.CR):
                    c = ord("r")

                self.__append0(escape, appendable)
                self.__append0(chr(c), appendable)

                if isDelimiterStart:
                    for i in range(1, delimLength):
                        c = bufferedReader.read0()
                        self.__append0(escape, appendable)
                        self.__append0(chr(c), appendable)

                start = pos + 1
            pos += 1
            c = bufferedReader.read0()

        if pos > start:
            self.__append1(builder[start:pos], appendable)

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
            if (
                c == Constants.CR
                or c == Constants.LF
                or c == escape
                or isDelimiterStart
            ):
                if pos > start:
                    if isinstance(appendable, list):
                        appendable.append(charSeq[start:pos])
                    else:
                        appendable.write(charSeq[start:pos])

                if c == Constants.LF:
                    c = "n"
                elif c == Constants.CR:
                    c = "r"

                if isinstance(appendable, list):
                    appendable.append(escape)
                    appendable.append(c)
                else:
                    appendable.write(escape)
                    appendable.write(c)

                if isDelimiterStart:
                    for i in range(1, delimLength):
                        pos += 1
                        c = charSeq[pos]
                        if isinstance(appendable, list):
                            appendable.append(escape)
                            appendable.append(c)
                        else:
                            appendable.write(escape)
                            appendable.write(c)

                start = pos + 1  # start on the current char after this one

            pos += 1

        if pos > start:
            if isinstance(appendable, list):
                appendable.append(charSeq[start:pos])
            else:
                appendable.write(charSeq[start:pos])

    def __print5(
        self,
        reader: typing.Union[io.TextIOWrapper, io.BufferedReader, io.TextIOBase],
        out: typing.Union[typing.List, io.TextIOBase],
        newRecord: bool,
    ) -> None:

        if not newRecord:
            self.__append1(self.getDelimiterString(), out)

        if self.isQuoteCharacterSet():
            self.__printWithQuotes1(reader, out)
        elif self.isEscapeCharacterSet():
            self.__printWithEscapes1(reader, out)
        elif isinstance(out, io.TextIOBase):
            IOUtils.copyLarge0(reader, out)
        else:
            IOUtils.copy0(reader, out)

    def __print3(
        self,
        object_: typing.Any,
        value: str,
        out: typing.Union[typing.List, io.TextIOBase],
        newRecord: bool,
    ) -> None:

        offset = 0
        len_ = len(value)
        if not newRecord:
            if isinstance(out, list):
                out.append(self.getDelimiterString())
            else:
                out.write(self.getDelimiterString())
        if object_ is None:
            if isinstance(out, list):
                out.append(value)
            else:
                out.write(value)
        elif self.isQuoteCharacterSet():
            self.__printWithQuotes0(object_, value, out, newRecord)
        elif self.isEscapeCharacterSet():
            self.__printWithEscapes0(value, out)
        else:
            if isinstance(out, list):
                out.append(value[offset:len_])
            else:
                out.write(value[offset:len_])

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

        if isinstance(appendable, list):
            appendable.append(csq)
        elif isinstance(appendable, io.TextIOBase):
            appendable.write(csq)
        elif isinstance(appendable, str):
            if csq:
                appendable += str(csq)

    def __append0(
        self, c: str, appendable: typing.Union[typing.List, io.TextIOBase]
    ) -> None:
        if isinstance(appendable, list):
            appendable.append(c)
        elif isinstance(appendable, io.TextIOBase):
            appendable.write(c)
        elif isinstance(appendable, str):
            if c:
                appendable += str(c)

    @staticmethod
    def __isTrimChar1(charSequence: str, pos: int) -> bool:
        return CSVFormat.__isTrimChar0(charSequence[pos])

    @staticmethod
    def __isTrimChar0(ch: str) -> bool:
        return ord(ch) <= ord(Constants.SP)

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
        if source is None:
            return False
        return source.find(searchCh) >= 0

    def trim1(self, value: str) -> str:
        return self.getTrim() and value.strip() or value

    def copy(self) -> CSVFormat:
        return self.builder().build()


CSVFormat.initialize_fields()
Predefined.Default = Predefined(CSVFormat.DEFAULT)
Predefined.Excel = Predefined(CSVFormat.EXCEL)
Predefined.InformixUnload = Predefined(CSVFormat.INFORMIX_UNLOAD)
Predefined.InformixUnloadCsv = Predefined(CSVFormat.INFORMIX_UNLOAD_CSV)
Predefined.MongoDBCsv = Predefined(CSVFormat.MONGODB_CSV)
Predefined.MongoDBTsv = Predefined(CSVFormat.MONGODB_TSV)
Predefined.MySQL = Predefined(CSVFormat.MYSQL)
Predefined.Oracle = Predefined(CSVFormat.ORACLE)
Predefined.PostgreSQLCsv = Predefined(CSVFormat.POSTGRESQL_CSV)
Predefined.PostgreSQLText = Predefined(CSVFormat.POSTGRESQL_TEXT)
Predefined.RFC4180 = Predefined(CSVFormat.RFC4180)
Predefined.TDF = Predefined(CSVFormat.TDF)
