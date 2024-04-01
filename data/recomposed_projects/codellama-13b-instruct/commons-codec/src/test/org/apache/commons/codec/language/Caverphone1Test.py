# Imports Begin
from src.main.org.apache.commons.codec.language.Caverphone1 import *
from src.main.org.apache.commons.codec.StringEncoderAbstractTest import *
from src.main.org.apache.commons.codec.StringEncoder import *
from src.main.org.apache.commons.codec.EncoderException import *
import unittest
# Imports End

class Caverphone1Test(unittest.TestCase, StringEncoderAbstractTest<Caverphone1>):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def testWikipediaExamples(self) -> None:

        data = [["Lee", "L11111"], ["Thompson", "TMPSN1"]]
        self.checkEncodings(data)

    def testSpecificationV1Examples(self) -> None:

        data = [["David", "TFT111"], ["Whittle", "WTL111"]]
        self.checkEncodings(data)

    def testIsCaverphoneEquals(self) -> None:

            caverphone = Caverphone1()
            self.assertFalse(
                "Caverphone encodings should not be equal",
                caverphone.isEncodeEqual("Peter", "Stevenson"))
            self.assertTrue(
                "Caverphone encodings should be equal",
                caverphone.isEncodeEqual("Peter", "Peady"))

    def testEndMb(self) -> None:

            data = [["mb", "M11111"], ["mbmb", "MPM111"]]
            self.checkEncodings(data)

    def testCaverphoneRevisitedCommonCodeAT1111(self) -> None:

            self.checkEncodingVariations(
                "AT1111",
                [
                    "add", "aid", "at", "art", "eat", "earth", "head", "hit", "hot", "hold", "hard",
                    "heart", "it", "out", "old"
                ]
            )

    def _createStringEncoder(self) -> Caverphone1:

            return Caverphone1()

    # Class Methods End


