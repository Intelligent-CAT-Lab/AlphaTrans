from __future__ import annotations
import re
import unittest
import pytest
import io
import typing
from typing import *
import unittest
from src.main.org.apache.commons.codec.language.bm.Languages import *
from src.main.org.apache.commons.codec.language.bm.Rule import *


class RuleTest(unittest.TestCase):

    def testSubSequenceWorks(self) -> None:

        pass  # LLM could not translate this method

    def testPhonemeComparedToSelfIsZero(self) -> None:
        for phs in self.__makePhonemes():
            for ph in phs:
                self.assertEqual(
                    "Phoneme compared to itself should be zero: " + ph.getPhonemeText(),
                    0,
                    Phoneme.COMPARATOR(ph, ph),
                )

    def __makePhonemes(self) -> typing.List[typing.List[Phoneme]]:
        words = [
            ["rinD", "rinDlt", "rina", "rinalt", "rino", "rinolt", "rinu", "rinult"],
            ["dortlaj", "dortlej", "ortlaj", "ortlej", "ortlej-dortlaj"],
        ]
        phonemes = [[None for _ in range(len(words[i]))] for i in range(len(words))]

        for i in range(len(words)):
            for j in range(len(words[i])):
                phonemes[i][j] = Phoneme(2, words[i][j], Languages.NO_LANGUAGES, None)

        return phonemes
