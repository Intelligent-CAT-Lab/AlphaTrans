from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.codec.language.bm.RuleType import *
from src.main.org.apache.commons.codec.language.bm.Rule import *
from src.main.org.apache.commons.codec.language.bm.NameType import *
from src.main.org.apache.commons.codec.language.bm.Languages import *
from src.main.org.apache.commons.codec.language.bm.Lang import *
import typing
from typing import *
import io

# Imports End


class PhonemeBuilder:

    # Class Fields Begin
    __phonemes: typing.Set[Phoneme] = None
    # Class Fields End

    # Class Methods Begin
    def makeString(self) -> str:
        pass

    def getPhonemes(self) -> typing.Set[Phoneme]:
        pass

    def apply(self, phonemeExpr: PhonemeExpr, maxPhonemes: int) -> None:
        pass

    def append(self, str_: str) -> None:
        pass

    def __init__(
        self, constructorId: int, phonemes: typing.Set[Phoneme], phoneme: Phoneme
    ) -> None:
        pass

    @staticmethod
    def empty(languages: LanguageSet) -> PhonemeBuilder:
        pass

    # Class Methods End


class RulesApplication:

    # Class Fields Begin
    __finalRules: typing.Dict[str, typing.List[Rule]] = None
    __input: str = None
    __phonemeBuilder: PhonemeBuilder = None
    __i: int = None
    __maxPhonemes: int = None
    __found: bool = None
    # Class Fields End

    # Class Methods Begin
    def isFound(self) -> bool:
        pass

    def invoke(self) -> RulesApplication:
        pass

    def getPhonemeBuilder(self) -> PhonemeBuilder:
        pass

    def getI(self) -> int:
        pass

    def __init__(
        self,
        finalRules: typing.Dict[str, typing.List[Rule]],
        input_: str,
        phonemeBuilder: PhonemeBuilder,
        i: int,
        maxPhonemes: int,
    ) -> None:
        pass

    # Class Methods End


class PhoneticEngine:

    # Class Fields Begin
    __NAME_PREFIXES: typing.Dict[NameType, typing.Set[str]] = None
    __DEFAULT_MAX_PHONEMES: int = None
    __lang: Lang = None
    __nameType: NameType = None
    __ruleType: RuleType = None
    __concat: bool = None
    __maxPhonemes: int = None
    # Class Fields End

    # Class Methods Begin
    def getMaxPhonemes(self) -> int:
        pass

    def isConcat(self) -> bool:
        pass

    def getRuleType(self) -> RuleType:
        pass

    def getNameType(self) -> NameType:
        pass

    def getLang(self) -> Lang:
        pass

    def encode1(self, input_: str, languageSet: LanguageSet) -> str:
        pass

    def encode0(self, input_: str) -> str:
        pass

    def __init__(
        self, nameType: NameType, ruleType: RuleType, concat: bool, maxPhonemes: int
    ) -> None:
        pass

    @staticmethod
    def PhoneticEngine0(
        nameType: NameType, ruleType: RuleType, concat: bool
    ) -> PhoneticEngine:
        pass

    def __applyFinalRules(
        self,
        phonemeBuilder: PhonemeBuilder,
        finalRules: typing.Dict[str, typing.List[Rule]],
    ) -> PhonemeBuilder:
        pass

    @staticmethod
    def __join(strings: typing.Iterable[str], sep: str) -> str:
        pass

    # Class Methods End
