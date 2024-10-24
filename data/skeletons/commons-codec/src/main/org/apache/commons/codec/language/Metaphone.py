from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.codec.StringEncoder import *
from src.main.org.apache.commons.codec.EncoderException import *
import typing
from typing import *
import io
from io import StringIO

# Imports End


class Metaphone(StringEncoder):

    # Class Fields Begin
    __VOWELS: str = None
    __FRONTV: str = None
    __VARSON: str = None
    __maxCodeLen: int = None
    # Class Fields End

    # Class Methods Begin
    def encode(self, str_: str) -> str:
        pass

    def encode(self, obj: typing.Any) -> typing.Any:
        pass

    def setMaxCodeLen(self, maxCodeLen: int) -> None:
        pass

    def getMaxCodeLen(self) -> int:
        pass

    def isMetaphoneEqual(self, str1: str, str2: str) -> bool:
        pass

    def encode1(self, str_: str) -> str:
        pass

    def encode0(self, obj: typing.Any) -> typing.Any:
        pass

    def metaphone(self, txt: str) -> str:
        pass

    def __init__(self) -> None:
        pass

    def __isLastChar(self, wdsz: int, n: int) -> bool:
        pass

    def __regionMatch(
        self, string: typing.Union[typing.List[str], io.StringIO], index: int, test: str
    ) -> bool:
        pass

    def __isNextChar(
        self, string: typing.Union[typing.List[str], io.StringIO], index: int, c: str
    ) -> bool:
        pass

    def __isPreviousChar(
        self, string: typing.Union[typing.List[str], io.StringIO], index: int, c: str
    ) -> bool:
        pass

    def __isVowel(
        self, string: typing.Union[typing.List[str], io.StringIO], index: int
    ) -> bool:
        pass

    # Class Methods End
