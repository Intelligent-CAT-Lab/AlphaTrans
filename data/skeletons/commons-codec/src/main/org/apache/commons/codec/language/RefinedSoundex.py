from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.codec.language.SoundexUtils import *
from src.main.org.apache.commons.codec.StringEncoder import *
from src.main.org.apache.commons.codec.EncoderException import *
import typing
from typing import *
import io

# Imports End


class RefinedSoundex(StringEncoder):

    # Class Fields Begin
    US_ENGLISH_MAPPING_STRING: str = None
    __US_ENGLISH_MAPPING: typing.List[str] = None
    __soundexMapping: typing.List[str] = None
    US_ENGLISH: RefinedSoundex = None
    # Class Fields End

    # Class Methods Begin
    def encode(self, str_: str) -> str:
        pass

    def encode(self, obj: typing.Any) -> typing.Any:
        pass

    def soundex(self, str_: str) -> str:
        pass

    def encode1(self, str_: str) -> str:
        pass

    def encode0(self, obj: typing.Any) -> typing.Any:
        pass

    def difference(self, s1: str, s2: str) -> int:
        pass

    def __init__(
        self, constructorId: int, mapping: str, mapping1: typing.List[str]
    ) -> None:
        pass

    def getMappingCode(self, c: str) -> str:
        pass

    # Class Methods End
