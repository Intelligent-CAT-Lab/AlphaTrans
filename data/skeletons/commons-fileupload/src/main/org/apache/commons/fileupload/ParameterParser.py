from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.fileupload.util.mime.MimeUtility import *
import os
import typing
from typing import *
import io

# Imports End


class ParameterParser:

    # Class Fields Begin
    __chars: typing.List[str] = None
    __pos: int = None
    __len: int = None
    __i1: int = None
    __i2: int = None
    __lowerCaseNames: bool = None
    # Class Fields End

    # Class Methods Begin
    def parse3(
        self, charArray: typing.List[str], offset: int, length: int, separator: str
    ) -> typing.Dict[str, str]:
        pass

    def parse2(
        self, charArray: typing.List[str], separator: str
    ) -> typing.Dict[str, str]:
        pass

    def parse1(self, str_: str, separator: str) -> typing.Dict[str, str]:
        pass

    def parse0(self, str_: str, separators: typing.List[str]) -> typing.Dict[str, str]:
        pass

    def setLowerCaseNames(self, b: bool) -> None:
        pass

    def isLowerCaseNames(self) -> bool:
        pass

    def __init__(self) -> None:
        pass

    def __parseQuotedToken(self, terminators: typing.List[str]) -> str:
        pass

    def __parseToken(self, terminators: typing.List[str]) -> str:
        pass

    def __isOneOf(self, ch: str, charray: typing.List[str]) -> bool:
        pass

    def __getToken(self, quoted: bool) -> str:
        pass

    def __hasChar(self) -> bool:
        pass

    # Class Methods End
