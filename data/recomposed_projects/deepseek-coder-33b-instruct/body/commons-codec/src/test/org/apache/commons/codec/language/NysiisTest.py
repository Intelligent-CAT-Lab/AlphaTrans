from __future__ import annotations
import re
import unittest
import pytest
import io
import typing
from typing import *
import unittest
from src.main.org.apache.commons.codec.EncoderException import *
from src.main.org.apache.commons.codec.StringEncoder import *
from src.test.org.apache.commons.codec.StringEncoderAbstractTest import *
from src.main.org.apache.commons.codec.language.Nysiis import *


class NysiisTest(StringEncoderAbstractTest, unittest.TestCase):

    __fullNysiis: Nysiis = Nysiis(False)

    def testTrueVariant(self) -> None:

        encoder = Nysiis(True)

        encoded = encoder.encode1("WESTERLUND")
        self.assertTrue(len(encoded) <= 6)
        self.assertEqual("WASTAR", encoded)

    def testTranan(self) -> None:
        self.__encodeAll(["Trueman", "Truman"], "TRANAN")

    def testSpecialBranches(self) -> None:

        self.__encodeAll(["Kobwick"], "CABWAC")
        self.__encodeAll(["Kocher"], "CACAR")
        self.__encodeAll(["Fesca"], "FASC")
        self.__encodeAll(["Shom"], "SAN")
        self.__encodeAll(["Ohlo"], "OL")
        self.__encodeAll(["Uhu"], "UH")
        self.__encodeAll(["Um"], "UN")

    def testSnat(self) -> None:
        self.__encodeAll(["Smith", "Schmit"], "SNAT")

    def testSnad(self) -> None:
        self.__encodeAll(["Schmidt"], "SNAD")

    def testRule7(self) -> None:

        testValues = [["XA", "X"], ["XAS", "X"]]
        self.__assertEncodings(testValues)

    def testRule6(self) -> None:

        testValues = [["XAY", "XY"], ["XAYS", "XY"]]
        self.__assertEncodings(testValues)

    def testRule5(self) -> None:

        testValues = [["XS", "X"], ["XSS", "X"]]
        self.__assertEncodings(testValues)

    def testRule4Dot2(self) -> None:

        testValues = [["XQ", "XG"], ["XZ", "X"], ["XM", "XN"]]
        self.__assertEncodings(testValues)

    def testRule4Dot1(self) -> None:

        testValues = [
            ["XEV", "XAF"],
            ["XAX", "XAX"],
            ["XEX", "XAX"],
            ["XIX", "XAX"],
            ["XOX", "XAX"],
            ["XUX", "XAX"],
        ]

        self.__assertEncodings(testValues)

    def testRule2(self) -> None:

        testValues = [
            ["XEE", "XY"],
            ["XIE", "XY"],
            ["XDT", "XD"],
            ["XRT", "XD"],
            ["XRD", "XD"],
            ["XNT", "XD"],
            ["XND", "XD"],
        ]

        self.__assertEncodings(testValues)

    def testRule1(self) -> None:

        testValues = [
            ["MACX", "MCX"],
            ["KNX", "NX"],
            ["KX", "CX"],
            ["PHX", "FX"],
            ["PFX", "FX"],
            ["SCHX", "SX"],
        ]

        self.__assertEncodings(testValues)

    def testOthers(self) -> None:

        self.__assertEncodings(
            [
                ["O'Daniel", "ODANAL"],
                ["O'Donnel", "ODANAL"],
                ["Cory", "CARY"],
                ["Corey", "CARY"],
                ["Kory", "CARY"],
                ["FUZZY", "FASY"],
            ]
        )

    def testFal(self) -> None:
        self.__encodeAll(["Phil"], "FAL")

    def testDropBy(self) -> None:

        testValues = [
            ["MACINTOSH", "MCANT"],
            ["KNUTH", "NAT"],
            ["KOEHN", "CAN"],
            ["PHILLIPSON", "FALAPSAN"],
            ["PFEISTER", "FASTAR"],
            ["SCHOENHOEFT", "SANAFT"],
            ["MCKEE", "MCY"],
            ["MACKIE", "MCY"],
            ["HEITSCHMIDT", "HATSNAD"],
            ["BART", "BAD"],
            ["HURD", "HAD"],
            ["HUNT", "HAD"],
            ["WESTERLUND", "WASTARLAD"],
            ["CASSTEVENS", "CASTAFAN"],
            ["VASQUEZ", "VASG"],
            ["FRAZIER", "FRASAR"],
            ["BOWMAN", "BANAN"],
            ["MCKNIGHT", "MCNAGT"],
            ["RICKERT", "RACAD"],
            ["DEUTSCH", "DAT"],
            ["WESTPHAL", "WASTFAL"],
            ["SHRIVER", "SRAVAR"],
            ["KUHL", "CAL"],
            ["RAWSON", "RASAN"],
            ["JILES", "JAL"],
            ["CARRAWAY", "CARY"],
            ["YAMADA", "YANAD"],
        ]

        self.__assertEncodings(testValues)

    def testDan(self) -> None:
        self.__encodeAll(["Dane", "Dean", "Dionne"], "DAN")

    def testDad(self) -> None:
        self.__encodeAll(["Dent"], "DAD")

    def testCap(self) -> None:
        self.__encodeAll(["Capp", "Cope", "Copp", "Kipp"], "CAP")

    def testBran(self) -> None:
        self.__encodeAll(["Brian", "Brown", "Brun"], "BRAN")

    def _createStringEncoder(self) -> Nysiis:
        return Nysiis.Nysiis1()

    def __encodeAll(self, strings: typing.List[str], expectedEncoding: str) -> None:

        for string in strings:
            with self.assertRaises(AssertionError, msg=f"Problem with {string}"):
                self.assertEqual(expectedEncoding, self.__fullNysiis.encode1(string))

    def __assertEncodings(self, testValues: typing.List[typing.List[str]]) -> None:

        for arr in testValues:
            self.assertEqual(
                "Problem with " + arr[0], arr[1], self.__fullNysiis.encode1(arr[0])
            )
