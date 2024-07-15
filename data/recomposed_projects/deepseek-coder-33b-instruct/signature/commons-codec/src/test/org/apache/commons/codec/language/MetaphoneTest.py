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

        # Create an instance of Metaphone
        metaphone = Metaphone()

        # Call the metaphone method with the string "AXEAXE"
        result = metaphone.metaphone("AXEAXE")

        # Assert that the result is "AKSK"
        self.assertEqual("AKSK", result)

    def testTCH(self) -> None:

        # Create an instance of Metaphone
        metaphone = Metaphone()

        # Assert that the metaphone method returns the expected result
        self.assertEqual("RX", metaphone.metaphone("RETCH"))
        self.assertEqual("WX", metaphone.metaphone("WATCH"))

    def testTIOAndTIAToX(self) -> None:

        # Create an instance of Metaphone
        metaphone = Metaphone()

        # Test the metaphone method
        self.assertEqual("OX", metaphone.metaphone("OTIA"))
        self.assertEqual("PRXN", metaphone.metaphone("PORTION"))

    def testSHAndSIOAndSIAToX(self) -> None:

        # Create an instance of the Metaphone class
        metaphone = Metaphone()

        # Assert that the metaphone method returns the expected result
        self.assertEqual("XT", metaphone.metaphone("SHOT"))
        self.assertEqual("OTXN", metaphone.metaphone("ODSIAN"))
        self.assertEqual("PLXN", metaphone.metaphone("PULSION"))

    def testPHTOF(self) -> None:

        # Create an instance of Metaphone
        metaphone = Metaphone()

        # Assert that the metaphone of "PHISH" is "FX"
        self.assertEqual("FX", metaphone.metaphone("PHISH"))

    def testDiscardOfSilentGN(self) -> None:

        self.assertEqual("N", self._stringEncoder.metaphone("GNU"))

        self.assertEqual("SNT", self._stringEncoder.metaphone("SIGNED"))

    def testDiscardOfSilentHAfterG(self) -> None:

        # Create an instance of Metaphone
        metaphone = Metaphone()

        # Test the metaphone method
        self.assertEqual("KNT", metaphone.metaphone("GHENT"))
        self.assertEqual("B", metaphone.metaphone("BAUGH"))

    def testTranslateToJOfDGEOrDGIOrDGY(self) -> None:

        self.assertEqual("TJ", self._stringEncoder.metaphone("DODGY"))
        self.assertEqual("TJ", self._stringEncoder.metaphone("DODGE"))
        self.assertEqual("AJMT", self._stringEncoder.metaphone("ADGIEMTI"))

    def testTranslateOfSCHAndCH(self) -> None:

        self.assertEqual("SKTL", self._stringEncoder.metaphone("SCHEDULE"))
        self.assertEqual("SKMT", self._stringEncoder.metaphone("SCHEMATIC"))

        self.assertEqual("KRKT", self._stringEncoder.metaphone("CHARACTER"))
        self.assertEqual("TX", self._stringEncoder.metaphone("TEACH"))

    def testWordsWithCIA(self) -> None:

        # Create an instance of the Metaphone class
        metaphone = Metaphone()

        # Call the metaphone method with the input "CIAPO"
        result = metaphone.metaphone("CIAPO")

        # Assert that the result is "XP"
        self.assertEqual(result, "XP")

    def testWhy(self) -> None:

        self.assertEqual("", self._stringEncoder.metaphone("WHY"))

    def testDiscardOfSCEOrSCIOrSCY(self) -> None:

        self.assertEqual("SNS", self._stringEncoder.metaphone("SCIENCE"))
        self.assertEqual("SN", self._stringEncoder.metaphone("SCENE"))
        self.assertEqual("S", self._stringEncoder.metaphone("SCY"))

    def testWordEndingInMB(self) -> None:

        # Create an instance of the Metaphone class
        metaphone = Metaphone()

        # Assert that the metaphone method returns the expected result
        self.assertEqual("KM", metaphone.metaphone("COMB"))
        self.assertEqual("TM", metaphone.metaphone("TOMB"))
        self.assertEqual("WM", metaphone.metaphone("WOMB"))

    def testMetaphone(self) -> None:

        # Create an instance of the Metaphone class
        metaphone = Metaphone()

        # Assert that the metaphone method returns the expected output
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

        # Create an instance of Metaphone
        metaphone = Metaphone()

        # Define the source string
        source = "Wright"

        # Define the expected matches
        matches = ["Rota", "Rudd", "Ryde"]

        # Iterate over the matches
        for match in matches:
            # Assert that the Metaphone encoding of the source string is equal to the expected match
            self.assertEqual(metaphone.encode(source), metaphone.encode(match))

    def testIsMetaphoneEqualSusan(self) -> None:

        source = "Susan"
        matches = [
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
        ]

        self.assertIsMetaphoneEqual(source, matches)

    def testIsMetaphoneEqualRay(self) -> None:

        # Create an instance of Metaphone
        metaphone = Metaphone()

        # Define the source string and the list of matches
        source = "Ray"
        matches = ["Ray", "Rey", "Roi", "Roy", "Ruy"]

        # Iterate over the matches
        for match in matches:
            # Assert that the Metaphone encoding of the source and the match are equal
            self.assertEqual(metaphone.encode(source), metaphone.encode(match))

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

        source = "John"
        matches = [
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
        ]

        self.assertIsMetaphoneEqual(source, matches)

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

        # Create an instance of Metaphone
        metaphone = Metaphone()

        # Define the source string and the list of matches
        source = "Albert"
        matches = ["Ailbert", "Alberik", "Albert", "Alberto", "Albrecht"]

        # Assert that the Metaphone encoding of the source string is equal to the Metaphone encoding of each match
        for match in matches:
            self.assertEqual(metaphone.encode(source), metaphone.encode(match))

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

        # Create an instance of Metaphone
        metaphone = Metaphone()

        # Define the source string and expected matches
        source = "Aero"
        matches = ["Eure"]

        # Encode the source string using Metaphone
        encoded_source = metaphone.encode(source)

        # Check if the encoded source string matches any of the expected matches
        self.assertIn(encoded_source, matches)

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

        for matche in matches:
            self.assertTrue(
                self._stringEncoder.isMetaphoneEqual(source, matche),
                "Source: " + source + ", should have same Metaphone as: " + matche,
            )

        for matche in matches:
            for matche2 in matches:
                self.assertTrue(self._stringEncoder.isMetaphoneEqual(matche, matche2))
