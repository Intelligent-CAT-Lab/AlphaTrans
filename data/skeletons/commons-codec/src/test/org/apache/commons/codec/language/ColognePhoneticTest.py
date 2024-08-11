from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.codec.language.ColognePhonetic import *
from src.test.org.apache.commons.codec.StringEncoderAbstractTest import *
from src.main.org.apache.commons.codec.StringEncoder import *
from src.main.org.apache.commons.codec.EncoderException import *
import unittest
import os
import typing
from typing import *
import io

# Imports End


class ColognePhoneticTest(StringEncoderAbstractTest, unittest.TestCase):

    # Class Fields Begin
    __TESTSET: typing.Set[str] = None
    __MATCHES: typing.List[typing.List[str]] = None
    # Class Fields End

    # Class Methods Begin
    def testSpecialCharsBetweenSameLetters_test0_decomposed(self) -> None:
        pass

    def testVariationsMeyer_test0_decomposed(self) -> None:
        pass

    def testVariationsMella_test0_decomposed(self) -> None:
        pass

    def testIsEncodeEquals_test0_decomposed(self) -> None:
        pass

    def testHyphen_test0_decomposed(self) -> None:
        pass

    def testExamples_test0_decomposed(self) -> None:
        pass

    def testEdgeCases_test0_decomposed(self) -> None:
        pass

    def testAychlmajrForCodec122_test0_decomposed(self) -> None:
        pass

    def testAaclan_test0_decomposed(self) -> None:
        pass

    def testAabjoe_test0_decomposed(self) -> None:
        pass

    def testCanFail_test0_decomposed(self) -> None:
        pass

    def _createStringEncoder(self) -> ColognePhonetic:
        pass

    def checkEncoding(self, expected: str, source: str) -> None:
        pass

    @staticmethod
    def finishTests() -> None:
        pass

    @staticmethod
    def main(args: typing.List[typing.List[str]]) -> None:
        pass

    @staticmethod
    def __hasTestCase(re: str) -> bool:
        pass

    # Class Methods End
