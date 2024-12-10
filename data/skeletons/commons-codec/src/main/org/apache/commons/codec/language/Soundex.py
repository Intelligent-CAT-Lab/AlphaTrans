from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.codec.language.SoundexUtils import *
from src.main.org.apache.commons.codec.StringEncoder import *
from src.main.org.apache.commons.codec.EncoderException import *
import typing
from typing import *
import io

# Imports End


class Soundex(StringEncoder):

    # Class Fields Begin
    US_ENGLISH_GENEALOGY: Soundex = None
    __maxLength: int = None
    __soundexMapping: typing.List[str] = None
    __specialCaseHW: bool = None
    SILENT_MARKER: str = None
    US_ENGLISH_MAPPING_STRING: str = None
    __US_ENGLISH_MAPPING: typing.List[str] = None
    US_ENGLISH: Soundex = None
    US_ENGLISH_SIMPLIFIED: Soundex = None
    # Class Fields End

    # Class Methods Begin
    def setMaxLength(self, maxLength: int) -> None:
        pass

    def getMaxLength(self) -> int:
        pass

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
        self,
        constructorId: int,
        specialCaseHW: bool,
        mapping: str,
        mapping1: typing.List[str],
    ) -> None:
        pass

    def __map_(self, ch: str) -> str:
        pass

    def __hasMarker(self, mapping: typing.List[str]) -> bool:
        pass

    # Class Methods End
