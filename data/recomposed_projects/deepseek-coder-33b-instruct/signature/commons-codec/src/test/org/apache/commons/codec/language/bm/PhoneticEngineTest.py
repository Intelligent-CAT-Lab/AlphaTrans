from __future__ import annotations
import re
import unittest
import pytest
import io
import typing
from typing import *
import unittest
from src.main.org.apache.commons.codec.language.bm.NameType import *
from src.main.org.apache.commons.codec.language.bm.PhoneticEngine import *
from src.main.org.apache.commons.codec.language.bm.RuleType import *


class PhoneticEngineTest(unittest.TestCase):

    __maxPhonemes: int = 0

    __ruleType: RuleType = None

    __phoneticExpected: str = ""

    __nameType: NameType = None

    __name: str = ""

    __concat: bool = False

    __TEN: int = 10

    def testEncode(self) -> None:

        engine = PhoneticEngine(
            self.__nameType, self.__ruleType, self.__concat, self.__maxPhonemes
        )

        phoneticActual = engine.encode0(self.__name)

        self.assertEqual(self.__phoneticExpected, phoneticActual, "phoneme incorrect")

        if self.__concat:
            split = phoneticActual.split("|")
            self.assertTrue(len(split) <= self.__maxPhonemes)
        else:
            words = phoneticActual.split("-")
            for word in words:
                split = word.split("|")
                self.assertTrue(len(split) <= self.__maxPhonemes)

    @staticmethod
    def data() -> typing.List[typing.List[typing.Any]]:
        return [
            [
                "Renault",
                "rinD|rinDlt|rina|rinalt|rino|rinolt|rinu|rinult",
                NameType.GENERIC,
                RuleType.APPROX,
                True,
                PhoneticEngineTest.__TEN,
            ],
            [
                "Renault",
                "rYnDlt|rYnalt|rYnult|rinDlt|rinalt|rinolt|rinult",
                NameType.ASHKENAZI,
                RuleType.APPROX,
                True,
                PhoneticEngineTest.__TEN,
            ],
            ["Renault", "rinDlt", NameType.ASHKENAZI, RuleType.APPROX, True, 1],
            [
                "Renault",
                "rinDlt",
                NameType.SEPHARDIC,
                RuleType.APPROX,
                True,
                PhoneticEngineTest.__TEN,
            ],
            [
                "SntJohn-Smith",
                "sntjonsmit",
                NameType.GENERIC,
                RuleType.EXACT,
                True,
                PhoneticEngineTest.__TEN,
            ],
            [
                "d'ortley",
                "(ortlaj|ortlej)-(dortlaj|dortlej)",
                NameType.GENERIC,
                RuleType.EXACT,
                True,
                PhoneticEngineTest.__TEN,
            ],
            [
                "van helsing",
                "(elSink|elsink|helSink|helsink|helzink|xelsink)-(banhelsink|fanhelsink|fanhelzink|vanhelsink|vanhelzink|vanjelsink)",
                NameType.GENERIC,
                RuleType.EXACT,
                False,
                PhoneticEngineTest.__TEN,
            ],
            [
                "Judenburg",
                "iudnbYrk|iudnbirk|iudnburk|xudnbirk|xudnburk|zudnbirk|zudnburk",
                NameType.GENERIC,
                RuleType.APPROX,
                True,
                PhoneticEngineTest.__TEN,
            ],
        ]

    def __init__(
        self,
        name: str,
        phoneticExpected: str,
        nameType: NameType,
        ruleType: RuleType,
        concat: bool,
        maxPhonemes: int,
    ) -> None:

        self.__name = name
        self.__phoneticExpected = phoneticExpected
        self.__nameType = nameType
        self.__ruleType = ruleType
        self.__concat = concat
        self.__maxPhonemes = maxPhonemes
