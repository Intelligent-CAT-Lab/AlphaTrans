from __future__ import annotations
import copy
import re
import io
import typing
from typing import *
from src.main.org.apache.commons.codec.EncoderException import *
from src.main.org.apache.commons.codec.StringEncoder import *
from src.main.org.apache.commons.codec.language.SoundexUtils import *


class Soundex(StringEncoder):

    US_ENGLISH_GENEALOGY: Soundex = None
    US_ENGLISH: Soundex = None
    US_ENGLISH_MAPPING_STRING: str = "01230120022455012623010202"
    SILENT_MARKER: str = "-"
    __specialCaseHW: bool = False

    __soundexMapping: typing.List[str] = None

    __maxLength: int = 4
    __US_ENGLISH_MAPPING: typing.List[str] = list(US_ENGLISH_MAPPING_STRING)
    US_ENGLISH_SIMPLIFIED: Soundex = None

    @staticmethod
    def initialize_fields() -> None:
        Soundex.US_ENGLISH_GENEALOGY: Soundex = Soundex(
            1, False, "-123-12--22455-12623-1-2-2", None
        )

        Soundex.US_ENGLISH: Soundex = Soundex(3, False, None, None)

        Soundex.US_ENGLISH_SIMPLIFIED: Soundex = Soundex(
            0, False, US_ENGLISH_MAPPING_STRING, None
        )

    def setMaxLength(self, maxLength: int) -> None:
        self.__maxLength = maxLength

    def getMaxLength(self) -> int:
        return self.__maxLength

    def soundex(self, str: str) -> str:
        if str is None:
            return None
        str = SoundexUtils.clean(str)
        if str == "":
            return str
        out = ["0", "0", "0", "0"]
        count = 0
        first = str[0]
        out[count] = first
        count += 1
        lastDigit = self.__map(first)  # previous digit
        for i in range(1, len(str)):
            if count >= len(out):
                break
            ch = str[i]
            if self.__specialCaseHW and (
                ch == "H" or ch == "W"
            ):  # these are ignored completely
                continue
            digit = self.__map(ch)
            if digit == Soundex.SILENT_MARKER:
                continue
            if digit != "0" and digit != lastDigit:  # don't store vowels or repeats
                out[count] = digit
                count += 1
            lastDigit = digit
        return "".join(out)

    def encode1(self, str: str) -> str:
        return self.soundex(str)

    def encode0(self, obj: typing.Any) -> typing.Any:
        if not isinstance(obj, str):
            raise EncoderException(
                "Parameter supplied to Soundex encode is not of type java.lang.String",
                None,
            )
        return self.soundex(obj)

    def difference(self, s1: str, s2: str) -> int:
        return SoundexUtils.difference(self, s1, s2)

    def __init__(
        self,
        constructorId: int,
        specialCaseHW: bool,
        mapping: str,
        mapping1: typing.List[str],
    ) -> None:
        if constructorId == 0:
            self.__soundexMapping = list(mapping)
            self.__specialCaseHW = specialCaseHW
        elif constructorId == 1:
            self.__soundexMapping = list(mapping)
            self.__specialCaseHW = not self.__hasMarker(self.__soundexMapping)
        elif constructorId == 2:
            self.__soundexMapping = mapping1.copy()
            self.__specialCaseHW = not self.__hasMarker(self.__soundexMapping)
        else:
            self.__soundexMapping = self.__US_ENGLISH_MAPPING
            self.__specialCaseHW = True

    def __map(self, ch: str) -> str:
        index = ord(ch) - ord("A")
        if index < 0 or index >= len(self.__soundexMapping):
            raise ValueError(
                "The character is not mapped: " + ch + " (index=" + str(index) + ")"
            )
        return self.__soundexMapping[index]

    def __hasMarker(self, mapping: typing.List[str]) -> bool:

        pass  # LLM could not translate this method


Soundex.initialize_fields()
