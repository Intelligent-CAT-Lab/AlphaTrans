# Imports Begin
from src.main.org.apache.commons.codec.language.Metaphone import *
from src.main.org.apache.commons.codec.StringEncoderAbstractTest import *
from src.main.org.apache.commons.codec.StringEncoder import *
import unittest
import os
import typing
from typing import *
# Imports End

class MetaphoneTest(unittest.TestCase, StringEncoderAbstractTest<Metaphone>):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def testSetMaxLengthWithTruncation(self) -> None:

            self.getStringEncoder().setMaxCodeLen(6)
            self.assertEqual("AKSKSK", self.getStringEncoder().metaphone("AXEAXEAXE"))

    def testExceedLength(self) -> None:

            self.assertEqual("AKSK", self.getStringEncoder().metaphone("AXEAXE"))

    def testTCH(self) -> None:


        pass # LLM could not translate method body

    def testTIOAndTIAToX(self) -> None:


        pass # LLM could not translate method body

    def testSHAndSIOAndSIAToX(self) -> None:

            self.assertEqual("XT", self.getStringEncoder().metaphone("SHOT"))
            self.assertEqual("OTXN", self.getStringEncoder().metaphone("ODSIAN"))
            self.assertEqual("PLXN", self.getStringEncoder().metaphone("PULSION"))

    def testPHTOF(self) -> None:

            assert self.getStringEncoder().metaphone("PHISH") == "FX"

    def testDiscardOfSilentGN(self) -> None:

            self.assertEqual("N", self.getStringEncoder().metaphone("GNU"))
            self.assertEqual("SNT", self.getStringEncoder().metaphone("SIGNED"))

    def testDiscardOfSilentHAfterG(self) -> None:

            self.assertEqual("KNT", self.getStringEncoder().metaphone("GHENT"))
            self.assertEqual("B", self.getStringEncoder().metaphone("BAUGH"))

    def testTranslateToJOfDGEOrDGIOrDGY(self) -> None:


        pass # LLM could not translate method body

    def testTranslateOfSCHAndCH(self) -> None:

            self.assertEqual(self.getStringEncoder().metaphone("SCHEDULE"), "SKTL")
            self.assertEqual(self.getStringEncoder().metaphone("SCHEMATIC"), "SKMT")
            self.assertEqual(self.getStringEncoder().metaphone("CHARACTER"), "KRKT")
            self.assertEqual(self.getStringEncoder().metaphone("TEACH"), "TX")

    def testWordsWithCIA(self) -> None:

            assert self.getStringEncoder().metaphone("CIAPO") == "XP"

    def testWhy(self) -> None:

            self.assertEqual("", self.getStringEncoder().metaphone("WHY"))

    def testDiscardOfSCEOrSCIOrSCY(self) -> None:


        pass # LLM could not translate method body

    def testWordEndingInMB(self) -> None:

            self.assertEqual("KM", self.getStringEncoder().metaphone("COMB"))
            self.assertEqual("TM", self.getStringEncoder().metaphone("TOMB"))
            self.assertEqual("WM", self.getStringEncoder().metaphone("WOMB"))

    def testMetaphone(self) -> None:

            assert self.getStringEncoder().metaphone("howl") == "HL"
            assert self.getStringEncoder().metaphone("testing") == "TSTN"
            assert self.getStringEncoder().metaphone("The") == "0"
            assert self.getStringEncoder().metaphone("quick") == "KK"
            assert self.getStringEncoder().metaphone("brown") == "BRN"
            assert self.getStringEncoder().metaphone("fox") == "FKS"
            assert self.getStringEncoder().metaphone("jumped") == "JMPT"
            assert self.getStringEncoder().metaphone("over") == "OFR"
            assert self.getStringEncoder().metaphone("the") == "0"
            assert self.getStringEncoder().metaphone("lazy") == "LS"
            assert self.getStringEncoder().metaphone("dogs") == "TKS"

    def testIsMetaphoneEqualXalan(self) -> None:

            self.assertIsMetaphoneEqual("Xalan", ["Celene", "Celina", "Celine", "Selena", "Selene", "Selina", "Seline", "Suellen", "Xylina"])

    def testIsMetaphoneEqualWright(self) -> None:

            self.assertIsMetaphoneEqual("Wright", ["Rota", "Rudd", "Ryde"])

    def testIsMetaphoneEqualSusan(self) -> None:

            self.assertIsMetaphoneEqual("Susan", ["Siusan", "Sosanna", "Susan", "Susana", "Susann", "Susanna", "Susannah", "Susanne", "Suzann", "Suzanna", "Suzanne", "Zuzana"])

    def testIsMetaphoneEqualRay(self) -> None:

            self.assertIsMetaphoneEqual("Ray", ["Ray", "Rey", "Roi", "Roy", "Ruy"])

    def testIsMetaphoneEqualPeter(self) -> None:

            self.assertIsMetaphoneEqual(
                "Peter",
                [
                    "Peadar", "Peder", "Pedro", "Peter", "Petr", "Peyter", "Pieter", "Pietro",
                    "Piotr"
                ]
            )

    def testIsMetaphoneEqualParis(self) -> None:

            self.assertIsMetaphoneEqual("Paris", ["Pearcy", "Perris", "Piercy", "Pierz", "Pryse"])

    def testIsMetaphoneEqualMary(self) -> None:

            self.assertIsMetaphoneEqual("Mary", [
                "Mair", "Maire", "Mara", "Mareah", "Mari", "Maria", "Marie", "Mary", "Maura",
                "Maure", "Meara", "Merrie", "Merry", "Mira", "Moira", "Mora", "Moria", "Moyra",
                "Muire", "Myra", "Myrah"
            ])

    def testIsMetaphoneEqualKnight(self) -> None:

            self.assertIsMetaphoneEqual(
                    "Knight",
                    [
                        "Hynda", "Nada", "Nadia", "Nady", "Nat", "Nata", "Natty", "Neda", "Nedda",
                        "Nedi", "Netta", "Netti", "Nettie", "Netty", "Nita", "Nydia"
                    ]
            )

    def testIsMetaphoneEqualJohn(self) -> None:


        pass # LLM could not translate method body

    def testIsMetaphoneEqualGary(self) -> None:

            self.assertIsMetaphoneEqual(
                "Gary",
                [
                    "Cahra", "Cara", "Carey", "Cari", "Caria", "Carie", "Caro", "Carree", "Carri",
                    "Carrie", "Carry", "Cary", "Cora", "Corey", "Cori", "Corie", "Correy", "Corri",
                    "Corrie", "Corry", "Cory", "Gray", "Kara", "Kare", "Karee", "Kari", "Karia",
                    "Karie", "Karrah", "Karrie", "Karry", "Kary", "Keri", "Kerri", "Kerrie",
                    "Kerry", "Kira", "Kiri", "Kora", "Kore", "Kori", "Korie", "Korrie", "Korry"
                ]
            )

    def testIsMetaphoneEqualAlbert(self) -> None:

            self.assertIsMetaphoneEqual("Albert", ["Ailbert", "Alberik", "Albert", "Alberto", "Albrecht"])

    def testIsMetaphoneEqualWhite(self) -> None:

            matches = [
                "Wade", "Wait", "Waite", "Wat", "Whit", "Wiatt", "Wit", "Wittie", "Witty",
                "Wood", "Woodie", "Woody"
            ]
            self.assertIsMetaphoneEqual("White", matches)

    def testIsMetaphoneEqualAero(self) -> None:

            self.assertIsMetaphoneEqual("Aero", ["Eure"])

    def testIsMetaphoneEqual2(self) -> None:

            self.assertMetaphoneEqual([["Lawrence", "Lorenza"], ["Gary", "Cahra"]])

    def testIsMetaphoneEqual1(self) -> None:

            self.assertMetaphoneEqual([
                ["Case", "case"],
                ["CASE", "Case"],
                ["caSe", "cAsE"],
                ["quick", "cookie"]
            ])

    def _createStringEncoder(self) -> Metaphone:

            return Metaphone()

    def validateFixture(self, pairs: typing.List[typing.List[str]]) -> None:

        if not pairs:
            self.fail("Test fixture is empty")
        for i, pair in enumerate(pairs):
            if len(pair) != 2:
                self.fail(f"Error in test fixture in the data array at index {i}")

    def assertMetaphoneEqual(self, pairs: typing.List[typing.List[str]]) -> None:

            self.validateFixture(pairs)
            for pair in pairs:
                name0, name1 = pair
                fail_msg = f"Expected match between {name0} and {name1}"
                assert self.getStringEncoder().isMetaphoneEqual(name0, name1), fail_msg
                assert self.getStringEncoder().isMetaphoneEqual(name1, name0), fail_msg

    def assertIsMetaphoneEqual(self, source: str, matches: typing.List[str]) -> None:

        for match in matches:
            assert self.isMetaphoneEqual(source, match), f"Source: {source}, should have same Metaphone as: {match}"
        for match in matches:
            for match2 in matches:
                assert self.isMetaphoneEqual(match, match2)

    # Class Methods End


