from __future__ import annotations
import re
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

    __recordSeparator: str = ''

    __quoteMode: QuoteMode = None

    __quotedNullString: str = ''

    __quoteCharacter: str = ''

    __nullString: str = ''

    __ignoreSurroundingSpaces: bool = False

    __ignoreHeaderCase: bool = False

    __ignoreEmptyLines: bool = False

    __headers: typing.List[str] = None

    __headerComments: typing.List[str] = None

    __escapeCharacter: str = ''

    __duplicateHeaderMode: DuplicateHeaderMode = None

    __delimiter: str = ''

    __commentMarker: str = ''

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
         if CSVFormat.__isLineBreak1(quoteCharacter):
             raise ValueError("The quoteChar cannot be a line break")
         self.__quoteCharacter = quoteCharacter
         return self
    def setQuote0(self, quoteCharacter: str) -> Builder:
         if CSVFormat.__isLineBreak1(quoteCharacter):
             raise ValueError("The quoteChar cannot be a line break")
         self.__quoteCharacter = quoteCharacter
         return self
    def setNullString(self, nullString: str) -> Builder:
         self.__nullString = nullString
         self.__quotedNullString = self.__quoteCharacter + nullString + self.__quoteCharacter
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
         self.__headerComments = CSVFormat.clone(CSVFormat.toStringArray(headerComments))
         return self
    def setEscape1(self, escapeCharacter: str) -> Builder:
         if escapeCharacter is not None and self.__isLineBreak0(escapeCharacter):
             raise ValueError("The escape character cannot be a line break")
         self.__escapeCharacter = escapeCharacter
         return self
    def setEscape0(self, escapeCharacter: str) -> Builder:
         if escapeCharacter is not None and self.__isLineBreak0(escapeCharacter):
             raise ValueError("The escape character cannot be a line break")
         self.__escapeCharacter = escapeCharacter
         return self
    def setDuplicateHeaderMode(self, duplicateHeaderMode: DuplicateHeaderMode) -> Builder:
        
        if duplicateHeaderMode is None:
            raise ValueError("duplicateHeaderMode cannot be None")
        
        self.__duplicateHeaderMode = duplicateHeaderMode
        return self
    def setDelimiter1(self, delimiter: str) -> Builder:
         if '\n' in delimiter or '\r' in delimiter:
             raise ValueError("The delimiter cannot be a line break")
         if not delimiter:
             raise ValueError("The delimiter cannot be empty")
         self.__delimiter = delimiter
         return self
    def setDelimiter0(self, delimiter: str) -> Builder:
         if '\n' in delimiter or '\r' in delimiter:
             raise ValueError("The delimiter cannot be a line break")
         if not delimiter:
             raise ValueError("The delimiter cannot be empty")
         self.__delimiter = delimiter
         return self
    def setCommentMarker1(self, commentMarker: str) -> Builder:
         if CSVFormat.__isLineBreak1(commentMarker):
            raise ValueError("The comment start marker character cannot be a line break")
         self.__commentMarker = commentMarker
         return self
    def setCommentMarker0(self, commentMarker: str) -> Builder:
         if CSVFormat.__isLineBreak1(commentMarker):
            raise ValueError("The comment start marker character cannot be a line break")
         self.__commentMarker = commentMarker
         return self
    def setAutoFlush(self, autoFlush: bool) -> Builder:
         self.__autoFlush = autoFlush
         return self
    def setAllowMissingColumnNames(self, allowMissingColumnNames: bool) -> Builder:
         self.__allowMissingColumnNames = allowMissingColumnNames
         return self
    def build(self) -> CSVFormat:
         return CSVFormat(0, self.__autoFlush, self.__skipHeaderRecord, self.__delimiter, self.__nullString, self.__escapeCharacter, self.__ignoreSurroundingSpaces, self.__trim, self, None, self.__ignoreHeaderCase, self.__quoteCharacter, self.__quoteMode, self.__ignoreEmptyLines, self.__duplicateHeaderMode, self.__headers, self.__allowMissingColumnNames, self.__trailingDelimiter, self.__headerComments, self.__recordSeparator)
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
class CSVFormat():

    RFC4180: CSVFormat = DEFAULT.builder().setIgnoreEmptyLines(False).build()
    POSTGRESQL_TEXT: CSVFormat = DEFAULT.builder().setDelimiter0(TAB).setIgnoreSurroundingSpaces(True).setQuote1(None).setRecordSeparator0(LF).setNullString(Constants.SQL_NULL_STRING).setQuoteMode(QuoteMode.ALL_NON_NULL).build()
    POSTGRESQL_CSV: CSVFormat = DEFAULT.builder().setDelimiter1(COMMA).setEscape1(None).setIgnoreEmptyLines(False).setQuote1(DOUBLE_QUOTE_CHAR).setRecordSeparator0(LF).setNullString(EMPTY).setQuoteMode(QuoteMode.ALL_NON_NULL).build()
    ORACLE: CSVFormat = DEFAULT.builder().setDelimiter1(COMMA).setEscape0(BACKSLASH).setIgnoreEmptyLines(False).setQuote1(DOUBLE_QUOTE_CHAR).setNullString(Constants.SQL_NULL_STRING).setTrim(True).setRecordSeparator1(os.linesep).setQuoteMode(QuoteMode.MINIMAL).build()
    MYSQL: CSVFormat = DEFAULT.builder().setDelimiter0(TAB).setIgnoreSurroundingSpaces(True).setQuote1(None).setRecordSeparator0(LF).setNullString(Constants.SQL_NULL_STRING).setQuoteMode(QuoteMode.ALL_NON_NULL).build()
    MONGODB_TSV: CSVFormat = DEFAULT.builder().setDelimiter0(TAB).setEscape1(DOUBLE_QUOTE_CHAR).setQuote1(DOUBLE_QUOTE_CHAR).setQuoteMode(QuoteMode.MINIMAL).setSkipHeaderRecord(False).build()
    MONGODB_CSV: CSVFormat = DEFAULT.builder().setDelimiter1(COMMA).setEscape1(DOUBLE_QUOTE_CHAR).setQuote1(DOUBLE_QUOTE_CHAR).setQuoteMode(QuoteMode.MINIMAL).setSkipHeaderRecord(False).build()
    INFORMIX_UNLOAD_CSV: CSVFormat = DEFAULT.builder().setDelimiter1(COMMA).setQuote1(DOUBLE_QUOTE_CHAR).setRecordSeparator0(LF).build()
    INFORMIX_UNLOAD: CSVFormat = DEFAULT.builder().setDelimiter0(PIPE).setEscape0(BACKSLASH).setQuote1(DOUBLE_QUOTE_CHAR).setRecordSeparator0(LF).build()
    EXCEL: CSVFormat = DEFAULT.builder().setIgnoreEmptyLines(False).setAllowMissingColumnNames(True).build()
    __trim: bool = False

    __trailingDelimiter: bool = False

    __skipHeaderRecord: bool = False

    __recordSeparator: str = ''

    __quoteMode: QuoteMode = None

    __quotedNullString: str = ''

    __quoteCharacter: str = ''

    __nullString: str = ''

    __ignoreSurroundingSpaces: bool = False

    __ignoreHeaderCase: bool = False

    __ignoreEmptyLines: bool = False

    __headerComments: typing.List[str] = None

    __headers: typing.List[str] = None

    __escapeCharacter: str = ''

    __delimiter: str = ''

    __commentMarker: str = ''

    __autoFlush: bool = False

    __allowMissingColumnNames: bool = False

    __duplicateHeaderMode: DuplicateHeaderMode = None

    __serialVersionUID: int = 2
    TDF: CSVFormat = DEFAULT.builder().setDelimiter0(TAB).setIgnoreSurroundingSpaces(True).build()
    RFC4180: CSVFormat = DEFAULT.builder().setIgnoreEmptyLines(False).build()
    POSTGRESQL_TEXT: CSVFormat = DEFAULT.builder().setDelimiter0(TAB).setIgnoreSurroundingSpaces(True).setQuote1(None).setRecordSeparator0(LF).setNullString(Constants.SQL_NULL_STRING).setQuoteMode(QuoteMode.ALL_NON_NULL).build()
    POSTGRESQL_CSV: CSVFormat = DEFAULT.builder().setDelimiter1(COMMA).setEscape1(None).setIgnoreEmptyLines(False).setQuote1(DOUBLE_QUOTE_CHAR).setRecordSeparator0(LF).setNullString(EMPTY).setQuoteMode(QuoteMode.ALL_NON_NULL).build()
    ORACLE: CSVFormat = DEFAULT.builder().setDelimiter1(COMMA).setEscape0(BACKSLASH).setIgnoreEmptyLines(False).setQuote1(DOUBLE_QUOTE_CHAR).setNullString(Constants.SQL_NULL_STRING).setTrim(True).setRecordSeparator1(os.linesep).setQuoteMode(QuoteMode.MINIMAL).build()
    MYSQL: CSVFormat = DEFAULT.builder().setDelimiter0(TAB).setIgnoreSurroundingSpaces(True).setQuote1(None).setRecordSeparator0(LF).setNullString(Constants.SQL_NULL_STRING).setQuoteMode(QuoteMode.ALL_NON_NULL).build()
    MONGODB_TSV: CSVFormat = DEFAULT.builder().setDelimiter0(TAB).setEscape1(DOUBLE_QUOTE_CHAR).setQuote1(DOUBLE_QUOTE_CHAR).setQuoteMode(QuoteMode.MINIMAL).setSkipHeaderRecord(False).build()
    MONGODB_CSV: CSVFormat = DEFAULT.builder().setDelimiter1(COMMA).setEscape1(DOUBLE_QUOTE_CHAR).setQuote1(DOUBLE_QUOTE_CHAR).setQuoteMode(QuoteMode.MINIMAL).setSkipHeaderRecord(False).build()
    INFORMIX_UNLOAD_CSV: CSVFormat = DEFAULT.builder().setDelimiter1(COMMA).setQuote1(DOUBLE_QUOTE_CHAR).setRecordSeparator0(LF).build()
    INFORMIX_UNLOAD: CSVFormat = DEFAULT.builder().setDelimiter0(PIPE).setEscape0(BACKSLASH).setQuote1(DOUBLE_QUOTE_CHAR).setRecordSeparator0(LF).build()
    EXCEL: CSVFormat = DEFAULT.builder().setIgnoreEmptyLines(False).setAllowMissingColumnNames(True).build()
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
         if CSVFormat.__isLineBreak1(quoteChar):
             raise ValueError("The quoteChar cannot be a line break")
         self.__quoteCharacter = quoteChar
         return self
    def withQuote0(self, quoteChar: str) -> CSVFormat:
         if CSVFormat.__isLineBreak1(quoteChar):
             raise ValueError("The quoteChar cannot be a line break")
         self.__quoteCharacter = quoteChar
         return self
    def withNullString(self, nullString: str) -> CSVFormat:
         return self.builder().setNullString(nullString).build()
    def withIgnoreSurroundingSpaces1(self, ignoreSurroundingSpaces: bool) -> CSVFormat:
         return self.builder().setIgnoreSurroundingSpaces(ignoreSurroundingSpaces).build()
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
         if '\n' in delimiter or '\r' in delimiter:
             raise ValueError("The delimiter cannot be a line break")
         if not delimiter:
             raise ValueError("The delimiter cannot be empty")
         self.__delimiter = delimiter
         return self
    def withCommentMarker1(self, commentMarker: str) -> CSVFormat:
         if CSVFormat.__isLineBreak1(commentMarker):
            raise ValueError("The comment start marker character cannot be a line break")
         self.__commentMarker = commentMarker
         return self
    def withCommentMarker0(self, commentMarker: str) -> CSVFormat:
         if CSVFormat.__isLineBreak1(commentMarker):
            raise ValueError("The comment start marker character cannot be a line break")
         self.__commentMarker = commentMarker
         return self
    def withAutoFlush(self, autoFlush: bool) -> CSVFormat:
         return self.builder().setAutoFlush(autoFlush).build()
    def withAllowMissingColumnNames1(self, allowMissingColumnNames: bool) -> CSVFormat:
         return self.builder().setAllowMissingColumnNames(allowMissingColumnNames).build()
    def withAllowMissingColumnNames0(self) -> CSVFormat:
         return self.builder().setAllowMissingColumnNames(True).build()
    def withAllowDuplicateHeaderNames1(self, allowDuplicateHeaderNames: bool) -> CSVFormat:
        
        mode = DuplicateHeaderMode.ALLOW_ALL if allowDuplicateHeaderNames else DuplicateHeaderMode.ALLOW_EMPTY
        return self.builder().setDuplicateHeaderMode(mode).build()
    def withAllowDuplicateHeaderNames0(self) -> CSVFormat:
        
        return self.builder().setDuplicateHeaderMode(DuplicateHeaderMode.ALLOW_ALL).build()
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
        
        if self.__recordSeparator is not None:
            sb += " RecordSeparator=<" + self.__recordSeparator + ">"
        
        if self.getIgnoreEmptyLines():
            sb += " EmptyLines:ignored"
        
        if self.getIgnoreSurroundingSpaces():
            sb += " SurroundingSpaces:ignored"
        
        if self.getIgnoreHeaderCase():
            sb += " IgnoreHeaderCase:ignored"
        
        sb += " SkipHeaderRecord:" + str(self.__skipHeaderRecord)
        
        if self.__headerComments is not None:
            sb += " HeaderComments:" + str(self.__headerComments)
        
        if self.__headers is not None:
            sb += " Header:" + str(self.__headers)
        
        return sb
    def print4(self, out: Path, charset: str) -> CSVPrinter:
        
        if out is None:
            raise ValueError("Appendable is not set")

        with open(out, 'w', encoding=charset) as f:
            return CSVPrinter(f, self)
    def print1(self, out: pathlib.Path, charset: str) -> CSVPrinter:
        
        if out is None:
            raise ValueError("File path is not set")

        if charset is None:
            raise ValueError("Charset is not set")

        appendable = open(out, 'w', encoding=charset)
        return CSVPrinter(appendable, self)
    def hashCode(self) -> int:
        
        prime = 31
        result = 1
        result = prime * result + hash(tuple(self.__headers))
        result = prime * result + hash(tuple(self.__headerComments))
        result = prime * result + hash((
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
            self.__trim
        ))
        return result
    def getDelimiter(self) -> str:
         return self.__delimiter
    def getAllowDuplicateHeaderNames(self) -> bool:
         return self.__duplicateHeaderMode == DuplicateHeaderMode.ALLOW_ALL
    def equals(self, obj: typing.Any) -> bool:
        
        if self is obj:
            return True
        if obj is None or self.__class__ != obj.__class__:
            return False
        other = obj
        return self.__duplicateHeaderMode == other.__duplicateHeaderMode and \
               self.__allowMissingColumnNames == other.__allowMissingColumnNames and \
               self.__autoFlush == other.__autoFlush and \
               self.__commentMarker == other.__commentMarker and \
               self.__delimiter == other.__delimiter and \
               self.__escapeCharacter == other.__escapeCharacter and \
               self.__headers == other.__headers and \
               self.__headerComments == other.__headerComments and \
               self.__ignoreEmptyLines == other.__ignoreEmptyLines and \
               self.__ignoreHeaderCase == other.__ignoreHeaderCase and \
               self.__ignoreSurroundingSpaces == other.__ignoreSurroundingSpaces and \
               self.__nullString == other.__nullString and \
               self.__quoteCharacter == other.__quoteCharacter and \
               self.__quoteMode == other.__quoteMode and \
               self.__quotedNullString == other.__quotedNullString and \
               self.__recordSeparator == other.__recordSeparator and \
               self.__skipHeaderRecord == other.__skipHeaderRecord and \
               self.__trailingDelimiter == other.__trailingDelimiter and \
               self.__trim == other.__trim
    @staticmethod
    def clone(values: typing.List[typing.Any]) -> typing.List[typing.Any]:
         return values.copy() if values is not None else None
    def printRecord(self, appendable: typing.Union[typing.List, io.TextIOBase], values: typing.List[typing.Any]) -> None:
         for i in range(len(values)):
             self.print2(values[i], appendable, i == 0)
         self.println(appendable)
    def println(self, appendable: typing.Union[typing.List, io.TextIOBase]) -> None:
         if self.getTrailingDelimiter():
             self.__append1(self.getDelimiterString(), appendable)
         if self.__recordSeparator:
             self.__append1(self.__recordSeparator, appendable)
    def printer(self) -> CSVPrinter:
        
        if self.__appendable is None:
            raise ValueError("Appendable is not set")

        if self.__format is None:
            raise ValueError("CSVFormat is not set")

        appendable = self.__appendable
        format = self.__format.copy()

        header_comments = format.getHeaderComments()
        if header_comments is not None:
            for line in header_comments:
                self.printComment(line)

        if format.getHeader() is not None and not format.getSkipHeaderRecord():
            self.printRecord1(format.getHeader())

        return CSVPrinter(appendable, format)
    def print2(self, value: typing.Any, out: typing.Union[typing.List, io.TextIOBase], newRecord: bool) -> None:
        
        charSequence: str
        if value is None:
            if self.__nullString is None:
                charSequence = ''
            elif self.__quoteMode == QuoteMode.ALL:
                charSequence = self.__quotedNullString
            else:
                charSequence = self.__nullString
        elif isinstance(value, str):
            charSequence = value
        elif isinstance(value, io.TextIOWrapper) or isinstance(value, io.BufferedReader):
            self.__print5(value, out, newRecord)
            return
        else:
            charSequence = str(value)

        charSequence = self.trim0(charSequence) if self.__trim else charSequence
        self.__print3(value, charSequence, out, newRecord)
    def print0(self, out: typing.Union[typing.List, io.TextIOBase]) -> CSVPrinter:
        
        if out is None:
            raise ValueError("Appendable is not set")

        return CSVPrinter(out, self)
    def parse(self, reader: typing.Union[io.TextIOWrapper, io.BufferedReader]) -> CSVParser:
        
        return CSVParser.CSVParser1(reader, self)
    def isQuoteCharacterSet(self) -> bool:
         return self.__quoteCharacter is not None
    def isNullStringSet(self) -> bool:
         return self.__nullString is not None
    def isEscapeCharacterSet(self) -> bool:
         return self.__escapeCharacter is not None
    def isCommentMarkerSet(self) -> bool:
         return self.__commentMarker is not None
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
         return self.__headerComments.copy() if self.__headerComments is not None else None
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
            len_res = len(res) - len(self.__recordSeparator) if self.__recordSeparator is not None else len(res)
            return res[:len_res]
        except IOError as e:
            raise ValueError(str(e))
    def builder(self) -> Builder:
        
        return Builder.create1(self)
    def __init__(self, constructorId: int, autoFlush: bool, skipHeaderRecord: bool, delimiter: str, nullString: str, escape: str, ignoreSurroundingSpaces: bool, trim: bool, builder: Builder, commentStart: str, ignoreHeaderCase: bool, quoteChar: str, quoteMode: QuoteMode, ignoreEmptyLines: bool, duplicateHeaderMode: DuplicateHeaderMode, header: typing.List[str], allowMissingColumnNames: bool, trailingDelimiter: bool, headerComments: typing.List[typing.Any], recordSeparator: str) -> None:
        
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
            self.__quotedNullString = quoteChar + nullString + quoteChar
            self.__duplicateHeaderMode = duplicateHeaderMode
            self.__validate()
        else:
            self.__delimiter = builder.delimiter
            self.__quoteCharacter = builder.quoteCharacter
            self.__quoteMode = builder.quoteMode
            self.__commentMarker = builder.commentMarker
            self.__escapeCharacter = builder.escapeCharacter
            self.__ignoreSurroundingSpaces = builder.ignoreSurroundingSpaces
            self.__allowMissingColumnNames = builder.allowMissingColumnNames
            self.__ignoreEmptyLines = builder.ignoreEmptyLines
            self.__recordSeparator = builder.recordSeparator
            self.__nullString = builder.nullString
            self.__headerComments = builder.headerComments
            self.__headers = builder.headers
            self.__skipHeaderRecord = builder.skipHeaderRecord
            self.__ignoreHeaderCase = builder.ignoreHeaderCase
            self.__trailingDelimiter = builder.trailingDelimiter
            self.__trim = builder.trim
            self.__autoFlush = builder.autoFlush
            self.__quotedNullString = builder.quotedNullString
            self.__duplicateHeaderMode = builder.duplicateHeaderMode
            self.__validate()
    @staticmethod
    def valueOf(format: str) -> CSVFormat:
         return CSVFormat.Predefined.valueOf(format).getFormat()
    @staticmethod
    def trim0(charSequence: str) -> str:
         if isinstance(charSequence, str):
             return charSequence.strip()
         pos = 0
         len_charSequence = len(charSequence)
         while pos < len_charSequence and CSVFormat.__isTrimChar1(charSequence, pos):
             pos += 1
         while pos < len_charSequence and CSVFormat.__isTrimChar1(charSequence, len_charSequence - 1):
             len_charSequence -= 1
         return charSequence[pos:len_charSequence] if pos > 0 or len_charSequence < len(charSequence) else charSequence
    @staticmethod
    def toStringArray(values: typing.List[typing.Any]) -> typing.List[str]:
         if values is None:
             return None
         strings = [str(value) if value is not None else None for value in values]
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
            None)
    @staticmethod
    def isBlank(value: str) -> bool:
         return value is None or value.strip() == ''
    def __validate(self) -> None:
        
        if self.__containsLineBreak(self.__delimiter):
            raise ValueError("The delimiter cannot be a line break")

        if self.__quoteCharacter is not None and self.__contains(self.__delimiter, self.__quoteCharacter):
            raise ValueError(f"The quoteChar character and the delimiter cannot be the same ('{self.__quoteCharacter}')")

        if self.__escapeCharacter is not None and self.__contains(self.__delimiter, self.__escapeCharacter):
            raise ValueError(f"The escape character and the delimiter cannot be the same ('{self.__escapeCharacter}')")

        if self.__commentMarker is not None and self.__contains(self.__delimiter, self.__commentMarker):
            raise ValueError(f"The comment start character and the delimiter cannot be the same ('{self.__commentMarker}')")

        if self.__quoteCharacter is not None and self.__quoteCharacter == self.__commentMarker:
            raise ValueError(f"The comment start character and the quoteChar cannot be the same ('{self.__commentMarker}')")

        if self.__escapeCharacter is not None and self.__escapeCharacter == self.__commentMarker:
            raise ValueError(f"The comment start and the escape character cannot be the same ('{self.__commentMarker}')")

        if self.__escapeCharacter is None and self.__quoteMode == QuoteMode.NONE:
            raise ValueError("No quotes mode set but no escape character is set")

        if self.__headers is not None and self.__duplicateHeaderMode != DuplicateHeaderMode.ALLOW_ALL:
            dupCheckSet = set()
            emptyDuplicatesAllowed = self.__duplicateHeaderMode == DuplicateHeaderMode.ALLOW_EMPTY
            for header in self.__headers:
                blank = self.isBlank(header)
                containsHeader = not dupCheckSet.add(blank if blank else header)
                if containsHeader and not (blank and emptyDuplicatesAllowed):
                    raise ValueError(f"The header contains a duplicate name: \"{header}\" in {self.__headers}. If this is valid then use CSVFormat.Builder.setDuplicateHeaderMode().")
    def __printWithQuotes1(self, reader: typing.Union[io.TextIOWrapper, io.BufferedReader], appendable: typing.Union[typing.List, io.TextIOBase]) -> None:
        
        if self.getQuoteMode() == QuoteMode.NONE:
            self.__printWithEscapes1(reader, appendable)
            return

        pos = 0

        quote = self.getQuoteCharacter()
        builder = []

        self.__append0(quote, appendable)

        while True:
            c = reader.read(1)
            if not c:
                break
            builder.append(c)
            if c == quote:
                if pos > 0:
                    self.__append1(''.join(builder[:pos]), appendable)
                    self.__append0(quote, appendable)
                    builder = []
                    pos = -1

                self.__append0(c, appendable)
            pos += 1

        if pos > 0:
            self.__append1(''.join(builder[:pos]), appendable)

        self.__append0(quote, appendable)
    def __printWithQuotes0(self, object: typing.Any, charSeq: str, out: typing.Union[typing.List, io.TextIOBase], newRecord: bool) -> None:
        
        quote = False
        start = 0
        pos = 0
        len_charSeq = len(charSeq)

        delim = list(self.getDelimiterString())
        delimLength = len(delim)
        quoteChar = ord(self.getQuoteCharacter())
        escapeChar = ord(self.getEscapeCharacter()) if self.isEscapeCharacterSet() else quoteChar

        quoteModePolicy = self.getQuoteMode()
        if quoteModePolicy is None:
            quoteModePolicy = QuoteMode.MINIMAL

        if quoteModePolicy == QuoteMode.ALL or quoteModePolicy == QuoteMode.ALL_NON_NULL:
            quote = True
        elif quoteModePolicy == QuoteMode.NON_NUMERIC:
            quote = not isinstance(object, Number)
        elif quoteModePolicy == QuoteMode.NONE:
            self.__printWithEscapes0(charSeq, out)
            return
        elif quoteModePolicy == QuoteMode.MINIMAL:
            if len_charSeq <= 0:
                if newRecord:
                    quote = True
            else:
                c = charSeq[pos]

                if ord(c) <= ord('#'):
                    quote = True
                else:
                    while pos < len_charSeq:
                        c = charSeq[pos]
                        if c == '\n' or c == '\r' or c == quoteChar or c == escapeChar or self.__isDelimiter(c, charSeq, pos, delim, delimLength):
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

        if not quote:
            out.append(charSeq[start:len_charSeq])
            return

        out.append(chr(quoteChar))

        while pos < len_charSeq:
            c = charSeq[pos]
            if c == quoteChar or c == escapeChar:
                out.append(charSeq[start:pos])
                out.append(chr(escapeChar))  # now output the escape
                start = pos  # and restart with the matched char
            pos += 1

        out.append(charSeq[start:pos])
        out.append(chr(quoteChar))
    def __printWithEscapes1(self, reader: typing.Union[io.TextIOWrapper, io.BufferedReader], appendable: typing.Union[typing.List, io.TextIOBase]) -> None:
        
        start = 0
        pos = 0

        bufferedReader = ExtendedBufferedReader(reader)
        delim = list(self.getDelimiterString())
        delimLength = len(delim)
        escape = self.getEscapeCharacter()
        builder = []

        while True:
            c = bufferedReader.read0()
            if c == -1:
                break
            builder.append(chr(c))
            isDelimiterStart = self.__isDelimiter(chr(c), ''.join(builder) + ''.join(bufferedReader.lookAhead2(delimLength - 1)), pos, delim, delimLength)
            if c == CR or c == LF or c == escape or isDelimiterStart:
                if pos > start:
                    self.__append1(''.join(builder[start:pos]), appendable)
                    builder = []
                    pos = -1
                if c == LF:
                    c = 'n'
                elif c == CR:
                    c = 'r'

                self.__append0(escape, appendable)
                self.__append0(chr(c), appendable)

                if isDelimiterStart:
                    for i in range(1, delimLength):
                        c = bufferedReader.read0()
                        self.__append0(escape, appendable)
                        self.__append0(chr(c), appendable)

                start = pos + 1
            pos += 1

        if pos > start:
            self.__append1(''.join(builder[start:pos]), appendable)
    def __printWithEscapes0(self, charSeq: str, appendable: typing.Union[typing.List, io.TextIOBase]) -> None:
        
        start = 0
        pos = 0
        end = len(charSeq)

        delim = list(self.getDelimiterString())
        delimLength = len(delim)
        escape = ord(self.getEscapeCharacter())

        while pos < end:
            c = charSeq[pos]
            isDelimiterStart = self.__isDelimiter(c, charSeq, pos, delim, delimLength)
            if c == '\r' or c == '\n' or c == escape or isDelimiterStart:
                if pos > start:
                    appendable.append(charSeq[start:pos])
                if c == '\n':
                    c = 'n'
                elif c == '\r':
                    c = 'r'

                appendable.append(chr(escape))
                appendable.append(c)

                if isDelimiterStart:
                    for i in range(1, delimLength):
                        pos += 1
                        c = charSeq[pos]
                        appendable.append(chr(escape))
                        appendable.append(c)

                start = pos + 1  # start on the current char after this one

            pos += 1

        if pos > start:
            appendable.append(charSeq[start:pos])
    def __print5(self, reader: typing.Union[io.TextIOWrapper, io.BufferedReader], out: typing.Union[typing.List, io.TextIOBase], newRecord: bool) -> None:
        
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
    def __print3(self, object: typing.Any, value: str, out: typing.Union[typing.List, io.TextIOBase], newRecord: bool) -> None:
        
        offset = 0
        len_value = len(value)
        if not newRecord:
            out.append(self.getDelimiterString())
        if object is None:
            out.append(value)
        elif self.isQuoteCharacterSet():
            self.__printWithQuotes0(object, value, out, newRecord)
        elif self.isEscapeCharacterSet():
            self.__printWithEscapes0(value, out)
        else:
            out.append(value[offset:len_value])
    def __isDelimiter(self, ch: str, charSeq: str, startIndex: int, delimiter: typing.List[str], delimiterLength: int) -> bool:
        
        if ch != delimiter[0]:
            return False
        
        len_charSeq = len(charSeq)
        if startIndex + delimiterLength > len_charSeq:
            return False
        
        for i in range(1, delimiterLength):
            if charSeq[startIndex + i] != delimiter[i]:
                return False
        
        return True
    def __append1(self, csq: str, appendable: typing.Union[typing.List, io.TextIOBase]) -> None:
         appendable.write(csq)
    def __append0(self, c: str, appendable: typing.Union[typing.List, io.TextIOBase]) -> None:
         appendable.append(c)
    @staticmethod
    def __isTrimChar1(charSequence: str, pos: int) -> bool:
         return CSVFormat.__isTrimChar0(charSequence[pos])
    @staticmethod
    def __isTrimChar0(ch: str) -> bool:
         return ord(ch) <= ord(' ')
    @staticmethod
    def __isLineBreak1(c: str) -> bool:
         return c is not None and CSVFormat.__isLineBreak0(c)
    @staticmethod
    def __isLineBreak0(c: str) -> bool:
         return c == LF or c == CR
    @staticmethod
    def __containsLineBreak(source: str) -> bool:
         return CSVFormat.__contains(source, '\r') or CSVFormat.__contains(source, '\n')
    @staticmethod
    def __contains(source: str, searchCh: str) -> bool:
         return source.find(searchCh) >= 0
    def trim1(self, value: str) -> str:
         return value.strip() if self.__trim else value
    def copy(self) -> CSVFormat:
         return CSVFormat(0, self.__autoFlush, self.__skipHeaderRecord, self.__delimiter, self.__nullString, self.__escapeCharacter, self.__ignoreSurroundingSpaces, self.__trim, self, None, self.__ignoreHeaderCase, self.__quoteCharacter, self.__quoteMode, self.__ignoreEmptyLines, self.__duplicateHeaderMode, self.__headers, self.__allowMissingColumnNames, self.__trailingDelimiter, self.__headerComments, self.__recordSeparator)
