from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.codec.language.Metaphone import *
from src.test.org.apache.commons.codec.StringEncoderAbstractTest import *
from src.main.org.apache.commons.codec.StringEncoder import *
import unittest
import typing
from typing import *
import io

# Imports End


class MetaphoneTest(StringEncoderAbstractTest, unittest.TestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def testSetMaxLengthWithTruncation(self) -> None:
        pass

    def testExceedLength(self) -> None:
        pass

    def testTCH(self) -> None:
        pass

    def testTIOAndTIAToX(self) -> None:
        pass

    def testSHAndSIOAndSIAToX(self) -> None:
        pass

    def testPHTOF(self) -> None:
        pass

    def testDiscardOfSilentGN(self) -> None:
        pass

    def testDiscardOfSilentHAfterG(self) -> None:
        pass

    def testTranslateToJOfDGEOrDGIOrDGY(self) -> None:
        pass

    def testTranslateOfSCHAndCH(self) -> None:
        pass

    def testWordsWithCIA(self) -> None:
        pass

    def testWhy(self) -> None:
        pass

    def testDiscardOfSCEOrSCIOrSCY(self) -> None:
        pass

    def testWordEndingInMB(self) -> None:
        pass

    def testMetaphone(self) -> None:
        pass

    def testIsMetaphoneEqualXalan(self) -> None:
        pass

    def testIsMetaphoneEqualWright(self) -> None:
        pass

    def testIsMetaphoneEqualSusan(self) -> None:
        pass

    def testIsMetaphoneEqualRay(self) -> None:
        pass

    def testIsMetaphoneEqualPeter(self) -> None:
        pass

    def testIsMetaphoneEqualParis(self) -> None:
        pass

    def testIsMetaphoneEqualMary(self) -> None:
        pass

    def testIsMetaphoneEqualKnight(self) -> None:
        pass

    def testIsMetaphoneEqualJohn(self) -> None:
        pass

    def testIsMetaphoneEqualGary(self) -> None:
        pass

    def testIsMetaphoneEqualAlbert(self) -> None:
        pass

    def testIsMetaphoneEqualWhite(self) -> None:
        pass

    def testIsMetaphoneEqualAero(self) -> None:
        pass

    def testIsMetaphoneEqual2(self) -> None:
        pass

    def testIsMetaphoneEqual1(self) -> None:
        pass

    def _createStringEncoder(self) -> Metaphone:
        pass

    def validateFixture(self, pairs: typing.List[typing.List[str]]) -> None:
        pass

    def assertMetaphoneEqual(self, pairs: typing.List[typing.List[str]]) -> None:
        pass

    def assertIsMetaphoneEqual(self, source: str, matches: typing.List[str]) -> None:
        pass

    # Class Methods End
