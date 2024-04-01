# Imports Begin
from src.main.org.apache.commons.codec.language.bm.Rule import *
from src.main.org.apache.commons.codec.language.bm.Languages import *
import unittest
import typing
from typing import *

# Imports End


class RuleTest(unittest.TestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def testSubSequenceWorks(self) -> None:

        pass  # LLM could not translate method body

    def testPhonemeComparedToSelfIsZero(self) -> None:

        pass  # LLM could not translate method body

    def __makePhonemes(self) -> typing.List[typing.List[Phoneme]]:

        words = [
            ["rinD", "rinDlt", "rina", "rinalt", "rino", "rinolt", "rinu", "rinult"],
            ["dortlaj", "dortlej", "ortlaj", "ortlej", "ortlej-dortlaj"],
        ]
        phonemes = []
        for i in range(len(words)):
            words_i = words[i]
            phonemes_i = phonemes[i] = []
            for j in range(len(words_i)):
                phonemes_i.append(
                    Rule.Phoneme(2, words_i[j], Languages.NO_LANGUAGES, None)
                )
        return phonemes

    # Class Methods End
