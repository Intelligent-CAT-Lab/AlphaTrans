from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.codec.language.bm.RuleType import *
from src.main.org.apache.commons.codec.language.bm.ResourceConstants import *
from src.main.org.apache.commons.codec.language.bm.NameType import *
from src.main.org.apache.commons.codec.language.bm.Languages import *
from src.main.org.apache.commons.codec.Resources import *
import typing
from typing import *
import io
from io import StringIO
from abc import ABC

# Imports End


class PhonemeExpr(ABC):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def getPhonemes(self) -> typing.Iterable[Phoneme]:
        pass

    # Class Methods End


class RPattern(ABC):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def isMatch(self, input_: str) -> bool:
        pass

    # Class Methods End


class Phoneme(PhonemeExpr):

    # Class Fields Begin
    __phonemeText: typing.Union[typing.List[str], io.StringIO] = None
    __languages: LanguageSet = None
    COMPARATOR: typing.Callable[[Phoneme, Phoneme], int] = None
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:
        pass

    def join(self, right: Phoneme) -> Phoneme:
        pass

    def getPhonemes(self) -> typing.Iterable[Phoneme]:
        pass

    def mergeWithLanguage(self, lang: LanguageSet) -> Phoneme:
        pass

    def getPhonemeText(self) -> str:
        pass

    def getLanguages(self) -> LanguageSet:
        pass

    def append(self, str_: str) -> Phoneme:
        pass

    @staticmethod
    def Phoneme1(
        phonemeLeft: Phoneme, phonemeRight: Phoneme, languages: LanguageSet
    ) -> Phoneme:
        pass

    @staticmethod
    def Phoneme0(phonemeLeft: Phoneme, phonemeRight: Phoneme) -> Phoneme:
        pass

    def __init__(
        self,
        constructorId: int,
        phonemeText: str,
        languages: LanguageSet,
        phonemeRight: Phoneme,
    ) -> None:
        pass

    # Class Methods End


class PhonemeList(PhonemeExpr):

    # Class Fields Begin
    __phonemes: typing.List[Phoneme] = None
    # Class Fields End

    # Class Methods Begin
    def getPhonemes(self) -> typing.List[Phoneme]:
        pass

    def __init__(self, phonemes: typing.List[Phoneme]) -> None:
        pass

    # Class Methods End


class Rule:

    # Class Fields Begin
    ALL_STRINGS_RMATCHER: RPattern = None
    ALL: str = None
    __DOUBLE_QUOTE: str = None
    __HASH_INCLUDE: str = None
    __HASH_INCLUDE_LENGTH: int = None
    __RULES: typing.Dict[
        NameType,
        typing.Dict[RuleType, typing.Dict[str, typing.Dict[str, typing.List[Rule]]]],
    ] = None
    __lContext: RPattern = None
    __pattern: str = None
    __phoneme: PhonemeExpr = None
    __rContext: RPattern = None
    # Class Fields End

    # Class Methods Begin
    def patternAndContextMatches(self, input_: str, i: int) -> bool:
        pass

    def getRContext(self) -> RPattern:
        pass

    def getPhoneme(self) -> PhonemeExpr:
        pass

    def getPattern(self) -> str:
        pass

    def getLContext(self) -> RPattern:
        pass

    def __init__(
        self, pattern: str, lContext: str, rContext: str, phoneme: PhonemeExpr
    ) -> None:
        pass

    @staticmethod
    def getInstanceMap1(
        nameType: NameType, rt: RuleType, lang: str
    ) -> typing.Dict[str, typing.List[Rule]]:
        pass

    @staticmethod
    def getInstanceMap0(
        nameType: NameType, rt: RuleType, langs: LanguageSet
    ) -> typing.Dict[str, typing.List[Rule]]:
        pass

    @staticmethod
    def getInstance1(nameType: NameType, rt: RuleType, lang: str) -> typing.List[Rule]:
        pass

    @staticmethod
    def getInstance0(
        nameType: NameType, rt: RuleType, langs: LanguageSet
    ) -> typing.List[Rule]:
        pass

    @staticmethod
    def __stripQuotes(str_: str) -> str:
        pass

    @staticmethod
    def __startsWith(input_: str, prefix: str) -> bool:
        pass

    @staticmethod
    def __pattern(regex: str) -> RPattern:
        pass

    @staticmethod
    def __parseRules(
        scanner: typing.Any, location: str
    ) -> typing.Dict[str, typing.List[Rule]]:
        pass

    @staticmethod
    def __parsePhonemeExpr(ph: str) -> PhonemeExpr:
        pass

    @staticmethod
    def __parsePhoneme(ph: str) -> Phoneme:
        pass

    @staticmethod
    def __endsWith(input_: str, suffix: str) -> bool:
        pass

    @staticmethod
    def __createScanner1(lang: str) -> typing.Any:
        pass

    @staticmethod
    def __createScanner0(nameType: NameType, rt: RuleType, lang: str) -> typing.Any:
        pass

    @staticmethod
    def __createResourceName(nameType: NameType, rt: RuleType, lang: str) -> str:
        pass

    @staticmethod
    def __contains(chars: str, input_: str) -> bool:
        pass

    # Class Methods End
