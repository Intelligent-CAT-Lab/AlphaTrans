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

    __MATCHES: List[str] = [
        ".*[AEIOUJY].*",  # A, E, I, J, O, U, Y
        ".*H.*",  # H
        ".*B.*",  # B
        ".*P[^H].*",  # P not before H
        ".*[DT][^CSZ].*",  # D,T not before C,S,Z
        ".*[FVW].*",  # F,V,W
        ".*PH.*",  # P before H
        ".*[GKQ].*",  # G,K,Q
        "C[AHKLOQRUX].*",  # Initial C before A, H, K, L, O, Q, R, U, X
        ".*[^SZ]C[AHKLOQRUX].*",  # C before A, H, K, L, O, Q, R, U, X but not after S, Z
        ".*[^CKQ]X.*",  # X not after C,K,Q
        ".*L.*",  # L
        ".*[MN].*",  # M,N
        ".*R.*",  # R
        ".*[SZ].*",  # S,Z
        ".*[SZ]C.*",  # C after S,Z
        "C[^AHKLOQRUX].*",  # Initial C except before A, H, K, L, O, Q, R, U, X
        ".+C[^AHKLOQRUX].*",  # C except before A, H, K, L, O, Q, R, U, X
        ".*[DT][CSZ].*",  # D,T before C,S,Z
        ".*[CKQ]X.*",  # X after C,K,Q
    ]
    __TESTSET: typing.Set[str] = set()

    def testSpecialCharsBetweenSameLetters(self) -> None:

        data = ["Test test", "Testtest", "Test-test", "TesT#Test", "TesT?test"]
        expected = "28282"

        for source in data:
            self.checkEncoding(expected, source)

    def testVariationsMeyer(self) -> None:

        data = ["Meier", "Maier", "Mair", "Meyer", "Meyr", "Mejer", "Major"]
        for source in data:
            self.checkEncoding("67", source)

    def testVariationsMella(self) -> None:

        data = ["mella", "milah", "moulla", "mellah", "muehle", "mule"]
        for source in data:
            self.checkEncoding("65", source)

    def testIsEncodeEquals(self) -> None:

        data = [
            ["Muller", "M�ller"],
            ["Meyer", "Mayr"],
            ["house", "house"],
            ["House", "house"],
            ["Haus", "house"],
            ["ganz", "Gans"],
            ["ganz", "Gänse"],
            ["Miyagi", "Miyako"],
        ]

        for element in data:
            encodeEqual = self._stringEncoder.isEncodeEqual(element[1], element[0])
            self.assertTrue(f"{element[1]} != {element[0]}", encodeEqual)

    def testHyphen(self) -> None:

        data = [["bergisch-gladbach", "174845214"], ["M�ller-L�denscheidt", "65752682"]]

        for source, expected in data:
            self.checkEncoding(expected, source)

    def testExamples(self) -> None:

        data = [
            ["m�ller", "657"],
            ["m�ller", "657"],
            ["schmidt", "862"],
            ["schneider", "8627"],
            ["fischer", "387"],
            ["weber", "317"],
            ["wagner", "3467"],
            ["becker", "147"],
            ["hoffmann", "0366"],
            ["schäfer", "837"],
            ["schäfer", "837"],
            ["breschnew", "17863"],
            ["wikipedia", "3412"],
            ["peter", "127"],
            ["pharma", "376"],
            ["m�nchengladbach", "664645214"],
            ["deutsch", "28"],
            ["deutz", "28"],
            ["hamburg", "06174"],
            ["hannover", "0637"],
            ["christstollen", "478256"],
            ["xanthippe", "48621"],
            ["zacharias", "8478"],
            ["holzbau", "0581"],
            ["matsch", "68"],
            ["matz", "68"],
            ["arbeitsamt", "071862"],
            ["eberhard", "01772"],
            ["eberhardt", "01772"],
            ["celsius", "8588"],
            ["ace", "08"],
            ["shch", "84"],
            ["xch", "484"],
            ["heithabu", "021"],
        ]

        for item in data:
            self.checkEncoding(item[0], item[1])

    def testEdgeCases(self) -> None:

        data = [
            ["a", "0"],
            ["e", "0"],
            ["i", "0"],
            ["o", "0"],
            ["u", "0"],
            ["ä", "0"],  # a-umlaut
            ["�", "0"],  # o-umlaut
            ["�", "0"],  # u-umlaut
            ["ß", "8"],  # small sharp s
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

        for source, expected in data:
            self.checkEncoding(expected, source)

    def testAychlmajrForCodec122(self) -> None:

        try:
            self.checkEncoding("04567", "Aychlmajr")
        except EncoderException as e:
            pytest.fail("Unexpected EncoderException: " + str(e))

    def testAaclan(self) -> None:
        self.checkEncoding("0856", "Aaclan")

    def testAabjoe(self) -> None:
        self.checkEncoding("01", "Aabjoe")

    def testCanFail(self) -> None:
        with pytest.raises(unittest.ComparisonFailure):
            self.checkEncoding("/", "Fehler")

    def _createStringEncoder(self) -> ColognePhonetic:
        return ColognePhonetic()

    def checkEncoding(self, expected: str, source: str) -> None:

        # Replace 'Ä', 'Ö', 'Ü' with 'A', 'O', 'U'
        source = source.upper().replace("Ä", "A").replace("Ö", "O").replace("Ü", "U")

        # Add the modified source to the test set
        self.__TESTSET.add(source)

        # Call the superclass's checkEncoding method
        super().checkEncoding(expected, source)

    @staticmethod
    def finishTests() -> None:

        errors = 0
        for m in ColognePhoneticTest.__MATCHES:
            if not ColognePhoneticTest.__hasTestCase(m):
                print(m + " has no test case")
                errors += 1
        assert errors == 0, "Not expecting any missing test cases"

    @staticmethod
    def main(args: typing.List[str]) -> None:

        coder = ColognePhonetic()
        for arg in args:
            code = coder.encode1(arg)
            print("'" + arg + "' = '" + code + "'")

    @staticmethod
    def __hasTestCase(re: str) -> bool:
        for s in ColognePhoneticTest.__TESTSET:
            if re.match(s):
                return True
        return False
