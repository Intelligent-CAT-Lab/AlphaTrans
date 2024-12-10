from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.codec.language.bm.ResourceConstants import *
from src.main.org.apache.commons.codec.language.bm.NameType import *
from src.main.org.apache.commons.codec.Resources import *
import typing
from typing import *
import io
from abc import ABC

# Imports End


class LanguageSet(ABC):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    @staticmethod
    def from_(langs: typing.Set[str]) -> LanguageSet:
        pass

    def merge(self, other: LanguageSet) -> LanguageSet:
        pass

    def restrictTo(self, other: LanguageSet) -> LanguageSet:
        pass

    def isSingleton(self) -> bool:
        pass

    def isEmpty(self) -> bool:
        pass

    def getAny(self) -> str:
        pass

    def contains(self, language: str) -> bool:
        pass

    # Class Methods End


class AnyLanguage(LanguageSet):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:
        pass

    def merge(self, other: LanguageSet) -> LanguageSet:
        pass

    def restrictTo(self, other: LanguageSet) -> LanguageSet:
        pass

    def isSingleton(self) -> bool:
        pass

    def isEmpty(self) -> bool:
        pass

    def getAny(self) -> str:
        pass

    def contains(self, language: str) -> bool:
        pass

    def __init__(self) -> None:
        pass

    # Class Methods End


class NoLanguage(LanguageSet):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:
        pass

    def merge(self, other: LanguageSet) -> LanguageSet:
        pass

    def restrictTo(self, other: LanguageSet) -> LanguageSet:
        pass

    def isSingleton(self) -> bool:
        pass

    def isEmpty(self) -> bool:
        pass

    def getAny(self) -> str:
        pass

    def contains(self, language: str) -> bool:
        pass

    def __init__(self) -> None:
        pass

    # Class Methods End


class SomeLanguages(LanguageSet):

    # Class Fields Begin
    __languages: typing.Set[str] = None
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:
        pass

    def merge(self, other: LanguageSet) -> LanguageSet:
        pass

    def restrictTo(self, other: LanguageSet) -> LanguageSet:
        pass

    def isSingleton(self) -> bool:
        pass

    def isEmpty(self) -> bool:
        pass

    def getAny(self) -> str:
        pass

    def contains(self, language: str) -> bool:
        pass

    def getLanguages(self) -> typing.Set[str]:
        pass

    def __init__(self, languages: typing.Set[str]) -> None:
        pass

    # Class Methods End


class Languages:

    # Class Fields Begin
    ANY: str = None
    __LANGUAGES: typing.Dict[NameType, Languages] = None
    __languages: typing.Set[str] = None
    NO_LANGUAGES: LanguageSet = None
    ANY_LANGUAGE: LanguageSet = None
    # Class Fields End

    # Class Methods Begin
    def getLanguages(self) -> typing.Set[str]:
        pass

    @staticmethod
    def getInstance1(languagesResourceName: str) -> Languages:
        pass

    @staticmethod
    def getInstance0(nameType: NameType) -> Languages:
        pass

    def __init__(self, languages: typing.Set[str]) -> None:
        pass

    @staticmethod
    def __langResourceName(nameType: NameType) -> str:
        pass

    # Class Methods End
