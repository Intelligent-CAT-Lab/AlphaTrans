from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.codec.language.SoundexUtils import *
from src.main.org.apache.commons.codec.StringEncoder import *
from src.main.org.apache.commons.codec.EncoderException import *
import typing
from typing import *
import io

# Imports End


class Nysiis(StringEncoder):

    # Class Fields Begin
    __strict: bool = None
    __CHARS_A: typing.List[str] = None
    __CHARS_AF: typing.List[str] = None
    __CHARS_C: typing.List[str] = None
    __CHARS_FF: typing.List[str] = None
    __CHARS_G: typing.List[str] = None
    __CHARS_N: typing.List[str] = None
    __CHARS_NN: typing.List[str] = None
    __CHARS_S: typing.List[str] = None
    __CHARS_SSS: typing.List[str] = None
    __PAT_MAC: re.Pattern = None
    __PAT_KN: re.Pattern = None
    __PAT_K: re.Pattern = None
    __PAT_PH_PF: re.Pattern = None
    __PAT_SCH: re.Pattern = None
    __PAT_EE_IE: re.Pattern = None
    __PAT_DT_ETC: re.Pattern = None
    __SPACE: str = None
    __TRUE_LENGTH: int = None
    # Class Fields End

    # Class Methods Begin
    def encode(self, str_: str) -> str:
        pass

    def encode(self, obj: typing.Any) -> typing.Any:
        pass

    def nysiis(self, str_: str) -> str:
        pass

    def isStrict(self) -> bool:
        pass

    def encode1(self, str_: str) -> str:
        pass

    def encode0(self, obj: typing.Any) -> typing.Any:
        pass

    @staticmethod
    def Nysiis1() -> Nysiis:
        pass

    def __init__(self, strict: bool) -> None:
        pass

    @staticmethod
    def __transcodeRemaining(
        prev: str, curr: str, next_: str, aNext: str
    ) -> typing.List[str]:
        pass

    @staticmethod
    def __isVowel(c: str) -> bool:
        pass

    # Class Methods End
