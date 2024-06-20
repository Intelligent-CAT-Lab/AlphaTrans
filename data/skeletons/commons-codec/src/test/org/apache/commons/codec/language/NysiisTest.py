from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.codec.language.Nysiis import *
from src.test.org.apache.commons.codec.StringEncoderAbstractTest import *
from src.main.org.apache.commons.codec.StringEncoder import *
from src.main.org.apache.commons.codec.EncoderException import *
import unittest
import typing
from typing import *
import io

# Imports End


class NysiisTest(StringEncoderAbstractTest, unittest.TestCase):

    # Class Fields Begin
    __fullNysiis: Nysiis = None
    # Class Fields End

    # Class Methods Begin
    def testTrueVariant(self) -> None:
        pass

    def testTranan(self) -> None:
        pass

    def testSpecialBranches(self) -> None:
        pass

    def testSnat(self) -> None:
        pass

    def testSnad(self) -> None:
        pass

    def testRule7(self) -> None:
        pass

    def testRule6(self) -> None:
        pass

    def testRule5(self) -> None:
        pass

    def testRule4Dot2(self) -> None:
        pass

    def testRule4Dot1(self) -> None:
        pass

    def testRule2(self) -> None:
        pass

    def testRule1(self) -> None:
        pass

    def testOthers(self) -> None:
        pass

    def testFal(self) -> None:
        pass

    def testDropBy(self) -> None:
        pass

    def testDan(self) -> None:
        pass

    def testDad(self) -> None:
        pass

    def testCap(self) -> None:
        pass

    def testBran(self) -> None:
        pass

    def _createStringEncoder(self) -> Nysiis:
        pass

    def __encodeAll(self, strings: typing.List[str], expectedEncoding: str) -> None:
        pass

    def __assertEncodings(self, testValues: typing.List[typing.List[str]]) -> None:
        pass

    # Class Methods End
