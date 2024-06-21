from __future__ import annotations
import re
import unittest
import pytest
import io
import typing
from typing import *
from src.main.org.apache.commons.codec.language.bm.Languages import *
from src.main.org.apache.commons.codec.language.bm.Rule import *


class RuleTest(unittest.TestCase):

    def testSubSequenceWorks(self) -> None:

        a = Phoneme(2, "a", None, None)
        b = Phoneme(2, "b", None, None)
        cd = Phoneme(2, "cd", None, None)
        ef = Phoneme(2, "ef", None, None)
        ghi = Phoneme(2, "ghi", None, None)
        jkl = Phoneme(2, "jkl", None, None)

        assert "a" == a.getPhonemeText()[0]
        assert "b" == b.getPhonemeText()[0]
        assert "c" == cd.getPhonemeText()[0]
        assert "d" == cd.getPhonemeText()[1]
        assert "e" == ef.getPhonemeText()[0]
        assert "f" == ef.getPhonemeText()[1]
        assert "g" == ghi.getPhonemeText()[0]
        assert "h" == ghi.getPhonemeText()[1]
        assert "i" == ghi.getPhonemeText()[2]
        assert "j" == jkl.getPhonemeText()[0]
        assert "k" == jkl.getPhonemeText()[1]
        assert "l" == jkl.getPhonemeText()[2]

        print("a: " + a.getPhonemeText())
        print("b: " + b.getPhonemeText())

        a_b = Phoneme.Phoneme0(a, b)
        assert "a" == a_b.getPhonemeText()[0]
        assert "b" == a_b.getPhonemeText()[1]
        assert "ab" == a_b.getPhonemeText()[0:2]
        assert "a" == a_b.getPhonemeText()[0:1]
        assert "b" == a_b.getPhonemeText()[1:2]

        cd_ef = Phoneme.Phoneme0(cd, ef)
        assert "c" == cd_ef.getPhonemeText()[0]
        assert "d" == cd_ef.getPhonemeText()[1]
        assert "e" == cd_ef.getPhonemeText()[2]
        assert "f" == cd_ef.getPhonemeText()[3]
        assert "c" == cd_ef.getPhonemeText()[0:1]
        assert "d" == cd_ef.getPhonemeText()[1:2]
        assert "e" == cd_ef.getPhonemeText()[2:3]
        assert "f" == cd_ef.getPhonemeText()[3:4]
        assert "cd" == cd_ef.getPhonemeText()[0:2]
        assert "de" == cd_ef.getPhonemeText()[1:3]
        assert "ef" == cd_ef.getPhonemeText()[2:4]
        assert "cde" == cd_ef.getPhonemeText()[0:3]
        assert "def" == cd_ef.getPhonemeText()[1:4]
        assert "cdef" == cd_ef.getPhonemeText()[0:4]

        a_b_cd = Phoneme.Phoneme0(Phoneme.Phoneme0(a, b), cd)
        assert "a" == a_b_cd.getPhonemeText()[0]
        assert "b" == a_b_cd.getPhonemeText()[1]
        assert "c" == a_b_cd.getPhonemeText()[2]
        assert "d" == a_b_cd.getPhonemeText()[3]
        assert "a" == a_b_cd.getPhonemeText()[0:1]
        assert "b" == a_b_cd.getPhonemeText()[1:2]
        assert "c" == a_b_cd.getPhonemeText()[2:3]
        assert "d" == a_b_cd.getPhonemeText()[3:4]
        assert "ab" == a_b_cd.getPhonemeText()[0:2]
        assert "bc" == a_b_cd.getPhonemeText()[1:3]
        assert "cd" == a_b_cd.getPhonemeText()[2:4]
        assert "abc" == a_b_cd.getPhonemeText()[0:3]
        assert "bcd" == a_b_cd.getPhonemeText()[1:4]
        assert "abcd" == a_b_cd.getPhonemeText()[0:4]

    def testPhonemeComparedToSelfIsZero(self) -> None:

        for phs in self.__makePhonemes():
            for ph in phs:
                assert Rule.Phoneme.COMPARATOR.compare(ph, ph) == 0, (
                    "Phoneme compared to itself should be zero: " + ph.getPhonemeText()
                )

    def __makePhonemes(self) -> typing.List[typing.List[Phoneme]]:

        words = [
            ["rinD", "rinDlt", "rina", "rinalt", "rino", "rinolt", "rinu", "rinult"],
            ["dortlaj", "dortlej", "ortlaj", "ortlej", "ortlej-dortlaj"],
        ]
        phonemes = [None] * len(words)

        for i in range(len(words)):
            words_i = words[i]
            phonemes_i = [None] * len(words_i)
            for j in range(len(words_i)):
                phonemes_i[j] = Phoneme(2, words_i[j], Languages.NO_LANGUAGES, None)
            phonemes[i] = phonemes_i

        return phonemes
