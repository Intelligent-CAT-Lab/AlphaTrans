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

        a = Phoneme(2, "a", None, None)
        b = Phoneme(2, "b", None, None)
        cd = Phoneme(2, "cd", None, None)
        ef = Phoneme(2, "ef", None, None)
        ghi = Phoneme(2, "ghi", None, None)
        jkl = Phoneme(2, "jkl", None, None)

        self.assertEqual("a", a.getPhonemeText()[0])
        self.assertEqual("b", b.getPhonemeText()[0])
        self.assertEqual("c", cd.getPhonemeText()[0])
        self.assertEqual("d", cd.getPhonemeText()[1])
        self.assertEqual("e", ef.getPhonemeText()[0])
        self.assertEqual("f", ef.getPhonemeText()[1])
        self.assertEqual("g", ghi.getPhonemeText()[0])
        self.assertEqual("h", ghi.getPhonemeText()[1])
        self.assertEqual("i", ghi.getPhonemeText()[2])
        self.assertEqual("j", jkl.getPhonemeText()[0])
        self.assertEqual("k", jkl.getPhonemeText()[1])
        self.assertEqual("l", jkl.getPhonemeText()[2])

        print("a: " + a.getPhonemeText())
        print("b: " + b.getPhonemeText())

        a_b = Phoneme.Phoneme0(a, b)
        self.assertEqual("a", a_b.getPhonemeText()[0])
        self.assertEqual("b", a_b.getPhonemeText()[1])
        self.assertEqual("ab", a_b.getPhonemeText()[0:2])
        self.assertEqual("a", a_b.getPhonemeText()[0:1])
        self.assertEqual("b", a_b.getPhonemeText()[1:2])

        cd_ef = Phoneme.Phoneme0(cd, ef)
        self.assertEqual("c", cd_ef.getPhonemeText()[0])
        self.assertEqual("d", cd_ef.getPhonemeText()[1])
        self.assertEqual("e", cd_ef.getPhonemeText()[2])
        self.assertEqual("f", cd_ef.getPhonemeText()[3])
        self.assertEqual("c", cd_ef.getPhonemeText()[0:1])
        self.assertEqual("d", cd_ef.getPhonemeText()[1:2])
        self.assertEqual("e", cd_ef.getPhonemeText()[2:3])
        self.assertEqual("f", cd_ef.getPhonemeText()[3:4])
        self.assertEqual("cd", cd_ef.getPhonemeText()[0:2])
        self.assertEqual("de", cd_ef.getPhonemeText()[1:3])
        self.assertEqual("ef", cd_ef.getPhonemeText()[2:4])
        self.assertEqual("cde", cd_ef.getPhonemeText()[0:3])
        self.assertEqual("def", cd_ef.getPhonemeText()[1:4])
        self.assertEqual("cdef", cd_ef.getPhonemeText()[0:4])

        a_b_cd = Phoneme.Phoneme0(Phoneme.Phoneme0(a, b), cd)
        self.assertEqual("a", a_b_cd.getPhonemeText()[0])
        self.assertEqual("b", a_b_cd.getPhonemeText()[1])
        self.assertEqual("c", a_b_cd.getPhonemeText()[2])
        self.assertEqual("d", a_b_cd.getPhonemeText()[3])
        self.assertEqual("a", a_b_cd.getPhonemeText()[0:1])
        self.assertEqual("b", a_b_cd.getPhonemeText()[1:2])
        self.assertEqual("c", a_b_cd.getPhonemeText()[2:3])
        self.assertEqual("d", a_b_cd.getPhonemeText()[3:4])
        self.assertEqual("ab", a_b_cd.getPhonemeText()[0:2])
        self.assertEqual("bc", a_b_cd.getPhonemeText()[1:3])
        self.assertEqual("cd", a_b_cd.getPhonemeText()[2:4])
        self.assertEqual("abc", a_b_cd.getPhonemeText()[0:3])
        self.assertEqual("bcd", a_b_cd.getPhonemeText()[1:4])
        self.assertEqual("abcd", a_b_cd.getPhonemeText()[0:4])

    def testPhonemeComparedToSelfIsZero(self) -> None:

        for phs in self.__makePhonemes():
            for ph in phs:
                self.assertEqual(
                    0,
                    Phoneme.COMPARATOR(ph, ph),
                    "Phoneme compared to itself should be zero: " + ph.getPhonemeText(),
                )

    def __makePhonemes(self) -> typing.List[typing.List[Phoneme]]:

        words = [
            ["rinD", "rinDlt", "rina", "rinalt", "rino", "rinolt", "rinu", "rinult"],
            ["dortlaj", "dortlej", "ortlaj", "ortlej", "ortlej-dortlaj"],
        ]

        phonemes = []

        for i in range(len(words)):
            words_i = words[i]
            phonemes_i = []
            for j in range(len(words_i)):
                phonemes_i.append(Phoneme(2, words_i[j], Languages.NO_LANGUAGES, None))
            phonemes.append(phonemes_i)

        return phonemes
