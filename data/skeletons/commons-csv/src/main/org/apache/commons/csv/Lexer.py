from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.csv.Token import *
from src.main.org.apache.commons.csv.ExtendedBufferedReader import *
from src.main.org.apache.commons.csv.Constants import *
from src.main.org.apache.commons.csv.CSVFormat import *
import os
import typing
from typing import *
import numbers
import io
from io import StringIO

# Imports End


class Lexer:

    # Class Fields Begin
    __CR_STRING: str = None
    __LF_STRING: str = None
    __DISABLED: str = None
    __delimiter: typing.List[str] = None
    __delimiterBuf: typing.List[str] = None
    __escapeDelimiterBuf: typing.List[str] = None
    __escape: str = None
    __quoteChar: str = None
    __commentStart: str = None
    __ignoreSurroundingSpaces: bool = None
    __ignoreEmptyLines: bool = None
    __reader: ExtendedBufferedReader = None
    __firstEol: str = None
    __isLastTokenDelimiter: bool = None
    # Class Fields End

    # Class Methods Begin
    def close(self) -> None:
        pass

    def __parseSimpleToken(self, token: Token, ch: int) -> Token:
        pass

    def __parseEncapsulatedToken(self, token: Token) -> Token:
        pass

    def __mapNullToDisabled(self, c: str) -> str:
        pass

    def __isMetaChar(self, ch: int) -> bool:
        pass

    def trimTrailingSpaces(
        self, buffer: typing.Union[typing.List[str], io.StringIO]
    ) -> None:
        pass

    def readEscape(self) -> int:
        pass

    def readEndOfLine(self, ch: int) -> bool:
        pass

    def nextToken(self, token: Token) -> Token:
        pass

    def isStartOfLine(self, ch: int) -> bool:
        pass

    def isQuoteChar(self, ch: int) -> bool:
        pass

    def isEscapeDelimiter(self) -> bool:
        pass

    def isEscape(self, ch: int) -> bool:
        pass

    def isEndOfFile(self, ch: int) -> bool:
        pass

    def isDelimiter(self, ch: int) -> bool:
        pass

    def isCommentStart(self, ch: int) -> bool:
        pass

    def isClosed(self) -> bool:
        pass

    def getFirstEol(self) -> str:
        pass

    def getCurrentLineNumber(self) -> int:
        pass

    def getCharacterPosition(self) -> int:
        pass

    def __init__(self, format_: CSVFormat, reader: ExtendedBufferedReader) -> None:
        pass

    # Class Methods End
