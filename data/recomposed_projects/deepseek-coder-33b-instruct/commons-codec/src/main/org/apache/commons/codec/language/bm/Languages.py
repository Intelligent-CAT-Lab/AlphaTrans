from __future__ import annotations
import re
from dataclasses import field
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

        if not langs:
            return NO_LANGUAGES
        else:
            return SomeLanguages(langs)

    def merge(self, other: LanguageSet) -> LanguageSet:

        # Your implementation here
        pass

    def restrictTo(self, other: LanguageSet) -> LanguageSet:

        # Your implementation here
        pass

    def isSingleton(self) -> bool:

        pass

    def isEmpty(self) -> bool:

        pass

    def getAny(self) -> str:

        pass

    def contains(self, language: str) -> bool:

        pass


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

        raise NoSuchElementException(
            "Can't fetch any language from the any language set."
        )

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

        raise NoSuchElementException(
            "Can't fetch any language from the empty language set."
        )

    def contains(self, language: str) -> bool:

        return False

    def __init__(self) -> None:

        super().__init__()


class SomeLanguages(LanguageSet):

    __languages: typing.Set[str] = None

    def toString(self) -> str:

        return "Languages(" + str(self.__languages) + ")"

    def merge(self, other: LanguageSet) -> LanguageSet:

        if other == NO_LANGUAGES:
            return self
        if other == ANY_LANGUAGE:
            return other
        someLanguages = other
        set_ = set(self.__languages)
        set_.update(someLanguages.languages)
        return self.from_(set_)

    def restrictTo(self, other: LanguageSet) -> LanguageSet:

        if other == NO_LANGUAGES:
            return other
        if other == ANY_LANGUAGE:
            return self
        someLanguages = other
        set_ = set(min(len(self.__languages), len(someLanguages.__languages)))
        for lang in self.__languages:
            if lang in someLanguages.__languages:
                set_.add(lang)
        return self.from_(set_)

    def isSingleton(self) -> bool:

        return len(self.__languages) == 1

    def isEmpty(self) -> bool:

        if self.__languages is None:
            return True
        else:
            return len(self.__languages) == 0

    def getAny(self) -> str:

        if self.__languages is None:
            return None

        for language in self.__languages:
            return language

    def contains(self, language: str) -> bool:

        if self.__languages is None:
            return False

        return language in self.__languages

    def getLanguages(self) -> typing.Set[str]:

        return self.__languages

    def __init__(self, languages: typing.Set[str]) -> None:

        self.__languages = frozenset(languages)


class Languages:

    ANY_LANGUAGE: LanguageSet = None
    NO_LANGUAGES: LanguageSet = None

    ANY: str = "any"
    __languages: typing.Set[str] = None

    __LANGUAGES: Dict[NameType, Languages] = {}

    @staticmethod
    def initialize_fields() -> None:
        Languages.ANY_LANGUAGE: LanguageSet = AnyLanguage()

        Languages.NO_LANGUAGES: LanguageSet = NoLanguage()

    def getLanguages(self) -> typing.Set[str]:

        return self.__languages

    @staticmethod
    def getInstance1(languagesResourceName: str) -> Languages:

        ls = set()
        with io.open(
            Resources.getInputStream(languagesResourceName),
            "r",
            encoding=ResourceConstants.ENCODING,
        ) as lsScanner:
            inExtendedComment = False
            for line in lsScanner:
                line = line.strip()
                if inExtendedComment:
                    if line.endswith(ResourceConstants.EXT_CMT_END):
                        inExtendedComment = False
                elif line.startswith(ResourceConstants.EXT_CMT_START):
                    inExtendedComment = True
                elif line:
                    ls.add(line)

        return Languages(frozenset(ls))

    @staticmethod
    def getInstance0(nameType: NameType) -> Languages:

        return Languages.__LANGUAGES.get(nameType)

    def __init__(self, languages: typing.Set[str]) -> None:

        self.__languages = languages

    @staticmethod
    def __langResourceName(nameType: NameType) -> str:

        return "org/apache/commons/codec/language/bm/{}_languages.txt".format(
            nameType.getName()
        )


Languages.initialize_fields()
