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

        # Create an instance of Metaphone
        metaphone = Metaphone()

        # Set the max code length
        metaphone.setMaxCodeLen(6)

        # Test the metaphone method
        self.assertEqual("AKSKSK", metaphone.metaphone("AXEAXEAXE"))

    def testExceedLength(self) -> None:

        # Create an instance of Metaphone
        metaphone = Metaphone()

        # Call the metaphone method and compare the result
        self.assertEqual("AKSK", metaphone.metaphone("AXEAXE"))

    def testTCH(self) -> None:

        # Create an instance of Metaphone
        metaphone = Metaphone()

        # Assert that the metaphone of "RETCH" is "RX"
        self.assertEqual("RX", metaphone.metaphone("RETCH"))

        # Assert that the metaphone of "WATCH" is "WX"
        self.assertEqual("WX", metaphone.metaphone("WATCH"))

    def testTIOAndTIAToX(self) -> None:

        # Create an instance of Metaphone
        metaphone = Metaphone()

        # Assert that the metaphone of "OTIA" is "OX"
        self.assertEqual("OX", metaphone.metaphone("OTIA"))

        # Assert that the metaphone of "PORTION" is "PRXN"
        self.assertEqual("PRXN", metaphone.metaphone("PORTION"))

    def testSHAndSIOAndSIAToX(self) -> None:

        # Create an instance of Metaphone
        metaphone = Metaphone()

        # Assert that the metaphone of "SHOT" is "XT"
        self.assertEqual("XT", metaphone.metaphone("SHOT"))

        # Assert that the metaphone of "ODSIAN" is "OTXN"
        self.assertEqual("OTXN", metaphone.metaphone("ODSIAN"))

        # Assert that the metaphone of "PULSION" is "PLXN"
        self.assertEqual("PLXN", metaphone.metaphone("PULSION"))

    def testPHTOF(self) -> None:

        # Create an instance of Metaphone
        metaphone = Metaphone()

        # Call the metaphone method with "PHISH" as input
        result = metaphone.metaphone("PHISH")

        # Assert that the result is "FX"
        self.assertEqual("FX", result)

    def testDiscardOfSilentGN(self) -> None:

        # Create an instance of Metaphone
        metaphone = Metaphone()

        # Test the metaphone method
        self.assertEqual("N", metaphone.metaphone("GNU"))
        self.assertEqual("SNT", metaphone.metaphone("SIGNED"))

    def testDiscardOfSilentHAfterG(self) -> None:

        # Create an instance of Metaphone
        metaphone = Metaphone()

        # Test the metaphone method
        self.assertEqual("KNT", metaphone.metaphone("GHENT"))
        self.assertEqual("B", metaphone.metaphone("BAUGH"))

    def testTranslateToJOfDGEOrDGIOrDGY(self) -> None:

        # Create an instance of Metaphone
        metaphone = Metaphone()

        # Assert that the metaphone of "DODGY" is "TJ"
        self.assertEqual("TJ", metaphone.metaphone("DODGY"))

        # Assert that the metaphone of "DODGE" is "TJ"
        self.assertEqual("TJ", metaphone.metaphone("DODGE"))

        # Assert that the metaphone of "ADGIEMTI" is "AJMT"
        self.assertEqual("AJMT", metaphone.metaphone("ADGIEMTI"))

    def testTranslateOfSCHAndCH(self) -> None:

        # Create an instance of Metaphone
        metaphone = Metaphone()

        # Assert the expected output of the metaphone method
        self.assertEqual("SKTL", metaphone.metaphone("SCHEDULE"))
        self.assertEqual("SKMT", metaphone.metaphone("SCHEMATIC"))

        self.assertEqual("KRKT", metaphone.metaphone("CHARACTER"))
        self.assertEqual("TX", metaphone.metaphone("TEACH"))

    def testWordsWithCIA(self) -> None:

        # Create an instance of Metaphone
        metaphone = Metaphone()

        # Call the metaphone method with "CIAPO" as argument
        result = metaphone.metaphone("CIAPO")

        # Assert that the result is "XP"
        self.assertEqual("XP", result)

    def testWhy(self) -> None:

        # Create an instance of Metaphone
        metaphone = Metaphone()

        # Call the metaphone method and compare the result with an empty string
        self.assertEqual("", metaphone.metaphone("WHY"))

    def testDiscardOfSCEOrSCIOrSCY(self) -> None:

        # Create an instance of Metaphone
        metaphone = Metaphone()

        # Test the metaphone method
        self.assertEqual("SNS", metaphone.metaphone("SCIENCE"))
        self.assertEqual("SN", metaphone.metaphone("SCENE"))
        self.assertEqual("S", metaphone.metaphone("SCY"))

    def testWordEndingInMB(self) -> None:

        # Create an instance of Metaphone
        metaphone = Metaphone()

        # Assert that the metaphone of "COMB" is "KM"
        self.assertEqual("KM", metaphone.metaphone("COMB"))

        # Assert that the metaphone of "TOMB" is "TM"
        self.assertEqual("TM", metaphone.metaphone("TOMB"))

        # Assert that the metaphone of "WOMB" is "WM"
        self.assertEqual("WM", metaphone.metaphone("WOMB"))

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

        self.assertMetaphoneEqual([["Lawrence", "Lorenza"], ["Gary", "Cahra"]])

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

        metaphone = Metaphone()

        for pair in pairs:
            name0 = pair[0]
            name1 = pair[1]
            failMsg = "Expected match between " + name0 + " and " + name1
            self.assertTrue(failMsg, metaphone.isMetaphoneEqual(name0, name1))
            self.assertTrue(failMsg, metaphone.isMetaphoneEqual(name1, name0))

    def assertIsMetaphoneEqual(self, source: str, matches: typing.List[str]) -> None:

        metaphone = Metaphone()

        for match in matches:
            assert metaphone.isMetaphoneEqual(
                source, match
            ), f"Source: {source}, should have same Metaphone as: {match}"

        for match in matches:
            for match2 in matches:
                assert metaphone.isMetaphoneEqual(match, match2)
