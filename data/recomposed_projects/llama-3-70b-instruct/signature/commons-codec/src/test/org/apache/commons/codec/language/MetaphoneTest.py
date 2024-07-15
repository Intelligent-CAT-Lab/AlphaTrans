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
        self._stringEncoder.setMaxCodeLen(6)
        self.assertEqual("AKSKSK", self._stringEncoder.metaphone("AXEAXEAXE"))

    def testExceedLength(self) -> None:
        self.assertEqual("AKSK", self._stringEncoder.metaphone("AXEAXE"))

    def testTCH(self) -> None:
        self.assertEqual("RX", self._stringEncoder.metaphone("RETCH"))
        self.assertEqual("WX", self._stringEncoder.metaphone("WATCH"))

    def testTIOAndTIAToX(self) -> None:
        self.assertEqual("OX", self._stringEncoder.metaphone("OTIA"))
        self.assertEqual("PRXN", self._stringEncoder.metaphone("PORTION"))

    def testSHAndSIOAndSIAToX(self) -> None:
        self.assertEqual("XT", self._stringEncoder.metaphone("SHOT"))
        self.assertEqual("OTXN", self._stringEncoder.metaphone("ODSIAN"))
        self.assertEqual("PLXN", self._stringEncoder.metaphone("PULSION"))

    def testPHTOF(self) -> None:
        self.assertEqual("FX", self._stringEncoder.metaphone("PHISH"))

    def testDiscardOfSilentGN(self) -> None:
        self.assertEqual("N", self.getStringEncoder().metaphone("GNU"))
        self.assertEqual("SNT", self.getStringEncoder().metaphone("SIGNED"))

    def testDiscardOfSilentHAfterG(self) -> None:
        self.assertEqual("KNT", self.getStringEncoder().metaphone("GHENT"))
        self.assertEqual("B", self.getStringEncoder().metaphone("BAUGH"))

    def testTranslateToJOfDGEOrDGIOrDGY(self) -> None:
        self.assertEqual("TJ", self.getStringEncoder().metaphone("DODGY"))
        self.assertEqual("TJ", self.getStringEncoder().metaphone("DODGE"))
        self.assertEqual("AJMT", self.getStringEncoder().metaphone("ADGIEMTI"))

    def testTranslateOfSCHAndCH(self) -> None:
        self.assertEqual("SKTL", self._stringEncoder.metaphone("SCHEDULE"))
        self.assertEqual("SKMT", self._stringEncoder.metaphone("SCHEMATIC"))

        self.assertEqual("KRKT", self._stringEncoder.metaphone("CHARACTER"))
        self.assertEqual("TX", self._stringEncoder.metaphone("TEACH"))

    def testWordsWithCIA(self) -> None:
        self.assertEqual("XP", self._stringEncoder.metaphone("CIAPO"))

    def testWhy(self) -> None:
        self.assertEqual("", self.getStringEncoder().metaphone("WHY"))

    def testDiscardOfSCEOrSCIOrSCY(self) -> None:
        self.assertEqual("SNS", self.getStringEncoder().metaphone("SCIENCE"))
        self.assertEqual("SN", self.getStringEncoder().metaphone("SCENE"))
        self.assertEqual("S", self.getStringEncoder().metaphone("SCY"))

    def testWordEndingInMB(self) -> None:
        self.assertEqual("KM", self._stringEncoder.metaphone("COMB"))
        self.assertEqual("TM", self._stringEncoder.metaphone("TOMB"))
        self.assertEqual("WM", self._stringEncoder.metaphone("WOMB"))

    def testMetaphone(self) -> None:
        self.assertEqual("HL", self._stringEncoder.metaphone("howl"))
        self.assertEqual("TSTN", self._stringEncoder.metaphone("testing"))
        self.assertEqual("0", self._stringEncoder.metaphone("The"))
        self.assertEqual("KK", self._stringEncoder.metaphone("quick"))
        self.assertEqual("BRN", self._stringEncoder.metaphone("brown"))
        self.assertEqual("FKS", self._stringEncoder.metaphone("fox"))
        self.assertEqual("JMPT", self._stringEncoder.metaphone("jumped"))
        self.assertEqual("OFR", self._stringEncoder.metaphone("over"))
        self.assertEqual("0", self._stringEncoder.metaphone("the"))
        self.assertEqual("LS", self._stringEncoder.metaphone("lazy"))
        self.assertEqual("TKS", self._stringEncoder.metaphone("dogs"))

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
        self.validateFixture(pairs)
        for pair in pairs:
            name0 = pair[0]
            name1 = pair[1]
            failMsg = "Expected match between " + name0 + " and " + name1
            self.assertTrue(
                failMsg, self.getStringEncoder().isMetaphoneEqual(name0, name1)
            )
            self.assertTrue(
                failMsg, self.getStringEncoder().isMetaphoneEqual(name1, name0)
            )

    def assertIsMetaphoneEqual(self, source: str, matches: typing.List[str]) -> None:

        pass  # LLM could not translate this method
