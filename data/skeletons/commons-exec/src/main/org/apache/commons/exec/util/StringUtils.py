from __future__ import annotations

# Imports Begin
import typing
from typing import *
import io
from io import StringIO

# Imports End


class StringUtils:

    # Class Fields Begin
    __EMPTY_STRING_ARRAY: typing.List[typing.List[str]] = None
    __SINGLE_QUOTE: str = None
    __DOUBLE_QUOTE: str = None
    __SLASH_CHAR: str = None
    __BACKSLASH_CHAR: str = None
    # Class Fields End

    # Class Methods Begin
    @staticmethod
    def toString(strings: typing.List[typing.List[str]], separator: str) -> str:
        pass

    @staticmethod
    def stringSubstitution(
        argStr: str, vars_: typing.Dict[str, typing.Any], isLenient: bool
    ) -> io.StringIO:
        pass

    @staticmethod
    def split(input_: str, splitChar: str) -> typing.List[typing.List[str]]:
        pass

    @staticmethod
    def quoteArgument(argument: str) -> str:
        pass

    @staticmethod
    def isQuoted(argument: str) -> bool:
        pass

    @staticmethod
    def fixFileSeparatorChar(arg: str) -> str:
        pass

    # Class Methods End
