from __future__ import annotations
import re
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.codec.EncoderException import *
from src.main.org.apache.commons.codec.StringEncoder import *
from src.test.org.apache.commons.codec.StringEncoderAbstractTest import *
from src.main.org.apache.commons.codec.language.Caverphone1 import *


class Caverphone1Test(StringEncoderAbstractTest, unittest.TestCase):

    def testWikipediaExamples(self) -> None:

        data = [["Lee", "L11111"], ["Thompson", "TMPSN1"]]
        self.checkEncodings(data)

    def testSpecificationV1Examples(self) -> None:

        data = [["David", "TFT111"], ["Whittle", "WTL111"]]
        self.checkEncodings(data)

    def testIsCaverphoneEquals(self) -> None:

        caverphone = Caverphone1()
        self.assertFalse(
            caverphone.isEncodeEqual("Peter", "Stevenson"),
            "Caverphone encodings should not be equal",
        )
        self.assertTrue(
            caverphone.isEncodeEqual("Peter", "Peady"),
            "Caverphone encodings should be equal",
        )

    def testEndMb(self) -> None:

        data = [["mb", "M11111"], ["mbmb", "MPM111"]]
        self.checkEncodings(data)

    def testCaverphoneRevisitedCommonCodeAT1111(self) -> None:

        self.checkEncodingVariations(
            "AT1111",
            [
                "add",
                "aid",
                "at",
                "art",
                "eat",
                "earth",
                "head",
                "hit",
                "hot",
                "hold",
                "hard",
                "heart",
                "it",
                "out",
                "old",
            ],
        )

    def _createStringEncoder(self) -> Caverphone1:
        return Caverphone1()
