from __future__ import annotations
import re
from abc import ABC
import io
import typing
from typing import *
from src.main.org.apache.commons.codec.Resources import *
from src.main.org.apache.commons.codec.language.bm.NameType import *
from src.main.org.apache.commons.codec.language.bm.ResourceConstants import *


class LanguageSet(ABC):

    @staticmethod
    def from_(langs: typing.Set[str]) -> LanguageSet:
        return NO_LANGUAGES if langs.isEmpty() else SomeLanguages(langs)

    def merge(self, other: LanguageSet) -> LanguageSet:
        return LanguageSet()

    def restrictTo(self, other: LanguageSet) -> LanguageSet:
        return LanguageSetIntersection(self, other)

    def isSingleton(self) -> bool:
        return self.size() == 1

    def isEmpty(self) -> bool:
        return self.languages == None or self.languages.isEmpty()

    def getAny(self) -> str:
        return self.getLanguages().get(0)

    def contains(self, language: str) -> bool:
        return language in self.languages


class AnyLanguage(LanguageSet):

    def toString(self) -> str:
        return "ANY_LANGUAGE"

    def merge(self, other: LanguageSet) -> LanguageSet:
        return other

    def restrictTo(self, other: LanguageSet) -> LanguageSet:
        return other

    def isSingleton(self) -> bool:
        return False

    def isEmpty(self) -> bool:
        return False

    def getAny(self) -> str:
        raise RuntimeError("Can't fetch any language from the any language set.")

    def contains(self, language: str) -> bool:
        return True

    def __init__(self) -> None:
        super().__init__()


class NoLanguage(LanguageSet):

    def toString(self) -> str:
        return "NO_LANGUAGES"

    def merge(self, other: LanguageSet) -> LanguageSet:
        return other

    def restrictTo(self, other: LanguageSet) -> LanguageSet:
        return self

    def isSingleton(self) -> bool:
        return False

    def isEmpty(self) -> bool:
        return True

    def getAny(self) -> str:
        raise RuntimeError("Can't fetch any language from the empty language set.")

    def contains(self, language: str) -> bool:
        return False

    def __init__(self) -> None:
        super().__init__()


class SomeLanguages(LanguageSet):

    __languages: typing.Set[str] = None

    def toString(self) -> str:
        return "Languages(" + self.__languages.toString() + ")"

    def merge(self, other: LanguageSet) -> LanguageSet:
        if other == NO_LANGUAGES:
            return self
        if other == ANY_LANGUAGE:
            return other
        some_languages = typing.cast(SomeLanguages, other)
        set_ = set(self.__languages)
        set_.update(some_languages.__languages)
        return LanguageSet.from_(set_)

    def restrictTo(self, other: LanguageSet) -> LanguageSet:
        if other == NO_LANGUAGES:
            return other
        if other == ANY_LANGUAGE:
            return self
        someLanguages = typing.cast(SomeLanguages, other)
        set = set()
        for lang in self.__languages:
            if lang in someLanguages.__languages:
                set.add(lang)
        return LanguageSet.from_(set)

    def isSingleton(self) -> bool:
        return len(self.__languages) == 1

    def isEmpty(self) -> bool:
        return self.__languages.isEmpty()

    def getAny(self) -> str:
        return next(iter(self.__languages))

    def contains(self, language: str) -> bool:
        return self.__languages.contains(language)

    def getLanguages(self) -> typing.Set[str]:
        return self.__languages

    def __init__(self, languages: typing.Set[str]) -> None:
        self.__languages = frozenset(languages)


class Languages:

    ANY_LANGUAGE: LanguageSet = None
    ANY_LANGUAGE: LanguageSet = None
    NO_LANGUAGES: LanguageSet = None
    NO_LANGUAGES: LanguageSet = None
    ANY: str = "any"
    __languages: typing.Set[str] = None

    __LANGUAGES: typing.Dict[NameType, Languages] = {}

    @staticmethod
    def initialize_fields() -> None:
        Languages.ANY_LANGUAGE: LanguageSet = AnyLanguage()

        Languages.ANY_LANGUAGE: LanguageSet = AnyLanguage()

        Languages.NO_LANGUAGES: LanguageSet = NoLanguage()

        Languages.NO_LANGUAGES: LanguageSet = NoLanguage()

        Languages.__LANGUAGES: typing.Dict[NameType, Languages] = {}

    @staticmethod
    def run_static_init():
        for s in NameType:
            Languages.__LANGUAGES[s] = Languages.getInstance1(
                Languages.__langResourceName(s)
            )

    def getLanguages(self) -> typing.Set[str]:
        return self.__languages

    @staticmethod
    def getInstance1(languagesResourceName: str) -> Languages:
        ls: typing.Set[str] = set()
        with Resources.getInputStream(languagesResourceName) as lsScanner:
            inExtendedComment: bool = False
            while lsScanner.hasNextLine():
                line: str = lsScanner.nextLine().trim()
                if inExtendedComment:
                    if line.endsWith(ResourceConstants.EXT_CMT_END):
                        inExtendedComment = False
                else:
                    if line.startsWith(ResourceConstants.EXT_CMT_START):
                        inExtendedComment = True
                    else:
                        if not line.isEmpty():
                            ls.add(line)
        return Languages(Collections.unmodifiableSet(ls))

    @staticmethod
    def getInstance0(nameType: NameType) -> Languages:
        return Languages.__LANGUAGES.get(nameType)

    def __init__(self, languages: typing.Set[str]) -> None:
        self.__languages = languages

    @staticmethod
    def __langResourceName(nameType: NameType) -> str:
        return (
            f"org/apache/commons/codec/language/bm/{nameType.getName()}_languages.txt"
        )


Languages.initialize_fields()

Languages.run_static_init()
