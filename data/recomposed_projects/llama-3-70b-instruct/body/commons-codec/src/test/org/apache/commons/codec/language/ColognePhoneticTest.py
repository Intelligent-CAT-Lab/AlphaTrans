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
from src.main.org.apache.commons.codec.language.ColognePhonetic import *


class ColognePhoneticTest(StringEncoderAbstractTest, unittest.TestCase):

    __MATCHES: typing.List[str] = [
        ".*[AEIOUJY].*",
        ".*H.*",
        ".*B.*",
        ".*P[^H].*",
        ".*[DT][^CSZ].*",
        ".*[FVW].*",
        ".*PH.*",
        ".*[GKQ].*",
        "C[AHKLOQRUX].*",
        ".*[^SZ]C[AHKLOQRUX].*",
        ".*[^CKQ]X.*",
        ".*L.*",
        ".*[MN].*",
        ".*R.*",
        ".*[SZ].*",
        ".*[SZ]C.*",
        "C[^AHKLOQRUX].*",
        ".+C[^AHKLOQRUX].*",
        ".*[DT][CSZ].*",
        ".*[CKQ]X.*",
    ]
    __TESTSET: typing.Set[str] = set()

    def testSpecialCharsBetweenSameLetters(self) -> None:

        pass  # LLM could not translate this method

    def testVariationsMeyer(self) -> None:

        pass  # LLM could not translate this method

    def testVariationsMella(self) -> None:

        pass  # LLM could not translate this method

    def testIsEncodeEquals(self) -> None:
        data = [
            ["Muller", "M\u00fcller"],  # Müller
            ["Meyer", "Mayr"],
            ["house", "house"],
            ["House", "house"],
            ["Haus", "house"],
            ["ganz", "Gans"],
            ["ganz", "G\u00e4nse"],  # Gänse
            ["Miyagi", "Miyako"],
        ]
        for element in data:
            encodeEqual = self._stringEncoder.isEncodeEqual(element[1], element[0])
            self.assertTrue(element[1] + " != " + element[0], encodeEqual)

    def testHyphen(self) -> None:
        data = [
            ["bergisch-gladbach", "174845214"],
            ["M\u00fcller-L\u00fcdenscheidt", "65752682"],
        ]
        self.checkEncodings(data)

    def testExamples(self) -> None:
        data = [
            ["m\u00DCller", "657"],  # mÜller - why upper case U-umlaut?
            ["m\u00FCller", "657"],  # müller - add equivalent lower-case
            ["schmidt", "862"],
            ["schneider", "8627"],
            ["fischer", "387"],
            ["weber", "317"],
            ["wagner", "3467"],
            ["becker", "147"],
            ["hoffmann", "0366"],
            ["sch\u00C4fer", "837"],  # schÄfer - why upper case A-umlaut ?
            ["sch\u00e4fer", "837"],  # schäfer - add equivalent lower-case
            ["Breschnew", "17863"],
            ["Wikipedia", "3412"],
            ["peter", "127"],
            ["pharma", "376"],
            ["m\u00f6nchengladbach", "664645214"],  # mönchengladbach
            ["deutsch", "28"],
            ["deutz", "28"],
            ["hamburg", "06174"],
            ["hannover", "0637"],
            ["christstollen", "478256"],
            ["Xanthippe", "48621"],
            ["Zacharias", "8478"],
            ["Holzbau", "0581"],
            ["matsch", "68"],
            ["matz", "68"],
            ["Arbeitsamt", "071862"],
            ["Eberhard", "01772"],
            ["Eberhardt", "01772"],
            ["Celsius", "8588"],
            ["Ace", "08"],
            ["shch", "84"],  # CODEC-254
            ["xch", "484"],  # CODEC-255
            ["heithabu", "021"],
        ]
        self.checkEncodings(data)

    def testEdgeCases(self) -> None:
        data = [
            ["a", "0"],
            ["e", "0"],
            ["i", "0"],
            ["o", "0"],
            ["u", "0"],
            ["\u00E4", "0"],  # a-umlaut
            ["\u00F6", "0"],  # o-umlaut
            ["\u00FC", "0"],  # u-umlaut
            ["\u00DF", "8"],  # small sharp s
            ["aa", "0"],
            ["ha", "0"],
            ["h", ""],
            ["aha", "0"],
            ["b", "1"],
            ["p", "1"],
            ["ph", "3"],
            ["f", "3"],
            ["v", "3"],
            ["w", "3"],
            ["g", "4"],
            ["k", "4"],
            ["q", "4"],
            ["x", "48"],
            ["ax", "048"],
            ["cx", "48"],
            ["l", "5"],
            ["cl", "45"],
            ["acl", "085"],
            ["mn", "6"],
            ["{mn}", "6"],  # test chars above Z
            ["r", "7"],
        ]
        self.checkEncodings(data)

    def testAychlmajrForCodec122(self) -> None:
        self.checkEncoding("04567", "Aychlmajr")

    def testAaclan(self) -> None:
        self.checkEncoding("0856", "Aaclan")

    def testAabjoe(self) -> None:
        self.checkEncoding("01", "Aabjoe")

    def testCanFail(self) -> None:
        with pytest.raises(org.junit.ComparisonFailure):
            self.checkEncoding("/", "Fehler")

    def _createStringEncoder(self) -> ColognePhonetic:
        return ColognePhonetic()

    def checkEncoding(self, expected: str, source: str) -> None:
        ColognePhoneticTest.__TESTSET.add(
            source.upper().replace("Ä", "A").replace("Ö", "O").replace("Ü", "U")
        )
        super().checkEncoding(expected, source)

    @staticmethod
    def finishTests() -> None:

        pass  # LLM could not translate this method

    @staticmethod
    def main(args: typing.List[str]) -> None:

        pass  # LLM could not translate this method

    @staticmethod
    def __hasTestCase(re: str) -> bool:
        for s in ColognePhoneticTest.__TESTSET:
            if re.match(s):
                return True
        return False
