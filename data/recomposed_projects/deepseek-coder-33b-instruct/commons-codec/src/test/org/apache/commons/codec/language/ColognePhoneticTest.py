from __future__ import annotations
import re
import unittest
import pytest
import io
import typing
from typing import *
from src.main.org.apache.commons.codec.EncoderException import *
from src.main.org.apache.commons.codec.StringEncoder import *
from src.test.org.apache.commons.codec.StringEncoderAbstractTest import *
from src.main.org.apache.commons.codec.language.ColognePhonetic import *


class ColognePhoneticTest(StringEncoderAbstractTest, unittest.TestCase):

    __MATCHES: typing.List[str] = [
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
        self.checkEncodingVariations("28282", data)

    def testVariationsMeyer(self) -> None:

        data = ["Meier", "Maier", "Mair", "Meyer", "Meyr", "Mejer", "Major"]
        self.checkEncodingVariations("67", data)

    def testVariationsMella(self) -> None:

        data = ["mella", "milah", "moulla", "mellah", "muehle", "mule"]
        self.checkEncodingVariations("65", data)

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
            encodeEqual = self.getStringEncoder().isEncodeEqual(element[1], element[0])
            assert encodeEqual, f"{element[1]} != {element[0]}"

    def testHyphen(self) -> None:

        data = [["bergisch-gladbach", "174845214"], ["M�ller-L�denscheidt", "65752682"]]

        self.checkEncodings(data)

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

        self.checkEncodings(data)

    def testEdgeCases(self) -> None:

        pass  # LLM could not translate this method

    def testAychlmajrForCodec122(self) -> None:

        # Assuming that the checkEncoding method is a method of the ColognePhonetic class
        # and it takes two arguments: the expected string and the source string
        # The checkEncoding method is not defined in the provided partial Python translation
        # So, I'm assuming that it's a method of the ColognePhonetic class

        # If the checkEncoding method is not a method of the ColognePhonetic class,
        # you would need to import and instantiate the ColognePhonetic class
        # and call the checkEncoding method on that instance

        # Assuming the checkEncoding method is a method of the ColognePhonetic class
        # and it doesn't raise an EncoderException

        self.checkEncoding("04567", "Aychlmajr")

    def testAaclan(self) -> None:

        self.checkEncoding("0856", "Aaclan")

    def testAabjoe(self) -> None:

        self.checkEncoding("01", "Aabjoe")

    def testCanFail(self) -> None:

        try:
            self.checkEncoding("/", "Fehler")
        except EncoderException as e:
            print(f"EncoderException occurred: {e}")

    def _createStringEncoder(self) -> ColognePhonetic:

        return ColognePhonetic()

    def checkEncoding(self, expected: str, source: str) -> None:

        self.__TESTSET.add(
            source.upper().replace("Ä", "A").replace("Ö", "O").replace("Ü", "U")
        )
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
