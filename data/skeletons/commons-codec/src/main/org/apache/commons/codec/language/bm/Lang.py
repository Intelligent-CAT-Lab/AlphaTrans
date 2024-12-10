from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.codec.language.bm.ResourceConstants import *
from src.main.org.apache.commons.codec.language.bm.NameType import *
from src.main.org.apache.commons.codec.language.bm.Languages import *
from src.main.org.apache.commons.codec.Resources import *
import typing
from typing import *
import io

# Imports End


class LangRule:

    # Class Fields Begin
    __acceptOnMatch: bool = None
    __languages: typing.Set[str] = None
    __pattern: re.Pattern = None
    # Class Fields End

    # Class Methods Begin
    def matches(self, txt: str) -> bool:
        pass

    def __init__(
        self, pattern: re.Pattern, languages: typing.Set[str], acceptOnMatch: bool
    ) -> None:
        pass

    # Class Methods End


class Lang:

    # Class Fields Begin
    __LANGUAGE_RULES_RN: str = None
    __languages: Languages = None
    __rules: typing.List[LangRule] = None
    __Langs: typing.Dict[NameType, Lang] = None
    # Class Fields End

    # Class Methods Begin
    def guessLanguages(self, input_: str) -> LanguageSet:
        pass

    def guessLanguage(self, text: str) -> str:
        pass

    @staticmethod
    def loadFromResource(languageRulesResourceName: str, languages: Languages) -> Lang:
        pass

    @staticmethod
    def instance(nameType: NameType) -> Lang:
        pass

    def __init__(self, rules: typing.List[LangRule], languages: Languages) -> None:
        pass

    # Class Methods End
