# Imports Begin
from src.main.org.apache.commons.fileupload.util.mime.MimeUtility import *
import os
import typing
from typing import *

from src.main.org.apache.commons.fileupload.java_handler import java_handler
# Imports End


@java_handler
class ParameterParser:

    # Class Fields Begin
    __chars: List[str] = []
    __pos: int = 0
    __len: int = ""  # LLM could not translate field
    __i1: int = ""  # LLM could not translate field
    __i2: int = ""  # LLM could not translate field
    __lowerCaseNames: bool = ""  # LLM could not translate field
    # Class Fields End

    # Class Methods Begin
    def parse3(
        self, charArray: typing.List[str], offset: int, length: int, separator: str
    ) -> typing.Dict[str, str]:

        pass  # LLM could not translate method body

    def parse2(
        self, charArray: typing.List[str], separator: str
    ) -> typing.Dict[str, str]:

        if charArray is None:
            return {}
        return self.parse3(charArray, 0, len(charArray), separator)

    def parse1(self, str: str, separator: str) -> typing.Dict[str, str]:

        if str is None:
            return {}
        return self.parse2(list(str), separator)

    def parse0(self, str: str, separators: typing.List[str]) -> typing.Dict[str, str]:

        if separators is None or len(separators) == 0:
            return {}
        separator = separators[0]
        if str is not None:
            idx = len(str)
            for separator2 in separators:
                tmp = str.find(separator2)
                if tmp != -1 and tmp < idx:
                    idx = tmp
                    separator = separator2
        return self.parse1(str, separator)

    def setLowerCaseNames(self, b: bool) -> None:

        self.__lowerCaseNames = b

    def isLowerCaseNames(self) -> bool:

        return self.__lowerCaseNames

    def __init__(self) -> None:

        super().__init__()

    def __parseQuotedToken(self, terminators: typing.List[str]) -> str:

        ch = None
        self.__i1 = self.__pos
        self.__i2 = self.__pos
        quoted = False
        charEscaped = False
        while self.__hasChar():
            ch = self.__chars[self.__pos]
            if not quoted and self.__isOneOf(ch, terminators):
                break
            if not charEscaped and ch == '"':
                quoted = not quoted
            charEscaped = not charEscaped and ch == "\\"
            self.__i2 += 1
            self.__pos += 1
        return self.__getToken(True)

    def __parseToken(self, terminators: typing.List[str]) -> str:

        ch = self.__chars[self.__pos]
        i1 = self.__pos
        i2 = self.__pos
        while self.__hasChar():
            if self.__isOneOf(ch, terminators):
                break
            i2 += 1
            self.__pos += 1
        return self.__getToken(False)

    def __isOneOf(self, ch: str, charray: typing.List[str]) -> bool:

        pass  # LLM could not translate method body

    def __getToken(self, quoted: bool) -> str:

        while (self.__i1 < self.__i2) and (
            Character.isWhitespace(self.__chars[self.__i1])
        ):
            self.__i1 += 1
        while (self.__i2 > self.__i1) and (
            Character.isWhitespace(self.__chars[self.__i2 - 1])
        ):
            self.__i2 -= 1
        if (
            quoted
            and ((self.__i2 - self.__i1) >= 2)
            and (self.__chars[self.__i1] == '"')
            and (self.__chars[self.__i2 - 1] == '"')
        ):
            self.__i1 += 1
            self.__i2 -= 1
        result = None
        if self.__i2 > self.__i1:
            result = str(self.__chars[self.__i1 : self.__i2])
        return result

    def __hasChar(self) -> bool:

        return self.__pos < self.__len

    # Class Methods End
