from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.codec.StringEncoder import *
from src.main.org.apache.commons.codec.EncoderException import *
import typing
from typing import *
import io

# Imports End


class MatchRatingApproachEncoder(StringEncoder):

    # Class Fields Begin
    __SPACE: str = None
    __EMPTY: str = None
    __PLAIN_ASCII: str = None
    __UNICODE: str = None
    __DOUBLE_CONSONANT: typing.List[typing.List[str]] = None
    # Class Fields End

    # Class Methods Begin
    def encode(self, name: str) -> str:
        pass

    def encode(self, pObject: typing.Any) -> typing.Any:
        pass

    def isEncodeEquals(self, name1: str, name2: str) -> bool:
        pass

    def encode1(self, name: str) -> str:
        pass

    def encode0(self, pObject: typing.Any) -> typing.Any:
        pass

    def removeVowels(self, name: str) -> str:
        pass

    def removeDoubleConsonants(self, name: str) -> str:
        pass

    def removeAccents(self, accentedWord: str) -> str:
        pass

    def leftToRightThenRightToLeftProcessing(self, name1: str, name2: str) -> int:
        pass

    def isVowel(self, letter: str) -> bool:
        pass

    def getMinRating(self, sumLength: int) -> int:
        pass

    def getFirst3Last3(self, name: str) -> str:
        pass

    def cleanName(self, name: str) -> str:
        pass

    # Class Methods End
