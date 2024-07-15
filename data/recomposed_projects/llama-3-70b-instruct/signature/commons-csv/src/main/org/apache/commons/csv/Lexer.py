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
    __LF_STRING: str = chr(10)
    __CR_STRING: str = chr(13)

    def close(self) -> None:
        self.__reader.close()

    def __parseSimpleToken(self, token: Token, ch: int) -> Token:

        pass  # LLM could not translate this method

    def __parseEncapsulatedToken(self, token: Token) -> Token:
        token.isQuoted = True
        startLineNumber = self.getCurrentLineNumber()
        c = 0
        while True:
            c = self.__reader.read0()
            if self.isEscape(c):
                if self.isEscapeDelimiter():
                    token.content.append(self.__delimiter)
                else:
                    unescaped = self.readEscape()
                    if unescaped == END_OF_STREAM:  # unexpected char after escape
                        token.content.append(chr(c)).append(
                            chr(self.__reader.getLastChar())
                        )
                    else:
                        token.content.append(chr(unescaped))
            elif self.isQuoteChar(c):
                if self.isQuoteChar(self.__reader.lookAhead0()):
                    c = self.__reader.read0()
                    token.content.append(chr(c))
                else:
                    while True:
                        c = self.__reader.read0()
                        if self.isDelimiter(c):
                            token.type = TOKEN
                            return token
                        if self.isEndOfFile(c):
                            token.type = EOF
                            token.isReady = True  # There is data at EOF
                            return token
                        if self.readEndOfLine(c):
                            token.type = EORECORD
                            return token
                        if not chr(c).isspace():
                            raise IOException(
                                "(line "
                                + str(self.getCurrentLineNumber())
                                + ") invalid char between encapsulated token and"
                                + " delimiter"
                            )
            elif self.isEndOfFile(c):
                raise IOException(
                    "(startline "
                    + str(startLineNumber)
                    + ") EOF reached before encapsulated token finished"
                )
            else:
                token.content.append(chr(c))

    def __mapNullToDisabled(self, c: str) -> str:
        return self.__DISABLED if c is None else c

    def __isMetaChar(self, ch: int) -> bool:
        return (
            ch == self.__escape or ch == self.__quoteChar or ch == self.__commentStart
        )

    def trimTrailingSpaces(self, buffer: str) -> None:
        length = len(buffer)
        while length > 0 and buffer[length - 1].isspace():
            length = length - 1
        if length != len(buffer):
            buffer = buffer[:length]

    def readEscape(self) -> int:
        ch = self.__reader.read0()
        if ch == ord("r"):
            return CR
        elif ch == ord("n"):
            return LF
        elif ch == ord("t"):
            return TAB
        elif ch == ord("b"):
            return BACKSPACE
        elif ch == ord("f"):
            return FF
        elif ch == CR or ch == LF or ch == FF or ch == TAB or ch == BACKSPACE:
            return ch
        elif ch == END_OF_STREAM:
            raise IOException("EOF whilst processing escape sequence")
        else:
            if self.__isMetaChar(ch):
                return ch
            return END_OF_STREAM

    def readEndOfLine(self, ch: int) -> bool:
        if ch == 13 and self.__reader.lookAhead0() == 10:
            ch = self.__reader.read0()
            if self.__firstEol == "":
                self.__firstEol = Constants.CRLF
        if self.__firstEol == "":
            if ch == 10:
                self.__firstEol = self.__LF_STRING
            elif ch == 13:
                self.__firstEol = self.__CR_STRING
        return ch == 10 or ch == 13

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
                    token.type = EOF
                    return token

        if (
            self.isEndOfFile(lastChar)
            or not self.__isLastTokenDelimiter
            and self.isEndOfFile(c)
        ):
            token.type = EOF
            return token

        if self.isStartOfLine(lastChar) and self.isCommentStart(c):
            line = self.__reader.readLine()
            if line is None:
                token.type = EOF
                return token
            comment = line.strip()
            token.content.append(comment)
            token.type = COMMENT
            return token

        while token.type == INVALID:
            if self.__ignoreSurroundingSpaces:
                while chr(c).isspace() and not self.isDelimiter(c) and not eol:
                    c = self.__reader.read0()
                    eol = self.readEndOfLine(c)

            if self.isDelimiter(c):
                token.type = TOKEN
            elif eol:
                token.type = EORECORD
            elif self.isQuoteChar(c):
                self.__parseEncapsulatedToken(token)
            elif self.isEndOfFile(c):
                token.type = EOF
                token.isReady = True  # there is data at EOF
            else:
                self.__parseSimpleToken(token, c)
        return token

    def isStartOfLine(self, ch: int) -> bool:
        return ch == LF or ch == CR or ch == UNDEFINED

    def isQuoteChar(self, ch: int) -> bool:
        return ch == self.__quoteChar

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
        return count != END_OF_STREAM

    def isEscape(self, ch: int) -> bool:
        return ch == self.__escape

    def isEndOfFile(self, ch: int) -> bool:
        return ch == END_OF_STREAM

    def isDelimiter(self, ch: int) -> bool:
        self.__isLastTokenDelimiter = False
        if ch != self.__delimiter[0]:
            return False
        if len(self.__delimiter) == 1:
            self.__isLastTokenDelimiter = True
            return True
        self.__reader.lookAhead1(self.__delimiterBuf)
        for i in range(len(self.__delimiterBuf)):
            if self.__delimiterBuf[i] != self.__delimiter[i + 1]:
                return False
        count = self.__reader.read1(self.__delimiterBuf, 0, len(self.__delimiterBuf))
        self.__isLastTokenDelimiter = count != END_OF_STREAM
        return self.__isLastTokenDelimiter

    def isCommentStart(self, ch: int) -> bool:
        return ch == self.__commentStart

    def isClosed(self) -> bool:
        return self.__reader.isClosed()

    def getFirstEol(self) -> str:
        return self.__firstEol

    def getCurrentLineNumber(self) -> int:
        return self.__reader.getCurrentLineNumber()

    def getCharacterPosition(self) -> int:
        return self.__reader.getPosition()

    def __init__(self, format: CSVFormat, reader: ExtendedBufferedReader) -> None:

        pass  # LLM could not translate this method
