from __future__ import annotations
import re
import io
import numbers
import typing
from typing import *
import os
from src.main.org.apache.commons.csv.CSVFormat import *
from src.main.org.apache.commons.csv.Constants import *
from src.main.org.apache.commons.csv.ExtendedBufferedReader import *
from src.main.org.apache.commons.csv.Token import *


class Lexer:

    __isLastTokenDelimiter: bool = False

    __firstEol: str = ""

    __reader: ExtendedBufferedReader = None

    __ignoreEmptyLines: bool = False

    __ignoreSurroundingSpaces: bool = False

    __commentStart: str = "\u0000"

    __quoteChar: str = "\u0000"

    __escape: str = "\u0000"

    __escapeDelimiterBuf: typing.List[str] = None

    __delimiterBuf: typing.List[str] = None

    __delimiter: typing.List[str] = None

    __DISABLED: str = "\ufffe"
    __LF_STRING: str = Constants.LF
    __CR_STRING: str = Constants.CR

    def close(self) -> None:
        self.__reader.close()

    def __parseSimpleToken(self, token: Token, ch: int) -> Token:

        while True:
            if self.readEndOfLine(ch):
                token.type = Token.Type.EORECORD
                break
            if self.isEndOfFile(ch):
                token.type = Token.Type.EOF
                token.isReady = True  # There is data at EOF
                break
            if self.isDelimiter(ch):
                token.type = Token.Type.TOKEN
                break
            if self.isEscape(ch):
                if self.isEscapeDelimiter():
                    token.content.write("".join(self.__delimiter))
                else:
                    unescaped = self.readEscape()
                    if (
                        unescaped == Constants.END_OF_STREAM
                    ):  # unexpected char after escape
                        token.content.write(chr(ch) + chr(self.__reader.getLastChar()))
                    else:
                        token.content.write(chr(unescaped))
            else:
                token.content.write(chr(ch))
            ch = self.__reader.read0()  # continue

        if self.__ignoreSurroundingSpaces:
            self.trimTrailingSpaces(token.content.getvalue())

        return token

    def __parseEncapsulatedToken(self, token: Token) -> Token:

        token.isQuoted = True
        startLineNumber = self.getCurrentLineNumber()
        c = None
        while True:
            c = self.__reader.read0()

            if self.isEscape(c):
                if self.isEscapeDelimiter():
                    token.content.write("".join(self.__delimiter))
                else:
                    unescaped = self.readEscape()
                    if (
                        unescaped == Constants.END_OF_STREAM
                    ):  # unexpected char after escape
                        token.content.write(chr(c) + chr(self.__reader.getLastChar()))
                    else:
                        token.content.write(chr(unescaped))
            elif self.isQuoteChar(c):
                if self.isQuoteChar(self.__reader.lookAhead0()):
                    c = self.__reader.read0()
                    token.content.write(chr(c))
                else:
                    while True:
                        c = self.__reader.read0()
                        if self.isDelimiter(c):
                            token.type = Type.TOKEN
                            return token
                        if self.isEndOfFile(c):
                            token.type = Type.EOF
                            token.isReady = True  # There is data at EOF
                            return token
                        if self.readEndOfLine(c):
                            token.type = Type.EORECORD
                            return token
                        if not chr(c).isspace():
                            raise IOError(
                                "(line "
                                + str(self.getCurrentLineNumber())
                                + ") invalid char between encapsulated token and"
                                + " delimiter"
                            )
            elif self.isEndOfFile(c):
                raise IOError(
                    "(startline "
                    + str(startLineNumber)
                    + ") EOF reached before encapsulated token finished"
                )
            else:
                token.content.write(chr(c))

    def __mapNullToDisabled(self, c: str) -> str:
        return self.__DISABLED if c is None else c

    def __isMetaChar(self, ch: int) -> bool:
        return (
            ch == ord(self.__escape)
            or ch == ord(self.__quoteChar)
            or ch == ord(self.__commentStart)
        )

    def trimTrailingSpaces(self, buffer: str) -> None:

        length = len(buffer)
        while length > 0 and buffer[length - 1].isspace():
            length -= 1
        if length != len(buffer):
            buffer = buffer[:length]

    def readEscape(self) -> int:

        ch = self.__reader.read0()
        if ch == ord(Constants.CR):
            return ord(Constants.CR)
        elif ch == ord(Constants.LF):
            return ord(Constants.LF)
        elif ch == ord(Constants.FF):
            return ord(Constants.FF)
        elif ch == ord(Constants.TAB):
            return ord(Constants.TAB)
        elif ch == ord(Constants.BACKSPACE):
            return ord(Constants.BACKSPACE)
        elif ch == Constants.END_OF_STREAM:
            raise IOError("EOF whilst processing escape sequence")
        elif self.__isMetaChar(ch):
            return ch
        else:
            return Constants.END_OF_STREAM

    def readEndOfLine(self, ch: int) -> bool:

        if ch == ord(Constants.CR) and self.__reader.lookAhead0() == ord(Constants.LF):
            ch = self.__reader.read0()
            if self.__firstEol is None:
                self.__firstEol = Constants.CRLF
        if self.__firstEol is None:
            if ch == ord(Constants.LF):
                self.__firstEol = self.__LF_STRING
            elif ch == ord(Constants.CR):
                self.__firstEol = self.__CR_STRING
        return ch == ord(Constants.LF) or ch == ord(Constants.CR)

    def nextToken(self, token: Token) -> Token:

        lastChar = self.__reader.getLastChar()

        c = self.__reader.read0()
        eol = self.readEndOfLine(c)

        if self.__ignoreEmptyLines:
            while eol and self.isStartOfLine(lastChar):
                lastChar = c
                c = self.__reader.read0()
                eol = self.readEndOfLine(c)
                if self.isEndOfFile(c):
                    token.type = Token.Type.EOF
                    return token

        if (
            self.isEndOfFile(lastChar)
            or not self.__isLastTokenDelimiter
            and self.isEndOfFile(c)
        ):
            token.type = Token.Type.EOF
            return token

        if self.isStartOfLine(lastChar) and self.isCommentStart(c):
            line = self.__reader.readLine()
            if line is None:
                token.type = Token.Type.EOF
                return token
            comment = line.strip()
            token.content.write(comment)
            token.type = Token.Type.COMMENT
            return token

        while token.type == Token.Type.INVALID:
            if self.__ignoreSurroundingSpaces:
                while chr(c).isspace() and not self.isDelimiter(c) and not eol:
                    c = self.__reader.read0()
                    eol = self.readEndOfLine(c)

            if self.isDelimiter(c):
                token.type = Token.Type.TOKEN
            elif eol:
                token.type = Token.Type.EORECORD
            elif self.isQuoteChar(c):
                self.__parseEncapsulatedToken(token)
            elif self.isEndOfFile(c):
                token.type = Token.Type.EOF
                token.isReady = True  # there is data at EOF
            else:
                self.__parseSimpleToken(token, c)

        return token

    def isStartOfLine(self, ch: int) -> bool:
        return ch == ord(self.LF) or ch == ord(self.CR) or ch == self.UNDEFINED

    def isQuoteChar(self, ch: int) -> bool:
        return ch == ord(self.__quoteChar)

    def isEscapeDelimiter(self) -> bool:

        self.__reader.lookAhead1(self.__escapeDelimiterBuf)
        if self.__escapeDelimiterBuf[0] != self.__delimiter[0]:
            return False
        for i in range(1, len(self.__delimiter)):
            if (
                self.__escapeDelimiterBuf[2 * i] != self.__delimiter[i]
                or self.__escapeDelimiterBuf[2 * i - 1] != self.__escape
            ):
                return False
        count = self.__reader.read1(
            self.__escapeDelimiterBuf, 0, len(self.__escapeDelimiterBuf)
        )
        return count != Constants.END_OF_STREAM

    def isEscape(self, ch: int) -> bool:
        return ch == ord(self.__escape)

    def isEndOfFile(self, ch: int) -> bool:
        return ch == Constants.END_OF_STREAM

    def isDelimiter(self, ch: int) -> bool:

        self.__isLastTokenDelimiter = False

        if ch != ord(self.__delimiter[0]):
            return False

        if len(self.__delimiter) == 1:
            self.__isLastTokenDelimiter = True
            return True

        self.__reader.lookAhead1(self.__delimiterBuf)

        for i in range(len(self.__delimiterBuf)):
            if self.__delimiterBuf[i] != self.__delimiter[i + 1]:
                return False

        count = self.__reader.read1(self.__delimiterBuf, 0, len(self.__delimiterBuf))

        self.__isLastTokenDelimiter = count != Constants.END_OF_STREAM

        return self.__isLastTokenDelimiter

    def isCommentStart(self, ch: int) -> bool:
        return ch == ord(self.__commentStart)

    def isClosed(self) -> bool:
        return self.__reader.isClosed()

    def getFirstEol(self) -> str:
        return self.__firstEol

    def getCurrentLineNumber(self) -> int:

        if (
            self.__reader.__lastChar == Constants.CR
            or self.__reader.__lastChar == Constants.LF
            or self.__reader.__lastChar == Constants.UNDEFINED
            or self.__reader.__lastChar == Constants.END_OF_STREAM
        ):
            return self.__reader.__eolCounter  # counter is accurate
        else:
            return (
                self.__reader.__eolCounter + 1
            )  # Allow for counter being incremented only at EOL

    def getCharacterPosition(self) -> int:
        return self.__reader.getPosition()

    def __init__(self, format_: CSVFormat, reader: ExtendedBufferedReader) -> None:

        self.__reader = reader
        self.__delimiter = list(format_.getDelimiterString())
        self.__escape = self.__mapNullToDisabled(format_.getEscapeCharacter())
        self.__quoteChar = self.__mapNullToDisabled(format_.getQuoteCharacter())
        self.__commentStart = self.__mapNullToDisabled(format_.getCommentMarker())
        self.__ignoreSurroundingSpaces = format_.getIgnoreSurroundingSpaces()
        self.__ignoreEmptyLines = format_.getIgnoreEmptyLines()
        self.__delimiterBuf = [None] * (len(self.__delimiter) - 1)
        self.__escapeDelimiterBuf = [None] * (2 * len(self.__delimiter) - 1)
