from __future__ import annotations
import re
import unittest
import pytest
import io
import typing
from typing import *
from src.main.org.apache.commons.codec.StringEncoder import *
from src.test.org.apache.commons.codec.StringEncoderAbstractTest import *
from src.main.org.apache.commons.codec.language.Metaphone import *


class MetaphoneTest(StringEncoderAbstractTest, unittest.TestCase):

    def testSetMaxLengthWithTruncation(self) -> None:

        self.getStringEncoder().setMaxCodeLen(6)
        assert "AKSKSK" == self.getStringEncoder().metaphone("AXEAXEAXE")

    def testExceedLength(self) -> None:

        # Create an instance of Metaphone
        metaphone = Metaphone()

        # Call the metaphone method and compare the result
        self.assertEqual("AKSK", metaphone.metaphone("AXEAXE"))

    def testTCH(self) -> None:

        # Create an instance of Metaphone
        metaphone = Metaphone()

        # Assert that the metaphone of "RETCH" is "RX"
        assert metaphone.metaphone("RETCH") == "RX"

        # Assert that the metaphone of "WATCH" is "WX"
        assert metaphone.metaphone("WATCH") == "WX"

    def testTIOAndTIAToX(self) -> None:

        # Create an instance of Metaphone
        metaphone = Metaphone()

        # Assert that the metaphone of "OTIA" is "OX"
        assert metaphone.metaphone("OTIA") == "OX"

        # Assert that the metaphone of "PORTION" is "PRXN"
        assert metaphone.metaphone("PORTION") == "PRXN"

    def testSHAndSIOAndSIAToX(self) -> None:

        metaphone = Metaphone()

        self.assertEqual("XT", metaphone.metaphone("SHOT"))
        self.assertEqual("OTXN", metaphone.metaphone("ODSIAN"))
        self.assertEqual("PLXN", metaphone.metaphone("PULSION"))

    def testPHTOF(self) -> None:

        metaphone = Metaphone()
        assert metaphone.metaphone("PHISH") == "FX"

    def testDiscardOfSilentGN(self) -> None:

        # Create an instance of Metaphone
        metaphone = Metaphone()

        # Test the metaphone method
        assert metaphone.metaphone("GNU") == "N"
        assert metaphone.metaphone("SIGNED") == "SNT"

    def testDiscardOfSilentHAfterG(self) -> None:

        # Create an instance of Metaphone
        metaphone = Metaphone()

        # Test the metaphone method
        assert metaphone.metaphone("GHENT") == "KNT"
        assert metaphone.metaphone("BAUGH") == "B"

    def testTranslateToJOfDGEOrDGIOrDGY(self) -> None:

        # Create an instance of Metaphone
        metaphone = Metaphone()

        # Assert the expected output
        self.assertEqual("TJ", metaphone.metaphone("DODGY"))
        self.assertEqual("TJ", metaphone.metaphone("DODGE"))
        self.assertEqual("AJMT", metaphone.metaphone("ADGIEMTI"))

    def testTranslateOfSCHAndCH(self) -> None:

        metaphone = Metaphone()

        self.assertEqual("SKTL", metaphone.metaphone("SCHEDULE"))
        self.assertEqual("SKMT", metaphone.metaphone("SCHEMATIC"))

        self.assertEqual("KRKT", metaphone.metaphone("CHARACTER"))
        self.assertEqual("TX", metaphone.metaphone("TEACH"))

    def testWordsWithCIA(self) -> None:

        # Create an instance of Metaphone
        metaphone = Metaphone()

        # Call the metaphone method
        result = metaphone.metaphone("CIAPO")

        # Assert the result
        self.assertEqual("XP", result)

    def testWhy(self) -> None:

        metaphone = Metaphone()
        assert metaphone.metaphone("WHY") == ""

    def testDiscardOfSCEOrSCIOrSCY(self) -> None:

        metaphone = Metaphone()

        assert metaphone.metaphone("SCIENCE") == "SNS"
        assert metaphone.metaphone("SCENE") == "SN"
        assert metaphone.metaphone("SCY") == "S"

    def testWordEndingInMB(self) -> None:

        metaphone = Metaphone()

        assert metaphone.metaphone("COMB") == "KM"
        assert metaphone.metaphone("TOMB") == "TM"
        assert metaphone.metaphone("WOMB") == "WM"

    def testMetaphone(self) -> None:

        # Create an instance of Metaphone
        metaphone = Metaphone()

        # Assert the expected output
        self.assertEqual("HL", metaphone.metaphone("howl"))
        self.assertEqual("TSTN", metaphone.metaphone("testing"))
        self.assertEqual("0", metaphone.metaphone("The"))
        self.assertEqual("KK", metaphone.metaphone("quick"))
        self.assertEqual("BRN", metaphone.metaphone("brown"))
        self.assertEqual("FKS", metaphone.metaphone("fox"))
        self.assertEqual("JMPT", metaphone.metaphone("jumped"))
        self.assertEqual("OFR", metaphone.metaphone("over"))
        self.assertEqual("0", metaphone.metaphone("the"))
        self.assertEqual("LS", metaphone.metaphone("lazy"))
        self.assertEqual("TKS", metaphone.metaphone("dogs"))

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
            assert self.getStringEncoder().isMetaphoneEqual(name0, name1), failMsg
            assert self.getStringEncoder().isMetaphoneEqual(name1, name0), failMsg

    def assertIsMetaphoneEqual(self, source: str, matches: typing.List[str]) -> None:

        for matche in matches:
            assert self.getStringEncoder().isMetaphoneEqual(source, matche), (
                "Source: " + source + ", should have same Metaphone as: " + matche
            )

        for matche in matches:
            for matche2 in matches:
                assert self.getStringEncoder().isMetaphoneEqual(matche, matche2)
