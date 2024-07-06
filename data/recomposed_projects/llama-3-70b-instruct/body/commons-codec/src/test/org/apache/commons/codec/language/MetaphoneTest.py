from __future__ import annotations
import re
import os
import unittest
import pytest
import io
import typing
from typing import *
import unittest
from src.main.org.apache.commons.codec.StringEncoder import *
from src.test.org.apache.commons.codec.StringEncoderAbstractTest import *
from src.main.org.apache.commons.codec.language.Metaphone import *


class MetaphoneTest(StringEncoderAbstractTest, unittest.TestCase):

    def testSetMaxLengthWithTruncation(self) -> None:

        pass  # LLM could not translate this method

    def testExceedLength(self) -> None:
        self.assertEqual("AKSK", self._stringEncoder.metaphone("AXEAXE"))

    def testTCH(self) -> None:

        pass  # LLM could not translate this method

    def testTIOAndTIAToX(self) -> None:

        pass  # LLM could not translate this method

    def testSHAndSIOAndSIAToX(self) -> None:

        pass  # LLM could not translate this method

    def testPHTOF(self) -> None:
        self.assertEqual("FX", self._stringEncoder.metaphone("PHISH"))

    def testDiscardOfSilentGN(self) -> None:

        pass  # LLM could not translate this method

    def testDiscardOfSilentHAfterG(self) -> None:

        pass  # LLM could not translate this method

    def testTranslateToJOfDGEOrDGIOrDGY(self) -> None:

        pass  # LLM could not translate this method

    def testTranslateOfSCHAndCH(self) -> None:

        pass  # LLM could not translate this method

    def testWordsWithCIA(self) -> None:
        self.assertEqual("XP", self.getStringEncoder().metaphone("CIAPO"))

    def testWhy(self) -> None:
        self.assertEqual("", self.getStringEncoder().metaphone("WHY"))

    def testDiscardOfSCEOrSCIOrSCY(self) -> None:

        pass  # LLM could not translate this method

    def testWordEndingInMB(self) -> None:

        pass  # LLM could not translate this method

    def testMetaphone(self) -> None:

        pass  # LLM could not translate this method

    def testIsMetaphoneEqualXalan(self) -> None:
        self.assertIsMetaphoneEqual(
            "Xalan",
            [
                "Celene",
                "Celina",
                "Celine",
                "Selena",
                "Selene",
                "Selina",
                "Seline",
                "Suellen",
                "Xylina",
            ],
        )

    def testIsMetaphoneEqualWright(self) -> None:
        self.assertIsMetaphoneEqual("Wright", ["Rota", "Rudd", "Ryde"])

    def testIsMetaphoneEqualSusan(self) -> None:
        self.assertIsMetaphoneEqual(
            "Susan",
            [
                "Siusan",
                "Sosanna",
                "Susan",
                "Susana",
                "Susann",
                "Susanna",
                "Susannah",
                "Susanne",
                "Suzann",
                "Suzanna",
                "Suzanne",
                "Zuzana",
            ],
        )

    def testIsMetaphoneEqualRay(self) -> None:
        self.assertIsMetaphoneEqual("Ray", ["Ray", "Rey", "Roi", "Roy", "Ruy"])

    def testIsMetaphoneEqualPeter(self) -> None:
        self.assertIsMetaphoneEqual(
            "Peter",
            [
                "Peadar",
                "Peder",
                "Pedro",
                "Peter",
                "Petr",
                "Peyter",
                "Pieter",
                "Pietro",
                "Piotr",
            ],
        )

    def testIsMetaphoneEqualParis(self) -> None:
        self.assertIsMetaphoneEqual(
            "Paris", ["Pearcy", "Perris", "Piercy", "Pierz", "Pryse"]
        )

    def testIsMetaphoneEqualMary(self) -> None:
        self.assertIsMetaphoneEqual(
            "Mary",
            [
                "Mair",
                "Maire",
                "Mara",
                "Mareah",
                "Mari",
                "Maria",
                "Marie",
                "Mary",
                "Maura",
                "Maure",
                "Meara",
                "Merrie",
                "Merry",
                "Mira",
                "Moira",
                "Mora",
                "Moria",
                "Moyra",
                "Muire",
                "Myra",
                "Myrah",
            ],
        )

    def testIsMetaphoneEqualKnight(self) -> None:
        self.assertIsMetaphoneEqual(
            "Knight",
            [
                "Hynda",
                "Nada",
                "Nadia",
                "Nady",
                "Nat",
                "Nata",
                "Natty",
                "Neda",
                "Nedda",
                "Nedi",
                "Netta",
                "Netti",
                "Nettie",
                "Netty",
                "Nita",
                "Nydia",
            ],
        )

    def testIsMetaphoneEqualJohn(self) -> None:
        self.assertIsMetaphoneEqual(
            "John",
            [
                "Gena",
                "Gene",
                "Genia",
                "Genna",
                "Genni",
                "Gennie",
                "Genny",
                "Giana",
                "Gianna",
                "Gina",
                "Ginni",
                "Ginnie",
                "Ginny",
                "Jaine",
                "Jan",
                "Jana",
                "Jane",
                "Janey",
                "Jania",
                "Janie",
                "Janna",
                "Jany",
                "Jayne",
                "Jean",
                "Jeana",
                "Jeane",
                "Jeanie",
                "Jeanna",
                "Jeanne",
                "Jeannie",
                "Jen",
                "Jena",
                "Jeni",
                "Jenn",
                "Jenna",
                "Jennee",
                "Jenni",
                "Jennie",
                "Jenny",
                "Jinny",
                "Jo Ann",
                "Jo-Ann",
                "Jo-Anne",
                "Joan",
                "Joana",
                "Joane",
                "Joanie",
                "Joann",
                "Joanna",
                "Joanne",
                "Joeann",
                "Johna",
                "Johnna",
                "Joni",
                "Jonie",
                "Juana",
                "June",
                "Junia",
                "Junie",
            ],
        )

    def testIsMetaphoneEqualGary(self) -> None:
        self.assertIsMetaphoneEqual(
            "Gary",
            [
                "Cahra",
                "Cara",
                "Carey",
                "Cari",
                "Caria",
                "Carie",
                "Caro",
                "Carree",
                "Carri",
                "Carrie",
                "Carry",
                "Cary",
                "Cora",
                "Corey",
                "Cori",
                "Corie",
                "Correy",
                "Corri",
                "Corrie",
                "Corry",
                "Cory",
                "Gray",
                "Kara",
                "Kare",
                "Karee",
                "Kari",
                "Karia",
                "Karie",
                "Karrah",
                "Karrie",
                "Karry",
                "Kary",
                "Keri",
                "Kerri",
                "Kerrie",
                "Kerry",
                "Kira",
                "Kiri",
                "Kora",
                "Kore",
                "Kori",
                "Korie",
                "Korrie",
                "Korry",
            ],
        )

    def testIsMetaphoneEqualAlbert(self) -> None:
        self.assertIsMetaphoneEqual(
            "Albert", ["Ailbert", "Alberik", "Albert", "Alberto", "Albrecht"]
        )

    def testIsMetaphoneEqualWhite(self) -> None:
        self.assertIsMetaphoneEqual(
            "White",
            [
                "Wade",
                "Wait",
                "Waite",
                "Wat",
                "Whit",
                "Wiatt",
                "Wit",
                "Wittie",
                "Witty",
                "Wood",
                "Woodie",
                "Woody",
            ],
        )

    def testIsMetaphoneEqualAero(self) -> None:
        self.assertIsMetaphoneEqual("Aero", ["Eure"])

    def testIsMetaphoneEqual2(self) -> None:
        self.assertMetaphoneEqual(
            [
                ["Lawrence", "Lorenza"],
                ["Gary", "Cahra"],
            ]
        )

    def testIsMetaphoneEqual1(self) -> None:
        self.assertMetaphoneEqual(
            [["Case", "case"], ["CASE", "Case"], ["caSe", "cAsE"], ["quick", "cookie"]]
        )

    def _createStringEncoder(self) -> Metaphone:
        return Metaphone()

    def validateFixture(self, pairs: typing.List[typing.List[str]]) -> None:
        if len(pairs) == 0:
            self.fail("Test fixture is empty")
        for i in range(len(pairs)):
            if len(pairs[i]) != 2:
                self.fail("Error in test fixture in the data array at index " + str(i))

    def assertMetaphoneEqual(self, pairs: typing.List[typing.List[str]]) -> None:

        pass  # LLM could not translate this method

    def assertIsMetaphoneEqual(self, source: str, matches: typing.List[str]) -> None:

        pass  # LLM could not translate this method
