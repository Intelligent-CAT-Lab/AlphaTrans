# Imports Begin
from src.main.org.apache.commons.codec.language.bm.NameType import *
from src.main.org.apache.commons.codec.language.bm.Languages import *
from src.main.org.apache.commons.codec.language.bm.Lang import *
import unittest
import typing
from typing import *

# Imports End


class LanguageGuessingTest(unittest.TestCase):

    # Class Fields Begin
    __lang: Lang = ""  # LLM could not translate field
    __language: str = None
    __name: str = None
    # Class Fields End

    # Class Methods Begin
    def testLanguageGuessing(self) -> None:

        guesses = self.lang.guessLanguages(self.name)
        self.assertTrue(
            "language predicted for name '"
            + self.name
            + "' is wrong: "
            + guesses
            + " should contain '"
            + self.language
            + "'",
            guesses.contains(self.language),
        )

    @staticmethod
    def data() -> typing.List[typing.List[typing.Any]]:

        pass  # LLM could not translate method body

    def __init__(self, name: str, language: str) -> None:

        self.__name = name
        self.__language = language

    # Class Methods End
