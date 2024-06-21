from __future__ import annotations
import re
import io
import typing
from typing import *
from src.main.org.apache.commons.codec.EncoderException import *
from src.main.org.apache.commons.codec.StringEncoder import *


class Metaphone(StringEncoder):

    __maxCodeLen: int = 4

    __VARSON: str = "CSPTG"

    __FRONTV: str = "EIY"

    __VOWELS: str = "AEIOU"

    def setMaxCodeLen(self, maxCodeLen: int) -> None:

        self.__maxCodeLen = maxCodeLen

    def getMaxCodeLen(self) -> int:

        return self.__maxCodeLen

    def isMetaphoneEqual(self, str1: str, str2: str) -> bool:

        return self.metaphone(str1) == self.metaphone(str2)

    def encode1(self, str: str) -> str:

        return self.metaphone(str)

    def encode0(self, obj: typing.Any) -> typing.Any:

        if not isinstance(obj, str):
            raise EncoderException(
                "Parameter supplied to Metaphone encode is not of type java.lang.String",
                None,
            )
        return self.metaphone(obj)

    def metaphone(self, txt: str) -> str:

        pass  # LLM could not translate this method

    def __init__(self) -> None:

        pass  # LLM could not translate this method

    def __isLastChar(self, wdsz: int, n: int) -> bool:

        return n + 1 == wdsz

    def __regionMatch(self, string: str, index: int, test: str) -> bool:

        matches = False
        if index >= 0 and index + len(test) - 1 < len(string):
            substring = string[index : index + len(test)]
            matches = substring == test
        return matches

    def __isNextChar(self, string: str, index: int, c: str) -> bool:

        matches = False
        if index >= 0 and index < len(string) - 1:
            matches = string[index + 1] == c
        return matches

    def __isPreviousChar(self, string: str, index: int, c: str) -> bool:

        matches = False
        if index > 0 and index < len(string):
            matches = string[index - 1] == c
        return matches

    def __isVowel(self, string: str, index: int) -> bool:

        return self.__VOWELS.find(string[index]) >= 0
