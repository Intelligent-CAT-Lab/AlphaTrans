from __future__ import annotations
import re
import unittest
import pytest
import io
import typing
from typing import *
import unittest
from src.main.org.apache.commons.codec.language.bm.Lang import *
from src.main.org.apache.commons.codec.language.bm.Languages import *
from src.main.org.apache.commons.codec.language.bm.NameType import *


class LanguageGuessingTest(unittest.TestCase):

    __name: str = ""

    __language: str = ""

    __lang: Lang = Lang.instance(NameType.GENERIC)

    def testLanguageGuessing(self) -> None:

        guesses = self.__lang.guessLanguages(self.__name)

        assert guesses.contains(
            self.__language
        ), f"language predicted for name '{self.__name}' is wrong: {guesses} should contain '{self.__language}'"

    @staticmethod
    def data() -> typing.List[typing.List[typing.Any]]:
        return [
            ["Renault", "french"],
            ["Mickiewicz", "polish"],
            ["Thompson", "english"],
            ["Nuñez", "spanish"],
            ["Carvalho", "portuguese"],
            ["Čapek", "czech"],
            ["Sjneijder", "dutch"],
            ["Klausewitz", "german"],
            ["K�ç�k", "turkish"],
            ["Giacometti", "italian"],
            ["Nagy", "hungarian"],
            ["Ceauşescu", "romanian"],
            ["Αγγελόπουλος", "greek"],
            ["Пушкин", "cyrillic"],
            ["כהן", "hebrew"],
            ["ácz", "any"],
            ["átz", "any"],
        ]

    def __init__(self, name: str, language: str) -> None:
        self.__name = name
        self.__language = language
