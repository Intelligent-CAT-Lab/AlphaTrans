from __future__ import annotations
import re
import io
import typing
from typing import *
from src.main.org.apache.commons.codec.EncoderException import *
from src.main.org.apache.commons.codec.StringEncoder import *
from src.main.org.apache.commons.codec.language.SoundexUtils import *


class RefinedSoundex(StringEncoder):

    US_ENGLISH: RefinedSoundex = None
    US_ENGLISH_MAPPING_STRING: str = "01360240043788015936020505"
    __soundexMapping: typing.List[str] = None

    __US_ENGLISH_MAPPING: typing.List[str] = list(US_ENGLISH_MAPPING_STRING)

    @staticmethod
    def initialize_fields() -> None:
        RefinedSoundex.US_ENGLISH: RefinedSoundex = RefinedSoundex(2, None, None)

    def soundex(self, str: str) -> str:
        if str is None:
            return None
        str = SoundexUtils.clean(str)
        if str == "":
            return str

        sBuf = []
        sBuf.append(str[0])

        last, current = "*", "*"

        for i in range(len(str)):

            current = self.getMappingCode(str[i])
            if current == last:
                continue
            if current != "0":
                sBuf.append(current)

            last = current

        return "".join(sBuf)

    def encode1(self, str: str) -> str:
        return self.soundex(str)

    def encode0(self, obj: typing.Any) -> typing.Any:
        if not isinstance(obj, str):
            raise EncoderException(
                "Parameter supplied to RefinedSoundex encode is not of type java.lang.String",
                None,
            )
        return self.soundex(obj)

    def difference(self, s1: str, s2: str) -> int:
        return SoundexUtils.difference(self, s1, s2)

    def __init__(
        self, constructorId: int, mapping: str, mapping1: typing.List[str]
    ) -> None:

        pass  # LLM could not translate this method

    def getMappingCode(self, c: str) -> str:
        if not c.isalpha():
            return "0"
        return self.__soundexMapping[ord(c.upper()) - ord("A")]


RefinedSoundex.initialize_fields()
