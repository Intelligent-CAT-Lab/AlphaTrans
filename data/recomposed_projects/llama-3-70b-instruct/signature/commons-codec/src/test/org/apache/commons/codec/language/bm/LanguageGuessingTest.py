from __future__ import annotations
import re
import os
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
        guesses: LanguageSet = self.__lang.guessLanguages(self.__name)

        self.assertTrue(
            "language predicted for name '"
            + self.__name
            + "' is wrong: "
            + str(guesses)
            + " should contain '"
            + self.__language
            + "'",
            guesses.contains(self.__language),
        )

    @staticmethod
    def data() -> typing.List[typing.List[typing.Any]]:
        return [
            ["Renault", "french"],
            ["Mickiewicz", "polish"],
            ["Thompson", "english"],  # this also hits german and greeklatin
            ["Nu\u00f1ez", "spanish"],  # Nuñez
            ["Carvalho", "portuguese"],
            ["\u010capek", "czech"],  # Čapek
            ["Sjneijder", "dutch"],
            ["Klausewitz", "german"],
            ["K\u00fc\u00e7\u00fck", "turkish"],  # Küçük
            ["Giacometti", "italian"],
            ["Nagy", "hungarian"],
            ["Ceau\u015fescu", "romanian"],  # Ceauşescu
            ["Angelopoulos", "greeklatin"],
            {
                "\u0391\u03b3\u03b3\u03b5\u03bb\u03cc\u03c0\u03bf\u03c5\u03bb\u03bf\u03c2",
                "greek",
            },  # Αγγελόπουλος
            ["\u041f\u0443\u0448\u043a\u0438\u043d", "cyrillic"],  # Пушкин
            ["\u05db\u05d4\u05df", "hebrew"],  # כהן
            ["\u00e1cz", "any"],  # ácz
            ["\u00e1tz", "any"],
        ]  # átz

    def __init__(self, name: str, language: str) -> None:
        self.__name = name
        self.__language = language
